from pydantic import BaseModel

class Bill(BaseModel):
    id: int
    patient_id: int
    amount: float
    status: str