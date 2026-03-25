import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
DB_PATH = BASE_DIR / "billing.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bills (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            status TEXT NOT NULL
        )
    """)

    cursor.execute("SELECT COUNT(*) FROM bills")
    count = cursor.fetchone()[0]

    if count == 0:
        cursor.executemany("""
            INSERT INTO bills (patient_id, amount, status)
            VALUES (?, ?, ?)
        """, [
            (1, 5000.00, "Paid"),
            (2, 7500.00, "Pending")
        ])

    conn.commit()
    conn.close()