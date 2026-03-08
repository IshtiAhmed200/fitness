from fastapi import APIRouter
from typing import Optional

router = APIRouter()

@router.get("/{name}")
def mobile(name : str):
    return{
        "Mobile Name":name
    }

@router.get("/{name}/{model}")
def mobile_with_model(name : str, model: str):
    return{
        "Mobile Name":name,
        "Model" : model
    }

@router.get("/{name}")
def mobile_model(name : str, model : Optional[str]=None):
    return{
        "Mobile Name":name,
        "Model": model
    }