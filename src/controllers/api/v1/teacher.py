from fastapi import APIRouter
from src.schemas.v1.teacherSchema import TeacherSchema 

router = APIRouter()

@router.post("/")
def teachers_info(data : TeacherSchema):
    return{"data" : data}