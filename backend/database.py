
import sqlite3
from pathlib import Path

DATABASE = Path(__file__).resolve().parent.parent / "database" / "bills.db"


def get_connection():
    DATABASE.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    with get_connection() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS bills (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT NOT NULL,
                amount REAL NOT NULL,
                people INTEGER NOT NULL,
                share REAL NOT NULL
            )
        """)


def save_bill(description, amount, people, share):
    with get_connection() as connection:
        cursor = connection.execute(
            """INSERT INTO bills
               (description, amount, people, share)
               VALUES (?, ?, ?, ?)""",
            (description, amount, people, share)
        )
        return cursor.lastrowid


def get_all_bills():
    with get_connection() as connection:
        rows = connection.execute(
            "SELECT * FROM bills ORDER BY id DESC"
        ).fetchall()
        return [dict(row) for row in rows]
