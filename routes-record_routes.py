from fastapi import APIRouter

router = APIRouter(prefix="/records")

@router.post("/")
def create_record():
    return {"message": "Record created"}

@router.get("/")
def get_records():
    return {"message": "All records"}