
from fastapi import FastAPI, Depends, HTTPException

app = FastAPI()

@app.get("/users/{user_id}")
async def read_user(user_id: int, q: str = None):
    return {"user_id": user_id, "q": q}

