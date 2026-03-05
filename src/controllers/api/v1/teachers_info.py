from fastapi import APIRouter
from src.schemas.v1.check import Teachers_info_check 

router = APIRouter()

@router.post("/")
def teachers_info(data : Teachers_info_check):
    return{"data" : data}
