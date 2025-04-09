from fastapi import FastAPI

from routes.users import router as users_router

import uvicorn

app =FastAPI(
    title="my fast api in python",
    description="this is my stuff!!!",
    version="0.0.1",    
)


app.include_router(users_router ,prefix="/users" , tags=["users"])

@app.get("/") 
async def root():
    return {"message":"server is running"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
    