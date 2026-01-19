from fastapi import APIRouter, Depends, Query
from dependencies.auth import get_current_user


router = APIRouter()

@router.get("/me")
def read_users(user:str = Depends(get_current_user)):
    return {"user": user, "users": ["Alice", "Bob", "Charlie"]}


@router.get("/search")
def search_users(q: str = Query(..., min_length=1), user: str = Depends(get_current_user)):
    users = ["Alice", "Bob", "Charlie"]
    filtered = [name for name in users if q.lower() in name.lower()]
    return filtered