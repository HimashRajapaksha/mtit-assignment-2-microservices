from fastapi import FastAPI
from app.routes.doctor_routes import router as doctor_router

app = FastAPI(title="Doctor Service", version="1.0.0")

app.include_router(doctor_router)

@app.get("/")
def root():
    return {"message": "Doctor Service is running"}