from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.post("/create_post/")
async def create_post(item: dict):
    if not item:
        raise HTTPException(status_code=400, detail="Item cannot be empty")
    
    item["message"] = "This is a response message"
    return item