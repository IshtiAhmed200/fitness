from fastapi import APIRouter
from src.schemas.v1.check import Student_info_check 

router = APIRouter()

@router.post("/")
def student_info(data : Student_info_check):
    return{"data" : data}
