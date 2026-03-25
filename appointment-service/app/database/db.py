import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
DB_PATH = BASE_DIR / "appointments.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id INTEGER NOT NULL,
            doctor_id INTEGER NOT NULL,
            date TEXT NOT NULL,
            time TEXT NOT NULL
        )
    """)

    cursor.execute("SELECT COUNT(*) FROM appointments")
    count = cursor.fetchone()[0]

    if count == 0:
        cursor.executemany("""
            INSERT INTO appointments (patient_id, doctor_id, date, time)
            VALUES (?, ?, ?, ?)
        """, [
            (1, 1, "2026-03-28", "10:00 AM"),
            (2, 2, "2026-03-29", "02:00 PM")
        ])

    conn.commit()
    conn.close()