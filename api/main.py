# backend/main.py
import asyncio
import os
import json
import re
import uuid
from contextlib import asynccontextmanager
from typing import Any, Dict, Optional

import langsmith
from fastapi import FastAPI, HTTPException, Query
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from sse_starlette.sse import EventSourceResponse

from lib.logger import get_logger

from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.runnables import RunnableConfig
from langgraph.types import Command
from apps.agentic.agents.orchestrator import OrchestratorAgent
from apps.agentic.core.constants import TOOL_START_LABELS, TOOL_END_LABELS, MCP_URL
from apps.agentic.core.mcp_tool_registry import MCPToolRegistry
from apps.agentic.db.series_cache import SeriesCache
from apps.agentic.db.report_cache import ReportCache
from apps.agentic.agents.plots.time_series_report_agent import TimeSeriesInfoEntry
from apps.agentic.core.pricing import estimate_cost
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parents[1] / ".env")

from api.document_router import router as document_router

# ---------------------------------------------------------------------------
# LangSmith trace URL helper — lazy-cached per process
# ---------------------------------------------------------------------------
_ls_client: langsmith.Client | None = None
_ls_url_prefix: str | None = None   # "{host}/o/{tenant}/projects/p/{project}"


def _get_ls_client() -> langsmith.Client | None:
    if os.environ.get("LANGCHAIN_TRACING_V2", "").lower() != "true":
        return None
    api_key = os.environ.get("LANGCHAIN_API_KEY") or os.environ.get("LANGSMITH_API_KEY")
    if not api_key:
        return None
    return langsmith.Client()


def get_trace_url(run_id: str) -> str | None:
    global _ls_client, _ls_url_prefix
    try:
        if _ls_client is None:
            _ls_client = _get_ls_client()
        if _ls_client is None:
            return None
        if _ls_url_prefix is None:
            tenant_id = _ls_client._get_tenant_id()
            project_name = os.environ.get("LANGCHAIN_PROJECT", "default")
            project = _ls_client.read_project(project_name=project_name)
            host = _ls_client._host_url
            _ls_url_prefix = f"{host}/o/{tenant_id}/projects/p/{project.id}"
        return f"{_ls_url_prefix}/r/{run_id}?poll=true"
    except Exception:
        return None

logger = get_logger("YADA")


@asynccontextmanager
async def lifespan(app: FastAPI):
    SeriesCache.initialize()
    ReportCache.initialize()
    await MCPToolRegistry.initialize(
        servers={"fred": {"transport": "sse", "url": MCP_URL}},
        required=["fred_series_observations"],
    )
    yield


app = FastAPI(lifespan=lifespan)

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

    orchestrator = await OrchestratorAgent.create()
    config = RunnableConfig(configurable={"thread_id": session_id}, recursion_limit=50)
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

    orchestrator = await OrchestratorAgent.create()
    config = RunnableConfig(configurable={"thread_id": session_id}, recursion_limit=50)

    # If the thread has a stale interrupt (user cancelled a form without resuming),
    # Anthropic will reject the history because a tool_use has no tool_result.
    # Silently start a fresh thread rather than propagating a 400 error.
    if req.session_id:
        state = await orchestrator.agent.aget_state(config)
        if state.tasks and state.tasks[0].interrupts:
            session_id = str(uuid.uuid4())
            config = RunnableConfig(configurable={"thread_id": session_id}, recursion_limit=50)
            logger.debug(f"Stream: stale interrupt on [{req.session_id}], fresh thread [{session_id}]")

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

                # Track the root run to identify the top-level graph's final output
                if root_run_id is None:
                    root_run_id = run_id

                # Skip per-token streaming events
                if event_type in ("on_chat_model_stream", "on_chain_stream"):
                    continue

                # Emit human-readable status for known tool/node events
                label: str | None = None
                if event_type == "on_tool_start":
                    label = TOOL_START_LABELS.get(name)
                elif event_type == "on_tool_end":
                    label = TOOL_END_LABELS.get(name)
                elif event_type == "on_chain_start":
                    label = TOOL_START_LABELS.get(name)
                elif event_type == "on_chain_end":
                    label = TOOL_END_LABELS.get(name)

                if label:
                    yield {
                        "event": "status",
                        "data": json.dumps({"text": label}),
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

            # Check for a pending interrupt before sending result
            state = await orchestrator.agent.aget_state(config)
            if state.tasks and state.tasks[0].interrupts:
                interrupt_value = state.tasks[0].interrupts[0].value
                logger.debug(f"Stream interrupted [{session_id}]: form_type={interrupt_value.get('type')}")
                yield {
                    "event": "interrupt",
                    "data": json.dumps({"form_schema": interrupt_value, "session_id": session_id}),
                }
                return

            # Send result immediately — do not block on LangSmith
            yield {
                "event": "result",
                "data": json.dumps({"result": final_result, "session_id": session_id}),
            }

            # Poll LangSmith for the finalized root run (aggregates all subagents)
            logger.debug(f"Meta poll: root_run_id={root_run_id}")
            if root_run_id:
                client = _get_ls_client()
                logger.debug(f"Meta poll: client={client}")
                if client:
                    model = os.getenv("AGENT_LLM_MODEL", "gpt-4.1")
                    for attempt in range(8):
                        await asyncio.sleep(1)
                        try:
                            run = client.read_run(str(root_run_id))
                            logger.debug(f"Meta poll attempt {attempt}: total_tokens={run.total_tokens}")
                            if run.total_tokens:
                                cost = float(run.total_cost) if run.total_cost else estimate_cost(
                                    model,
                                    run.prompt_tokens or 0,
                                    run.completion_tokens or 0,
                                )
                                yield {
                                    "event": "meta",
                                    "data": json.dumps({
                                        "input_tokens":  run.prompt_tokens or 0,
                                        "output_tokens": run.completion_tokens or 0,
                                        "total_tokens":  run.total_tokens,
                                        "cost_usd":      cost,
                                        "trace_url":     get_trace_url(str(root_run_id)),
                                    }),
                                }
                                break
                        except Exception as e:
                            logger.debug(f"Meta poll attempt {attempt} error: {e}")
                            continue

        except Exception as e:
            logger.error(f"Stream error [{session_id}]: {e}")
            yield {
                "event": "error",
                "data": json.dumps({"message": str(e)}),
            }

    return EventSourceResponse(event_generator())


class ResumePayload(BaseModel):
    session_id: str
    form_data: Dict[str, Any]


@app.post("/api/request/resume")
async def resume_request(req: ResumePayload):
    logger.debug(f"YADA resume request [{req.session_id}]: {req.form_data}")

    orchestrator = await OrchestratorAgent.create()
    config = RunnableConfig(configurable={"thread_id": req.session_id})

    async def event_generator():
        final_result = ""
        root_run_id = None

        try:
            async for event in orchestrator.agent.astream_events(
                Command(resume=req.form_data),
                config,
                version="v2",
            ):
                event_type = event.get("event", "")
                name = event.get("name", "")
                run_id = event.get("run_id", "")

                if root_run_id is None:
                    root_run_id = run_id

                if event_type in ("on_chat_model_stream", "on_chain_stream"):
                    continue

                label: str | None = None
                if event_type == "on_tool_start":
                    label = TOOL_START_LABELS.get(name)
                elif event_type == "on_tool_end":
                    label = TOOL_END_LABELS.get(name)
                elif event_type == "on_chain_start":
                    label = TOOL_START_LABELS.get(name)
                elif event_type == "on_chain_end":
                    label = TOOL_END_LABELS.get(name)

                if label:
                    yield {
                        "event": "status",
                        "data": json.dumps({"text": label}),
                    }

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
                "data": json.dumps({"result": final_result, "session_id": req.session_id}),
            }

            logger.debug(f"Resume meta poll: root_run_id={root_run_id}")
            if root_run_id:
                client = _get_ls_client()
                if client:
                    model = os.getenv("AGENT_LLM_MODEL", "gpt-4.1")
                    for attempt in range(8):
                        await asyncio.sleep(1)
                        try:
                            run = client.read_run(str(root_run_id))
                            logger.debug(f"Resume meta poll attempt {attempt}: total_tokens={run.total_tokens}")
                            if run.total_tokens:
                                cost = float(run.total_cost) if run.total_cost else estimate_cost(
                                    model,
                                    run.prompt_tokens or 0,
                                    run.completion_tokens or 0,
                                )
                                yield {
                                    "event": "meta",
                                    "data": json.dumps({
                                        "input_tokens":  run.prompt_tokens or 0,
                                        "output_tokens": run.completion_tokens or 0,
                                        "total_tokens":  run.total_tokens,
                                        "cost_usd":      cost,
                                        "trace_url":     get_trace_url(str(root_run_id)),
                                    }),
                                }
                                break
                        except Exception as e:
                            logger.debug(f"Resume meta poll attempt {attempt} error: {e}")
                            continue

        except Exception as e:
            logger.error(f"Resume error [{req.session_id}]: {e}")
            yield {
                "event": "error",
                "data": json.dumps({"message": str(e)}),
            }

    return EventSourceResponse(event_generator())


@app.get("/api/reports/{report_id}")
async def get_report(report_id: str):
    record = await ReportCache.get_by_report_id(report_id)
    if record is None:
        raise HTTPException(status_code=404, detail="Report not found")
    return {
        "report_id": str(record["report_id"]),
        "report_title": record["report_title"],
        "report_description": record.get("report_description") or "",
        "tags": list(record.get("tags") or []),
        "time_range_from": str(record.get("time_range_from") or ""),
        "time_range_to": str(record["time_range_to"]) if record.get("time_range_to") else None,
        "time_series_info": [
            {
                "native_id": entry.get("native_id", ""),
                "external_id": entry.get("external_id", ""),
                "title": entry.get("title", ""),
                "source": entry.get("source", ""),
            }
            for entry in (record.get("time_series_info") or [])
        ],
    }


class UpdateReportPayload(BaseModel):
    report_title: str
    report_description: str
    tags: str
    time_series_ids: str
    time_range_from: str
    time_range_to: Optional[str] = None


@app.put("/api/reports/{report_id}")
async def update_report(report_id: str, req: UpdateReportPayload):
    ids = [s.strip() for s in req.time_series_ids.split(",") if s.strip()]
    tags = [t.strip() for t in req.tags.split(",") if t.strip()]

    time_series_info: list[TimeSeriesInfoEntry] = []
    missing: list[str] = []
    for cache_id in ids:
        entry = SeriesCache._get_by_cache_id_sync(cache_id)
        if not entry:
            missing.append(cache_id)
            continue
        raw_metadata = entry.get("metadata")
        metadata = raw_metadata if isinstance(raw_metadata, dict) else {}
        time_series_info.append({
            "native_id": str(entry["native_id"]),
            "title": str(entry.get("title") or ""),
            "source": str(entry.get("source") or ""),
            "external_id": str(entry.get("external_id") or ""),
            "frequency": str(entry.get("frequency") or ""),
            "observation_start": str(entry.get("observation_start") or ""),
            "observation_end": str(entry.get("observation_end") or ""),
            "metadata": metadata,
        })

    if missing:
        raise HTTPException(status_code=400, detail=f"Unknown cache IDs: {', '.join(missing)}")

    updated = await ReportCache.update_report(
        report_id=report_id,
        report_title=req.report_title,
        report_description=req.report_description,
        time_series_info=time_series_info,
        time_range_from=req.time_range_from,
        time_range_to=req.time_range_to or None,
        tags=tags,
    )
    if updated is None:
        raise HTTPException(status_code=404, detail="Report not found")
    return updated


@app.delete("/api/reports/{report_id}", status_code=204)
async def delete_report(report_id: str):
    deleted = await ReportCache.delete_report(report_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Report not found")


@app.get("/api/reports")
async def list_reports(q: str = Query("", description="Filter by title, tags, or description")):
    reports = await ReportCache.list_reports()
    if q:
        q_lower = q.lower()
        reports = [
            r for r in reports
            if q_lower in r["report_title"].lower()
            or q_lower in r["report_description"].lower()
            or any(q_lower in tag.lower() for tag in r["tags"])
        ]
    return reports


# Mount the document API router
app.include_router(document_router, prefix="/api")

# Serve static files from the html directory
html_path = os.path.join(os.path.dirname(__file__), "../html")
app.mount("/", StaticFiles(directory=html_path, html=True), name="html")

# uvicorn api.main:app --reload --port 8000
