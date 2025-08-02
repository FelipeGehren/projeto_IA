import uvicorn
from fastapi import FastAPI
from database import engine, Base
from mongodb_database import mongodb_client
from routers import chat

app = FastAPI()

@app.get("/")
def check_api():
    return {"response": "Api Online!"}

app.include_router(chat.router)

mongodb_client.admin.command('ping')

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5002, reload=True )