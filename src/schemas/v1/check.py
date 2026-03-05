from pydantic import BaseModel

class Student_info_check(BaseModel):
    id : int
    name : str
    department : str

class Teachers_info_check(BaseModel):
    id : int
    name : str
