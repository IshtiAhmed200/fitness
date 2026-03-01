from fastapi import FastAPI
from typing import Optional
from src.routes.v1.router import router as v1_router

app = FastAPI()

app.include_router(v1_router, prefix="/api/v1")




