"""
The two tools that make a chart real: fetch a series into the cache, plot from the cache.

Why these exist
---------------
Asked to plot US GDP, the chain produced a correct-looking chart of **invented numbers**.
The leaf agent said so in a message the plumbing then discarded -- *"I don't have a live
data connection to pull the exact GDP figures"* -- and supplied 22 values from memory,
2.4% out on average and 6.8% at worst. It was not a bug: `search_fred` can tell a client
that `GDP` exists, nothing on the MCP surface could hand back its observations, and
`plot` charts whatever it is given. Fabrication was the only route available.

`server.py`'s own rule says why that matters:

    Tools take ids and return rendered artifacts. The model never holds series values,
    so it cannot paraphrase or interpolate them.

The rule was never violated. There was simply no tool obeying it, so these two are it:
`fetch_fred_series` returns a cache id and no observations, `plot_series` renders from
the cache and never from the request. Between them the model holds ids and pictures,
never numbers.

They ship together on purpose. A `plot_series` without a fetch is unreachable -- no
other tool on this server mints a cache id -- and a fetch without a plot just moves the
observations somewhere the client cannot use.

The registry, and a silent failure it was already causing
---------------------------------------------------------
`fetch_series_into_cache` needs `MCPToolRegistry` holding meida's tools, and this server
never initialised it: `_initialize()` in server.py is sync and runs at import, while
`MCPToolRegistry.initialize` is async. So the registry was empty here, and
`render_report_plot`'s per-series refresh -- which calls the same function and swallows
failures -- has been a no-op over MCP since it was written. Every `plot_report` plotted
the persisted snapshot. The lazy initialise below fixes that too, as a side effect of
being the first caller that needs the registry to work.
"""

from __future__ import annotations

import asyncio
from time import perf_counter
from typing import Any

from mcp.types import ImageContent, TextContent

from apps.agentic.agents.data.series_fetch import (
    SERIES_SOURCE_SPECS, fetch_series_into_cache,
)
from apps.agentic.agents.plots.time_series_report_plot_agent import render_series_plot
from apps.agentic.core.constants import MCP_URL
from apps.agentic.core.mcp_tool_registry import MCPToolRegistry
from apps.agentic.db.series_cache import cache_entries_for

from lib.logger import get_logger

logger = get_logger("YADA")

#: Guards the one-time registry connect. Several tool calls can arrive concurrently and
#: `initialize` is not idempotent-safe against itself.
_registry_lock = asyncio.Lock()
_registry_ready = False


async def _ensure_registry() -> bool:
    """Connect to meida's MCP server once, lazily. True when tools are available.

    Lazy because this cannot happen at import: `MCPServer` is constructed at module
    scope in server.py and `_initialize()` there is sync, while this is async. Doing it
    on first use also means merely listing tools never dials out.
    """
    global _registry_ready
    if _registry_ready:
        return True
    async with _registry_lock:
        if _registry_ready:
            return True
        await MCPToolRegistry.initialize(
            servers={"fred": {"transport": "sse", "url": MCP_URL}},
            required=["fred_series_observations"],
        )
        _registry_ready = MCPToolRegistry.get("fred_series_observations") is not None
        if not _registry_ready:
            logger.warning(f"series_tools: no fetch tools from {MCP_URL}")
    return _registry_ready


def _log(tool: str, arguments: dict, started: float, outcome: str) -> None:
    shown = " ".join(f"{k}={v!r}" for k, v in arguments.items() if v is not None)
    logger.info(f"{tool} <- {shown} | {outcome} in {perf_counter() - started:.2f}s")


def register(server, plot_uri: str, plot_meta: dict) -> None:
    """Register fetch_fred_series and plot_series.

    `plot_uri`/`plot_meta` are passed in rather than imported because server.py defines
    them and imports this module; taking them as arguments keeps the dependency one-way.
    """

    async def fetch_fred_series(series_id: str) -> dict[str, Any]:
        started = perf_counter()
        native_id = (series_id or "").strip()
        if not native_id:
            return {"status": "error", "detail": "series_id is required."}

        if not await _ensure_registry():
            _log("fetch_fred_series", {"series_id": native_id}, started, "no registry")
            return {"status": "unavailable",
                    "detail": f"Cannot reach the data server at {MCP_URL}. The series "
                              f"was not fetched; nothing was cached."}
        try:
            entry = await fetch_series_into_cache("fred", native_id)
        except Exception as exc:
            logger.warning(f"fetch_fred_series({native_id!r}) failed: {exc}")
            _log("fetch_fred_series", {"series_id": native_id}, started, "error")
            return {"status": "error", "detail": f"Fetch failed: {exc}"}
        if entry is None:
            _log("fetch_fred_series", {"series_id": native_id}, started, "no entry")
            return {"status": "error",
                    "detail": f"No series was returned for '{native_id}'. Check the id "
                              f"with search_fred."}

        _log("fetch_fred_series", {"series_id": native_id}, started, "ok")
        return {
            "status": "ok",
            "cache_id": str(entry["cache_id"]),
            "source": str(entry.get("source") or "fred"),
            "native_id": str(entry.get("native_id") or native_id),
            "title": str(entry.get("title") or ""),
            "frequency": str(entry.get("frequency") or ""),
            "units": str((entry.get("metadata") or {}).get("units") or ""),
            "observation_start": str(entry.get("observation_start") or ""),
            "observation_end": str(entry.get("observation_end") or ""),
            "observation_count": int((entry.get("metadata") or {}).get("observation_count") or 0),
            "detail": "Pass cache_id to plot_series. The observations are in the cache, "
                      "not in this reply, and should not be reproduced from memory.",
        }

    async def plot_series(series_ids: list[str] | None = None,
                          cache_ids: list[str] | None = None,
                          title: str = "Time Series",
                          date_from: str | None = None,
                          date_to: str | None = None) -> list[TextContent | ImageContent]:
        started = perf_counter()
        ids = [str(c).strip() for c in (cache_ids or []) if str(c).strip()]

        # Fetching here is what makes the honest path the SHORT one. Plotting a FRED
        # series used to be three calls -- search, fetch, plot -- against `plot`'s one,
        # and a tool that is cheaper to call wins regardless of what the other tools'
        # descriptions say about provenance. "Plot US GDP" is one call now, and the
        # observations still never enter the conversation.
        for sid in [str(s).strip() for s in (series_ids or []) if str(s).strip()]:
            if not await _ensure_registry():
                return [TextContent(type="text", text=(
                    f"Cannot reach the data server at {MCP_URL}, so '{sid}' could not "
                    f"be fetched. Nothing was plotted."))]
            try:
                entry = await fetch_series_into_cache("fred", sid)
            except Exception as exc:
                # An unknown id comes back as a JSON parse failure from the vendor
                # reply, which says nothing useful to whoever typed the id. Name the
                # likely cause and keep the original for the log.
                logger.warning(f"plot_series: fetch {sid!r} failed: {exc}")
                return [TextContent(type="text", text=(
                    f"Could not fetch '{sid}'. If that is not an exact FRED series id, "
                    f"find it with search_fred — the id is the short code like 'GDP' or "
                    f"'UNRATE', not the series title. Nothing was plotted."))]
            if entry is None:
                return [TextContent(type="text", text=(
                    f"No series '{sid}' — check the id with search_fred. "
                    f"Nothing was plotted."))]
            ids.append(str(entry["cache_id"]))

        if not ids:
            return [TextContent(type="text", text=(
                "Give series_ids (FRED ids like 'GDP') or cache_ids from "
                "fetch_fred_series."))]
        try:
            entries = cache_entries_for(ids)
            # refresh=False: the caller has just fetched, and a second round trip per
            # series would double the cost of a preview for data minutes old.
            result = await render_series_plot(entries, title, date_from, date_to,
                                              refresh=False)
        except ValueError as exc:
            _log("plot_series", {"cache_ids": ids}, started, "refused")
            return [TextContent(type="text", text=f"Could not plot: {exc}")]

        # The legend table render_series_plot builds never reaches an MCP client -- only
        # the first <img> survives -- so the id/title/units mapping goes in the text, or
        # the chart arrives with a legend of bare ids and no key.
        from mcp_server.server import _as_image, _plot_file   # late: server imports us
        key = "; ".join(
            f"{e['native_id'] or e['cache_id'][:8]}"
            + (f" ({e['metadata'].get('units')})" if (e.get('metadata') or {}).get("units") else "")
            + (f" — {e['title']}" if e.get("title") else "")
            for e in entries)
        summary = (f"{title} — {result['plot_type']} plot of {result['series_count']} "
                   f"series from cache: {key}")

        path = _plot_file(result["html"])
        if path is None:
            logger.error("plot_series: rendered but found no PNG")
            _log("plot_series", {"cache_ids": ids}, started, "no png")
            return [TextContent(type="text", text=f"{summary}\n\n(plot file missing)")]
        _log("plot_series", {"cache_ids": ids}, started, result["plot_type"])
        return [TextContent(type="text", text=summary), _as_image(path)]

    server.add_tool(
        fetch_fred_series, name="fetch_fred_series",
        description=(
            "Fetch a FRED series into yada's cache and return a cache_id. Returns the "
            "series' metadata and the id — NOT its observations, which stay in the "
            "cache so they cannot be paraphrased or misremembered on the way to a "
            "chart.\n"
            "- series_id: a FRED series id as search_fred reports it, e.g. 'GDP', "
            "'UNRATE', 'CPIAUCSL'.\n"
            "Idempotent: fetching the same series again returns the same cache_id and "
            "re-reads the source only once its data is stale. Pass the cache_id to "
            "plot_series to draw it. Use this rather than fetching observations "
            "yourself whenever the data is going to be charted."),
    )

    # Bound to the chart App, exactly as `plot` and `plot_report` are. A bare image
    # block is a *tool result*, which means the CLIENT decides how it appears -- and
    # Goose collapses those behind an "Output" expander, so a chart you asked for
    # arrives folded away. An App means yada decides, and it renders inline. This is
    # what plot_app.py was written for; plot_series simply was not wired to it.
    #
    # Registered with add_tool rather than @apps.tool because the decorator must run
    # before MCPServer is constructed and this runs after. add_tool takes the same
    # `meta`, which is how the Apps extension registers its own tools.
    server.add_tool(
        plot_series, name="plot_series", meta=plot_meta,
        description=(
            "Chart one or more FRED series and return the image. **This is the tool for "
            "charting economic data** — it fetches what it needs and draws only from "
            "stored values, so the numbers are never ones the model supplied.\n"
            "- series_ids: FRED ids, e.g. ['GDP'] or ['GDP','GDPC1']. Fetched "
            "automatically if not already cached. This is the usual way to call it: "
            "'plot US GDP' is one call.\n"
            "- cache_ids: ids already returned by fetch_fred_series. Mixes freely with "
            "series_ids.\n"
            "- title: chart title.\n"
            "- date_from / date_to: optional ISO dates to restrict the window.\n"
            "Several series are plotted together, with the plot type and axes chosen "
            "from their count and units. Use this rather than `plot` for anything in "
            "FRED: `plot` charts whatever it is handed, so if the data has to come from "
            "somewhere it comes from the model, and the chart will look right and be "
            "wrong."),
    )

    logger.info("Series tools registered: fetch_fred_series, plot_series")
