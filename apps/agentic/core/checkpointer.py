import os
from pathlib import Path

from lib.logger import get_logger

logger = get_logger("YADA")

try:
    from langgraph.checkpoint.sqlite import SqliteSaver
except ImportError as exc:
    logger.warning(
        "SqliteSaver not available (%s). Falling back to in-memory checkpointing.",
        exc,
    )
    from langgraph.checkpoint.memory import MemorySaver

    checkpointer = MemorySaver()
else:
    # Shared LangGraph checkpointer for the entire application.
    # Uses a sqlite store under ./.langgraph by default so agent
    # graphs can persist conversation state across invocations.
    _default_dir = Path(os.getenv("YADA_CHECKPOINT_DIR", ".langgraph")).resolve()
    _default_dir.mkdir(parents=True, exist_ok=True)

    _db_path = _default_dir / "state.sqlite"

    # SqliteSaver handles locking internally; a single instance can be reused safely.
    checkpointer = SqliteSaver(str(_db_path))


__all__ = ["checkpointer"]
