from fastapi import APIRouter, HTTPException
from app.schemas.bill_schema import Bill
from app.database.db import bills

router = APIRouter()

@router.get("/bills")
def get_bills():
    return bills

@router.get("/bills/{bill_id}")
def get_bill(bill_id: int):
    for bill in bills:
        if bill["id"] == bill_id:
            return bill
    raise HTTPException(status_code=404, detail="Bill not found")

@router.post("/bills")
def create_bill(bill: Bill):
    bills.append(bill.dict())
    return {"message": "Bill added successfully", "bill": bill}