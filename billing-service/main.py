from fastapi import FastAPI
from app.routes.billing_routes import router as billing_router

app = FastAPI(title="Billing Service", version="1.0.0")

app.include_router(billing_router)

@app.get("/")
def root():
    return {"message": "Billing Service is running"}