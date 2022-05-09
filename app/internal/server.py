from fastapi import FastAPI
from routers import user
from schema.index import graphql_app
import uvicorn
from app.internal.configs import configs

app = FastAPI()

app.include_router(user.router)
app.include_router(graphql_app, prefix="/schema")

def run():
    uvicorn.run(app, host="127.0.0.1", port=5000, log_level="info")