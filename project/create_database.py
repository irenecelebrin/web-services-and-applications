"""Create slackline.db with emergency_contacts, people, and memberships tables."""

import sqlite3
from pathlib import Path

SCHEMA_STATEMENTS = [
    """
    CREATE TABLE IF NOT EXISTS emergency_contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(255) NOT NULL,
        phone VARCHAR(50)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS people (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(100) NOT NULL,
        last_name VARCHAR(100) NOT NULL,
        email VARCHAR(255),
        phone VARCHAR(50),
        address VARCHAR(255),
        date_of_birth TEXT,
        emergency_contact_id INTEGER,
        FOREIGN KEY (emergency_contact_id) REFERENCES emergency_contacts(id)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS memberships (
        person_id INTEGER PRIMARY KEY,
        registration_date TEXT NOT NULL,
        payment_date TEXT,
        payment_amount REAL,
        FOREIGN KEY (person_id) REFERENCES people(id)
    );
    """,
]


def create_database(db_path: Path) -> None:
    Path(db_path).parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    try:
        conn.execute("PRAGMA foreign_keys = ON;")
        for stmt in SCHEMA_STATEMENTS:
            conn.execute(stmt)
        conn.commit()
    finally:
        conn.close()


def main() -> None:
    db_path = Path(__file__).resolve().parent / "data" / "slackline.db"
    create_database(db_path)
    print(f"Database ready: {db_path}")


if __name__ == "__main__":
    main()
