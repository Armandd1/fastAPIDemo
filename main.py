from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from routes import items, users

app = FastAPI()

app.include_router(items.router, prefix="/items", tags=["items"])
app.include_router(users.router, prefix="/users", tags=["users"])