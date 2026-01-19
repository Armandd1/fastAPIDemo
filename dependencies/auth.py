from fastapi import Header, HTTPException


def get_current_user(token: str = Header(..., alias="X-Token")):
    if token == "secret":
        return "authenticated_user"
    raise HTTPException(status_code=401, detail="Invalid or missing token")