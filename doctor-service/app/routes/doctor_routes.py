from fastapi import APIRouter, HTTPException
from app.schemas.doctor_schema import DoctorCreate
from app.database.db import get_connection

router = APIRouter()

@router.get("/doctors")
def get_doctors():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM doctors")
    rows = cursor.fetchall()
    conn.close()

    return [dict(row) for row in rows]

@router.get("/doctors/{doctor_id}")
def get_doctor(doctor_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM doctors WHERE id = ?", (doctor_id,))
    row = cursor.fetchone()
    conn.close()

    if not row:
        raise HTTPException(status_code=404, detail="Doctor not found")

    return dict(row)

@router.post("/doctors")
def create_doctor(doctor: DoctorCreate):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO doctors (name, specialization)
        VALUES (?, ?)
    """, (doctor.name, doctor.specialization))
    conn.commit()

    doctor_id = cursor.lastrowid
    conn.close()

    return {
        "message": "Doctor added successfully",
        "doctor": {
            "id": doctor_id,
            "name": doctor.name,
            "specialization": doctor.specialization
        }
    }