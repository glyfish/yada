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

logger = get_logger("YADA")


def _load_series_by_cache_id(
    cache_id: str, date_from: str | None, date_to: str | None
) -> tuple[list[datetime], list[float]]:
    try:
        entry = SeriesCache._get_by_cache_id_sync(cache_id)
        if entry is None:
            raise ValueError(f"Series {cache_id} not found in cache or expired")
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


class GetReportInfoInput(BaseModel):
    report_id_or_title: str = Field(
        ...,
        description="Report UUID or case-insensitive title substring to search for.",
    )


class ReportSinglePlotInput(BaseModel):
    native_id: str = Field(..., description="native_id UUID of the series from get_report_info.")
    date_from: str | None = Field(None, description="Start date YYYY-MM-DD (from report time_range_from).")
    date_to: str | None = Field(None, description="End date YYYY-MM-DD (from report time_range_to, or None for latest).")
    title: str = Field(default="Time Series", description="Plot title.")
    ylabel: str = Field(default="Value", description="Y-axis label.")
    plot_axis_type: PlotType = Field(default=PlotType.LINEAR)


class ReportComparisonPlotInput(BaseModel):
    native_ids: list[str] = Field(..., description="List of native_id UUIDs (2-5) from get_report_info.")
    date_from: str | None = Field(None, description="Start date YYYY-MM-DD.")
    date_to: str | None = Field(None, description="End date YYYY-MM-DD, or None for latest.")
    title: str = Field(default="Time Series Comparison", description="Plot title.")
    ylabel: str = Field(default="Value", description="Shared y-axis label.")
    labels: list[str] | None = Field(None, description="Legend label per series.")
    plot_axis_type: PlotType = Field(default=PlotType.LINEAR)


class ReportTwinxPlotInput(BaseModel):
    left_native_id: str = Field(..., description="native_id UUID for the left y-axis series.")
    right_native_id: str = Field(..., description="native_id UUID for the right y-axis series.")
    date_from: str | None = Field(None)
    date_to: str | None = Field(None)
    title: str = Field(default="Time Series", description="Plot title.")
    left_ylabel: str = Field(default="Value", description="Left y-axis label.")
    right_ylabel: str = Field(default="Value", description="Right y-axis label.")
    plot_axis_type: PlotType = Field(default=PlotType.LINEAR)


class ReportTwinxComparisonPlotInput(BaseModel):
    left_native_ids: list[str] = Field(..., description="native_id UUIDs for the left y-axis series.")
    right_native_ids: list[str] = Field(..., description="native_id UUIDs for the right y-axis series.")
    date_from: str | None = Field(None)
    date_to: str | None = Field(None)
    title: str = Field(default="Time Series", description="Plot title.")
    left_ylabel: str = Field(default="Value", description="Left y-axis label.")
    right_ylabel: str = Field(default="Value", description="Right y-axis label.")
    plot_axis_type: PlotType = Field(default=PlotType.LINEAR)


class ReportStackPlotInput(BaseModel):
    native_ids: list[str] = Field(..., description="List of native_id UUIDs (2-5) from get_report_info.")
    date_from: str | None = Field(None)
    date_to: str | None = Field(None)
    title: str = Field(default="Time Series Stack", description="Plot title.")
    ylabels: list[str] | None = Field(None, description="Y-axis label per series.")
    labels: list[str] | None = Field(None, description="Annotation label per series.")
    plot_axis_type: PlotType = Field(default=PlotType.LINEAR)


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
               This returns time_range_from, time_range_to, and a time_series list with native_id,
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

            - 1 series → report_plot_single. If the value range extends over more than one order of magnitude, use YLOG axis.
              Otherwise, use LINEAR axis.
            - 2-5 series, same units → report_plot_comparison, if the value ranges are comparable (within one order of magnitude) use a LINEAR axis and
                if the value ranges are very different (greater than one order of magnitude) use a YLOG axis.
            - Exactly 2 series, different units → report_plot_twinx if the value range extends over more than one order of magnitude, 
              use YLOG axis. Otherwise, use LINEAR axis.
            - 3-5 series, exactly 2 distinct units (assign the majority-unit series to left, 
              the minority-unit series to right) → report_plot_twinx_comparison.f the value range extends over more than one 
              order of magnitude, use YLOG axis. Otherwise, use LINEAR axis.
            - 2-5 series, more than 2 distinct units or very different scales
              → report_plot_stack
            </plot_type_selection>

            <axis_scale_selection>
            For each group, inspect all value_range.min and value_range.max values across the series:
            - If all values are positive and max / min > 10 → use YLOG
            - Otherwise → use LINEAR
            </axis_scale_selection>

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
                native_id, units, value_range, observation_start, and observation_end per series.
                If multiple reports match a title search, returns the match list so the user
                can be asked to select one by report_id. Never returns raw observations.
            """,
            positive_examples=[
                PositiveExample(input="Plot report 'GDP Overview'"),
                PositiveExample(input="Plot report 24c23e96-5e97-4c3d-bb4a-c85116839d36"),
            ],
        ),
    )
    def get_report_info(report_id_or_title: str) -> str:
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

        time_series = []
        for entry in (record.get("time_series_info") or []):
            native_id = entry.get("native_id", "")
            value_range = None
            try:
                _, values = _load_series_by_cache_id(native_id, date_from, date_to)
                if values:
                    value_range = {"min": float(min(values)), "max": float(max(values))}
            except Exception as exc:
                logger.warning(f"get_report_info: could not load series {native_id} for value_range: {exc}")
            metadata = dict(entry.get("metadata") or {})
            time_series.append({
                "native_id": native_id,
                "title": entry.get("title", ""),
                "source": entry.get("source", ""),
                "external_id": entry.get("external_id", ""),
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
            "tags": list(record.get("tags") or []),
            "time_range_from": date_from or "",
            "time_range_to": date_to,
            "time_series": time_series,
        })


    @staticmethod
    @tool_spec(
        args_schema=ReportSinglePlotInput,
        metadata=ToolSpec(
            primary_function="""
                Plot a single time series from the report using its native_id.
                Use when the group contains exactly one series.
                Pass date_from and date_to from the report time_range.
            """,
            positive_examples=[
                PositiveExample(input="Plot the single series in this report."),
            ],
        ),
    )
    def report_plot_single(
        native_id: str,
        date_from: str | None,
        date_to: str | None,
        title: str,
        ylabel: str,
        plot_axis_type: PlotType,
    ) -> str:
        try:
            times, values = _load_series_by_cache_id(native_id, date_from, date_to)
            file = generate_time_series_plot(
                time=numpy.array(times),
                values=numpy.array(values),
                title=title,
                xlabel="Time",
                ylabel=ylabel,
                plot_axis_type=plot_axis_type,
            )
            logger.debug(f"report_plot_single: saved plot → {file}")
            return f'<div class="time-series-plot"><img src="{file}"></div>'
        except Exception as exc:
            logger.error(f"report_plot_single failed for native_id={native_id}: {exc}", exc_info=True)
            raise


    @staticmethod
    @tool_spec(
        args_schema=ReportComparisonPlotInput,
        metadata=ToolSpec(
            primary_function="""
                Plot 2-5 report series overlaid on the same axis.
                Use when all series share the same units and comparable value ranges
                (within one order of magnitude of each other).
            """,
            positive_examples=[
                PositiveExample(input="Compare multiple GDP series from the report on the same axis."),
            ],
        ),
    )
    def report_plot_comparison(
        native_ids: list[str],
        date_from: str | None,
        date_to: str | None,
        title: str,
        ylabel: str,
        labels: list[str] | None,
        plot_axis_type: PlotType,
    ) -> str:
        loaded = [_load_series_by_cache_id(nid, date_from, date_to) for nid in native_ids]
        file = generate_time_series_comparison(
            time=numpy.array(loaded[0][0]),
            values=[numpy.array(t[1]) for t in loaded],
            title=title,
            xlabel="Time",
            ylabel=ylabel,
            labels=labels,
            plot_axis_type=plot_axis_type,
        )
        return f'<div class="time-series-plot"><img src="{file}"></div>'


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
        left_native_id: str,
        right_native_id: str,
        date_from: str | None,
        date_to: str | None,
        title: str,
        left_ylabel: str,
        right_ylabel: str,
        plot_axis_type: PlotType,
    ) -> str:
        left_times, left_values = _load_series_by_cache_id(left_native_id, date_from, date_to)
        _, right_values = _load_series_by_cache_id(right_native_id, date_from, date_to)
        file = generate_time_series_twinx(
            time=numpy.array(left_times),
            left=numpy.array(left_values),
            right=numpy.array(right_values),
            title=title,
            xlabel="Time",
            left_ylabel=left_ylabel,
            right_ylabel=right_ylabel,
            plot_axis_type=plot_axis_type,
        )
        return f'<div class="time-series-plot"><img src="{file}"></div>'


    @staticmethod
    @tool_spec(
        args_schema=ReportTwinxComparisonPlotInput,
        metadata=ToolSpec(
            primary_function="""
                Plot 3-5 report series with exactly 2 distinct units on dual y-axes.
                Assign series sharing the majority unit to left_native_ids and the
                remaining series to right_native_ids.
            """,
            positive_examples=[
                PositiveExample(input="Plot GDP (left) with CPI and PCE (right) on dual axes."),
            ],
        ),
    )
    def report_plot_twinx_comparison(
        left_native_ids: list[str],
        right_native_ids: list[str],
        date_from: str | None,
        date_to: str | None,
        title: str,
        left_ylabel: str,
        right_ylabel: str,
        plot_axis_type: PlotType,
    ) -> str:
        left_loaded = [_load_series_by_cache_id(nid, date_from, date_to) for nid in left_native_ids]
        right_loaded = [_load_series_by_cache_id(nid, date_from, date_to) for nid in right_native_ids]
        file = generate_time_series_twinx_comparison(
            time=numpy.array(left_loaded[0][0]),
            left=[numpy.array(t[1]) for t in left_loaded],
            right=[numpy.array(t[1]) for t in right_loaded],
            title=title,
            xlabel="Time",
            left_ylabel=left_ylabel,
            right_ylabel=right_ylabel,
            plot_axis_type=plot_axis_type,
        )
        return f'<div class="time-series-plot"><img src="{file}"></div>'


    @staticmethod
    @tool_spec(
        args_schema=ReportStackPlotInput,
        metadata=ToolSpec(
            primary_function="""
                Plot 2-5 report series on vertically stacked axes sharing a common time axis.
                Use when series have more than 2 distinct units or widely different scales.
            """,
            positive_examples=[
                PositiveExample(input="Stack GDP, unemployment, and CPI from the report."),
            ],
        ),
    )
    def report_plot_stack(
        native_ids: list[str],
        date_from: str | None,
        date_to: str | None,
        title: str,
        ylabels: list[str] | None,
        labels: list[str] | None,
        plot_axis_type: PlotType,
    ) -> str:
        loaded = [_load_series_by_cache_id(nid, date_from, date_to) for nid in native_ids]
        file = generate_time_series_stack(
            time=numpy.array(loaded[0][0]),
            values=[numpy.array(t[1]) for t in loaded],
            title=title,
            xlabel="Time",
            ylabels=ylabels,
            labels=labels,
            plot_axis_type=plot_axis_type,
        )
        return f'<div class="time-series-plot"><img src="{file}"></div>'
