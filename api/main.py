# backend/main.py
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import os

app = FastAPI()

class RequestPayload(BaseModel):
    input: str

html_path = os.path.join(os.path.dirname(__file__), "../html")
app.mount("/", StaticFiles(directory=html_path, html=True), name="html")

@app.post("/api/request")
async def generate_markdown(req: RequestPayload):
    # For now, return a hardcoded markdown string
    print(req.input)
    return {"result": f"# You sent:\n\n{req.input}\n"}

# To run: uvicorn backend.main:app --reload