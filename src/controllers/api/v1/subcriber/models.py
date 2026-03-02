from sqlalchemy import Column, Integer, String
from . database import Base

class Subcriber(Base):
    __tablename__ = "subcriber"
    id = Column(Integer, primary_key=True, nullable=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)

