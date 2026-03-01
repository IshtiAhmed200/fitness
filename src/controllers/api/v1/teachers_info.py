from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Check(BaseModel):
    id : int
    name : str

@router.post("/")
def teachers_info(data : Check):
    return{"data" : data}
