# backend/main.py
import os

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from apps.agentic.agents.supervisor import SupervisorAgent
from apps.agentic.core.utils import set_chatgpt_env, set_langsmith_env, set_tavily_env

app = FastAPI()


set_langsmith_env()
set_chatgpt_env()
set_tavily_env()


class RequestPayload(BaseModel):
    input: str


@app.post("/api/request")
async def generate_markdown(req: RequestPayload):
    supervisor = SupervisorAgent()
    return await supervisor.process_request(req.input)


html_path = os.path.join(os.path.dirname(__file__), "../html")
app.mount("/", StaticFiles(directory=html_path, html=True), name="html")

# uvicorn api.main:app --reload --port 8000