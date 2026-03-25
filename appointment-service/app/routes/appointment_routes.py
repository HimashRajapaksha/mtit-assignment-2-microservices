from fastapi import APIRouter, HTTPException
from app.schemas.appointment_schema import AppointmentCreate
from app.database.db import get_connection

router = APIRouter()

@router.get("/appointments")
def get_appointments():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM appointments")
    rows = cursor.fetchall()
    conn.close()

    return [dict(row) for row in rows]

@router.get("/appointments/{appointment_id}")
def get_appointment(appointment_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM appointments WHERE id = ?", (appointment_id,))
    row = cursor.fetchone()
    conn.close()

    if not row:
        raise HTTPException(status_code=404, detail="Appointment not found")

    return dict(row)

@router.post("/appointments")
def create_appointment(appointment: AppointmentCreate):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO appointments (patient_id, doctor_id, date, time)
        VALUES (?, ?, ?, ?)
    """, (appointment.patient_id, appointment.doctor_id, appointment.date, appointment.time))
    conn.commit()

    appointment_id = cursor.lastrowid
    conn.close()

    return {
        "message": "Appointment added successfully",
        "appointment": {
            "id": appointment_id,
            "patient_id": appointment.patient_id,
            "doctor_id": appointment.doctor_id,
            "date": appointment.date,
            "time": appointment.time
        }
    }