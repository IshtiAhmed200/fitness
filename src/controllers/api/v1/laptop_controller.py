from fastapi import APIRouter
from typing import Optional

router = APIRouter()

@router.get("/{name}")
def laptop(name : str):
    return{
        "Laptop Name":name
    }

@router.get("/{name}/{model}")
def laptop_with_model(name : str, model: str):
    return{
        "Laptop Name":name,
        "Model" : model
    }

@router.get("/{name}")
def laptop_model(name : str, model : Optional[str]=None):
    return{
        "Laptop Name":name,
        "Model": model
    }
