from pydantic import BaseModel, Field

from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder


from apps.agentic.core.tool_spec import PositiveExample, NegativeExample, ToolSpec, tool_spec

from pathlib import Path

from apps.agentic.core.agents.react_agent import ReactAgent
from apps.agentic.core.constants import GITHUB_LOCAL_PATH, DB_PATH
from apps.agentic.core.document_loaders.etf.finance_database_loader import FinanceDatabaseLoader
from apps.agentic.core.document_loaders.etf.exchange_metadata import EXCHANGES, CURRENCIES
from apps.agentic.core.document_loaders.research_library_document_loader import (
    ResearchLibraryChromaDocumentLoader,
)
from apps.agentic.core.document_loaders.document_library_loader import (
    DocumentLibraryLoader,
)

from apps.agentic.db.series_cache import SeriesCache
from apps.agentic.db.report_cache import ReportCache

from apps.agentic.agents.document.code_repo_agent import CodeRepoAgent
from apps.agentic.agents.document.fred_data_info_agent import FredDataInfoAgent
from apps.agentic.agents.document.research_library_agent import ResearchLibraryAgent
from apps.agentic.agents.document.pdf_document_library_agent import PDFDocumentLibraryAgent

from lib.logger import get_logger

logger = get_logger("YADA")

class ListTimeSeriesReportsInput(BaseModel):
    pass


class TimeSeriesReportDetailsInput(BaseModel):
    report_id_or_title: str = Field(
        ...,
        description="report_id UUID or title substring of the report to retrieve details for.",
    )


class ListTimeSeriesInput(BaseModel):
    pass


class TimeSeriesDetailsInput(BaseModel):
    native_id_or_external_id: str = Field(
        ...,
        description="native_id UUID or external_id (e.g. UNRATE) of the cached series.",
    )


class RepositoryFilesInput(BaseModel):
    """Schema for requesting filenames within a repository."""
    account: str = Field(
        ...,
        description="GitHub account/owner name, e.g., 'troystribling'.",
    )
    repository: str = Field(
        ...,
        description="Repository name, e.g., 'yada'.",
    )
    max_results: int = Field(
        default=250,
        ge=1,
        le=5000,
        description="Maximum number of filenames to return (default 250).",
    )

class ResearchLibraryMetadataListInput(BaseModel):
    """Schema for slicing research library metadata rows."""

    max_results: int = Field(
        default=100,
        ge=1,
        le=1000,
        description="Maximum number of research note metadata rows to return (default 100).",
    )
    start_after: str | None = Field(
        default=None,
        description="Filename or path after which to start the listing (exclusive).",
    )

class ETFMetadataFieldInput(BaseModel):
    field: str = Field(
        ...,
        description="""
ETF metadata field to list distinct values for. Must be one of:
'exchange' — exchange codes with full name and country,
'currency' — currency codes with full name and country,
'family' — fund family names,
'category_group' — broad asset classes,
'category' — specific fund categories.
""",
    )


class ResearchLibraryTitleQueryInput(BaseModel):
    """Schema for filtering research library titles by metadata."""

    author: str | None = Field(
        default=None,
        description="Author name to filter by (case-insensitive substring match).",
    )
    topic: str | None = Field(
        default=None,
        description="Topic text to filter by (case-insensitive substring match).",
    )
    shelf: str | None = Field(
        default=None,
        description="Require that the document belongs to this shelf (case-insensitive).",
    )
    limit: int = Field(
        default=100,
        ge=1,
        le=200,
        description="Maximum number of titles to return (default 100).",
    )


def collect_metadata_rows(loader, row_factory) -> list[dict]:
    collection = getattr(loader.vectorstore, "_collection", None)
    if collection is None:
        logger.warning("Vector store collection unavailable for loader %s", loader)
        return []

    try:
        result = collection.get(include=["metadatas"], limit=100_000)
    except Exception as exc:
        logger.error("Failed to read metadata: %s", exc)
        return []

    metadatas = result.get("metadatas") or []
    aggregated: dict[str, dict] = {}

    for meta in metadatas:
        if not meta:
            continue
        path = meta.get("path") or meta.get("filename")
        if not path:
            continue
        if path in aggregated:
            continue

        aggregated[path] = row_factory(meta, path)

    return list(aggregated.values())


def paginate_metadata_rows(rows: list[dict], max_results: int, start_after: str | None) -> list[dict]:
    if not rows:
        return []

    sorted_rows = sorted(rows, key=lambda r: (r.get("filename") or r.get("path") or "").lower())
    start_index = 0
    if start_after:
        token = start_after.lower()
        for idx, row in enumerate(sorted_rows):
            filename = (row.get("filename") or "").lower()
            path = (row.get("path") or "").lower()
            if token in {filename, path}:
                start_index = idx + 1
                break

    end_index = min(start_index + max_results, len(sorted_rows))
    return sorted_rows[start_index:end_index]

class DataInfoAgent(ReactAgent):
    """
    Handle requests for information about document libraries.
    """

    @classmethod
    async def create(cls) -> "DataInfoAgent":
        return cls()

    def __init__(self, mcp_tools: list = []):
        tools = [
            DataInfoAgent.list_time_series_reports,
            DataInfoAgent.list_time_series_report_details,
            DataInfoAgent.list_time_series,
            DataInfoAgent.list_time_series_details,
            DataInfoAgent.repository_names,
            DataInfoAgent.filenames_for_repository,
            DataInfoAgent.research_library_metadata_summary,
            DataInfoAgent.research_library_titles_by_metadata,
            DataInfoAgent.etf_metadata_values,
        ]
        tool_node_name = "document_info_tool_node"

        super().__init__(tools, tool_node_name, mcp_tools=mcp_tools)

    
    def create_prompt(self):
        """
        Create the prompt template for the document library agent.
        """
    
        system_prompt = """
        <instructions>
        You are an expert in retrieving information about the contents of documents and data available
        in all data stores. The tools allow you to:
        - List all time series reports (title, report_id, time range).
        - Show full metadata for a specific report by report_id or title substring, including the series it contains.
        - List all cached time series (title, native_id, external_id, source, frequency, date range).
        - Show full metadata for a specific cached time series by native_id or external_id.
        - List repository names and filenames for code repositories.
        - Summarize metadata for research notes, including filename, title, author, topic, and shelf.
        - Filter research note titles using author/topic/shelf metadata.
        - Summarize metadata for PDF documents, including filename, title, authors, published date, topic, and shelf.
        - Filter PDF document titles using author/topic/shelf metadata.
        - List distinct ETF metadata values for exchange, currency, family, category_group, or category fields.
        Call the appropriate tool when the user asks about any of these data sources.
        </instructions>
        """

        return ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            MessagesPlaceholder(variable_name="messages"),
        ])


    @staticmethod
    def _research_library_metadata(db_path=DB_PATH) -> list[dict]:
        """
        Aggregate research library metadata from the Chroma collection, one row per file.
        """

        loader = ResearchLibraryChromaDocumentLoader(db_path)

        def _row_factory(meta, path):
            shelf = (meta.get("shelf") or "").strip()
            return {
                "filename": meta.get("filename") or Path(path).name,
                "path": path,
                "title": meta.get("title") or Path(path).stem,
                "authors": meta.get("authors") or "",
                "topic": meta.get("topic") or "",
                "shelf": shelf,
            }

        return collect_metadata_rows(loader, _row_factory)


    @staticmethod
    @tool_spec(
        args_schema=None,
        metadata=ToolSpec(
            primary_function=
            """
            List all repository names available in the code repository document store.
            Returns account/repository pairs for every indexed GitHub repository.
            """,
            positive_examples=[
                PositiveExample(input="What repositories are in my code store?"),
                PositiveExample(input="List all code repositories in the glyfish account."),
                PositiveExample(input="What GitHub repositories do I have?"),
                PositiveExample(input="What GitHub accounts do I have?"),
            ],
            suggests_followup=[
                "filenames_for_repository to list files within a specific repository",
            ],
        ),
    )
    def repository_names() -> list[str]:

        base_path = Path(GITHUB_LOCAL_PATH)
        if not base_path.exists():
            logger.warning(f"GitHub local path '{base_path}' does not exist.")
            return []

        repo_names: list[str] = []
        for account_dir in sorted(p for p in base_path.iterdir() if p.is_dir()):
            for repo_dir in sorted(p for p in account_dir.iterdir() if p.is_dir()):
                repo_names.append(f"{account_dir.name}/{repo_dir.name}")

        return repo_names


    @staticmethod
    @tool_spec(
        args_schema=RepositoryFilesInput,
        metadata=ToolSpec(
            primary_function=
            """
            List filenames within a specific code repository.
            Returns relative file paths for all files in the given account/repository.
            """,
            positive_examples=[
                PositiveExample(input="What file are in the yada repository implement an agent?"),
                PositiveExample(input="List files in troystribling/zgomot."),
                PositiveExample(input="Show me the files in my gly.fish/navi repo."),
            ],
            requires_context=[
                "Call repository_names first if the account or repository name is not known.",
            ],
        ),
    )
    def filenames_for_repository(account: str, repository: str, max_results: int = 250) -> list[str]:

        base_path = Path(GITHUB_LOCAL_PATH)
        repo_path = base_path / account / repository

        if not repo_path.exists():
            logger.warning("Repository path does not exist: %s", repo_path)
            return []

        files: list[str] = []
        limit = max(1, min(max_results, 5000))

        for path in repo_path.rglob("*"):
            if path.is_file():
                files.append(str(path.relative_to(repo_path)))
                if len(files) >= limit:
                    break

        return files


    @staticmethod
    @tool_spec(
        args_schema=ResearchLibraryMetadataListInput,
        metadata=ToolSpec(
            primary_function=
            """
            Return paginated metadata rows (filename, title, author, topic, shelf)
            for research notes in the research library.
            """,
            positive_examples=[
                PositiveExample(input="What metadata is available for documents in the research library?"),
            ],
            suggests_followup=[
                "research_library_titles_by_metadata to filter results by author, topic, or shelf",
            ],
        ),
    )
    def research_library_metadata_summary(
        max_results: int = 100, start_after: str | None = None
    ) -> list[dict]:

        rows = DataInfoAgent._research_library_metadata()
        return paginate_metadata_rows(rows, max_results, start_after)


    @staticmethod
    @tool_spec(
        args_schema=ResearchLibraryTitleQueryInput,
        metadata=ToolSpec(
            primary_function=
            """
            Return research note titles filtered by author, topic, or shelf metadata.
            All filters are optional and use case-insensitive matching.
            """,
            positive_examples=[
                PositiveExample(input="What are the titles of papers by Jaynes in the research library?"),
                PositiveExample(input="Find the titles of research notes on thermodynamics."),
                PositiveExample(input="What are the titles of documents on the 'publications' shelf?"),
                PositiveExample(input="What are the document shelves available in my research library?"),                
            ],
            requires_context=[
                "Call research_library_metadata_summary first to get available metadata before filtering titles.",
            ],
            negative_examples=[
            ],
        ),
    )
    def research_library_titles_by_metadata(
        author: str | None = None,
        topic: str | None = None,
        shelf: str | None = None,
        limit: int = 25,
    ) -> list[dict]:

        rows = DataInfoAgent._research_library_metadata()
        if not rows:
            return []

        filtered = []
        author_token = author.lower() if author else None
        topic_token = topic.lower() if topic else None
        shelf_token = shelf.lower() if shelf else None

        for row in rows:
            row_author = (row.get("author") or "").lower()
            row_topic = (row.get("topic") or "").lower()
            row_shelf = (row.get("shelf") or "").lower()

            if author_token and author_token not in row_author:
                continue
            if topic_token and topic_token not in row_topic:
                continue
            if shelf_token and shelf_token != row_shelf:
                continue

            filtered.append(row)
            if len(filtered) >= limit:
                break

        return [
            {
                "title": item.get("title"),
                "filename": item.get("filename"),
                "author": item.get("author"),
                "topic": item.get("topic"),
                "shelf": item.get("shelf"),
            }
            for item in filtered
        ]


    @staticmethod
    def _etf_distinct_values(field: str, db_path: str = DB_PATH) -> list[str]:
        loader = FinanceDatabaseLoader(db_path=db_path)
        collection = getattr(loader.vectorstore, "_collection", None)
        if collection is None:
            return []
        total = collection.count()
        if total == 0:
            return []
        distinct: set[str] = set()
        BATCH = 5000
        for offset in range(0, total, BATCH):
            result = collection.get(limit=BATCH, offset=offset, include=["metadatas"])
            for meta in result.get("metadatas") or []:
                val = (meta or {}).get(field)
                if val:
                    distinct.add(val)
        return sorted(distinct)


    @staticmethod
    @tool_spec(
        args_schema=ETFMetadataFieldInput,
        metadata=ToolSpec(
            primary_function=
            """
            Return distinct metadata values for a single ETF field.
            Supports: 'exchange' (with full name and country), 'currency' (with full name and country),
            'family' (fund family names), 'category_group' (broad asset classes), 'category' (fund categories).
            """,
            positive_examples=[
                PositiveExample(input="What exchanges are available in the ETF store?"),
                PositiveExample(input="What currencies are used in the ETF database?"),
                PositiveExample(input="List all fund families in the ETF store."),
                PositiveExample(input="What category groups are available for ETFs?"),
                PositiveExample(input="What ETF categories are in the database?"),
            ],
        ),
    )
    def etf_metadata_values(field: str) -> str:
        VALID = {"exchange", "currency", "family", "category_group", "category"}
        if field not in VALID:
            return f"Invalid field '{field}'. Must be one of: {', '.join(sorted(VALID))}."

        values = DataInfoAgent._etf_distinct_values(field)
        if not values:
            return f"No values found for field '{field}'."

        lines = [f"**ETF {field} values ({len(values)} distinct):**", ""]
        for code in values:
            if field == "exchange":
                info = EXCHANGES.get(code)
                label = f"{info['name']} ({info['location']})" if info else ""
                lines.append(f"- {code}" + (f" — {label}" if label else ""))
            elif field == "currency":
                info = CURRENCIES.get(code)
                label = f"{info['name']} ({info['country']})" if info else ""
                lines.append(f"- {code}" + (f" — {label}" if label else ""))
            else:
                lines.append(f"- {code}")
        return "\n".join(lines)


    @staticmethod
    @tool_spec(
        args_schema=ListTimeSeriesReportsInput,
        metadata=ToolSpec(
            primary_function="""
                List all time series reports stored in the report cache.
                Returns report_id, report_title, time_range_from, and time_range_to for each report.
            """,
            positive_examples=[
                PositiveExample(input="What time series reports do I have?"),
                PositiveExample(input="List all time series reports."),
                PositiveExample(input="Show me my reports."),
            ],
            suggests_followup=[
                "list_time_series_report_details to see full metadata for a specific report",
            ],
        ),
    )
    def list_time_series_reports() -> str:
        rows = ReportCache._list_reports_sync()
        if not rows:
            return "No time series reports found."
        lines = [
            "| Title | Tags | report_id | Time Range From | Time Range To |",
            "|-------|------|-----------|-----------------|---------------|",
        ]
        for r in rows:
            time_to = r["time_range_to"] or "latest"
            tags_str = ", ".join(r.get("tags") or [])
            lines.append(
                f"| {r['report_title']} | {tags_str} | `{r['report_id']}` | {r['time_range_from']} | {time_to} |"
            )
        return "\n".join(lines)


    @staticmethod
    @tool_spec(
        args_schema=TimeSeriesReportDetailsInput,
        metadata=ToolSpec(
            primary_function="""
                Return full metadata for a time series report identified by report_id UUID or
                a title substring. Returns the title, description, time range, and the list of
                time series entries (native_id, external_id, title, units, value_range, etc.).
                If multiple reports match the title fragment, a disambiguation list is returned.
            """,
            positive_examples=[
                PositiveExample(input="Show me the details for my unemployment report."),
                PositiveExample(input="What time series are in the GDP report?"),
                PositiveExample(input="Show the details of report abc-123."),
            ],
            requires_context=[
                "Call list_time_series_reports first if the report_id or title is not already known.",
            ],
        ),
    )
    def list_time_series_report_details(report_id_or_title: str) -> str:
        import uuid as _uuid
        try:
            uid = _uuid.UUID(report_id_or_title)
            record = ReportCache._get_by_report_id_sync(str(uid))
        except ValueError:
            matches = ReportCache._search_by_title_sync(report_id_or_title)
            if not matches:
                return f"No report found matching `{report_id_or_title}`."
            if len(matches) > 1:
                lines = [f"Multiple reports match '{report_id_or_title}'. Please specify one:"]
                for m in matches:
                    lines.append(f"- **{m['report_title']}** (`{m['report_id']}`)")
                return "\n".join(lines)
            record = ReportCache._get_by_report_id_sync(matches[0]["report_id"])

        if record is None:
            return f"No report found matching `{report_id_or_title}`."

        time_to = str(record.get("time_range_to") or "latest")
        tags_str = ", ".join(record.get("tags") or [])
        series_info = record.get("time_series_info") or []
        lines = [
            f"**{record['report_title']}**",
            "",
            "| Field | Value |",
            "|-------|-------|",
            f"| report_id | `{record['report_id']}` |",
            f"| description | {record.get('report_description', '')} |",
            f"| tags | {tags_str} |",
            f"| time_range_from | {record.get('time_range_from', '')} |",
            f"| time_range_to | {time_to} |",
            "",
            "**Time Series:**",
            "",
            "| Title | native_id | external_id | Source | Frequency | Units |",
            "|-------|-----------|-------------|--------|-----------|-------|",
        ]
        for s in series_info:
            units = (s.get("metadata") or {}).get("units", "")
            lines.append(
                f"| {s.get('title', '')} | `{s.get('native_id', '')}` | {s.get('external_id', '')}"
                f" | {s.get('source', '')} | {s.get('frequency', '')} | {units} |"
            )
        return "\n".join(lines)


    @staticmethod
    @tool_spec(
        args_schema=ListTimeSeriesInput,
        metadata=ToolSpec(
            primary_function="""
                List all time series stored in the cache.
                Returns title, native_id, external_id, source, frequency,
                observation_start, and observation_end for each series.
            """,
            positive_examples=[
                PositiveExample(input="What time series do I have cached?"),
                PositiveExample(input="List all cached time series."),
                PositiveExample(input="Show me the time series in the cache."),
            ],
            suggests_followup=[
                "list_time_series_details to see full metadata for a specific series",
            ],
        ),
    )
    def list_time_series() -> str:
        rows = SeriesCache._list_series_sync()
        if not rows:
            return "No time series found in the cache."
        lines = ["| Title | native_id | external_id | Source | Frequency | Start | End |",
                 "|-------|-----------|-------------|--------|-----------|-------|-----|"]
        for r in rows:
            lines.append(
                f"| {r['title']} | `{r['native_id']}` | {r['external_id']}"
                f" | {r['source']} | {r['frequency']}"
                f" | {r['observation_start']} | {r['observation_end']} |"
            )
        return "\n".join(lines)


    @staticmethod
    @tool_spec(
        args_schema=TimeSeriesDetailsInput,
        metadata=ToolSpec(
            primary_function="""
                Return full metadata for a cached time series identified by native_id UUID
                or external_id (e.g. UNRATE). Does not return observations.
                If external_id matches multiple entries all are returned.
            """,
            positive_examples=[
                PositiveExample(input="Show me the details for time series UNRATE."),
                PositiveExample(input="What are the details of the series with native_id abc-123?"),
            ],
            requires_context=[
                "Call list_time_series first if the native_id or external_id is not already known.",
            ],
        ),
    )
    def list_time_series_details(native_id_or_external_id: str) -> str:
        rows = SeriesCache._get_details_by_id_sync(native_id_or_external_id)
        if not rows:
            return f"No cached series found matching `{native_id_or_external_id}`."
        blocks = []
        for r in rows:
            units = (r.get("metadata") or {}).get("units", "")
            obs_count = (r.get("metadata") or {}).get("observation_count", "")
            blocks.append(
                f"**{r['title']}**\n\n"
                f"| Field | Value |\n|-------|-------|\n"
                f"| native_id | `{r['native_id']}` |\n"
                f"| external_id | {r['external_id']} |\n"
                f"| source | {r['source']} |\n"
                f"| frequency | {r['frequency']} |\n"
                f"| units | {units} |\n"
                f"| observation_count | {obs_count} |\n"
                f"| observation_start | {r['observation_start']} |\n"
                f"| observation_end | {r['observation_end']} |\n"
                f"| created_at | {r['created_at']} |\n"
                f"| updated_at | {r['updated_at']} |\n"
                f"| expires_at | {r['expires_at']} |"
            )
        return "\n\n---\n\n".join(blocks)
