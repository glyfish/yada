# backend/main.py
import os

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from lib.logger import get_logger

from apps.agentic.agents.supervisor import SupervisorAgent
from apps.agentic.core.utils import (set_chatgpt_env, set_langsmith_env, set_tavily_env, 
                                     set_github_env)

from api.github_router import router as github_router

logger = get_logger("YADA")

app = FastAPI()

set_langsmith_env()
set_chatgpt_env()
set_tavily_env()
set_github_env()

os.environ["TOKENIZERS_PARALLELISM"] = "false"

class RequestPayload(BaseModel):
    input: str


@app.post("/api/request")
async def generate_markdown(req: RequestPayload):
    logger.debug(f"YADA request: {req.input}")
    supervisor = SupervisorAgent()
    result = await supervisor.process_request(req.input)

    message = result['messages'][-1].content
    logger.debug(f"Supervisor response Message: {message}")

    return {"result": message}

# Mount the GitHub API router
app.include_router(github_router, prefix="/api")

# Serve static files from the html directory
html_path = os.path.join(os.path.dirname(__file__), "../html")
app.mount("/", StaticFiles(directory=html_path, html=True), name="html")

# uvicorn api.main:app --reload --port 8000