from fastapi import APIRouter, HTTPException
from app.schemas.doctor_schema import Doctor
from app.database.db import doctors

router = APIRouter()

@router.get("/doctors")
def get_doctors():
    return doctors

@router.get("/doctors/{doctor_id}")
def get_doctor(doctor_id: int):
    for doctor in doctors:
        if doctor["id"] == doctor_id:
            return doctor
    raise HTTPException(status_code=404, detail="Doctor not found")

@router.post("/doctors")
def create_doctor(doctor: Doctor):
    doctors.append(doctor.dict())
    return {"message": "Doctor added successfully", "doctor": doctor}