import asyncio
import os
import threading
from pathlib import Path

from lib.logger import get_logger

logger = get_logger("YADA")

checkpointer = None

SafeAsyncSqliteSaver = None  # type: ignore[assignment]

try:
    # Async saver moved under langgraph.checkpoint.sqlite.aio in newer releases.
    from langgraph.checkpoint.sqlite.aio import AsyncSqliteSaver
    from langgraph.checkpoint.base import get_serializable_checkpoint_metadata
    import aiosqlite
except ImportError:
    AsyncSqliteSaver = None
    get_serializable_checkpoint_metadata = None  # type: ignore
else:

    class SafeAsyncSqliteSaver(AsyncSqliteSaver):
        """AsyncSqliteSaver that strips non-serializable metadata."""

        async def aput(self, config, checkpoint, metadata, new_versions):
            if get_serializable_checkpoint_metadata:
                metadata = get_serializable_checkpoint_metadata(config, metadata)
            return await super().aput(config, checkpoint, metadata, new_versions)


def _create_async_checkpointer(db_path: Path):
    """Spin up a background event loop and initialize AsyncSqliteSaver on it."""

    loop = asyncio.new_event_loop()

    def _run_loop():
        asyncio.set_event_loop(loop)
        loop.run_forever()

    threading.Thread(target=_run_loop, daemon=True).start()

    async def _init_saver() -> "AsyncSqliteSaver":
        conn = await aiosqlite.connect(str(db_path))
        saver_cls = SafeAsyncSqliteSaver or AsyncSqliteSaver
        return saver_cls(conn)

    future = asyncio.run_coroutine_threadsafe(_init_saver(), loop)
    return future.result()


if AsyncSqliteSaver:
    try:
        # Shared LangGraph checkpointer for the entire application.
        # Uses a sqlite store under ./.langgraph by default so agent
        # graphs can persist conversation state across invocations.
        _default_dir = Path(os.getenv("YADA_CHECKPOINT_DIR", ".langgraph")).resolve()
        _default_dir.mkdir(parents=True, exist_ok=True)

        _db_path = _default_dir / "state.sqlite"
        checkpointer = _create_async_checkpointer(_db_path)
    except Exception as exc:  # pragma: no cover - defensive fallback
        logger.warning(
            "Async SqliteSaver init failed (%s). Falling back to in-memory checkpointing.",
            exc,
        )
        from langgraph.checkpoint.memory import MemorySaver

        checkpointer = MemorySaver()
else:
    from langgraph.checkpoint.memory import MemorySaver

    checkpointer = MemorySaver()


__all__ = ["checkpointer"]
