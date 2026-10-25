"""
Log every JSON-RPC message a client sends, before anything interprets it.

The tool-level logging in ``document_tools`` records arguments *after* the SDK has
parsed them and bound them to a function signature. That is the right view most of the
time and the wrong one exactly when something is going wrong:

- a call whose arguments fail schema validation is refused before the tool runs, so it
  produces no tool-level line at all -- the most confusing case logs nothing;
- ``tools/list``, ``initialize`` and ``resources/*`` never reach a tool, so a client
  that only enumerates looks identical to a client doing nothing;
- an argument the tool does not declare is dropped silently, and the bound view cannot
  show what was discarded;
- defaults are indistinguishable from values the client actually sent.

This sits in the server's middleware chain, which wraps every inbound message, so it
sees the params as they arrived.

Set ``YADA_MCP_LOG_REQUESTS=0`` to turn it off.
"""

from __future__ import annotations

import os
from time import perf_counter
from typing import Any

from mcp.server.lowlevel.server import ServerMiddleware

from lib.logger import get_logger

logger = get_logger("YADA")

#: Params are logged whole up to this, then truncated. A tool call's params are small;
#: a resource write would not be, and a log line nobody can read is not a record.
_MAX_PARAMS = 600


def _render(params: Any) -> str:
    if not params:
        return ""
    text = repr(params)
    return text if len(text) <= _MAX_PARAMS else f"{text[:_MAX_PARAMS]}... ({len(text)} chars)"


def _caller_of(params: Any) -> str:
    """
    Who sent this, out of the request's ``_meta``, rendered for the line header.

    Several distinct client operations share one protocol method -- listing tools and
    inspecting one tool's schema are both ``tools/list`` -- so the method alone cannot
    tell them apart, and buried in the params dict the difference is easy to miss. A
    client that names itself gets that name in the header instead.
    """
    if not isinstance(params, dict):
        return ""
    meta = params.get("_meta")
    if not isinstance(meta, dict) or not meta.get("caller"):
        return ""
    extra = " ".join(f"{k}={v!r}" for k, v in meta.items() if k != "caller")
    return f" ({meta['caller']}{' ' + extra if extra else ''})"


def _without_meta(params: Any) -> Any:
    """Params minus ``_meta``, which the header already shows."""
    if isinstance(params, dict) and "_meta" in params:
        return {k: v for k, v in params.items() if k != "_meta"}
    return params


def _first_text(result: dict) -> str:
    """The message out of a serialized CallToolResult, which carries it as content."""
    for block in result.get("content") or []:
        text = block.get("text") if isinstance(block, dict) else None
        if text:
            return text[:200]
    return "(no message)"


class RequestLogMiddleware(ServerMiddleware[Any]):
    """One line in with the raw params, one line out with the outcome."""

    async def __call__(self, ctx, call_next):
        started = perf_counter()
        who = _caller_of(ctx.params)
        logger.info(f"rpc {ctx.method}{who} <- {_render(_without_meta(ctx.params))}".rstrip())
        try:
            result = await call_next(ctx)
        except Exception as e:
            # The case the tool-level log cannot see: refused before the handler ran.
            logger.warning(f"rpc {ctx.method}{who} -> {type(e).__name__}: {e} "
                           f"in {perf_counter() - started:.2f}s")
            raise
        # A failing tool reports in band rather than raising, so "the handler
        # returned" is not "the call succeeded" -- an unknown tool name and a
        # schema violation both come back as ordinary results. The middleware is
        # handed the SERIALIZED result, a plain dict, so the flag is the wire
        # spelling `isError` and not the python attribute. Logging ok for a call
        # that failed would be the same confusion this module exists to remove.
        if isinstance(result, dict) and result.get("isError"):
            logger.warning(f"rpc {ctx.method}{who} -> isError in {perf_counter() - started:.2f}s: "
                           f"{_first_text(result)}")
            return result

        logger.info(f"rpc {ctx.method}{who} -> ok in {perf_counter() - started:.2f}s")
        return result


def install(server) -> None:
    """Add the request log to a server, unless it is switched off."""
    if os.environ.get("YADA_MCP_LOG_REQUESTS", "1") == "0":
        logger.info("Request logging disabled (YADA_MCP_LOG_REQUESTS=0)")
        return
    if any(isinstance(m, RequestLogMiddleware) for m in server.middleware):
        return
    server.middleware.append(RequestLogMiddleware())
    logger.info("Request logging enabled: every inbound message is logged as received")
