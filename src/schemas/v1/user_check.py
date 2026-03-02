from pydantic import BaseModel

class Check(BaseModel):
    name : str
    age : int