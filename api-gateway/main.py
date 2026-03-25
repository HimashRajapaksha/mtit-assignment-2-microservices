from fastapi import FastAPI
from app.routes import router as gateway_router

app = FastAPI(title="API Gateway", version="1.0.0")

app.include_router(gateway_router)

@app.get("/")
def root():
    return {"message": "API Gateway is running"}