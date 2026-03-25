from fastapi import APIRouter, HTTPException
from app.schemas.patient_schema import Patient
from app.database.db import patients

router = APIRouter()

@router.get("/patients")
def get_patients():
    return patients

@router.get("/patients/{patient_id}")
def get_patient(patient_id: int):
    for patient in patients:
        if patient["id"] == patient_id:
            return patient
    raise HTTPException(status_code=404, detail="Patient not found")

@router.post("/patients")
def create_patient(patient: Patient):
    patients.append(patient.dict())
    return {"message": "Patient added successfully", "patient": patient}