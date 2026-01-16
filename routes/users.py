from fastapi import APIRouter, HTTPException
from typing import List
from models.user import User, User_Response

router = APIRouter()

# Sample data for testing
users_db = [
    User(id=1, username="john_doe", email="john@example.com", full_name="John Doe"),
    User(id=2, username="jane_smith", email="jane@example.com", full_name="Jane Smith"),
    User(id=3, username="bob", email="bob@example.com"),
]


@router.get("/", response_model=List[User])
async def get_all_users():
    """Return all users"""
    return users_db


@router.post("/", response_model=User_Response, status_code=201)
async def create_user(user: User):
    """Create a new user"""
    # Check if id already exists
    for existing_user in users_db:
        if existing_user.id == user.id:
            raise HTTPException(status_code=400, detail="User with this ID already exists")
    
    users_db.append(user)
    return user


@router.get("/{id}", response_model=User)
async def get_user_by_id(id: int):
    """Return a user by ID"""
    for user in users_db:
        if user.id == id:
            return user
    raise HTTPException(status_code=404, detail="User not found")


@router.delete("/{id}", status_code=204)
async def delete_user(id: int):
    """Delete a user by ID"""
    for index, user in enumerate(users_db):
        if user.id == id:
            users_db.pop(index)
            return
    raise HTTPException(status_code=404, detail="User not found")
