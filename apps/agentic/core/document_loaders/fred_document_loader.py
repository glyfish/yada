import os
import re, bisect
from pathlib import Path
import aiofiles
import yaml

from lib.logger import get_logger
from git import Repo

from langchain.text_splitter import RecursiveCharacterTextSplitter, MarkdownHeaderTextSplitter
from langchain_core.documents import Document

from apps.agentic.core.document_loaders.chroma_document_loader import ChromaDocumentLoader
from apps.agentic.core.constants import (FRED_DB_NAME, FRED_COLLECTION_NAME, FRED_LOCAL_PATH, 
                                         DB_PATH)

from lib.utils import get_param_throw_if_missing

logger = get_logger("YADA")


def _date_to_int(value) -> int | None:
    """
    Convert an ISO date/datetime string to a YYYYMMDD integer so it can be range
    filtered in Chroma, which rejects string operands for $gte/$lte. Handles plain
    dates ('1937-08-12') and datetimes ('2020-07-03T16:29:23-05:00'), including
    historic pre-1970 dates (the result stays positive and monotonic). Returns
    None when the value is missing or unparseable.
    """
    if not isinstance(value, str):
        return None
    m = re.match(r"\s*(\d{4})-(\d{2})-(\d{2})", value)
    if not m:
        return None
    return int(m.group(1) + m.group(2) + m.group(3))


class FREDChromaDocumentLoader(ChromaDocumentLoader):
    """
    Document loader for FRED API metadata files stored as YAML files. The documents will be small
    enough to not require further splitting.

    Metadata added to each document
    ------------------------------
    - filename: Base name of the file
    - path: File path relative to the research notes root
    - category: Category identifier of the FRED data
    - series: Series identifier of the FRED data
    - observation_start: Start date of observations
    - observation_end: End date of observations
    """

    def __init__(self, db_path=DB_PATH):
        super().__init__(FRED_DB_NAME, FRED_COLLECTION_NAME, db_path)
    

    async def load_document(self, path: str, **kwargs):
        """
        Load a **Markdown** research document into the ChromaDB collection.
        """

        category_path = os.path.join(FRED_LOCAL_PATH, "categories", path)
        series_path = os.path.join(FRED_LOCAL_PATH, "series", path)
        logger.info(f"Loading FRED series meta data from {category_path} and {series_path}.")

        async with aiofiles.open(category_path, "r", encoding="utf-8", errors="ignore") as f:
            category_yaml = await f.read()

        async with aiofiles.open(series_path, "r", encoding="utf-8", errors="ignore") as f:
            series_yaml = await f.read()

        try:
            categories = yaml.safe_load(category_yaml) or []
        except yaml.YAMLError as exc:
            logger.exception(f"Failed to parse category YAML {category_path}: {exc}")
            return

        try:
            series_groups = yaml.safe_load(series_yaml) or []
        except yaml.YAMLError as exc:
            logger.exception(f"Failed to parse series YAML {series_path}: {exc}")
            return

        if not isinstance(categories, list):
            logger.warning(f"Unexpected category YAML format in {category_path}. Expected list.")
            categories = [categories]

        if not isinstance(series_groups, list):
            logger.warning(f"Unexpected series YAML format in {series_path}. Expected list.")
            series_groups = [series_groups]

        category_lookup = {}
        for category in categories:
            if not isinstance(category, dict):
                continue
            leaf_id = category.get("leaf_id")
            if leaf_id is not None:
                category_lookup[leaf_id] = category

        documents = []
        for group in series_groups:
            if not isinstance(group, dict):
                continue

            category_id = group.get("category_id")
            matched_category = category_lookup.get(category_id, {})
            category_name = group.get("category_name") or matched_category.get("leaf_name")
            category_path = matched_category.get("path") or []
            category_path_str = " > ".join(
                p.get("name", "")
                if isinstance(p, dict)
                else str(p)
                for p in category_path
            ).strip()

            for series in group.get("seriess", []):
                if not isinstance(series, dict):
                    continue

                series_id = series.get("id")
                series_title = series.get("title", "Unknown Series")
                observation_range = f"{series.get('observation_start', 'N/A')} – {series.get('observation_end', 'N/A')}"
                frequency = series.get("frequency", "Unknown")
                units = series.get("units", "Unknown")
                seasonal_adjustment = series.get("seasonal_adjustment", "Unknown")
                last_updated = series.get("last_updated", "Unknown")
                popularity = series.get("popularity", "Unknown")
                notes = (series.get("notes") or "").replace("\r\n", "\n").strip()

                markdown = [
                    f"# {series_title}",
                    "",
                    "## Series Information",
                    f"- **Series ID:** {series_id}",
                    f"- **Frequency:** {frequency}",
                    f"- **Units:** {units}",
                    f"- **Seasonal Adjustment:** {seasonal_adjustment}",
                    f"- **Observation Range:** {observation_range}",
                    f"- **Last Updated:** {last_updated}",
                    f"- **Popularity:** {popularity}",
                ]

                markdown.extend(
                    [
                        "",
                        "## Category Information",
                        f"- **Category ID:** {category_id}",
                        f"- **Category Name:** {category_name}",
                        f"- **Leaf Name:** {matched_category.get('leaf_name') or ''}",
                        f"- **Category Path:** {category_path_str or 'N/A'}",
                    ]
                )

                if notes:
                    markdown.extend(["", "## Notes", notes])

                doc_metadata = {
                    "filename": path,
                    "category_id": category_id,
                    "category_name": category_name,
                    "leaf_name": matched_category.get("leaf_name"),
                    "category_path": category_path_str,
                    "series_id": series_id,
                    "series_title": series_title,
                    "observation_start": series.get("observation_start"),
                    "observation_end": series.get("observation_end"),
                    "frequency": frequency,
                    "units": units,
                    "seasonal_adjustment": seasonal_adjustment,
                    "last_updated": last_updated,
                    "popularity": popularity,
                }

                # Numeric YYYYMMDD copies of the date fields for range filtering
                # (Chroma $gte/$lte require int/float, not strings). Omitted when
                # the source date is missing or unparseable.
                for _key, _raw in (
                    ("observation_start_int", series.get("observation_start")),
                    ("observation_end_int", series.get("observation_end")),
                    ("last_updated_int", last_updated),
                ):
                    _int = _date_to_int(_raw)
                    if _int is not None:
                        doc_metadata[_key] = _int

                documents.append(
                    Document(page_content="\n".join(markdown), metadata=doc_metadata)
                )

        if not documents:
            logger.warning(f"No FRED metadata documents created from {path}.")
            return

        BATCH = 128
        for i in range(0, len(documents), BATCH):
            self.vectorstore.add_documents(documents[i : i + BATCH])

        logger.info(f"Loaded {len(documents)} FRED metadata documents from {path} into collection {self.collection_name}.")


    async def load_all_documents(self, base_path: str = os.path.join(FRED_LOCAL_PATH, "categories"), **kwargs):
        """
        Iterate over every FRED metadata file and delegate to load_document.
        """

        categories_dir = os.path.realpath(base_path)
        if not os.path.isdir(categories_dir):
            raise FileNotFoundError(f"FRED categories directory not found: {categories_dir}")

        logger.info(f"Loading FRED metadata files from {categories_dir}.")

        filenames = sorted(
            f for f in os.listdir(categories_dir)
            if os.path.isfile(os.path.join(categories_dir, f))
        )

        if not filenames:
            logger.warning(f"No files found in {categories_dir}; nothing to load.")
            return

        for filename in filenames:
            logger.debug(f"Enqueuing FRED metadata load for {filename}.")
            try:
                await self.load_document(filename, **kwargs)
            except Exception:
                logger.exception(f"Failed to load FRED metadata for {filename}. Continuing with next file.")

        logger.info("Finished loading FRED metadata files.")
        
