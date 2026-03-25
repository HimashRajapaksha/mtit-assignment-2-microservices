from fastapi import FastAPI
from app.routes.appointment_routes import router as appointment_router

app = FastAPI(title="Appointment Service", version="1.0.0")

app.include_router(appointment_router)

@app.get("/")
def root():
    return {"message": "Appointment Service is running"}