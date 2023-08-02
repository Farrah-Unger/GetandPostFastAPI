from fastapi import FastAPI

app = FastAPI()

@app.get("/get_message/")
async def get_message():
    return {"message": "Hello, this is a GET request response"}