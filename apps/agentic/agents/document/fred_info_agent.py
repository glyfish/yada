from pydantic import BaseModel, Field

from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.tools import tool

from functools import lru_cache

from pathlib import Path

from apps.agentic.core.agents.tool_agent import ToolAgent
from apps.agentic.core.constants import GITHUB_LOCAL_PATH, DB_PATH
from apps.agentic.core.document_loaders.research_library_document_loader import (
    ResearchLibraryChromaDocumentLoader,
)
from apps.agentic.core.document_loaders.document_library_loader import (
    DocumentLibraryLoader,
)

from lib.logger import get_logger

logger = get_logger("YADA")

