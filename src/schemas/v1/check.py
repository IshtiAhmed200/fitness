from pydantic import BaseModel,EmailStr,Field


class Customer_info_check(BaseModel):
    id : int
    name : str = Field(..., min_length=3, max_length=20)
    address : EmailStr
    contact : str

class Teachers_info_check(BaseModel):
    id : int
    name : str

class Student_info_check(BaseModel):
    id : int
    name : str
    department : str




