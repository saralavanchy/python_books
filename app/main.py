from internal.server import app, run

@app.get("/")
def index():
    return {"data": "Hello World!"}


run()