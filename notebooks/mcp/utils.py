"""Helpers for exercising yada's MCP server from a notebook.

Mirrors meida's notebooks/{fred,cdc,bls}/utils.py — same three entry points
(``list_mcp_tools``, ``show_tool_schema``, ``call_tool``) so the notebooks read
alike. It does **not** use navi's ``lib.mcp_client``: that client is SSE-only
(navi/lib/mcp_client.py:41), and yada's server runs streamable-HTTP, the
transport the MCP spec treats as current.

The server must be running. In VSCode: **yada MCP server (http)**. Or:

    YADA_MCP_TRANSPORT=streamable-http python -m mcp_server.server

Override the endpoint with ``YADA_MCP_URL``.
"""

import sys as _sys
from pathlib import Path as _Path

# yada's repo root, so `lib` and `apps` resolve whatever directory the kernel
# started in. Anchored to __file__ rather than "../.." for the same reason.
_YADA_ROOT = str(_Path(__file__).resolve().parents[2])
if _YADA_ROOT not in _sys.path:
    _sys.path.insert(0, _YADA_ROOT)

import base64
import os
from collections.abc import Awaitable, Callable
from typing import Any

from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client
from mcp.types import CallToolResult

from lib.utils import print_json_vertical

MCP_URL = os.getenv("YADA_MCP_URL", "http://127.0.0.1:8081/mcp")


async def _with_session(fn: Callable[[ClientSession], Awaitable[Any]]) -> Any:
    """Run ``fn`` against a freshly connected session, then close it.

    The whole exchange stays inside one ``async with`` chain in a single task.
    That is not style: ``streamable_http_client`` and ``ClientSession`` open anyio
    **cancel scopes**, which must be entered and exited in the same task. Holding
    the context managers open across awaits — e.g. driving ``__aenter__`` from a
    wrapper class — raises ``CancelledError: Cancelled via cancel scope`` under
    ipykernel's event loop, even though it appears to work under ``asyncio.run``.

    A notebook cannot hold a session open across cells anyway, so each helper
    connects for the call. That is cheap because the server is already running;
    with stdio every call would re-import yada's agent tree.
    """
    # 2.x yields (read, write); 1.x yielded a third get_session_id callable.
    async with streamable_http_client(MCP_URL) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            return await fn(session)


async def list_mcp_tools(prefix: str | tuple[str, ...] | None = None) -> None:
    """Print the server's tools, optionally only those whose name starts with ``prefix``.

    Print-only: the notebooks call this as a bare expression, so returning a
    value would echo the list underneath the printed output.
    """
    prefixes = (prefix,) if isinstance(prefix, str) else prefix
    tools = await _with_session(lambda s: s.list_tools())
    for tool in tools.tools:
        if prefixes and not tool.name.startswith(tuple(prefixes)):
            continue
        first_line = (tool.description or "").strip().split(". ")[0]
        print(f"{tool.name}: {first_line}.")


def _schema_type(spec: dict[str, Any]) -> str:
    return str(spec.get("type") or ("enum" if "enum" in spec else "any"))


async def show_tool_schema(tool_name: str, raw: bool = False) -> dict[str, Any]:
    """Print one tool's arguments compactly: type, required/optional, default.

    ``raw=True`` dumps the JSON schema instead — the authoritative shape an MCP
    consumer actually parses.
    """
    listed = await _with_session(lambda s: s.list_tools())
    tools = {tool.name: tool for tool in listed.tools}
    if tool_name not in tools:
        raise RuntimeError(f"no tool {tool_name!r} on the server. Available: {sorted(tools)}")
    schema = dict(tools[tool_name].input_schema or {})
    if raw:
        print_json_vertical(schema)
        return schema
    required = set(schema.get("required") or [])
    print(f"{tool_name}\n  {tools[tool_name].description}\n")
    for name, spec in (schema.get("properties") or {}).items():
        flag = "required" if name in required else "optional"
        default = spec.get("default")
        suffix = "" if default is None else f", default={default!r}"
        print(f"  {name:20} {_schema_type(spec):8} {flag}{suffix}")
    return schema


async def call_tool(tool_name: str, arguments: dict[str, Any] | None = None) -> CallToolResult:
    """Call a tool and return the raw result, images and all."""
    return await _with_session(lambda s: s.call_tool(tool_name, arguments or {}))


def show_result(result: CallToolResult) -> None:
    """Render a tool result in the notebook: text as text, images as images.

    yada's plot tools return a text block plus one or more ``ImageContent``
    blocks. This is the notebook's stand-in for what Goose does with the same
    payload, so what renders here is what a client sees.
    """
    from IPython.display import Image, Markdown, display

    if result.is_error:
        print("is_error: True")
    for block in result.content:
        if block.type == "text":
            display(Markdown(block.text))
        elif block.type == "image":
            raw = base64.b64decode(block.data)
            print(f"[{block.mime_type}] {len(raw):,} bytes "
                  f"({len(block.data):,} base64 chars)")
            display(Image(data=raw))
        else:
            print(f"[{block.type}] {block!r}")


def show_structured(result: CallToolResult, *, facets: int = 12, hits: int = 5) -> None:
    """Render a document-tool result: the outcome fields, then facets or hits.

    The document tools return no text blocks at all -- everything is in
    ``structured_content``, derived from the pydantic return annotation. That is the
    payload a client reasons over, so this prints it rather than prose about it.

    ``filters_requested`` against ``filters_applied`` is the pair worth watching: they
    differ whenever resolution did something, and a caller that cannot see the
    difference cannot tell a widened search from the one it asked for.
    """
    data = result.structured_content or {}
    if result.is_error:
        print("is_error: True")

    print(f"status            {data.get('status')}")
    for key in ("filters_requested", "filters_applied", "filters_resolved",
                "filters_relaxed", "detail"):
        value = data.get(key)
        if value:
            print(f"{key:18}{value}")

    if data.get("documents") or data.get("chunks"):
        print(f"{'size':18}{data.get('documents', 0):,} documents, "
              f"{data.get('chunks', 0):,} chunks")
    if data.get("retrieved") is not None and "hits" in data:
        print(f"{'retrieved':18}{data.get('retrieved')} candidates, "
              f"best score {data.get('best_score')}")

    for field, values in (data.get("facets") or {}).items():
        shown = list(values.items())[:facets]
        more = f"  (+{len(values) - len(shown)} more)" if len(values) > len(shown) else ""
        print(f"\n  {field} -- {len(values)} values{more}")
        for name, count in shown:
            print(f"     {name:52} {count:>9,}")

    for hit in (data.get("hits") or [])[:hits]:
        print(f"\n  {hit['rank']}. [{hit['score']:.2f}] {hit['path']}")
        print(f"     {hit['uri']}")
        print(f"     {hit['metadata']}")
        print(f"     {hit['snippet'][:160].strip()!r}...")

    for field, values in (data.get("available") or {}).items():
        print(f"\n  available {field}: {', '.join(values[:12])}"
              f"{' ...' if len(values) > 12 else ''}")
