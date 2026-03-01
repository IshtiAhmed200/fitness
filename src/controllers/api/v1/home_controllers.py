from fastapi import APIRouter
from typing import Optional

router = APIRouter()

@router.get("/")
def home():
    return {"name" : "Ishti Ahmed"}
