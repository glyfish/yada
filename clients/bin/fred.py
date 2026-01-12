#!/usr/bin/env python3
"""
Populate the FRED Chroma collection from the local YAML exports.

Examples
--------
- Load all files into default DB_PATH:
    python clients/bin/fred.py

- Load a specific file:
    python clients/bin/fred.py --filename fred_finance_32991.yaml

- Load all files from a custom categories directory and write to an alternate DB path:
    python clients/bin/fred.py --db-path ./my_chroma_db

"""

from __future__ import annotations

import argparse
import asyncio
import os
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from apps.agentic.core.document_loaders.fred_document_loader import FREDChromaDocumentLoader
from apps.agentic.core.constants import DB_PATH
from apps.agentic.core.utils import set_chatgpt_env


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Load category/series YAML files into the FRED Chroma collection."
    )
    parser.add_argument(
        "--filename",
        help="Specific YAML filename (e.g., fred_finance_32991.yaml). "
        "If omitted, every file in the categories directory is ingested.",
    )
    parser.add_argument(
        "--db-path",
        default=None,
        help="Optional override for the Chroma persistence directory (defaults to DB_PATH).",
    )
    return parser


async def run_ingest(filename: str | None, db_path: str | None) -> None:
    loader = FREDChromaDocumentLoader(db_path=db_path or DB_PATH)
    if filename:
        await loader.load_document(Path(filename).name)
    else:
        await loader.load_all_documents()


def ensure_openai_api_key() -> None:
    """
    Ensure OPENAI_API_KEY is available, loading it from .keys/.chatgpt_key if needed.
    """

    if os.environ.get("OPENAI_API_KEY"):
        return
    try:
        set_chatgpt_env()
    except FileNotFoundError as exc:
        raise RuntimeError(
            "OPENAI_API_KEY is not set and .keys/.chatgpt_key could not be loaded."
        ) from exc


def main() -> None:
    args = build_parser().parse_args()
    ensure_openai_api_key()
    asyncio.run(run_ingest(args.filename, args.db_path))


if __name__ == "__main__":
    main()
