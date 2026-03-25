from fastapi import APIRouter, HTTPException
from app.schemas.appointment_schema import Appointment
from app.database.db import appointments

router = APIRouter()

@router.get("/appointments")
def get_appointments():
    return appointments

@router.get("/appointments/{appointment_id}")
def get_appointment(appointment_id: int):
    for appointment in appointments:
        if appointment["id"] == appointment_id:
            return appointment
    raise HTTPException(status_code=404, detail="Appointment not found")

@router.post("/appointments")
def create_appointment(appointment: Appointment):
    appointments.append(appointment.dict())
    return {"message": "Appointment added successfully", "appointment": appointment}