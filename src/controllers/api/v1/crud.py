from fastapi import APIRouter
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor

router = APIRouter()

#Database Connection
try:
    connection = psycopg2.connect(
        host = 'localhost',
        user = 'postgres',
        database = 'fitness',
        password = 'hello',
        cursor_factory = RealDictCursor
    )
    cursor = connection.cursor()
    print("Database connect successfully")

except Exception as error:
    print("Database not connected")
    print("Error =",error)

#Base Model
class Check(BaseModel):
    id : int
    name : str
    age : int

#Create
@router.post("/")
def create(data : Check):
    cursor.execute(
        f"""
            insert into 
            "coustomer" (id,name, age) 
            values (%s,%s, %s) 
            returning *
        """,
        (   
            data.id,
            data.name,
            data.age
        )
    )
    connection.commit()
    coustomer = cursor.fetchone()
    return{"coustomer" : coustomer}


#Read
@router.get("/")
def read():
    cursor.execute(
        """
            select 
                *
            from "coustomer"
            order by id Asc
        """
    )

    coustomer = cursor.fetchall()
    return{"coustomer" : coustomer}


#Update
@router.put("/")
def update(data : Check):
    cursor.execute(
        f"""
            update "coustomer"
            set name = %s,
                age = %s
            where id = %s
            returning *
        """,
        (
            data.name,
            data.age,
            data.id
        )
    )
    connection.commit()
    coustomer = cursor.fetchone()
    return{"coustomer" : coustomer}


#Delete
@router.delete("/{id}")
def delete(id:int):
    cursor.execute(
        f"""
            delete from "coustomer"
            where id = %s
        """,
        (
            id,
        )
    )

    connection.commit()
    return{"status" : "Data successfully deleted"}