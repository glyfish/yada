"""The owner must survive the trip from the HTTP request to a sync agent tool.

`identity.scoped()` installs a caller in a ContextVar, and the report tools read it
back with `current_user_id()`. Between those two points sit two hops that are easy to
assume and expensive to get wrong, because the failure is silent: the owner comes back
None, `_owned_by` turns scoping off, and the tool quietly serves every user's reports.

1. LangGraph runs a *sync* tool in a worker thread. It does so through
   `langchain_core.runnables.config.run_in_executor`, which copies the context -- but
   that is a property of LangChain's helper, not of `ThreadPoolExecutor`, so it is
   worth pinning rather than believing.
2. The streaming endpoints run the agent inside an async generator wrapped by
   `with identity.scoped(...)`. Async generators do not own a context; each `asend`
   runs in the consumer's. The wrapper relies on that, so it is pinned too.

No database: `current_user_id()` only reads the ContextVar.
"""
import asyncio

import pytest
from langchain_core.runnables.config import run_in_executor
from langchain_core.tools import StructuredTool

from apps.core import identity
from apps.core.identity import Caller, current_user_id

TROY = Caller(user_id="11111111-1111-1111-1111-111111111111", name="troy")


def test_scoped_installs_and_restores():
    assert current_user_id() is None
    with identity.scoped(TROY):
        assert current_user_id() == TROY.user_id
    assert current_user_id() is None


def test_scoped_restores_on_exception():
    with pytest.raises(RuntimeError):
        with identity.scoped(TROY):
            raise RuntimeError("boom")
    assert current_user_id() is None


@pytest.mark.asyncio
async def test_owner_reaches_a_sync_tool_run_in_a_worker_thread():
    """The hop LangGraph makes for every sync @staticmethod tool."""
    def a_report_tool() -> str | None:
        return current_user_id()

    with identity.scoped(TROY):
        in_thread = await run_in_executor(None, a_report_tool)
    assert in_thread == TROY.user_id


@pytest.mark.asyncio
async def test_owner_reaches_a_sync_tool_invoked_as_langchain_invokes_it():
    """The same hop, through the StructuredTool wrapper the agents actually build."""
    tool = StructuredTool.from_function(
        func=lambda: current_user_id() or "anonymous",
        name="whoami", description="probe",
    )
    with identity.scoped(TROY):
        assert await tool.ainvoke({}) == TROY.user_id
    assert await tool.ainvoke({}) == "anonymous"


@pytest.mark.asyncio
async def test_owner_is_visible_inside_a_wrapped_async_generator():
    """The shape api/main.py uses for the two streaming endpoints."""
    async def agent_work():
        for _ in range(3):
            await asyncio.sleep(0)
            yield current_user_id()

    async def event_generator():
        with identity.scoped(TROY):
            async for item in agent_work():
                yield item

    assert [x async for x in event_generator()] == [TROY.user_id] * 3
    assert current_user_id() is None
