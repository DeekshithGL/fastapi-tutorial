from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def get_app():
        return {"message" : "Hello World!"}

@app.post("/", description = "Post app")
async def post():
        return {"message" : "Hello from post route"}

@app.put("/")
async def put():
        return {"message" : "Hello from put route"}