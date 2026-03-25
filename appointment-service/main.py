from fastapi import FastAPI
from app.routes.appointment_routes import router as appointment_router
from app.database.db import init_db

app = FastAPI(title="Appointment Service", version="1.0.0")

init_db()
app.include_router(appointment_router)

@app.get("/")
def root():
    return {"message": "Appointment Service is running"}