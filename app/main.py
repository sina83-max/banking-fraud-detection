from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
async def ping():
    return {"message": "pong"}

@app.get("/hello")
async def hello():
    return {"message": "hello!"}