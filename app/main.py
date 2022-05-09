from internal.server import app, run
from internal.configs import generateJWT

@app.get("/")
def index():
    return {"data": "Hello World!"}

@app.post("/auth")
def get_token(user_id:int):
    token = generateJWT(user_id)
    return {"token": token}

run()