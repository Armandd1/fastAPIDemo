from typing import Optional
from pydantic import BaseModel, Field, EmailStr


class User(BaseModel):
    id: int
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    full_name: Optional[str] = Field(None, max_length=100)
    is_active: bool = True


class User_Response(BaseModel):
    id: int
    full_name: Optional[str] = None
