from fastapi import FastAPI, Depends
from typing import Optional
from fastapi.exceptions import HTTPException
from routers import users
from dependencies.auth import get_current_user

app = FastAPI()

app.include_router(users.router, prefix="/users")

# Dependency function
def get_query_param(q: Optional[str] = None):
    return q

# Endpoint using the dependency
@app.get("/search")
def search(query: str = Depends(get_query_param)):
    if query:
        return {"query": query}
    return HTTPException(status_code=400, detail="Query parameter is required")

def get_fake_db():
    print("Opening DB")
    try:
        yield {"users": ["Alice", "Bob", "Charlie"]}
    finally:
        print("Closing DB")

@app.get("/users")
def read_users(db: dict = Depends(get_fake_db)):
    return {"users": db["users"]}

@app.get("/profile")
def read_profile(user: str = Depends(get_current_user)):
    return {"user": user}

# befejezni module 5 és próbáljuk ki egy rendes adatbázissal, postgres
# elég a module 4 postgresre !!!
# megnézni szerdára a frontendet