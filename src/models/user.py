from src.config.database import Base
from sqlalchemy import Column,Integer,String

class User(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String(50),nullable=True)
    email = Column(String(100),unique=True,index=True,nullable=False)
    password = Column(String(50),nullable=True)