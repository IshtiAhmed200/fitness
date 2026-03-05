from fastapi import APIRouter
from src.schemas.v1.studentSchema import StudentSchema

router = APIRouter()

@router.post("/")
def student_info(data : StudentSchema):
    return{"data" : data}