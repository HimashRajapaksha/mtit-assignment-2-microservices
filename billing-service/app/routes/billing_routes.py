from fastapi import APIRouter, HTTPException
from app.schemas.bill_schema import BillCreate
from app.database.db import get_connection

router = APIRouter()

@router.get("/bills")
def get_bills():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bills")
    rows = cursor.fetchall()
    conn.close()

    return [dict(row) for row in rows]

@router.get("/bills/{bill_id}")
def get_bill(bill_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bills WHERE id = ?", (bill_id,))
    row = cursor.fetchone()
    conn.close()

    if not row:
        raise HTTPException(status_code=404, detail="Bill not found")

    return dict(row)

@router.post("/bills")
def create_bill(bill: BillCreate):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO bills (patient_id, amount, status)
        VALUES (?, ?, ?)
    """, (bill.patient_id, bill.amount, bill.status))
    conn.commit()

    bill_id = cursor.lastrowid
    conn.close()

    return {
        "message": "Bill added successfully",
        "bill": {
            "id": bill_id,
            "patient_id": bill.patient_id,
            "amount": bill.amount,
            "status": bill.status
        }
    }