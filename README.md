# YADA

A conversational, multi-agent system for economic and financial **data analysis**. YADA pairs a
FastAPI backend with a LangGraph agent orchestrator and a web UI: ask a question in natural
language and the agents search data sources, fetch and cache time series, run statistical
analysis, and generate plots and reports.

## Dependency on `navi`

> **YADA requires the [`navi`](https://github.com/glyfish/navi) library and does not run without it.**

YADA is the agent/application layer; **[`navi`](https://github.com/glyfish/navi) is the underlying quantitative-finance
library** it is built on. `navi` provides the `lib` package that YADA imports throughout
(`from lib.logger import get_logger`, API clients, statistical models, plots, DB helpers, and the
MCP client).

It is wired up as an **editable install of a sibling directory** — the first line of
[`requirements.in`](requirements.in) is:

```text
-e ../navi
```

This means:

- `navi` must be cloned **next to** `yada` so the layout is:

  ```text
  gly.fish/
  ├── navi/      # the library (provides the `lib` package) — required
  ├── meida/     # the MCP data server (FRED/Tiingo over SSE) — required to run
  └── yada/      # this repo
  ```

- Installing YADA's requirements (`pip install -r requirements.txt`) installs `navi` in editable
  mode, so local changes to `navi` are picked up immediately.
- The data API clients (FRED, Tiingo, BLS) and the SSE **MCP client** live in `navi`; YADA calls
  them through the agents and the MCP tool registry.

See [navi's README](https://github.com/glyfish/navi) for the library's own setup and feature list.

## Architecture

A single **orchestrator** agent ([`apps/agentic/agents/orchestrator.py`](apps/agentic/agents/orchestrator.py))
receives each request and delegates to specialized sub-agents:

| Delegate | Responsibility |
| --- | --- |
| `delegate_to_document_agent` | RAG search over local ChromaDB stores — FRED metadata, ETF/mutual-fund info, GitHub code repos, PDF & research libraries |
| `delegate_to_time_series_agent` | Fetch time series from external sources via the MCP server and cache them |
| `delegate_to_data_info_agent` | Inspect already-cached series and report metadata |
| `delegate_to_plot_agent` | Build charts, time-series plots, and report plots |
| `delegate_to_search_agent` | Web search (Tavily) for anything not covered by the local stores |

Supporting pieces:

- **LLMs** via LangChain — OpenAI or Anthropic, selectable through env vars.
- **Vector stores** — ChromaDB collections persisted under `.db/` (FRED, ETF, GitHub, research, PDF).
- **Relational cache** — PostgreSQL (SQLAlchemy + Alembic) holding the time-series cache and saved reports.
- **MCP** — the agents fetch live data through the [`meida`](https://github.com/glyfish/meida) MCP server (FastMCP, FRED/Tiingo tools over SSE).
- **Web UI** — a static frontend in `html/`, served at `/`.
- **Tracing** — optional LangSmith integration.

## Repository layout

```text
api/                 FastAPI app (api.main:app) and routers
apps/agentic/        Agent orchestrator, sub-agents, document loaders, DB cache models
clients/fred/        FRED category/series data exports
alembic/             Database migrations
document_library/    Source documents for the RAG stores
research_library/
notebooks/           Jupyter notebooks for data loading and exploration
html/                Static web UI (served at /)
requirements.in      Top-level deps (includes `-e ../navi`); compiled to requirements.txt
```

## Prerequisites

- **Python 3.11** (this repo pins `3.11.11`)
- **[`navi`](https://github.com/glyfish/navi)** cloned as a sibling directory (see above)
- **PostgreSQL** for the time-series / report cache
- The **[`meida`](https://github.com/glyfish/meida)** MCP server running — exposes FRED/Tiingo tools at `MCP_URL` (default `http://localhost:8080/sse`); also a sibling repo built on `navi`
- API keys (see [Configuration](#configuration))

## Setup

```bash
# 1. Clone navi alongside yada (if not already present)
#    gly.fish/navi  and  gly.fish/yada  must be siblings
git clone <navi-repo-url> ../navi

# 2. Create and activate a Python 3.11 environment, then install.
#    This installs navi in editable mode via `-e ../navi`.
pip install -r requirements.txt

# 3. Configure environment variables
cp .env.example .env   # then edit (see Configuration below)

# 4. Run database migrations
alembic upgrade head
```

## Running

```bash
# 1. Start the meida MCP server (sibling repo) so the FRED/Tiingo tools are
#    reachable at MCP_URL. From the meida checkout:
#        python mcp_server/server.py        # serves SSE on http://localhost:8080
#    See https://github.com/glyfish/meida for its setup.

# 2. Start the API + UI
uvicorn api.main:app --reload --port 8000
```

Then open <http://localhost:8000/> — the web UI is served from `html/` at the API root.

### Key endpoints

| Method | Path | Purpose |
| --- | --- | --- |
| `POST` | `/api/request` | Submit a request (non-streaming) |
| `POST` | `/api/request/stream` | Submit a request with streamed (SSE) responses |
| `POST` | `/api/request/resume` | Resume a run paused for human input |
| `GET` | `/api/reports`, `/api/reports/{id}` | List / fetch saved reports |
| `PUT` / `DELETE` | `/api/reports/{id}` | Update / delete a report |

## Configuration

Environment variables are loaded from `.env` at startup. The data-source keys (`FRED_API_KEY`,
`BLS_API_KEY`, Tiingo) are shared with `navi` — see [navi's .env.example](https://github.com/glyfish/navi/blob/main/.env.example).

| Variable | Required | Description |
| --- | --- | --- |
| `OPENAI_API_KEY` | yes¹ | OpenAI key (default LLM provider) |
| `ANTHROPIC_API_KEY` | yes¹ | Anthropic key (if `LLM_MODEL_PROVIDER=anthropic`) |
| `LLM_MODEL_PROVIDER` | no | `openai` (default) or `anthropic` |
| `AGENT_LLM_MODEL` | no | Orchestrator/agent model (default `gpt-4.1`) |
| `FILTER_LLM_MODEL` / `SCORING_LLM_MODEL` | no | Models for query-filter extraction and RAG scoring |
| `FRED_API_KEY` | yes | Federal Reserve Economic Data |
| `BLS_API_KEY` | no | Bureau of Labor Statistics |
| `TAVILY_API_KEY` | yes | Web search |
| `GITHUB_API_KEY` | no | Loading GitHub repos into the code RAG store |
| `YADA_DB_URL` | yes | PostgreSQL connection string for the cache |
| `MCP_URL` | no | MCP server URL (default `http://localhost:8080/sse`) |
| `RAG_SCORE_THRESHOLD` | no | Minimum similarity score for RAG retrieval |
| `YADA_CHECKPOINT_DIR` | no | LangGraph checkpoint directory (default `.langgraph`) |
| `LANGCHAIN_TRACING_V2`, `LANGCHAIN_API_KEY` / `LANGSMITH_API_KEY`, `LANGCHAIN_PROJECT` | no | LangSmith tracing |

¹ Provide the key matching your selected `LLM_MODEL_PROVIDER`.

## Notebooks

`notebooks/` contains Jupyter notebooks for loading the document stores (e.g.
`notebooks/documents/etf_document_loader.ipynb`) and exploring data. They import the same
`apps.agentic` and `navi` code as the application, so the editable `navi` install must be in place.
