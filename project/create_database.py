"""Create slackline.db with emergency_contacts, people, and memberships tables."""

# import dependencies 
import sqlite3
from pathlib import Path

# schema statements for the database
SCHEMA_STATEMENTS = [
    # emergency contacts table
    """
    CREATE TABLE IF NOT EXISTS emergency_contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(255) NOT NULL,
        phone VARCHAR(50)
    );
    """,
    # people table
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
    # memberships table
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

# function tocreate database 
# python type annotations: https://typing.python.org/en/latest/spec/annotations.html 
def create_database(db_path: Path) -> None:
    # create database file if it doesn't exist
    Path(db_path).parent.mkdir(parents=True, exist_ok=True)
    # connect to database
    conn = sqlite3.connect(db_path)
    try:
        # enable foreign keys
        conn.execute("PRAGMA foreign_keys = ON;")
        # execute schema statements
        for stmt in SCHEMA_STATEMENTS:
            conn.execute(stmt)
        # commit changes
        conn.commit()
    finally:
        conn.close()


def main() -> None:
    # set database path
    db_path = Path(__file__).resolve().parent / "data" / "slackline.db"
    # create database
    create_database(db_path)
    print(f"Database ready: {db_path}")

# ── Main ──────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    main()
