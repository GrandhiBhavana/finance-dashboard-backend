from fastapi import APIRouter

router = APIRouter(prefix="/dashboard")

@router.get("/summary")
def summary():
    return {
        "total_income": 10000,
        "total_expense": 5000,
        "net_balance": 5000
    }