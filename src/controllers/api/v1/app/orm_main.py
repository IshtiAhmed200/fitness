from fastapi import APIRouter,Depends
from . database import engine, get_db
from . import models
from sqlalchemy.orm import Session
from src.schemas.v1.user_check import Check

router = APIRouter()

models.Base.metadata.create_all(bind=engine)


#Create
@router.post("/")
def create(data : Check, db : Session = Depends(get_db)):
    new_data = models.User(
        name = data.name,
        age = data.age
    )
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return{"Subcriber" : new_data}


# Read All
@router.get("/")
def read(db: Session = Depends(get_db)):
    data = db.query(models.User).order_by(models.User.id.asc()).all()
    return {"data": data}


#Read by id
@router.get("/{id}")
def read_by_id(id:int, db : Session = Depends(get_db)):
    data = db.query(models.User).filter(models.User.id == id).first()
    return {"data" : data}


#Update
@router.put("/{id}")
def update(id: int,data : Check, db : Session = Depends(get_db)):
    selected_data = db.query(models.User).filter(models.User.id == id).first()
    
    setattr(selected_data, "name", data.name)
    setattr(selected_data, "age", data.age)

    db.commit()
    db.refresh(selected_data)
    return {"data" : data}


#Delete
@router.delete("/{id}")
def delete(id : int, db : Session = Depends(get_db)):
    data = db.query(models.User).filter(models.User.id == id).first()
    
    db.delete(data)
    db.commit()
    return {"status" : "Data successfully Deleted"}

