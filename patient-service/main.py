from fastapi import FastAPI
from app.routes.patient_routes import router as patient_router

app = FastAPI(title="Patient Service", version="1.0.0")

app.include_router(patient_router)

@app.get("/")
def root():
    return {"message": "Patient Service is running"}