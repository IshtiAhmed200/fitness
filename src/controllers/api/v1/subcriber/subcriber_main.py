from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from . database import get_db,engine
from . import models
from src.schemas.v1.subcriber_check import Check

router = APIRouter()

models.Base.metadata.create_all(bind=engine)

#Create
@router.post("/")
def create(data : Check, db : Session = Depends(get_db)):
    members = models.Subcriber(
        name = data.name,
        email = data.email,
        password = data.password
    )
    db.add(members)
    db.commit()
    db.refresh(members)
    return{"Subcriber" : members}


#Read 
@router.get("/")
def read(db : Session = Depends(get_db)):
    members = db.query(models.Subcriber).order_by(models.Subcriber.id.asc()).all()
    return{"Subcriber":members}

@router.get("/{id}")
def read_by_id(id:int, db : Session = Depends(get_db)):
    members = db.query(models.Subcriber).filter(models.Subcriber.id == id).first()
    return{"Subcriber" : members}


#Update
@router.put("/id")
def update(id: int, data : Check, db : Session = Depends(get_db)):
    members = db.query(models.Subcriber).filter(models.Subcriber.id == id).first()
    
    setattr(members, "name", data.name)
    setattr(members, "email", data.email)
    setattr(members, "password", data.password)

    db.commit()
    db.refresh(members)
    return{"data" : members}


#Delete
@router.delete("/{id}")
def delete(id : int, db : Session = Depends(get_db)):
    members = db.query(models.Subcriber).filter(models.Subcriber.id == id).first()
    db.delete(members)
    return{"status" : "Data successfully deleted"}

