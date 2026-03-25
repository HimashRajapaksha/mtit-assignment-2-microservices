from fastapi import APIRouter, HTTPException
from app.schemas.patient_schema import PatientCreate
from app.database.db import get_connection

router = APIRouter()

@router.get("/patients")
def get_patients():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patients")
    rows = cursor.fetchall()
    conn.close()

    return [dict(row) for row in rows]

@router.get("/patients/{patient_id}")
def get_patient(patient_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patients WHERE id = ?", (patient_id,))
    row = cursor.fetchone()
    conn.close()

    if not row:
        raise HTTPException(status_code=404, detail="Patient not found")

    return dict(row)

@router.post("/patients")
def create_patient(patient: PatientCreate):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO patients (name, age, gender)
        VALUES (?, ?, ?)
    """, (patient.name, patient.age, patient.gender))
    conn.commit()

    patient_id = cursor.lastrowid
    conn.close()

    return {
        "message": "Patient added successfully",
        "patient": {
            "id": patient_id,
            "name": patient.name,
            "age": patient.age,
            "gender": patient.gender
        }
    }