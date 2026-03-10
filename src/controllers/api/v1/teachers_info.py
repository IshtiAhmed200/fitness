from fastapi import APIRouter
from src.schemas.v1.teacher_shcema import Teacher 

router = APIRouter()

@router.post("/")
def teachers_info(data : Teacher):
    return{"data" : data}
