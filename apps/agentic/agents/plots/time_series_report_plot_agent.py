from __future__ import annotations

import json
import os
import sys
import uuid as _uuid
from datetime import datetime

import numpy
import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot

from pydantic import BaseModel, Field

from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder

from apps.agentic.core.tool_spec import PositiveExample, ToolSpec, tool_spec
from apps.agentic.core.agents.react_agent import ReactAgent
from apps.agentic.agents.data.series_fetch import fetch_series_into_cache
from apps.agentic.db.series_cache import SeriesCache
from apps.agentic.db.report_cache import ReportCache
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


async def render_report_plot(report_id_or_title: str) -> dict:
    """
    Render a report's plot deterministically — no LLM, no agent. Resolves the report,
    refreshes and loads each series, then picks the plot type (count + distinct units)
    and axis scale (value span) and renders with the matching generate_time_series_*
    function. Mirrors the plot agent's tools exactly, so output matches the chat path.

    Returns {report_id, report_title, plot_type, series_count, html}.
    Raises ValueError when the report is missing or no series data can be loaded.
    """
    record = None
    try:
        _uuid.UUID(report_id_or_title)
        record = ReportCache._get_by_report_id_sync(report_id_or_title)
    except ValueError:
        pass
    if record is None:
        matches = ReportCache._search_by_title_sync(report_id_or_title)
        if len(matches) == 1:
            record = ReportCache._get_by_report_id_sync(matches[0]["report_id"])
    if record is None:
        raise ValueError(f"No report found matching '{report_id_or_title}'.")

    date_from = str(record["time_range_from"]) if record.get("time_range_from") else None
    date_to = str(record["time_range_to"]) if record.get("time_range_to") else None

    entries = record.get("time_series_info") or []
    if not entries:
        raise ValueError("Report has no series to plot.")

    # Refresh each series (re-fetches only past TTL; preserves cache_id). Best-effort:
    # loading below falls back to the persisted snapshot via include_expired.
    for e in entries:
        src, nid = e.get("source", ""), e.get("native_id", "")
        if src and nid:
            try:
                await fetch_series_into_cache(src, nid)
            except Exception as exc:
                logger.warning(f"render_report_plot: refresh failed for {src}:{nid}: {exc}")

    series: list[dict] = []
    for e in entries:
        cache_id = e.get("cache_id", "")
        try:
            times, values = _load_series_by_cache_id(cache_id, date_from, date_to)
        except Exception as exc:
            logger.warning(f"render_report_plot: could not load {cache_id}: {exc}")
            continue
        if not times:
            continue
        series.append({
            "label": e.get("native_id") or e.get("title") or cache_id,
            "units": str((e.get("metadata") or {}).get("units") or ""),
            "time": numpy.array(times),
            "values": numpy.array(values),
        })
    if not series:
        raise ValueError("No series data available to plot.")

    title = record["report_title"]
    plot_type = _select_plot_type([s["units"] for s in series])
    axis = _axis_type_for([s["values"] for s in series])

    if plot_type == "single":
        s = series[0]
        file = generate_time_series_plot(
            time=s["time"], values=s["values"], title=title,
            xlabel="Time", ylabel=s["units"] or "Value", plot_axis_type=axis,
        )
    elif plot_type == "comparison":
        file = generate_time_series_comparison(
            time=series[0]["time"], values=[s["values"] for s in series], title=title,
            xlabel="Time", ylabel=series[0]["units"] or "Value",
            labels=[s["label"] for s in series], plot_axis_type=axis,
        )
    elif plot_type == "twinx":
        left, right = series[0], series[1]
        file = generate_time_series_twinx(
            time=left["time"], left=left["values"], right=right["values"], title=title,
            xlabel="Time", left_ylabel=left["units"] or "Value",
            right_ylabel=right["units"] or "Value", plot_axis_type=axis,
            labels=[left["label"], right["label"]],
        )
    elif plot_type == "twinx_comparison":
        majority_unit = Counter(s["units"] for s in series).most_common(1)[0][0]
        left = [s for s in series if s["units"] == majority_unit]
        right = [s for s in series if s["units"] != majority_unit]
        file = generate_time_series_twinx_comparison(
            time=left[0]["time"], left=[s["values"] for s in left],
            right=[s["values"] for s in right], title=title, xlabel="Time",
            left_ylabel=left[0]["units"] or "Value", right_ylabel=right[0]["units"] or "Value",
            plot_axis_type=axis, labels=[s["label"] for s in left + right],
        )
    else:  # stack
        file = generate_time_series_stack(
            time=series[0]["time"], values=[s["values"] for s in series], title=title,
            xlabel="Time", ylabels=[s["units"] or "Value" for s in series],
            labels=[s["label"] for s in series], plot_axis_type=axis,
        )

    return {
        "report_id": str(record["report_id"]),
        "report_title": title,
        "plot_type": plot_type,
        "series_count": len(series),
        "html": f'<div class="time-series-plot"><img src="{file}"></div>',
    }


class GetReportInfoInput(BaseModel):
    report_id_or_title: str = Field(
        ...,
        description="Report UUID or case-insensitive title substring to search for.",
    )


class ReportSinglePlotInput(BaseModel):
    cache_id: str = Field(..., description="cache_id UUID of the series from get_report_info.")
    date_from: str | None = Field(None, description="Start date YYYY-MM-DD (from report time_range_from).")
    date_to: str | None = Field(None, description="End date YYYY-MM-DD (from report time_range_to, or None for latest).")
    title: str = Field(default="Time Series", description="Plot title.")
    ylabel: str = Field(default="Value", description="Y-axis label.")


class ReportComparisonPlotInput(BaseModel):
    cache_ids: list[str] = Field(..., description="List of cache_id UUIDs (2-5) from get_report_info.")
    date_from: str | None = Field(None, description="Start date YYYY-MM-DD.")
    date_to: str | None = Field(None, description="End date YYYY-MM-DD, or None for latest.")
    title: str = Field(default="Time Series Comparison", description="Plot title.")
    ylabel: str = Field(default="Value", description="Shared y-axis label.")
    labels: list[str] | None = Field(None, description="Legend label per series.")


class ReportTwinxPlotInput(BaseModel):
    left_cache_id: str = Field(..., description="cache_id UUID for the left y-axis series.")
    right_cache_id: str = Field(..., description="cache_id UUID for the right y-axis series.")
    date_from: str | None = Field(None)
    date_to: str | None = Field(None)
    title: str = Field(default="Time Series", description="Plot title.")
    left_ylabel: str = Field(default="Value", description="Left y-axis label.")
    right_ylabel: str = Field(default="Value", description="Right y-axis label.")
    left_label: str | None = Field(None, description="Legend label for the left series.")
    right_label: str | None = Field(None, description="Legend label for the right series.")


class ReportTwinxComparisonPlotInput(BaseModel):
    left_cache_ids: list[str] = Field(..., description="cache_id UUIDs for the left y-axis series.")
    right_cache_ids: list[str] = Field(..., description="cache_id UUIDs for the right y-axis series.")
    date_from: str | None = Field(None)
    date_to: str | None = Field(None)
    title: str = Field(default="Time Series", description="Plot title.")
    left_ylabel: str = Field(default="Value", description="Left y-axis label.")
    right_ylabel: str = Field(default="Value", description="Right y-axis label.")
    labels: list[str] | None = Field(None, description="Legend label per series (left series first, then right).")


class ReportStackPlotInput(BaseModel):
    cache_ids: list[str] = Field(..., description="List of cache_id UUIDs (2-5) from get_report_info.")
    date_from: str | None = Field(None)
    date_to: str | None = Field(None)
    title: str = Field(default="Time Series Stack", description="Plot title.")
    ylabels: list[str] | None = Field(None, description="Y-axis label per series.")
    labels: list[str] | None = Field(None, description="Annotation label per series.")


class TimeSeriesReportPlotAgent(ReactAgent):

    @classmethod
    async def create(cls) -> "TimeSeriesReportPlotAgent":
        return cls()


    def __init__(self, mcp_tools: list = []):
        sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "..")))
        pyplot.style.use(config.glyfish_style)

        tools = [
            TimeSeriesReportPlotAgent.get_report_info,
            TimeSeriesReportPlotAgent.report_plot_single,
            TimeSeriesReportPlotAgent.report_plot_comparison,
            TimeSeriesReportPlotAgent.report_plot_twinx,
            TimeSeriesReportPlotAgent.report_plot_twinx_comparison,
            TimeSeriesReportPlotAgent.report_plot_stack,
        ]
        super().__init__(tools, "time_series_report_plot_tool_node", mcp_tools=mcp_tools)


    def create_prompt(self):
        system_prompt = """
            <instructions>
            You are a time series report plot agent. Your job is to generate all plots for a report.

            Always follow this sequence:
            1. Call get_report_info with the report ID or title to retrieve report metadata.
               This returns time_range_from, time_range_to, and a time_series list with cache_id,
               units, value_range, observation_start, and observation_end per series.
               Never load raw observations — use only this metadata to choose plot types.
            2. Group the series into batches of at most 5. For reports with more than 5 series,
               emit multiple plot tool calls with successive groups.
            3. For each group call the appropriate plot tool, always passing
               date_from=time_range_from and date_to=time_range_to (pass None for date_to
               when time_range_to is null — this means plot up to the latest available data).
            </instructions>

            <plot_type_selection>
            Choose the plot type for each group using these rules in order:

            - 1 series → report_plot_single
            - 2-5 series, same units → report_plot_comparison
            - Exactly 2 series, different units → report_plot_twinx
            - 3-5 series, exactly 2 distinct units (assign the majority-unit series to left,
              the minority-unit series to right) → report_plot_twinx_comparison
            - 2-5 series, more than 2 distinct units → report_plot_stack

            Axis scale (LINEAR vs YLOG) is determined automatically by the plot tool
            from the loaded data — do not pass a plot_axis_type parameter.
            </plot_type_selection>

            <output_format>
            CRITICAL: You MUST include the exact HTML string returned by each plot tool verbatim
            in your response. Do not omit, paraphrase, or replace it with a description.
            Provide markdown commentary above each chart.
            Place the HTML fragment on its own line with a blank line before and after it.
            Do not mix HTML fragments within the markdown text.
            Do not use the $ symbol for currency — use USD, EUR, etc. instead.
            </output_format>
            """

        return ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            MessagesPlaceholder(variable_name="messages"),
        ])


    @staticmethod
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
    async def get_report_info(report_id_or_title: str) -> str:
        record = None
        try:
            _uuid.UUID(report_id_or_title)
            record = ReportCache._get_by_report_id_sync(report_id_or_title)
        except ValueError:
            pass

        if record is None:
            matches = ReportCache._search_by_title_sync(report_id_or_title)
            if not matches:
                return json.dumps({"error": f"No report found matching '{report_id_or_title}'."})
            if len(matches) > 1:
                return json.dumps({
                    "matches": matches,
                    "message": "Multiple reports match. Please ask the user to select one by report_id.",
                })
            record = ReportCache._get_by_report_id_sync(matches[0]["report_id"])

        if record is None:
            return json.dumps({"error": f"No report found matching '{report_id_or_title}'."})

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


    @staticmethod
    @tool_spec(
        args_schema=ReportSinglePlotInput,
        metadata=ToolSpec(
            primary_function="""
                Plot a single time series from the report using its cache_id.
                Use when the group contains exactly one series.
                Pass date_from and date_to from the report time_range.
            """,
            positive_examples=[
                PositiveExample(input="Plot the single series in this report."),
            ],
        ),
    )
    def report_plot_single(
        cache_id: str,
        date_from: str | None,
        date_to: str | None,
        title: str,
        ylabel: str,
    ) -> str:
        try:
            times, values = _load_series_by_cache_id(cache_id, date_from, date_to)
            file = generate_time_series_plot(
                time=numpy.array(times),
                values=numpy.array(values),
                title=title,
                xlabel="Time",
                ylabel=ylabel,
                plot_axis_type=_axis_type_for([values]),
            )
            logger.debug(f"report_plot_single: saved plot → {file}")
            return f'<div class="time-series-plot"><img src="{file}"></div>'
        except Exception as exc:
            logger.error(f"report_plot_single failed for cache_id={cache_id}: {exc}", exc_info=True)
            raise


    @staticmethod
    @tool_spec(
        args_schema=ReportComparisonPlotInput,
        metadata=ToolSpec(
            primary_function="""
                Plot 2-5 report series overlaid on the same axis.
                Use when all series share the same units.
            """,
            positive_examples=[
                PositiveExample(input="Compare multiple GDP series from the report on the same axis."),
            ],
        ),
    )
    def report_plot_comparison(
        cache_ids: list[str],
        date_from: str | None,
        date_to: str | None,
        title: str,
        ylabel: str,
        labels: list[str] | None,
    ) -> str:
        try:
            loaded = [_load_series_by_cache_id(nid, date_from, date_to) for nid in cache_ids]
            file = generate_time_series_comparison(
                time=numpy.array(loaded[0][0]),
                values=[numpy.array(t[1]) for t in loaded],
                title=title,
                xlabel="Time",
                ylabel=ylabel,
                labels=labels,
                plot_axis_type=_axis_type_for([t[1] for t in loaded]),
            )
            logger.debug(f"report_plot_comparison: saved plot → {file}")
            return f'<div class="time-series-plot"><img src="{file}"></div>'
        except Exception as exc:
            logger.error(f"report_plot_comparison failed for cache_ids={cache_ids}: {exc}", exc_info=True)
            raise


    @staticmethod
    @tool_spec(
        args_schema=ReportTwinxPlotInput,
        metadata=ToolSpec(
            primary_function="""
                Plot exactly 2 report series on dual y-axes (left and right).
                Use when exactly 2 series have different units.
            """,
            positive_examples=[
                PositiveExample(input="Plot GDP and unemployment rate on dual axes."),
            ],
        ),
    )
    def report_plot_twinx(
        left_cache_id: str,
        right_cache_id: str,
        date_from: str | None,
        date_to: str | None,
        title: str,
        left_ylabel: str,
        right_ylabel: str,
        left_label: str | None,
        right_label: str | None,
    ) -> str:
        try:
            left_times, left_values = _load_series_by_cache_id(left_cache_id, date_from, date_to)
            _, right_values = _load_series_by_cache_id(right_cache_id, date_from, date_to)
            labels = [left_label, right_label] if left_label and right_label else None
            file = generate_time_series_twinx(
                time=numpy.array(left_times),
                left=numpy.array(left_values),
                right=numpy.array(right_values),
                title=title,
                xlabel="Time",
                left_ylabel=left_ylabel,
                right_ylabel=right_ylabel,
                plot_axis_type=_axis_type_for([left_values, right_values]),
                labels=labels,
            )
            logger.debug(f"report_plot_twinx: saved plot → {file}")
            return f'<div class="time-series-plot"><img src="{file}"></div>'
        except Exception as exc:
            logger.error(f"report_plot_twinx failed for left={left_cache_id}, right={right_cache_id}: {exc}", exc_info=True)
            raise


    @staticmethod
    @tool_spec(
        args_schema=ReportTwinxComparisonPlotInput,
        metadata=ToolSpec(
            primary_function="""
                Plot 3-5 report series with exactly 2 distinct units on dual y-axes.
                Assign series sharing the majority unit to left_cache_ids and the
                remaining series to right_cache_ids.
            """,
            positive_examples=[
                PositiveExample(input="Plot GDP (left) with CPI and PCE (right) on dual axes."),
            ],
        ),
    )
    def report_plot_twinx_comparison(
        left_cache_ids: list[str],
        right_cache_ids: list[str],
        date_from: str | None,
        date_to: str | None,
        title: str,
        left_ylabel: str,
        right_ylabel: str,
        labels: list[str] | None,
    ) -> str:
        try:
            left_loaded = [_load_series_by_cache_id(nid, date_from, date_to) for nid in left_cache_ids]
            right_loaded = [_load_series_by_cache_id(nid, date_from, date_to) for nid in right_cache_ids]
            file = generate_time_series_twinx_comparison(
                time=numpy.array(left_loaded[0][0]),
                left=[numpy.array(t[1]) for t in left_loaded],
                right=[numpy.array(t[1]) for t in right_loaded],
                title=title,
                xlabel="Time",
                left_ylabel=left_ylabel,
                right_ylabel=right_ylabel,
                plot_axis_type=_axis_type_for([t[1] for t in left_loaded + right_loaded]),
                labels=labels,
            )
            logger.debug(f"report_plot_twinx_comparison: saved plot → {file}")
            return f'<div class="time-series-plot"><img src="{file}"></div>'
        except Exception as exc:
            logger.error(f"report_plot_twinx_comparison failed for left={left_cache_ids}, right={right_cache_ids}: {exc}", exc_info=True)
            raise


    @staticmethod
    @tool_spec(
        args_schema=ReportStackPlotInput,
        metadata=ToolSpec(
            primary_function="""
                Plot 2-5 report series on vertically stacked axes sharing a common time axis.
                Use when series have more than 2 distinct units.
            """,
            positive_examples=[
                PositiveExample(input="Stack GDP, unemployment, and CPI from the report."),
            ],
        ),
    )
    def report_plot_stack(
        cache_ids: list[str],
        date_from: str | None,
        date_to: str | None,
        title: str,
        ylabels: list[str] | None,
        labels: list[str] | None,
    ) -> str:
        try:
            loaded = [_load_series_by_cache_id(nid, date_from, date_to) for nid in cache_ids]
            file = generate_time_series_stack(
                time=numpy.array(loaded[0][0]),
                values=[numpy.array(t[1]) for t in loaded],
                title=title,
                xlabel="Time",
                ylabels=ylabels,
                labels=labels,
                plot_axis_type=_axis_type_for([t[1] for t in loaded]),
            )
            logger.debug(f"report_plot_stack: saved plot → {file}")
            return f'<div class="time-series-plot"><img src="{file}"></div>'
        except Exception as exc:
            logger.error(f"report_plot_stack failed for cache_ids={cache_ids}: {exc}", exc_info=True)
            raise
