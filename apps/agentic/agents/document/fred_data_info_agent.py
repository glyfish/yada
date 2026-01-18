from pydantic import BaseModel, Field
from collections import Counter
from functools import lru_cache
from pathlib import Path

from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.tools import tool

from apps.agentic.core.agents.tool_agent import ToolAgent
from apps.agentic.core.constants import GITHUB_LOCAL_PATH, DB_PATH
from apps.agentic.core.document_loaders.fred_document_loader import (
    FREDChromaDocumentLoader,
)

from lib.logger import get_logger

logger = get_logger("YADA")

def _collect_metadata_rows(loader, row_factory, limit=100_000) -> list[dict]:
    collection = getattr(loader.vectorstore, "_collection", None)
    if collection is None:
        logger.warning("Vector store collection unavailable for loader %s", loader)
        return []

    try:
        result = collection.get(include=["metadatas"], limit=limit)
    except Exception as exc:
        logger.error("Failed to read metadata: %s", exc)
        return []

    metadatas = result.get("metadatas") or []
    aggregated: dict[str, dict] = {}

    for meta in metadatas:
        if not meta:
            continue
        series_id = meta.get("series_id")
        if not series_id:
            continue
        if series_id in aggregated:
            continue

        aggregated[series_id] = row_factory(meta, series_id)

    return list(aggregated.values())


@lru_cache(maxsize=1)
def _fred_metadata(db_path=DB_PATH) -> list[dict]:
    """
    Aggregate research library metadata from the Chroma collection, one row per file.
    """

    loader = FREDChromaDocumentLoader(db_path)

    def _row_factory(meta, series_id):
        series_id = (meta.get("series_id") or "").strip()
        return {
            "category_id": meta.get("category_id") or "",
            "category_name": meta.get("category_name") or "",
            "category_path": meta.get("category_path") or "",
            "filename": meta.get("filename") or "",
            "frequency": meta.get("frequency") or "",
            "last_updated": meta.get("last_updated") or "",
            "leaf_name": meta.get("leaf_name") or "",
            "observation_end": meta.get("observation_end") or "",
            "observation_start": meta.get("observation_start") or "",
            "popularity": meta.get("popularity") or "",
            "seasonal_adjustment": meta.get("seasonal_adjustment") or "",
            "series_id": series_id,
            "series_title": meta.get("series_title") or "",
            "units": meta.get("units") or "",
        }

    return _collect_metadata_rows(loader, _row_factory)


class FredDataInfoAgent(ToolAgent):
    """
    Handle requests for information about FRED time series data.
    """

    def __init__(self):
        tools = [
        ]
        tool_node_name = "fred_info_tool_node"

        super().__init__(tools, tool_node_name)

    
    def create_prompt(self):
        """
        Create the prompt template for the FRED agent.
        """
    
        system_prompt = """
        You are an expert in retrieving information about the FRED document store which
        contains indexed Markdown files with descriptions of time series data from the FRED 
        (Federal Reserve Economic Data) website. The time series data is organized in a hierarchy
        of categories that describe the type of data contained in each time series. The categories
        are described in the markdown documents contained in the document store.
        - List the available FRED time series categories and the number of time series in each category.
          Return the data in a markdown table format with columns "Category Name" and "Count" sorted by 
          count descending.
        
        Call the appropriate tool when the user asks about any of these data sources.
        """

        logger.debug(f"DocumentInfoAgent Agent prompt: {system_prompt}")

        return ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            MessagesPlaceholder(variable_name="messages"),
            ("system", "If you choose to call a tool, do so; otherwise, provide your findings in plain text."),
        ])


    @staticmethod
    @tool
    def category_list(max_results: int = 100) -> list[tuple[str, int]]:
        """
        Obtain a list of categories available in the FRED document store sorted by the number of
        time series in each category descending.        

        Parameters
        ----------
        max_results: int
            Maximum number of metadata rows to return (default 100, capped at 1,000).

        Returns:
            list[tuple[str, int]]
                List of tuples containing category name and count of time series in 
                that category.
        """

        meta_data = _fred_metadata()

        # Count the number of time series in each category
        category_counts = Counter(meta.get("category") or "Unknown" for meta in meta_data)

        # Return the top categories by count
        return list(category_counts.items())[:max_results] if max_results else list(category_counts.items())


