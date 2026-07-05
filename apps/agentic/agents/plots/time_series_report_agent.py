from __future__ import annotations

from typing import Any, TypedDict

import shortuuid
from pydantic import BaseModel, Field

from langchain_core.messages import HumanMessage
from langchain_core.runnables import RunnableConfig
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder

from apps.agentic.core.tool_spec import PositiveExample, NegativeExample, ToolSpec, tool_spec
from apps.agentic.core.agents.react_agent import ReactAgent
from apps.agentic.db.report_cache import ReportCache
from apps.agentic.db.series_cache import SeriesCache
from apps.agentic.agents.plots.time_series_report_plot_agent import TimeSeriesReportPlotAgent

from lib.logger import get_logger

logger = get_logger("YADA")

_plot_agent = TimeSeriesReportPlotAgent()


class TimeSeriesInfoEntry(TypedDict):
    cache_id: str
    title: str
    source: str
    native_id: str
    frequency: str
    observation_start: str
    observation_end: str
    metadata: dict[str, Any]


class CreateReportInput(BaseModel):
    report_title: str = Field(..., description="Title of the report.")
    report_description: str = Field(..., description="Description of the report.")
    time_series_ids_csv: str = Field(
        ...,
        description="Comma-separated list of time series cache IDs to include in the report.",
    )
    tags_csv: str = Field(
        "",
        description="Comma-separated list of tags to categorize the report (e.g. gdp,labor,quarterly).",
    )
    time_range_from: str = Field(
        ...,
        description="Start date of the report time range in ISO format YYYY-MM-DD.",
    )
    time_range_to: str | None = Field(
        None,
        description="End date of the report time range in ISO format YYYY-MM-DD. Omit for latest available data.",
    )


class GetReportInput(BaseModel):
    report_id: str = Field(..., description="UUID of the report to retrieve.")


class ListReportsInput(BaseModel):
    pass


class PlotReportInput(BaseModel):
    request: str = Field(
        ...,
        description="The plot request, including the report ID or title and any other instructions.",
    )


@tool_spec(
    args_schema=PlotReportInput,
    metadata=ToolSpec(
        primary_function="""
            Delegate a plot request to the Time Series Report Plot Agent.
            Use when the user wants to plot or visualize a time series report.
            Pass the report ID or title and any other instructions in the request string.
        """,
        positive_examples=[
            PositiveExample(input="Plot the GDP Overview report."),
            PositiveExample(input="Plot report 24c23e96-5e97-4c3d-bb4a-c85116839d36."),
        ],
        negative_examples=[
            NegativeExample(
                input="Show me the details of my GDP report.",
                reason="Use get_time_series_report to retrieve report details.",
            ),
        ],
    ),
)
async def plot_time_series_report(request: str) -> str:
    from langchain_core.messages import ToolMessage
    state = {"messages": [HumanMessage(content=request)]}
    config = RunnableConfig(configurable={"thread_id": shortuuid.uuid()})
    result = await _plot_agent.agent.ainvoke(state, config)

    raw = result["messages"][-1].content
    if isinstance(raw, str):
        commentary = raw
    else:
        commentary = "\n".join(
            block.get("text", "")
            for block in raw
            if isinstance(block, dict) and block.get("type") == "text"
        )

    logger.debug(f"plot_time_series_report: commentary has_img={'<img' in commentary}")

    extra_html = [
        msg.content
        for msg in result["messages"]
        if isinstance(msg, ToolMessage) and isinstance(msg.content, str) and "<img" in msg.content and msg.content not in commentary
    ]
    logger.debug(f"plot_time_series_report: extra_html count={len(extra_html)}")

    if extra_html:
        return commentary + "\n\n" + "\n\n".join(extra_html)
    return commentary


class TimeSeriesReportAgent(ReactAgent):

    @classmethod
    async def create(cls) -> "TimeSeriesReportAgent":
        return cls()

    def __init__(self, mcp_tools: list = []):
        tools = [
            TimeSeriesReportAgent.create_time_series_report,
            TimeSeriesReportAgent.get_time_series_report,
            TimeSeriesReportAgent.list_time_series_reports,
            TimeSeriesReportAgent.delete_time_series_report,
            plot_time_series_report,
        ]
        super().__init__(tools, "time_series_report_tool_node", mcp_tools=mcp_tools)

    def create_prompt(self):
        system_prompt = """
            <instructions>
            You are a time series report agent. You create, retrieve, list, and plot time series reports.
            A report groups a set of time series cache IDs under a title and description for later reference.

            Use create_time_series_report when the user wants to save a new report. The time series IDs
            will be provided as a comma-separated string.

            Use get_time_series_report when the user wants to view the details of a specific report by ID.

            Use list_time_series_reports when the user wants to see all existing reports.

            Use plot_time_series_report when the user wants to plot or visualize a report.

            Use delete_time_series_report when the user wants to delete a report. A report_id must
            be known — call list_time_series_reports first if the user only provides a title.

            Always respond in markdown. For created reports, confirm the title and report ID.
            For retrieved reports, format the details clearly including each series native_id, title, and source.
            For listed reports, present a markdown table with report ID and title columns.

            CRITICAL: When plot_time_series_report returns a result that contains HTML (e.g. <div> or <img> tags),
            you MUST copy that HTML verbatim into your response, exactly as returned. Do not paraphrase,
            summarize, or omit any HTML tags. Place the HTML on its own line with a blank line before it.
            </instructions>
            """

        return ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            MessagesPlaceholder(variable_name="messages"),
        ])

    @staticmethod
    @tool_spec(
        args_schema=CreateReportInput,
        metadata=ToolSpec(
            primary_function="""
                Create a new time series report with a title, description, and list of time series cache IDs.
                The time series IDs are provided as a comma-separated string and resolved from the cache.
                The report stores structured time_series_info records.
                Returns a confirmation message containing the new report ID.
            """,
            positive_examples=[
                PositiveExample(input="Create a time series report."),
                PositiveExample(input="Create a time series report called 'GDP Overview' with these cache IDs: id-001, id-002"),
            ],
            negative_examples=[
                NegativeExample(
                    input="Show me the GDP report.",
                    reason="Use get_time_series_report or list_time_series_reports to retrieve existing reports.",
                ),
            ],
        ),
    )
    def create_time_series_report(
        report_title: str,
        report_description: str,
        time_series_ids_csv: str,
        tags_csv: str = "",
        time_range_from: str = "",
        time_range_to: str | None = None,
    ) -> str:
        ids = [s.strip() for s in time_series_ids_csv.split(",") if s.strip()]
        if not ids:
            raise ValueError("No time series cache IDs were provided.")

        tags = [t.strip() for t in tags_csv.split(",") if t.strip()]

        time_series_info: list[TimeSeriesInfoEntry] = []
        missing: list[str] = []
        for cache_id in ids:
            entry = SeriesCache._get_by_cache_id_sync(cache_id)
            if not entry:
                missing.append(cache_id)
                continue
            raw_metadata = entry.get("metadata")
            metadata = raw_metadata if isinstance(raw_metadata, dict) else {}
            time_series_info.append(
                {
                    "cache_id": str(entry["cache_id"]),
                    "title": str(entry.get("title") or ""),
                    "source": str(entry.get("source") or ""),
                    "native_id": str(entry.get("native_id") or ""),
                    "frequency": str(entry.get("frequency") or ""),
                    "observation_start": str(entry.get("observation_start") or ""),
                    "observation_end": str(entry.get("observation_end") or ""),
                    "metadata": metadata,
                }
            )

        if missing:
            raise ValueError(
                "Report creation aborted. Missing cache IDs: "
                + ", ".join(missing)
            )

        report_id = ReportCache._put_sync(
            report_title=report_title,
            report_description=report_description,
            time_series_info=time_series_info,
            time_range_from=time_range_from,
            time_range_to=time_range_to,
            tags=tags,
        )
        logger.debug(f"TimeSeriesReportAgent: created report '{report_title}' → {report_id}")
        detail_lines = "\n".join(
            f"  - `{row['cache_id']}` | {row['source']} | {row['title']}"
            for row in time_series_info
        )
        return (
            f"Report **{report_title}** created successfully.\n\n"
            f"- **Report ID:** `{report_id}`\n"
            f"- **Tags:** {', '.join(tags) if tags else '(none)'}\n"
            f"- **Time Series Count:** {len(time_series_info)}\n"
            f"- **Series:**\n{detail_lines}"
        )

    @staticmethod
    @tool_spec(
        args_schema=GetReportInput,
        metadata=ToolSpec(
            primary_function="""
                Retrieve a time series report by its UUID and return its details formatted in markdown.
            """,
            positive_examples=[
                PositiveExample(input="Show me report 24c23e96-5e97-4c3d-bb4a-c85116839d36."),
            ],
            negative_examples=[
                NegativeExample(
                    input="List all my reports.",
                    reason="Use list_time_series_reports to list all reports.",
                ),
            ],
        ),
    )
    def get_time_series_report(report_id: str) -> str:
        record = ReportCache._get_by_report_id_sync(report_id)
        if record is None:
            return f"No report found with ID `{report_id}`."
        info = record.get("time_series_info") or []
        lines = []
        for item in info:
            lines.append(
                f"- `{item.get('native_id', '')}` | {item.get('source', '')} | {item.get('title', '')}"
            )
        series_block = "\n".join(lines) if lines else "- (none)"
        time_range = str(record.get("time_range_from") or "")
        if record.get("time_range_to"):
            time_range += f" to {record['time_range_to']}"
        else:
            time_range += " to latest"
        tags_str = ", ".join(record.get("tags") or []) or "(none)"
        return (
            f"## {record['report_title']}\n\n"
            f"{record.get('report_description', '')}\n\n"
            f"**Tags:** {tags_str}\n\n"
            f"**Time Range:** {time_range}\n\n"
            f"**Time Series Info:**\n{series_block}"
        )

    @staticmethod
    @tool_spec(
        args_schema=ListReportsInput,
        metadata=ToolSpec(
            primary_function="""
                List all time series reports ordered by title.
                Returns a markdown table with report ID and title columns.
            """,
            positive_examples=[
                PositiveExample(input="List all time series reports."),
                PositiveExample(input="What reports do I have?"),
            ],
            negative_examples=[
                NegativeExample(
                    input="Show me the details of my GDP report.",
                    reason="Use get_time_series_report when a specific report ID is known.",
                ),
            ],
        ),
    )
    def list_time_series_reports() -> str:
        reports = ReportCache._list_reports_sync()
        if not reports:
            return "No time series reports found."
        rows = "\n".join(
            f"| `{r['report_id']}` | {r['report_title']} | {', '.join(r.get('tags') or [])} |"
            for r in reports
        )
        return (
            "| Report ID | Title | Tags |\n"
            "|-----------|-------|------|\n"
            f"{rows}"
        )


    @staticmethod
    @tool_spec(
        args_schema=GetReportInput,
        metadata=ToolSpec(
            primary_function="""
                Delete a time series report by its UUID.
                Returns a confirmation message on success or an error if the report is not found.
                If the user provides a title rather than an ID, call list_time_series_reports first
                to find the matching report_id.
            """,
            positive_examples=[
                PositiveExample(input="Delete report 24c23e96-5e97-4c3d-bb4a-c85116839d36."),
                PositiveExample(input="Delete the GDP Overview report."),
            ],
        ),
    )
    def delete_time_series_report(report_id: str) -> str:
        deleted = ReportCache._delete_report_sync(report_id)
        if deleted:
            return f"Report `{report_id}` deleted successfully."
        return f"No report found with ID `{report_id}`."
