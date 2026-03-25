from pydantic import BaseModel

class BillCreate(BaseModel):
    patient_id: int
    amount: float
    status: str

class BillResponse(BaseModel):
    id: int
    patient_id: int
    amount: float
    status: str