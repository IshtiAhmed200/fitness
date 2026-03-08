from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

DATABASE_URL = "sqlite:///./app.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread" : False})
def get_engine():
    return engine


Base = declarative_base()


session_local = sessionmaker(autocommit=False, autoflush=False, bind=get_engine())
def get_db():
    databse = session_local()
    try:
        yield databse
    finally:
        databse.close()
        

def init_db():
    Base.metadata.create_all(bind=get_engine())