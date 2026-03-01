from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Check(BaseModel):
    id : int
    name : str
    department : str

@router.post("/")
def student_info(data : Check):
    return{"data" : data}
