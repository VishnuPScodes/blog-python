
from fastapi import FastAPI,APIRouter, Depends, HTTPException

router = APIRouter()

@router.get("/users/{user_id}")
async def read_user(user_id: int, q: str = None):
    return {"user_id": user_id, "q": q}

