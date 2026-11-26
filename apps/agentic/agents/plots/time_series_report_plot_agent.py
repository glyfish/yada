from __future__ import annotations

import json
import os
import sys
from datetime import datetime
from html import escape

import numpy
import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot

from pydantic import BaseModel, Field

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from apps.agentic.core.tool_spec import PositiveExample, NegativeExample, ToolSpec, tool_spec
from apps.agentic.core.agents.react_agent import ReactAgent
from apps.agentic.agents.data.series_fetch import fetch_series_into_cache
from apps.agentic.db.series_cache import SeriesCache
from apps.agentic.agents.data.reports import resolve_report, resolve_report_or_raise
from apps.core.identity import current_user_id
from apps.plots.time_series_plots import (
    generate_time_series_plot,
    generate_time_series_stack,
    generate_time_series_comparison,
    generate_time_series_twinx,
    generate_time_series_twinx_comparison,
)
from lib import config
from lib.plots import PlotType
from lib.logger import get_logger

from collections import Counter

logger = get_logger("YADA")


def _axis_type_for(groups: list[list[float]]) -> PlotType:
    """Return YLOG when the global value span exceeds one order of magnitude."""
    all_vals = [v for g in groups for v in g]
    if not all_vals:
        return PlotType.LINEAR
    lo, hi = min(all_vals), max(all_vals)
    if lo > 0 and hi / lo > 10:
        return PlotType.YLOG
    return PlotType.LINEAR


def _load_series_by_cache_id(
    cache_id: str, date_from: str | None, date_to: str | None
) -> tuple[list[datetime], list[float]]:
    try:
        # Reports are durable references — load the persisted snapshot even if the
        # cache entry has aged out (Tiingo TTL is only a day), so a saved report can
        # always be plotted without a re-fetch.
        entry = SeriesCache._get_by_cache_id_sync(cache_id, include_expired=True)
        if entry is None:
            raise ValueError(f"Series {cache_id} not found in cache")
        observations = (entry.get("observations") or {}).get("observations", [])
        times: list[datetime] = []
        values: list[float] = []
        for obs in observations:
            if obs.get("value") in (None, ".", ""):
                continue
            d = obs["date"]
            if date_from and d < date_from:
                continue
            if date_to and d > date_to:
                continue
            times.append(datetime.strptime(d, "%Y-%m-%d"))
            values.append(float(obs["value"]))
        logger.debug(f"_load_series_by_cache_id: {cache_id} → {len(times)} points (date_from={date_from}, date_to={date_to})")
        return times, values
    except Exception as exc:
        logger.error(f"_load_series_by_cache_id failed for {cache_id}: {exc}", exc_info=True)
        raise


# The metadata field that best describes a series per source, shown in the legend table.
_CATEGORY_FIELD = {"tiingo": "category", "fred": "category_name"}


def _series_category(entry: dict) -> str:
    """A concise category descriptor for a series (ETF category / FRED category_name)."""
    source = str(entry.get("source") or "").strip().lower()
    field = _CATEGORY_FIELD.get(source)
    if not field:
        return ""
    values = ((entry.get("metadata") or {}).get(source) or {}).get(field)
    return str(values[0]) if isinstance(values, list) and values else ""


def _cell(value) -> str:
    # Escape HTML, then encode '$' as an entity. The client renders this table through a
    # markdown pipeline whose LaTeX pre-processor treats $...$ as math; two currency units
    # like "Mil. of $" would otherwise make it swallow the table structure between them.
    return escape(str(value)).replace("$", "&#36;")


def _series_table_html(series: list[dict]) -> str:
    """A legend key table (ID | Title | Description | Units) rendered above the plot, so
    the plot legend can stay compact with just the series id."""
    rows = "".join(
        "<tr>"
        f"<td><code>{_cell(s['native_id'])}</code></td>"
        f"<td>{_cell(s['title'])}</td>"
        f"<td>{_cell(s['description'])}</td>"
        f"<td>{_cell(s['units'])}</td>"
        "</tr>"
        for s in series
    )
    return (
        '<table class="report-series-table">'
        "<thead><tr><th>ID</th><th>Title</th><th>Description</th><th>Units</th></tr></thead>"
        f"<tbody>{rows}</tbody>"
        "</table>"
    )


def _select_plot_type(units: list[str]) -> str:
    """
    Deterministic plot-type selection from series units — the same rules the plot
    agent's prompt encodes, as pure code (no LLM). Keys only off series count and the
    number of distinct units.
    """
    n = len(units)
    distinct = len(set(units))
    if n == 1:
        return "single"
    if distinct == 1:
        return "comparison"
    if n == 2 and distinct == 2:
        return "twinx"
    if distinct == 2:
        return "twinx_comparison"
    return "stack"


def _apply_plot_style() -> None:
    """Apply the project matplotlib style to this process.

    The style was only ever set in the agent constructors
    (`TimeSeriesReportPlotAgent.__init__` and its siblings), which works for the
    agent-backed `plot` tool and not for anything else: `plot_series` and
    `plot_report` reach the render functions below without constructing an agent,
    and `mcp_server/server.py` builds `PlotAgent` lazily on the first `plot` call
    so that listing tools does not create an LLM client.

    The result was that a chart's appearance depended on what had been called
    before it in the same process. On a freshly restarted server, `plot_series`
    rendered in matplotlib's defaults -- black frame, no gridlines -- and only
    picked up the project style once an unrelated `plot` call had set the
    rcParams process-wide. Applied here, every render path gets it regardless of
    call order. rcParams are global, so this is cheap and idempotent.
    """
    pyplot.style.use(config.glyfish_web_style)


async def render_report_plot(report_id_or_title: str, owner: str | None = None) -> dict:
    """
    Render a report's plot deterministically — no LLM, no agent. Resolves the report,
    refreshes and loads each series, then picks the plot type (count + distinct units)
    and axis scale (value span) and renders with the matching generate_time_series_*
    function. Mirrors the plot agent's tools exactly, so output matches the chat path.

    Returns {report_id, report_title, plot_type, series_count, html}.
    Raises ValueError when the report is missing or no series data can be loaded.
    """
    _apply_plot_style()
    # Shared with the MCP report tools and the REST routes. A title match is a
    # SUBSTRING and titles are not unique, so "GDP" legitimately means both "GDP
    # Overview" and "GDP Deflator"; the resolver names the candidates rather than
    # picking one, and every door reports that the same way.
    record = resolve_report_or_raise(report_id_or_title, owner=owner, action="plot")

    date_from = str(record["time_range_from"]) if record.get("time_range_from") else None
    date_to = str(record["time_range_to"]) if record.get("time_range_to") else None

    entries = record.get("time_series_info") or []
    if not entries:
        raise ValueError("Report has no series to plot.")

    result = await render_series_plot(entries, record["report_title"], date_from, date_to)
    return {"report_id": str(record["report_id"]),
            "report_title": record["report_title"], **result}


async def render_series_plot(
    entries: list[dict],
    title: str,
    date_from: str | None = None,
    date_to: str | None = None,
    refresh: bool = True,
) -> dict:
    """
    Render a chart from cache entries. No report, no LLM, no agent.

    This is `render_report_plot`'s whole body after the report lookup, lifted so a
    caller holding cache ids can reach it without inventing a report first. The three
    places that read `record` -- the dates, the title, the entry list -- are parameters
    now; everything else is unchanged, which is the point: a preview and a saved report
    must render identically or the preview is not one.

    `entries` is the 8-key cache projection (cache_id/title/source/native_id/frequency/
    observation_start/observation_end/metadata) that report rows already store, so both
    callers feed the same shape.

    `refresh=False` skips the per-series re-fetch, for a caller that has just fetched.

    Returns {plot_type, series_count, html}.
    Raises ValueError when no series data can be loaded.
    """
    _apply_plot_style()
    # Refresh each series (re-fetches only past TTL; preserves cache_id). Best-effort:
    # loading below falls back to the persisted snapshot via include_expired.
    for e in entries if refresh else ():
        src, nid = e.get("source", ""), e.get("native_id", "")
        if src and nid:
            try:
                await fetch_series_into_cache(src, nid)
            except Exception as exc:
                logger.warning(f"render_series_plot: refresh failed for {src}:{nid}: {exc}")

    series: list[dict] = []
    for e in entries:
        cache_id = e.get("cache_id", "")
        try:
            times, values = _load_series_by_cache_id(cache_id, date_from, date_to)
        except Exception as exc:
            logger.warning(f"render_series_plot: could not load {cache_id}: {exc}")
            continue
        if not times:
            continue
        units = str((e.get("metadata") or {}).get("units") or "")
        native_id = e.get("native_id") or ""
        series.append({
            # Legend stays compact: just the id. The table above maps id -> title/units.
            "label": native_id or e.get("title") or cache_id,
            "native_id": native_id,
            "title": str(e.get("title") or ""),
            "description": _series_category(e),
            "units": units,
            "time": numpy.array(times),
            "values": numpy.array(values),
        })
    if not series:
        raise ValueError("No series data available to plot.")

    plot_type = _select_plot_type([s["units"] for s in series])
    axis = _axis_type_for([s["values"] for s in series])

    # Every MULTI-SERIES branch passes one time array per series, as a list.
    # The `report_plot_*` tools further down do the same, for the same reason
    # (`single` has only its own, so it passes it bare). Passing a single
    # array instead -- which the signatures also accept -- makes navi broadcast it
    # to every curve and pair values with dates by array index, so a series whose
    # dates differ from the first one's is drawn at the wrong times and silently
    # truncated to the shortest. Index pairing is only correct when every series
    # has identical dates: same frequency, same start, no gaps. Observed economic
    # series satisfy none of that, and the `None`/"." filter in
    # `_load_series_by_cache_id` creates gaps even between two series that agree.
    if plot_type == "single":
        s = series[0]
        file = generate_time_series_plot(
            time=s["time"], values=s["values"], title=title,
            xlabel="Time", ylabel=s["units"] or "Value", plot_axis_type=axis,
        )
    elif plot_type == "comparison":
        file = generate_time_series_comparison(
            time=[s["time"] for s in series], values=[s["values"] for s in series],
            title=title, xlabel="Time", ylabel=series[0]["units"] or "Value",
            labels=[s["label"] for s in series], plot_axis_type=axis,
        )
    elif plot_type == "twinx":
        left, right = series[0], series[1]
        left["axis"], right["axis"] = "left", "right"
        file = generate_time_series_twinx(
            time=[left["time"], right["time"]],
            left=left["values"], right=right["values"], title=title,
            xlabel="Time", left_ylabel=left["units"] or "Value",
            right_ylabel=right["units"] or "Value", plot_axis_type=axis,
            labels=[left["label"], right["label"]],
        )
    elif plot_type == "twinx_comparison":
        majority_unit = Counter(s["units"] for s in series).most_common(1)[0][0]
        left = [s for s in series if s["units"] == majority_unit]
        right = [s for s in series if s["units"] != majority_unit]
        for s in left:
            s["axis"] = "left"
        for s in right:
            s["axis"] = "right"
        file = generate_time_series_twinx_comparison(
            time=[s["time"] for s in left + right], left=[s["values"] for s in left],
            right=[s["values"] for s in right], title=title, xlabel="Time",
            left_ylabel=left[0]["units"] or "Value", right_ylabel=right[0]["units"] or "Value",
            plot_axis_type=axis, labels=[s["label"] for s in left + right],
        )
    else:  # stack
        file = generate_time_series_stack(
            time=[s["time"] for s in series], values=[s["values"] for s in series],
            title=title, xlabel="Time", ylabels=[s["units"] or "Value" for s in series],
            labels=[s["label"] for s in series], plot_axis_type=axis,
        )

    return {
        "plot_type": plot_type,
        "series_count": len(series),
        "html": _series_table_html(series) + f'<div class="time-series-plot"><img src="{file}"></div>',
        # The legend key, without the observation arrays. The browser reads the same
        # mapping out of the HTML table above, but only the <img> survives a trip to an
        # MCP client, so that door has to be handed the key separately or the chart
        # arrives labelled with bare ids and nothing to resolve them against. `axis` is
        # set only on a twin-axis plot, where which scale a curve reads against is the
        # thing a legend of ids cannot express.
        "key": [{"native_id": s["native_id"], "title": s["title"],
                 "units": s["units"], "axis": s.get("axis", "")}
                for s in series],
    }


class GetReportInfoInput(BaseModel):
    report_id_or_title: str = Field(
        ...,
        description="Report UUID or case-insensitive title substring to search for.",
    )


class TimeSeriesReportPlotAgent(ReactAgent):

    @classmethod
    async def create(cls) -> "TimeSeriesReportPlotAgent":
        return cls()


    def __init__(self, mcp_tools: list = []):
        sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "..")))
        pyplot.style.use(config.glyfish_web_style)

        tools = [
            TimeSeriesReportPlotAgent.get_report_info,
            TimeSeriesReportPlotAgent.report_plot,
        ]
        super().__init__(tools, "time_series_report_plot_tool_node", mcp_tools=mcp_tools)


    def create_prompt(self):
        system_prompt = """
            <instructions>
            You are a time series report plot agent. You draw plots for saved reports.

            To plot a report, call report_plot with the report's id or a substring of
            its title. That is the whole sequence — one call. It resolves the report,
            refreshes its series, chooses the plot type and axis scale from the data,
            and returns the chart.

            Do not choose a plot type. Do not pass dates: a report carries its own
            time range, and report_plot reads it.

            Call get_report_info only when the user asks ABOUT a report — which series
            it holds, their units, their ranges — rather than to see it. It is not a
            step on the way to a plot.

            If report_plot reports that several reports match, do not pick one. Show
            the user the candidates it named and ask which they meant.
            </instructions>

            <output_format>
            CRITICAL: You MUST include the exact HTML string returned by report_plot
            verbatim in your response. Do not omit, paraphrase, or replace it with a
            description.
            Provide markdown commentary above the chart.
            Place the HTML fragment on its own line with a blank line before and after it.
            Do not mix HTML fragments within the markdown text.
            Do not use the $ symbol for currency — use USD, EUR, etc. instead.
            </output_format>
            """

        return ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            MessagesPlaceholder(variable_name="messages"),
        ])


    @tool_spec(
        args_schema=GetReportInfoInput,
        metadata=ToolSpec(
            primary_function="""
                Retrieve report metadata by UUID or case-insensitive title substring.
                Returns time_range_from, time_range_to, and the time_series list containing
                cache_id, units, value_range, observation_start, and observation_end per series.
                If multiple reports match a title search, returns the match list so the user
                can be asked to select one by report_id. Never returns raw observations.
            """,
            positive_examples=[
                PositiveExample(input="Plot report 'GDP Overview'"),
                PositiveExample(input="Plot report 24c23e96-5e97-4c3d-bb4a-c85116839d36"),
            ],
        ),
    )
    @staticmethod
    async def get_report_info(report_id_or_title: str) -> str:
        # Same resolver as render_report_plot and the MCP tools; only the reporting
        # differs, because this tool answers a model and the others answer a caller.
        resolution = resolve_report(report_id_or_title, owner=current_user_id())
        if resolution.ambiguous:
            return json.dumps({
                "matches": resolution.candidates,
                "message": "Multiple reports match. Please ask the user to select one by report_id.",
            })
        if not resolution.resolved:
            return json.dumps({"error": f"No report found matching '{report_id_or_title}'."})
        record = resolution.record
        assert record is not None

        date_from = str(record["time_range_from"]) if record.get("time_range_from") else None
        date_to = str(record["time_range_to"]) if record.get("time_range_to") else None

        # Refresh each series through the caching tool before loading. It re-fetches only
        # when the entry is missing or past its TTL (a fresh entry is a cache hit, no
        # network), and the upsert preserves the cache_id so the report's references stay
        # valid. Best-effort: on failure the include_expired load below still serves the
        # persisted snapshot.
        for entry in (record.get("time_series_info") or []):
            src = entry.get("source", "")
            nid = entry.get("native_id", "")
            if src and nid:
                try:
                    await fetch_series_into_cache(src, nid)
                except Exception as exc:
                    logger.warning(f"get_report_info: refresh failed for {src}:{nid}: {exc}")

        time_series = []
        for entry in (record.get("time_series_info") or []):
            cache_id = entry.get("cache_id", "")
            value_range = None
            try:
                _, values = _load_series_by_cache_id(cache_id, date_from, date_to)
                if values:
                    value_range = {"min": float(min(values)), "max": float(max(values))}
            except Exception as exc:
                logger.warning(f"get_report_info: could not load series {cache_id} for value_range: {exc}")
            metadata = dict(entry.get("metadata") or {})
            time_series.append({
                "cache_id": cache_id,
                "title": entry.get("title", ""),
                "source": entry.get("source", ""),
                "native_id": entry.get("native_id", ""),
                "frequency": entry.get("frequency", ""),
                "observation_start": entry.get("observation_start", ""),
                "observation_end": entry.get("observation_end", ""),
                "units": metadata.get("units", ""),
                "value_range": value_range,
            })

        return json.dumps({
            "report_id": str(record["report_id"]),
            "report_title": record["report_title"],
            "report_description": record.get("report_description", ""),
            "metadata": dict(record.get("metadata") or {}),
            "time_range_from": date_from or "",
            "time_range_to": date_to,
            "time_series": time_series,
        })


    @tool_spec(
        args_schema=GetReportInfoInput,
        metadata=ToolSpec(
            primary_function="""
                Plot a report and return the chart as an HTML fragment. Accepts the
                report's UUID or a case-insensitive substring of its title. Chooses the
                plot type and axis scale from the report's own series -- do not choose
                them, and do not pass dates: the report carries its own time range.
                Returns the HTML to include verbatim in your reply.
            """,
            positive_examples=[
                PositiveExample(input="Plot the unemployment report."),
                PositiveExample(input="Plot report 24c23e96-5e97-4c3d-bb4a-c85116839d36."),
            ],
            negative_examples=[
                NegativeExample(
                    input="What series are in the GDP report?",
                    reason="Use get_report_info, which returns metadata without drawing anything.",
                ),
            ],
        ),
    )
    @staticmethod
    async def report_plot(report_id_or_title: str) -> str:
        """Plot a report through the same function every other surface calls.

        This replaced five tools -- single, comparison, twinx, twinx_comparison and
        stack -- that existed so the model could pick a plot type. `_select_plot_type`
        already makes that choice from the series count and their distinct units, is
        unit-tested, and is what the MCP tools and the REST route use.

        Having both was not a redundancy, it was a second implementation, and the two
        drifted: the agent's charts carried no legend key table, batched into groups of
        five where the deterministic path draws one chart, refreshed a series only when
        the model happened to call get_report_info first, and reported an ambiguous
        title in a different shape. A per-series date fix had to be applied to both by
        hand, and the copy here was missed for a commit.
        """
        try:
            result = await render_report_plot(report_id_or_title,
                                              owner=current_user_id())
        except ValueError as exc:
            # Missing, ambiguous, or nothing loadable. The message names the candidates
            # when a title matched several, which is the model's cue to ask.
            logger.warning(f"report_plot({report_id_or_title!r}): {exc}")
            return str(exc)
        return result["html"]
