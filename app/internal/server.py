from fastapi import FastAPI
from app.routers import user
import uvicorn

app = FastAPI()

app.include_router(user.router)

def run():
    uvicorn.run(app, host="127.0.0.1", port=5000, log_level="info")