from pydantic import BaseModel,EmailStr,Field

class Customer(BaseModel):
    id : int
    name : str = Field(..., min_length=3, max_length=20)
    address : EmailStr
    contact : str