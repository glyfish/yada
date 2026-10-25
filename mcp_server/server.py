"""yada MCP server.

Exposes yada's capabilities to an MCP client (Goose), which supplies the agent.
This is the first slice of the migration described in
``sefer/planning/yada-mcp-migration-plan.md``: one tool, wrapping the existing
deterministic ``render_report_plot``.

Design rules this server follows, from §5.3 and §5.4 of that plan:

* **Id-passing.** Tools take ids and return rendered artifacts. The model never
  holds series values, so it cannot paraphrase or interpolate them.
* **The chart is shown by an App.** A tool result means the *client* decides how
  output appears, and Goose collapses images behind an expander. An App means yada
  decides, and it is the only component that can read ``hostContext.theme``.
* **Thin shell.** Everything SDK-specific lives in this module; tool bodies
  delegate immediately into existing app code — which is what kept the
  ``FastMCP`` → ``MCPServer`` move to three edits.

Runs on the ``mcp>=2`` line. SSE is still supported there; what 2.0 changed
was the class name and where the transport knobs live.
"""
from __future__ import annotations

import logging
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[1]


def _logs_to_stderr() -> None:
    """Move every stdout log handler to stderr.

    On a stdio server **stdout is the JSON-RPC channel**, so one log line
    interleaved with the protocol makes the client reject the server. `lib.logger`
    attaches a `StreamHandler(sys.stdout)` (navi/lib/logger.py:24).

    This must run *before* the app imports: `apps.agentic.core.checkpointer`
    builds its saver at import time and warns on failure, which would otherwise
    reach stdout before anything could redirect it.
    """
    for log in [logging.getLogger()] + [
        logging.getLogger(n) for n in logging.root.manager.loggerDict
    ]:
        for handler in log.handlers:
            if isinstance(handler, logging.StreamHandler) and handler.stream is sys.stdout:
                handler.setStream(sys.stderr)


_logs_to_stderr()

# Put yada's root on sys.path so `apps`, `api` and `lib` resolve however this was
# started. The client spawns us, and it decides the working directory: running
# from anywhere but the repo root otherwise fails with
# "No module named 'mcp_server'" or "No module named 'apps'". Anchored to
# __file__, so it holds for `python -m mcp_server.server` and for an absolute
# path to this file alike.
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

# Load .env before any app imports: the agent tree builds LLM clients at import
# time and needs provider/API-key env vars already set. (Same ordering as api/main.py.)
load_dotenv(ROOT / ".env")

# The checkpointer defaults to "./.langgraph/state.sqlite", i.e. relative to the
# working directory the client chose for us. From a read-only or unexpected cwd it
# fails and warns at import time. Anchor it to the repo so it is cwd-independent.
os.environ.setdefault("YADA_CHECKPOINT_DIR", str(ROOT / ".langgraph"))

import base64  # noqa: E402
import hashlib  # noqa: E402
import re  # noqa: E402
from importlib.metadata import version as _pkg_version  # noqa: E402

from mcp.server.apps import Apps  # noqa: E402
from mcp.server.mcpserver import MCPServer  # noqa: E402
from mcp.types import ImageContent, TextContent  # noqa: E402

import shortuuid  # noqa: E402
from langchain_core.messages import HumanMessage  # noqa: E402
from langchain_core.runnables import RunnableConfig  # noqa: E402

from apps.agentic.agents.plots.time_series_report_plot_agent import render_report_plot  # noqa: E402
from apps.agentic.core.agents.messages import WorkerState  # noqa: E402
from apps.agentic.db.report_cache import ReportCache  # noqa: E402
from apps.agentic.db.series_cache import SeriesCache  # noqa: E402
from apps.agentic.db.vocabulary import Vocabulary  # noqa: E402
from apps.core.environment import current_environment, verify_database  # noqa: E402
from mcp_server.document_tools import register as register_document_tools  # noqa: E402
from mcp_server.plot_app import HTML as PLOT_APP_HTML, meta_for  # noqa: E402

from lib.logger import get_logger  # noqa: E402

logger = get_logger("YADA")
_logs_to_stderr()  # get_logger may have attached a fresh stdout handler

#: Transport is selectable so the same server serves a local client over stdio and a
#: remote one over HTTP. Defaults to stdio, which is what Goose spawns.
#:   stdio            — client spawns this process; no network (default)
#:   streamable-http  — single endpoint at <host>:<port>/mcp; the current spec transport
#:   sse              — legacy two-endpoint form; what meida still runs
TRANSPORT = os.getenv("YADA_MCP_TRANSPORT", "stdio")
HOST = os.getenv("YADA_MCP_HOST", "127.0.0.1")  # loopback: see the warning in run()
PORT = int(os.getenv("YADA_MCP_PORT", "8081"))  # 8000 is the yada API, 8080 is meida

#: Reply with plain JSON rather than an SSE-framed stream.
#:
#: This is not cosmetic -- it decides which clients can connect at all. With SSE
#: framing the SDK demands the client send BOTH content types and answers 406
#: otherwise (mcp/server/streamable_http.py:462). Goose's rmcp client does not,
#: so it fails to add the extension with "406 Not Acceptable" in the server log.
#: With json_response the check relaxes to application/json alone (:452-454),
#: which is strictly more permissive -- a client sending both still passes.
#: We send no progress notifications, so nothing needs the stream.
JSON_RESPONSE = os.getenv("YADA_MCP_JSON_RESPONSE", "1") not in ("0", "false", "False")

#: mcp 2.x took the transport knobs off the constructor -- host, port and
#: json_response are run()/app-factory keywords now, and the factories do NOT fall
#: back to anything set here. They must be passed at the call site in run().
#: Reported in serverInfo and in the startup log. The SDK version goes alongside
#: it because an SDK mismatch is invisible otherwise -- mcp 2.3.0 sat in this env
#: for a week against 1.x code before anyone noticed.
VERSION = "0.1.0"
MCP_VERSION = _pkg_version("mcp")

#: The chart is shown by an App rather than returned as a bare image block, so
#: yada controls the presentation (Goose collapses tool-result images behind an
#: expander) and so the app can read hostContext.theme. See plan §5.4.
PLOT_URI = "ui://yada/plot"

apps = Apps()
#: Stamped into the page so a stale build is visible at a glance rather than
#: mistaken for a code bug: the client caches nothing, but the SERVER must be
#: restarted for an edit to plot_app.py to take effect.
APP_BUILD = hashlib.sha256(PLOT_APP_HTML.encode()).hexdigest()[:6]

apps.add_html_resource(
    PLOT_URI,
    PLOT_APP_HTML.replace("__BUILD__", APP_BUILD),
    name="yada-plot",
    title="yada chart",
    description="Displays a chart returned by the plot tools.",
)

# `server` is constructed AFTER the tool definitions below: MCPServer collects an
# extension's tools at construction, so decorators that run later are invisible to it.

#: The plotting code writes the PNG under html/plots/ but hands back a URL-shaped
#: "./plots/<name>.png" for the static mount in api/main.py. Only the <img src>
#: escapes render_report_plot, so recover the name and resolve it on disk.
PLOT_DIR = ROOT / "html" / "plots"
_IMG_SRC = re.compile(r'<img src="([^"]+)"')


def _plot_file(html: str) -> Path | None:
    """Resolve the PNG that `html` references, or None if it cannot be found."""
    match = _IMG_SRC.search(html)
    if not match:
        return None
    path = PLOT_DIR / match.group(1).rsplit("/", 1)[-1]
    return path if path.is_file() else None


def _as_image(path: Path) -> ImageContent:
    data = base64.b64encode(path.read_bytes()).decode()
    logger.info(f"returning {path.name} ({path.stat().st_size} bytes)")
    return ImageContent(type="image", data=data, mime_type="image/png")


def _split_html(output: str) -> tuple[str, list[Path]]:
    """Split an agent's HTML output into prose and the PNGs it references.

    Plot tools return ``<div class="..."><img src="./plots/x.png"></div>``, and the
    bar-chart agent prepends markdown commentary. Strip the image markup, keep the
    rest as text, and resolve each image on disk.
    """
    files: list[Path] = []
    for src in _IMG_SRC.findall(output):
        path = PLOT_DIR / src.rsplit("/", 1)[-1]
        if path.is_file():
            files.append(path)
        else:
            logger.warning(f"agent referenced a missing plot file: {src}")
    text = re.sub(r'<div class="[^"]*">\s*<img src="[^"]+">\s*</div>', "", output)
    # The plot agents' model intermittently echoes the wrapper's class name as a
    # pseudo-tag -- a stray "</bar-chart>" on its own line. It survives the rule
    # above (no <img> inside) and renders as literal text in the app, which escapes
    # HTML. Strip the known wrapper names, and any tag left alone on a line.
    text = re.sub(r"</?(?:bar-chart|multi-bar-chart|time-series-plot)>", "", text)
    text = re.sub(r"^\s*</?[A-Za-z][\w-]*\s*/?>\s*$", "", text, flags=re.MULTILINE)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip(), files


_initialized = False


def _initialize() -> None:
    """Verify the database and wire the caches. Idempotent."""
    global _initialized
    if _initialized:
        return
    environment = current_environment()
    logger.info(f"Starting yada MCP server: {verify_database(environment)}")
    SeriesCache.initialize(environment.db_url)
    ReportCache.initialize(environment.db_url)
    # Rows only -- no Chroma scan. Rebuilding here would add 34 s to every boot of
    # a server that stays up for days, and even verifying costs 3.8 s on the code
    # store, so staleness is checked lazily on first use instead.
    Vocabulary.initialize(environment.db_url)
    _initialized = True


_plot_agent = None


@apps.tool(
    resource_uri=PLOT_URI,
    visibility=["model", "app"],
    meta=meta_for(PLOT_URI, ["model", "app"]),
    name="plot",
    description=(
        "Create a chart from data supplied in the request and return it as an image. "
        "Handles time series (trends over time, comparisons, stacked series) and bar "
        "charts (categorical or labelled data). Send a plain-language request such as "
        "'Plot a time series for the population of Tennessee' or 'Compare the "
        "population of Tennessee and Alabama over time'. Include the data points in "
        "the request when you have them. "
        "Note: this charts whatever it is given — it does not look anything up, and "
        "the result carries no provenance. For a chart of stored series with a "
        "report_id behind it, use plot_report instead."
    ),
)
async def plot(request: str) -> list[TextContent | ImageContent]:
    """Delegate to PlotAgent, which routes between bar charts and time series."""
    global _plot_agent
    _initialize()

    if _plot_agent is None:
        # Built lazily: constructing it makes an LLM client, which should not be a
        # cost of merely listing tools.
        from apps.agentic.agents.plots.plot_agent import PlotAgent

        _plot_agent = PlotAgent()

    state: WorkerState = {"messages": [HumanMessage(content=request)]}
    config = RunnableConfig(
        configurable={"thread_id": shortuuid.uuid()}, recursion_limit=50
    )
    try:
        result = await _plot_agent.agent.ainvoke(state, config)
    except Exception as exc:
        logger.warning(f"plot({request!r}) failed: {exc}")
        return [TextContent(type="text", text=f"Could not create the plot: {exc}")]

    output = str(result["messages"][-1].content)
    text, files = _split_html(output)

    if not files:
        # No chart was produced. Say so plainly rather than returning prose that
        # could be mistaken for a result.
        logger.warning(f"plot({request!r}) produced no image")
        return [TextContent(type="text", text=text or "No chart was produced.")]

    content: list[TextContent | ImageContent] = []
    if text:
        content.append(TextContent(type="text", text=text))
    content.extend(_as_image(f) for f in files)
    return content


@apps.tool(
    resource_uri=PLOT_URI,
    visibility=["model", "app"],
    meta=meta_for(PLOT_URI, ["model", "app"]),
    name="plot_report",
    description=(
        "Render a stored time series report as a chart and return it as an image. "
        "Takes a report UUID, or a case-insensitive substring of the report title. "
        "The chart is drawn from the series cached under that report — it is never "
        "built from values supplied in the request, so the returned numbers are "
        "always the stored ones. Plot type and axis scale are chosen automatically "
        "from the series count and their units. Use this whenever the user asks to "
        "see, plot, chart or visualise a report they have already created."
    ),
)
async def plot_report(report_id_or_title: str) -> list[TextContent | ImageContent]:
    _initialize()

    try:
        result = await render_report_plot(report_id_or_title)
    except ValueError as exc:
        # Report missing, or no series could be loaded. Fail loudly rather than
        # returning an empty success the model might paper over with prose.
        logger.warning(f"plot_report({report_id_or_title!r}) failed: {exc}")
        return [TextContent(type="text", text=f"Could not plot report: {exc}")]

    summary = (
        f"{result['report_title']} — {result['plot_type']} plot of "
        f"{result['series_count']} series (report_id {result['report_id']})"
    )

    plot_file = _plot_file(result["html"])
    if plot_file is None:
        logger.error(f"plot_report: rendered {result['report_id']} but found no PNG")
        return [TextContent(type="text", text=f"{summary}\n\n(plot file missing)")]

    return [TextContent(type="text", text=summary), _as_image(plot_file)]


server = MCPServer("yada", version=VERSION, extensions=[apps])

# After the server exists, not before -- the opposite of the @apps.tool rule above,
# which has to be earlier because MCPServer collects extension tools at construction.
# These are registered with add_tool because their descriptions are generated from the
# vocabulary, and a decorator takes a literal. Needs the database, so initialize first;
# that is a Postgres connect and a reflect, with no Chroma scan.
_initialize()
register_document_tools(server)


def run() -> None:
    """Start the server on the transport named by YADA_MCP_TRANSPORT.

    Over a network transport the server is **unauthenticated**: anything that can
    reach the port can plot, and `plot_report` reads the report store. The default
    binds loopback only. Before setting YADA_MCP_HOST to 0.0.0.0, put a
    `token_verifier`/`auth` on the FastMCP constructor or a reverse proxy in front —
    both are supported by this SDK version.
    """
    if TRANSPORT == "stdio":
        logger.info(f"Starting yada MCP server {VERSION} (mcp {MCP_VERSION}, transport=stdio)")
    else:
        path = "/mcp" if TRANSPORT == "streamable-http" else "/sse"
        logger.info(
            f"Starting yada MCP server {VERSION} (mcp {MCP_VERSION}) on "
            f"http://{HOST}:{PORT}{path} (transport={TRANSPORT})"
        )
        if HOST not in ("127.0.0.1", "localhost", "::1"):
            logger.warning(
                f"yada MCP server is bound to {HOST} with no authentication configured"
            )

    # Each transport takes its own keywords in 2.x, so dispatch rather than pass
    # one bag. json_response is load-bearing for Goose (see its note above) and is
    # NOT inherited from anywhere — omitting it here silently restores SSE framing
    # and the 406 it causes.
    if TRANSPORT == "streamable-http":
        server.run(transport="streamable-http", host=HOST, port=PORT,
                   json_response=JSON_RESPONSE)
    elif TRANSPORT == "sse":
        server.run(transport="sse", host=HOST, port=PORT)
    else:
        server.run(transport="stdio")


if __name__ == "__main__":
    run()
