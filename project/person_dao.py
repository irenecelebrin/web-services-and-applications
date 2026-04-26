# Functions for CRUD operations on the database
# Created with Cursor / Claude Opus 4.7 (planning mode)

import sqlite3
from datetime import date
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "data" / "slackline.db"

# canonical SELECT joining people + emergency_contacts + memberships
_MEMBER_SELECT_SQL = """
SELECT
    p.id, p.name, p.last_name, p.email, p.phone, p.address, p.date_of_birth,
    ec.id   AS emergency_contact_id,
    ec.name AS emergency_contact_name,
    ec.phone AS emergency_contact_phone,
    m.registration_date, m.payment_date, m.payment_amount
FROM people p
LEFT JOIN emergency_contacts ec ON ec.id = p.emergency_contact_id
LEFT JOIN memberships m ON m.person_id = p.id
"""

# fields accepted by update(), grouped per table
_PEOPLE_UPDATE_FIELDS = ("name", "last_name", "email", "phone", "address", "date_of_birth")
_EMERGENCY_UPDATE_FIELDS = {
    "emergency_contact_name": "name",
    "emergency_contact_phone": "phone",
}


def _connect() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def _row_to_dict(row: sqlite3.Row | None) -> dict | None:
    return dict(row) if row is not None else None


# get all persons
def get_all() -> list[dict]:
    conn = _connect()
    try:
        rows = conn.execute(_MEMBER_SELECT_SQL + " ORDER BY p.id").fetchall()
        return [dict(r) for r in rows]
    finally:
        conn.close()


# get person by id
def get_by_id(id: int) -> dict | None:
    conn = _connect()
    try:
        row = conn.execute(_MEMBER_SELECT_SQL + " WHERE p.id = ?", (id,)).fetchone()
        return _row_to_dict(row)
    finally:
        conn.close()


# get persons by last name (case-insensitive exact match)
def get_by_surname(surname: str) -> list[dict]:
    conn = _connect()
    try:
        rows = conn.execute(
            _MEMBER_SELECT_SQL + " WHERE LOWER(p.last_name) = LOWER(?) ORDER BY p.id",
            (surname,),
        ).fetchall()
        return [dict(r) for r in rows]
    finally:
        conn.close()


# get persons by email (case-insensitive exact match)
def get_by_email(email: str) -> list[dict]:
    conn = _connect()
    try:
        rows = conn.execute(
            _MEMBER_SELECT_SQL + " WHERE LOWER(p.email) = LOWER(?) ORDER BY p.id",
            (email,),
        ).fetchall()
        return [dict(r) for r in rows]
    finally:
        conn.close()


# create new person (also creates emergency contact + membership rows)
def create(person: dict) -> dict | None:
    today = date.today().isoformat()
    payment_amount = person.get("payment_amount")
    payment_date = today if payment_amount is not None else None

    conn = _connect()
    try:
        with conn:
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO emergency_contacts (name, phone) VALUES (?, ?)",
                (person.get("emergency_contact_name"), person.get("emergency_contact_phone")),
            )
            ec_id = cur.lastrowid

            cur.execute(
                """
                INSERT INTO people (
                    name, last_name, email, phone, address, date_of_birth, emergency_contact_id
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    person.get("name"),
                    person.get("last_name"),
                    person.get("email"),
                    person.get("phone"),
                    person.get("address"),
                    person.get("date_of_birth"),
                    ec_id,
                ),
            )
            person_id = cur.lastrowid

            cur.execute(
                """
                INSERT INTO memberships (person_id, registration_date, payment_date, payment_amount)
                VALUES (?, ?, ?, ?)
                """,
                (person_id, today, payment_date, payment_amount),
            )
    finally:
        conn.close()

    return get_by_id(person_id)


# update person (partial; updates relevant fields across the three tables)
def update(id: int, person: dict) -> dict | None:
    conn = _connect()
    try:
        row = conn.execute(
            "SELECT emergency_contact_id FROM people WHERE id = ?", (id,)
        ).fetchone()
        if row is None:
            return None
        ec_id = row["emergency_contact_id"]

        with conn:
            people_updates = {k: person[k] for k in _PEOPLE_UPDATE_FIELDS if k in person}
            if people_updates:
                assignments = ", ".join(f"{col} = ?" for col in people_updates)
                conn.execute(
                    f"UPDATE people SET {assignments} WHERE id = ?",
                    (*people_updates.values(), id),
                )

            ec_updates = {
                col: person[key]
                for key, col in _EMERGENCY_UPDATE_FIELDS.items()
                if key in person
            }
            if ec_updates and ec_id is not None:
                assignments = ", ".join(f"{col} = ?" for col in ec_updates)
                conn.execute(
                    f"UPDATE emergency_contacts SET {assignments} WHERE id = ?",
                    (*ec_updates.values(), ec_id),
                )

            if "payment_amount" in person:
                conn.execute(
                    "UPDATE memberships SET payment_amount = ?, payment_date = ? WHERE person_id = ?",
                    (person["payment_amount"], date.today().isoformat(), id),
                )
    finally:
        conn.close()

    return get_by_id(id)


# delete person (cascades to membership and emergency contact)
def delete(id: int) -> bool:
    conn = _connect()
    try:
        row = conn.execute(
            "SELECT emergency_contact_id FROM people WHERE id = ?", (id,)
        ).fetchone()
        if row is None:
            return False
        ec_id = row["emergency_contact_id"]

        with conn:
            conn.execute("DELETE FROM memberships WHERE person_id = ?", (id,))
            conn.execute("DELETE FROM people WHERE id = ?", (id,))
            if ec_id is not None:
                conn.execute("DELETE FROM emergency_contacts WHERE id = ?", (ec_id,))
    finally:
        conn.close()

    return True
