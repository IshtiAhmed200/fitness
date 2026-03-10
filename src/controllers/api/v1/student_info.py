from fastapi import APIRouter
from src.schemas.v1.student_schema import Student 

router = APIRouter()

@router.post("/")
def student_info(data : Student):
    return{"data" : data}
