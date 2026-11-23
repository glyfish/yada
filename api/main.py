# backend/main.py
import asyncio
import os
import json
import re
import uuid
from contextlib import asynccontextmanager
from typing import Any, Dict, Optional

from pathlib import Path
from dotenv import load_dotenv

# Load .env before any app imports: the agent tree builds LLM clients at
# import time and needs provider/API-key env vars already set.
load_dotenv(Path(__file__).resolve().parents[1] / ".env")

import langsmith
from fastapi import Depends, FastAPI, HTTPException, Query, Request, Response
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
from apps.agentic.agents.plots.time_series_report_plot_agent import render_report_plot
from apps.agentic.core.agents.series_metadata import report_metadata_from_series
from apps.agentic.core.agents.llm_filter_extractor import extract_etf_filters, extract_fred_filters
from apps.agentic.agents.data.series_fetch import fetch_series_into_cache, SERIES_SOURCE_SPECS
from apps.agentic.agents.document.document_agent import search_series_rows
from apps.agentic.core.pricing import estimate_cost
from apps.core.environment import current_environment, verify_database
from api.document_router import router as document_router
from apps.core import identity

#: Secure cookies are dropped by the browser over plain http, which is how this is
#: served locally. On anything but localhost the cookie must be Secure or the token
#: travels in clear text.
_COOKIE_SECURE = os.environ.get("YADA_COOKIE_SECURE", "0") not in ("0", "false", "False")


# ---------------------------------------------------------------------------
# Who is calling
# ---------------------------------------------------------------------------
#: Where the browser keeps its token. The cookie carries the TOKEN ITSELF, not an
#: opaque session id, and the server stores nothing against it -- resolution is the same
#: per-request hash-and-lookup the Authorization header gets. So this is not a session:
#: revocation still lands on the next request, a restart logs nobody out, and there is
#: no session table to expire or invalidate.
#:
#: It exists because the browser should not hold the token anywhere JavaScript can read
#: it. The feed renders model-authored markdown into innerHTML by design, which is an
#: injection path that sessionStorage would be exposed to and HttpOnly is not.
SESSION_COOKIE = "yada_token"


async def current_caller(request: Request) -> identity.Caller:
    """Resolve the bearer token to a caller, or ANONYMOUS when no users are configured.

    The chat endpoints need the whole `Caller`, not just the id: they install it for the
    duration of the agent run so the report tools -- plain `@staticmethod`s with no
    request context -- can read it, and the name is what makes the log line legible.
    """
    token = identity.bearer_of(request.headers) or request.cookies.get(SESSION_COOKIE)
    try:
        return identity.resolve(token)
    except identity.AuthRequired as exc:
        raise HTTPException(status_code=401, detail=str(exc),
                            headers={"WWW-Authenticate": "Bearer"})


async def current_owner(request: Request) -> str | None:
    """Resolve the bearer token to an owner, or None when no users are configured.

    Shares `mcp_server.identity` with the MCP server so there is one credential story
    and one place revocation takes effect, rather than an HTTP surface that drifts from
    the tool surface. Returns None -- scoping off -- while `app_user` is empty, which is
    what keeps the single-user local setup working untouched.

    Unlike the MCP path, this CAN answer 401. `ServerMiddleware` runs after the request
    is accepted, so a bad token there is a JSON-RPC error; here it is the real status
    with a WWW-Authenticate challenge, which is what a browser and any OAuth-capable
    client expect.
    """
    return (await current_caller(request)).user_id

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
    # Which database this process serves, checked before anything touches it: the
    # schema must be at the code's alembic head (DatabaseStateError aborts startup).
    environment = current_environment()
    logger.info(f"Starting yada: {verify_database(environment)}")
    SeriesCache.initialize(environment.db_url)
    ReportCache.initialize(environment.db_url)
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
async def generate_markdown(req: RequestPayload,
                            caller: identity.Caller = Depends(current_caller)):
    session_id = req.session_id or str(uuid.uuid4())
    logger.debug(f"YADA request [{session_id}] ({caller.name}): {req.input}")

    orchestrator = await OrchestratorAgent.create()
    config = RunnableConfig(configurable={"thread_id": session_id}, recursion_limit=50)
    with identity.scoped(caller):
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
async def stream_request(req: RequestPayload,
                         caller: identity.Caller = Depends(current_caller)):
    session_id = req.session_id or str(uuid.uuid4())
    logger.debug(f"YADA stream request [{session_id}] ({caller.name}): {req.input}")

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

    async def _stream_events():
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

    async def event_generator():
        # The caller is installed around the generator's whole run, not around the
        # endpoint: the body is produced after the endpoint returns, and the report
        # tools the agent may call read the owner from this contextvar.
        with identity.scoped(caller):
            async for item in _stream_events():
                yield item

    return EventSourceResponse(event_generator())


class ResumePayload(BaseModel):
    session_id: str
    form_data: Dict[str, Any]


@app.post("/api/request/resume")
async def resume_request(req: ResumePayload,
                         caller: identity.Caller = Depends(current_caller)):
    logger.debug(f"YADA resume request [{req.session_id}] ({caller.name}): {req.form_data}")

    orchestrator = await OrchestratorAgent.create()
    config = RunnableConfig(configurable={"thread_id": req.session_id})

    async def _resume_events():
        final_result = ""
        root_run_id = None

        try:
            # A resume only makes sense against a thread paused at an interrupt.
            # If the thread has no pending interrupt — its session was lost on a
            # server restart, or the form was already submitted — resuming would
            # start the graph from scratch with empty input and fail with a cryptic
            # "at least one message is required" 400. Detect that and report clearly.
            snapshot = await orchestrator.agent.aget_state(config)
            if not snapshot.next:
                logger.warning(f"Resume with no pending interrupt [{req.session_id}]; ignoring.")
                yield {
                    "event": "error",
                    "data": json.dumps({
                        "message": "This form is no longer active — its session was lost "
                                   "(the server likely restarted). Please make the request again.",
                    }),
                }
                return

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

    async def event_generator():
        # Same as the stream endpoint: installed around the generator, because the
        # agent -- and any report tool it calls -- runs while the body is streamed.
        with identity.scoped(caller):
            async for item in _resume_events():
                yield item

    return EventSourceResponse(event_generator())


class SessionPayload(BaseModel):
    token: str


@app.post("/api/session")
async def create_session(req: SessionPayload, response: Response):
    """Exchange a token for the cookie the browser will send from then on.

    Not a login in the session sense -- nothing is created server-side. This validates
    the token once so the UI can report a bad one immediately rather than on the next
    data request, and parks it somewhere JavaScript cannot read.
    """
    try:
        caller = identity.resolve(req.token)
    except identity.AuthRequired as exc:
        raise HTTPException(status_code=401, detail=str(exc),
                            headers={"WWW-Authenticate": "Bearer"})
    if caller.user_id is None:
        # No users configured, so the server is not checking anything. Say so rather
        # than setting a cookie that means nothing.
        return {"authenticated": False, "name": caller.name,
                "detail": "This server has no users configured; no token is required."}
    response.set_cookie(
        SESSION_COOKIE, req.token,
        httponly=True,       # the whole point: JS, including injected JS, cannot read it
        samesite="strict",   # the cookie is sent automatically, so this is the CSRF guard
        secure=_COOKIE_SECURE,
        path="/",
    )
    return {"authenticated": True, "name": caller.name, "user_id": caller.user_id}


@app.delete("/api/session", status_code=204)
async def end_session(response: Response):
    response.delete_cookie(SESSION_COOKIE, path="/")


@app.get("/api/session")
async def whoami(request: Request):
    """Who the browser currently is, without 401ing when it is nobody.

    The UI calls this on load to decide whether to prompt, so it must distinguish
    "no token" from "bad token" without the failure being an error.
    """
    token = identity.bearer_of(request.headers) or request.cookies.get(SESSION_COOKIE)
    try:
        caller = identity.resolve(token)
    except identity.AuthRequired as exc:
        return {"authenticated": False, "required": True, "detail": str(exc)}
    return {"authenticated": caller.user_id is not None, "required": caller.user_id is not None,
            "name": caller.name, "user_id": caller.user_id}


@app.post("/api/reports/{report_id}/plot")
async def plot_report(report_id: str, owner: str | None = Depends(current_owner)):
    """
    Render a report's plot deterministically — no LLM, no agent hops. This is the
    cheap path the UI 'Plot Report' button uses instead of resuming the agent graph.

    Note the path segment reaches a resolver that also accepts a title SUBSTRING, so
    this route is a title search as much as an id lookup. Scoping it matters more than
    it looks: unscoped, `/api/reports/GDP/plot` would reach any user's "GDP Overview".
    """
    try:
        return await render_report_plot(report_id, owner=owner)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        logger.error(f"plot_report {report_id} failed: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to render plot: {e}")


@app.get("/api/reports/{report_id}")
async def get_report(report_id: str, owner: str | None = Depends(current_owner)):
    record = await ReportCache.get_by_report_id(report_id, owner=owner)
    if record is None:
        raise HTTPException(status_code=404, detail="Report not found")
    return {
        "report_id": str(record["report_id"]),
        "report_title": record["report_title"],
        "report_description": record.get("report_description") or "",
        "created_by": str(record["created_by"]) if record.get("created_by") else None,
        "metadata": dict(record.get("metadata") or {}),
        "time_range_from": str(record.get("time_range_from") or ""),
        "time_range_to": str(record["time_range_to"]) if record.get("time_range_to") else None,
        "time_series_info": [
            {
                "cache_id": entry.get("cache_id", ""),
                "native_id": entry.get("native_id", ""),
                "title": entry.get("title", ""),
                "source": entry.get("source", ""),
            }
            for entry in (record.get("time_series_info") or [])
        ],
    }


class UpdateReportPayload(BaseModel):
    report_title: str
    report_description: str
    time_series_ids: str
    time_range_from: str
    time_range_to: Optional[str] = None


@app.put("/api/reports/{report_id}")
async def update_report(report_id: str, req: UpdateReportPayload,
                        owner: str | None = Depends(current_owner)):
    ids = [s.strip() for s in req.time_series_ids.split(",") if s.strip()]

    time_series_info: list[TimeSeriesInfoEntry] = []
    missing: list[str] = []
    for cache_id in ids:
        entry = SeriesCache._get_by_cache_id_sync(cache_id, include_expired=True)
        if not entry:
            missing.append(cache_id)
            continue
        raw_metadata = entry.get("metadata")
        metadata = raw_metadata if isinstance(raw_metadata, dict) else {}
        time_series_info.append({
            "cache_id": str(entry["cache_id"]),
            "title": str(entry.get("title") or ""),
            "source": str(entry.get("source") or ""),
            "native_id": str(entry.get("native_id") or ""),
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
        metadata=report_metadata_from_series(time_series_info),
        owner=owner,
    )
    # 404 whether the report is absent or belongs to someone else. Distinguishing them
    # would turn this into a probe for other people's report ids.
    if updated is None:
        raise HTTPException(status_code=404, detail="Report not found")
    return updated


@app.delete("/api/reports/{report_id}", status_code=204)
async def delete_report(report_id: str, owner: str | None = Depends(current_owner)):
    deleted = await ReportCache.delete_report(report_id, owner=owner)
    if not deleted:
        raise HTTPException(status_code=404, detail="Report not found")


async def _reports_matching_filter(phrase: str, source: str = "",
                                   owner: str | None = None) -> list[dict]:
    """
    Reports whose merged metadata satisfies a natural-language constraint (e.g.
    'government bonds', 'VanEck funds'), reusing the document-search filter extractors
    and the source-keyed metadata filter.

    The ETF and FRED vocabularies overlap (words like 'treasury'/'government' live in
    both catalogs) and the extractors ignore the store name, so `source` scopes which
    extractor applies: 'etf' -> ETF only, 'fred' -> FRED only. When the request names
    no store (source empty) a report matches the ETF *or* the FRED reading. Falls back
    to all reports when the phrase yields no recognizable filter.
    """
    source = (source or "").strip().lower()
    plan = {
        "etf": [(extract_etf_filters, "tiingo")],
        "fred": [(extract_fred_filters, "fred")],
    }.get(source, [(extract_etf_filters, "tiingo"), (extract_fred_filters, "fred")])

    matched: dict[str, dict] = {}
    any_filter = False
    for extractor, cache_source in plan:
        where, _ = await extractor(phrase)
        if where is None:
            continue
        any_filter = True
        for r in await ReportCache.list_reports(source=cache_source, where=where,
                                                owner=owner):
            matched[r["report_id"]] = r
    if any_filter:
        return sorted(matched.values(), key=lambda r: r["report_title"])

    # The phrase didn't map to the scoped store's vocabulary. Still honor an explicit
    # source by returning reports that contain that store's data; with no source given,
    # the request is genuinely unfilterable, so show everything.
    all_reports = await ReportCache.list_reports(owner=owner)
    src_key = {"etf": "tiingo", "fred": "fred"}.get(source)
    if src_key:
        return [r for r in all_reports if src_key in (r.get("metadata") or {})]
    return all_reports


@app.get("/api/reports")
async def list_reports(
    q: str = Query("", description="Filter by title or description"),
    metadata_filter: str = Query("", alias="filter", description="Natural-language metadata filter, e.g. 'government bonds'"),
    source: str = Query("", description="Restrict the metadata filter to a store: 'etf' or 'fred'"),
    owner: str | None = Depends(current_owner),
):
    # `q` filters in Python AFTER the fetch, so the fetch itself has to be scoped --
    # otherwise a title search would narrow a list it should never have been given.
    reports = (await _reports_matching_filter(metadata_filter, source, owner=owner)
               if metadata_filter else await ReportCache.list_reports(owner=owner))
    if q:
        q_lower = q.lower()
        reports = [
            r for r in reports
            if q_lower in r["report_title"].lower()
            or q_lower in r["report_description"].lower()
        ]
    return reports


@app.get("/api/series/search")
async def search_series(
    source: str = Query(..., description="Search source: 'etf' or 'fred'"),
    q: str = Query(..., description="Natural-language search query"),
):
    """
    Structured search over the ETF or FRED metadata store, returning selectable
    rows for the report-builder table. Uses the same LLM filter extraction as the
    chat search agents. Rows carry the fetch source ('tiingo' for ETFs, 'fred' for
    FRED) so each selection can be handed straight to /api/series/fetch.
    """
    src = source.strip().lower()
    if src not in ("etf", "fred"):
        raise HTTPException(status_code=400, detail="source must be 'etf' or 'fred'")
    if not q.strip():
        raise HTTPException(status_code=400, detail="q is required")
    try:
        rows = await search_series_rows(src, q)
    except Exception as e:
        logger.error(f"search_series {src} q={q!r} failed: {e}")
        raise HTTPException(status_code=502, detail=f"Search failed: {e}")
    return {"source": src, "query": q, "rows": rows}


class FetchSeriesPayload(BaseModel):
    source: str
    native_id: str


@app.post("/api/series/fetch")
async def fetch_series(req: FetchSeriesPayload):
    """
    Fetch a single series from its source into SeriesCache and return the resulting
    cache entry. Idempotent — a second call for the same series returns the existing
    cache_id. This is the bridge from a search result (source + native_id) to the
    cache_id a report is built from.
    """
    source = req.source.strip().lower()
    native_id = req.native_id.strip()
    if not native_id:
        raise HTTPException(status_code=400, detail="native_id is required")
    if source not in SERIES_SOURCE_SPECS:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported source '{req.source}'. Expected one of: {', '.join(SERIES_SOURCE_SPECS)}",
        )

    try:
        entry = await fetch_series_into_cache(source, native_id)
    except Exception as e:
        logger.error(f"fetch_series {source}:{native_id} failed: {e}")
        raise HTTPException(status_code=502, detail=f"Failed to fetch series: {e}")
    if entry is None:
        raise HTTPException(
            status_code=503,
            detail="MCP tool unavailable. Is the MCP server running?",
        )

    return {
        "cache_id": str(entry["cache_id"]),
        "source": str(entry.get("source") or source),
        "native_id": str(entry.get("native_id") or native_id),
        "title": str(entry.get("title") or ""),
        "frequency": str(entry.get("frequency") or ""),
        "units": str(entry.get("units") or ""),
        "observation_start": str(entry.get("observation_start") or ""),
        "observation_end": str(entry.get("observation_end") or ""),
        "observation_count": int(entry.get("observation_count") or 0),
    }


# Mount the document API router
app.include_router(document_router, prefix="/api")

# Serve static files from the html directory
html_path = os.path.join(os.path.dirname(__file__), "../html")
app.mount("/", StaticFiles(directory=html_path, html=True), name="html")

# uvicorn api.main:app --reload --port 8000
