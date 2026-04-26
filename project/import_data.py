## Parse members data from csv and import to database 

import csv
import os
import sqlite3

from create_database import create_database

# set directory paths 
project_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(project_dir, "data")
anonymized_data = os.path.join(data_dir, "db_anonymised.csv")
db_path = os.path.join(data_dir, "slackline.db")

# parse registration date to format YYYY-MM-DD
def _parse_registration_date(raw: str) -> str:
    raw = raw.strip()
    if not raw:
        raise ValueError("Date registered is empty")
    date_part = raw.split()[0]
    day, month, year = date_part.split("/")
    return f"{int(year):04d}-{int(month):02d}-{int(day):02d}"

# parse date of birth to format YYYY-MM-DD
def _parse_dob(raw: str) -> str | None:
    raw = raw.strip()
    if not raw:
        return None
    parts = raw.split("/")
    if len(parts) != 3:
        return None
    day, month, year = (int(parts[0]), int(parts[1]), int(parts[2]))
    if year < 100:
        year += 2000 if year < 50 else 1900
    return f"{year:04d}-{month:02d}-{day:02d}"

# import rows from csv file to database
def import_rows(conn: sqlite3.Connection, csv_path: str) -> int:
    ## connect to database and enable foreign keys
    conn.execute("PRAGMA foreign_keys = ON;")
    # open csv file and read rows
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        count = 0
        # get values from each row
        for row in reader:
            name = (row.get("Name") or "").strip()
            last_name = (row.get("Last Name") or "").strip()
            email = (row.get("Email") or "").strip() or None
            phone = (row.get("Phone number") or "").strip() or None
            address = (row.get("Address") or "").strip() or None
            ec_name = (row.get("Emergency Contact Name") or "").strip()
            ec_phone_key = "Emergency Contact Phone Number "
            ec_phone = (row.get(ec_phone_key) or row.get(ec_phone_key.strip()) or "").strip() or None
            reg_raw = row.get("Date registered") or ""
            dob_raw = row.get("Date of Birth (dd/mm/yy)") or ""

            if not ec_name:
                raise ValueError(f"Missing emergency contact name for row {count + 2}")

            # reformat date and date of birth
            registration_date = _parse_registration_date(reg_raw)
            dob = _parse_dob(dob_raw)

            cur = conn.cursor()
            # add to emergency contacts table
            cur.execute(
                "INSERT INTO emergency_contacts (name, phone) VALUES (?, ?)",
                (ec_name, ec_phone),
            )
            ec_id = cur.lastrowid

            # add to people table
            cur.execute(
                """
                INSERT INTO people (
                    name, last_name, email, phone, address, date_of_birth, emergency_contact_id
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (name, last_name, email, phone, address, dob, ec_id),
            )
            person_id = cur.lastrowid

            # add to memberships table
            cur.execute(
                """
                INSERT INTO memberships (person_id, registration_date, payment_date, payment_amount)
                VALUES (?, ?, NULL, NULL)
                """,
                (person_id, registration_date),
            )
            count += 1
    return count


def main() -> None:
    # check if csv file exists
    if not os.path.isfile(anonymized_data):
        raise SystemExit(f"CSV not found: {anonymized_data}")

    # create database
    create_database(db_path)

    # connect to database and try to delete existing data
    conn = sqlite3.connect(db_path)
    #  to delete existing data
    try:
        conn.execute("PRAGMA foreign_keys = ON;")
        conn.execute("DELETE FROM memberships")
        conn.execute("DELETE FROM people")
        conn.execute("DELETE FROM emergency_contacts")
        conn.execute("DELETE FROM sqlite_sequence WHERE name IN ('people', 'emergency_contacts')")
        # import rows from csv file to database
        n = import_rows(conn, anonymized_data)
        # commit changes
        conn.commit()
    finally:
        conn.close()

    print(f"Imported {n} members from {anonymized_data}")
    print(f"Database: {os.path.abspath(db_path)}")


if __name__ == "__main__":
    main()
