# backend/main.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class RequestPayload(BaseModel):
    input: str

@app.post("/api/request")
async def generate_markdown(req: RequestPayload):
    # For now, return a hardcoded markdown string
    print(req.input)
    return {"result": f"# You sent:\n\n{req.input}\n"}

# To run: uvicorn backend.main:app --reload