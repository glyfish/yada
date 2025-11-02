# backend/main.py
import os
import json
import re

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from lib.logger import get_logger

from apps.agentic.agents.supervisor import SupervisorAgent
from apps.agentic.core.utils import (
    set_chatgpt_env,
    set_langsmith_env,
    set_tavily_env,
    set_github_env,
)

from api.document_router import router as document_router

logger = get_logger("YADA")

app = FastAPI()

set_langsmith_env()
set_chatgpt_env()
set_tavily_env()
set_github_env()

os.environ["TOKENIZERS_PARALLELISM"] = "false"

class RequestPayload(BaseModel):
    input: str


# Regex to pull out the embedded PDF hint block (if any)
PDF_HINT_RE = re.compile(
    r"```json\s*__PDF_HINT_START__\s*(\{.*?\})\s*__PDF_HINT_END__\s*```",
    re.DOTALL,
)


@app.post("/api/request")
async def generate_markdown(req: RequestPayload):
    logger.debug(f"YADA request: {req.input}")

    supervisor = SupervisorAgent()
    state = await supervisor.process_request(req.input)

    # state should be {"messages": [...]} from the final worker
    messages = state.get("messages", [])
    last_msg = messages[-1] if messages else None

    if last_msg is None:
        # Nothing came back at all
        return {"result": ""}

    # Get the raw text content from the final message
    try:
        raw_text = last_msg.content
    except AttributeError:
        # fallback if it's just a plain string or something unexpected
        raw_text = str(last_msg)

    pdfs_list = []

    # Look for an embedded PDF hint block at the end of the answer
    m = PDF_HINT_RE.search(raw_text)
    if m:
        json_blob = m.group(1).strip()
        try:
            pdf_hint = json.loads(json_blob)
            if isinstance(pdf_hint, dict):
                # Shape it for the UI. UI expects: { path, pages }
                pdfs_list.append(pdf_hint)
        except Exception as e:
            logger.error(f"Failed to decode pdf_hint JSON: {e}")

        # Strip the hint block from the visible markdown we send to UI
        raw_text = PDF_HINT_RE.sub("", raw_text).strip()

    resp = {"result": raw_text}
    if pdfs_list:
        resp["pdfs"] = pdfs_list

    return resp


# Mount the document API router
app.include_router(document_router, prefix="/api")

# Serve static files from the html directory
html_path = os.path.join(os.path.dirname(__file__), "../html")
app.mount("/", StaticFiles(directory=html_path, html=True), name="html")

# uvicorn api.main:app --reload --port 8000