from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.models.user import User
from src.schemas.v1.user import UserCreate,UserResponse
from src.config.database import get_db
from typing import List

router = APIRouter()

@router.post('/',response_model=UserResponse)
def create_users(user_data:UserCreate, db:Session = Depends(get_db)):
    try:
        user = User(
            name = user_data.name,
            email = user_data.email,
            password = user_data.password
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    except:
        return "Error"
    

@router.get('/',response_model=List[UserResponse])
def read_users(db:Session = Depends(get_db)):
    data = db.query(User).all()
    return data


