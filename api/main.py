# backend/main.py
import os
import json
import re
import uuid
from typing import Any, Dict, List, Optional

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from sse_starlette.sse import EventSourceResponse

from lib.logger import get_logger

from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.runnables import RunnableConfig
from apps.agentic.agents.orchestrator import OrchestratorAgent
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parents[1] / ".env")

from api.document_router import router as document_router

logger = get_logger("YADA")

app = FastAPI()

os.environ["TOKENIZERS_PARALLELISM"] = "false"

class RequestPayload(BaseModel):
    input: str
    session_id: Optional[str] = None


def _message_content_to_text(message: Any) -> str:
    """
    LangChain messages sometimes return a structured content list. Convert whatever
    comes back into a plain string so downstream regex helpers always receive str.
    """

    content = getattr(message, "content", message)
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = []
        for chunk in content:
            if isinstance(chunk, dict):
                text_value = chunk.get("text")
                if isinstance(text_value, str):
                    parts.append(text_value)
                    continue
            parts.append(str(chunk))
        return "\n".join(parts)
    return str(content)


# Regex to pull out the embedded PDF hint block (if any)
PDF_HINT_RE = re.compile(
    r"```json\s*__PDF_HINT_START__\s*(\{.*?\})\s*__PDF_HINT_END__\s*```",
    re.DOTALL,
)


@app.post("/api/request")
async def generate_markdown(req: RequestPayload):
    session_id = req.session_id or str(uuid.uuid4())
    logger.debug(f"YADA request [{session_id}]: {req.input}")

    orchestrator = OrchestratorAgent()
    config = RunnableConfig(configurable={"thread_id": session_id})
    state = await orchestrator.agent.ainvoke(
        {"messages": [HumanMessage(content=req.input)]},
        config,
    )

    # Get the last AIMessage (the orchestrator's final response),
    # skipping any trailing ToolMessages
    messages = state.get("messages", [])
    last_msg = next(
        (m for m in reversed(messages) if isinstance(m, AIMessage) and not m.tool_calls),
        None,
    )

    if last_msg is None:
        # Nothing came back at all
        return {"result": "", "session_id": session_id}

    # Get the raw text content from the final message
    raw_text = _message_content_to_text(last_msg)

    # Look for an embedded PDF hint block at the end of the answer
    resp: Dict[str, Any] = {"result": raw_text, "session_id": session_id}

    return resp


@app.post("/api/request/stream")
async def stream_request(req: RequestPayload):
    session_id = req.session_id or str(uuid.uuid4())
    logger.debug(f"YADA stream request [{session_id}]: {req.input}")

    orchestrator = OrchestratorAgent()
    config = RunnableConfig(configurable={"thread_id": session_id})

    async def event_generator():
        final_result = ""
        root_run_id = None

        try:
            async for event in orchestrator.agent.astream_events(
                {"messages": [HumanMessage(content=req.input)]},
                config,
                version="v2",
            ):
                event_type = event.get("event", "")
                name = event.get("name", "")
                run_id = event.get("run_id", "")

                # Track the root run so we can identify the top-level graph's final output
                if root_run_id is None:
                    root_run_id = run_id

                # Skip per-token streaming events — too noisy for status feed
                if event_type in ("on_chat_model_stream", "on_chain_stream"):
                    continue

                # Emit raw event info (step 2 will replace with human-readable labels)
                yield {
                    "event": "status",
                    "data": json.dumps({"event": event_type, "name": name}),
                }

                # Capture final output from the root orchestrator graph
                if event_type == "on_chain_end" and run_id == root_run_id:
                    output = event.get("data", {}).get("output", {})
                    if isinstance(output, dict):
                        messages = output.get("messages", [])
                        last_msg = next(
                            (m for m in reversed(messages)
                             if isinstance(m, AIMessage) and not getattr(m, "tool_calls", None)),
                            None,
                        )
                        if last_msg:
                            final_result = _message_content_to_text(last_msg)

            yield {
                "event": "result",
                "data": json.dumps({"result": final_result, "session_id": session_id}),
            }

        except Exception as e:
            logger.error(f"Stream error [{session_id}]: {e}")
            yield {
                "event": "error",
                "data": json.dumps({"message": str(e)}),
            }

    return EventSourceResponse(event_generator())


# Mount the document API router
app.include_router(document_router, prefix="/api")

# Serve static files from the html directory
html_path = os.path.join(os.path.dirname(__file__), "../html")
app.mount("/", StaticFiles(directory=html_path, html=True), name="html")

# uvicorn api.main:app --reload --port 8000
