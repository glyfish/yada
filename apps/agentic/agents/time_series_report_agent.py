from __future__ import annotations

from pydantic import BaseModel, Field

from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder

from apps.agentic.core.tool_spec import PositiveExample, NegativeExample, ToolSpec, tool_spec
from apps.agentic.core.agents.react_agent import ReactAgent
from apps.agentic.db.report_cache import ReportCache

from lib.logger import get_logger

logger = get_logger("YADA")


class CreateReportInput(BaseModel):
    report_title: str = Field(..., description="Title of the report.")
    report_description: str = Field(..., description="Description of the report.")
    time_series_ids_csv: str = Field(
        ...,
        description="Comma-separated list of time series cache IDs to include in the report.",
    )


class GetReportInput(BaseModel):
    report_id: str = Field(..., description="UUID of the report to retrieve.")


class ListReportsInput(BaseModel):
    pass


class TimeSeriesReportAgent(ReactAgent):

    @classmethod
    async def create(cls) -> "TimeSeriesReportAgent":
        return cls()

    def __init__(self, mcp_tools: list = []):
        tools = [
            TimeSeriesReportAgent.create_time_series_report,
            TimeSeriesReportAgent.get_time_series_report,
            TimeSeriesReportAgent.list_time_series_reports,
        ]
        super().__init__(tools, "time_series_report_tool_node", mcp_tools=mcp_tools)

    def create_prompt(self):
        system_prompt = """
            <instructions>
            You are a time series report agent. You create, retrieve, and list time series reports.
            A report groups a set of time series cache IDs under a title and description for later reference.

            Use create_time_series_report when the user wants to save a new report. The time series IDs
            will be provided as a comma-separated string.

            Use get_time_series_report when the user wants to view the details of a specific report by ID.

            Use list_time_series_reports when the user wants to see all existing reports.

            Always respond in markdown. For created reports, confirm the title and report ID.
            For retrieved reports, format the details clearly including the list of time series IDs.
            For listed reports, present a markdown table with report ID and title columns.
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
                The time series IDs are provided as a comma-separated string and stored as a list.
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
    ) -> str:
        ids = [s.strip() for s in time_series_ids_csv.split(",") if s.strip()]
        report_id = ReportCache._put_sync(
            report_title=report_title,
            report_description=report_description,
            time_series_ids=ids,
        )
        logger.debug(f"TimeSeriesReportAgent: created report '{report_title}' → {report_id}")
        return (
            f"Report **{report_title}** created successfully.\n\n"
            f"- **Report ID:** `{report_id}`\n"
            f"- **Time series IDs:** {', '.join(ids)}"
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
        ids = record["time_series_ids"]
        id_list = "\n".join(f"- `{i}`" for i in ids)
        return (
            f"## {record['report_title']}\n\n"
            f"**Time Series IDs:**\n{id_list}"
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
            f"| `{r['report_id']}` | {r['report_title']} |"
            for r in reports
        )
        return (
            "| Report ID | Title |\n"
            "|-----------|-------|\n"
            f"{rows}"
        )
