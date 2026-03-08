from pydantic import BaseModel,EmailStr,Field

class User(BaseModel):
    name: str = Field(...,min_length=0,max_length=50)
    email: EmailStr
    password: str = Field(...,min_length=0,max_length=50)

class UserCreate(User):
    pass

class UserResponse(User):
    id: int
    email: EmailStr
    name: str
    password: str