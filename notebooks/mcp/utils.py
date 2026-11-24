"""Helpers for exercising yada's MCP server from a notebook.

Mirrors meida's notebooks/{fred,cdc,bls}/utils.py — same three entry points
(``list_mcp_tools``, ``show_tool_schema``, ``call_tool``) so the notebooks read
alike. It does **not** use navi's ``lib.mcp_client``: that client is SSE-only
(navi/lib/mcp_client.py:41), and yada's server runs streamable-HTTP, the
transport the MCP spec treats as current.

The server must be running. In VSCode: **yada MCP server (http)**. Or:

    YADA_MCP_TRANSPORT=streamable-http python -m mcp_server.server

Override the endpoint with ``YADA_MCP_URL``.

**Tokens.** The server's auth switch is the ``app_user`` table -- zero active rows and
it is unauthenticated, one and every client must present a bearer token. Set
``YADA_MCP_TOKEN`` (in the repo's ``.env``, which this module loads, or in the shell)
to the same value Goose carries in
``~/.config/goose/config.yaml`` under ``extensions.yada.headers.Authorization``. With
no token set no header is sent at all, which is the right behaviour for an
unauthenticated server.
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

from dotenv import load_dotenv
from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client
from mcp.shared._httpx_utils import create_mcp_http_client
from mcp.shared.exceptions import MCPError
from mcp.types import CallToolResult, PaginatedRequestParams

from lib.utils import print_json_vertical

# Shell values win, matching apps/core/environment.py. Done at import rather than per
# call so a kernel started outside the repo still sees the project's settings.
load_dotenv(_Path(_YADA_ROOT) / ".env")

MCP_URL = os.getenv("YADA_MCP_URL", "http://127.0.0.1:8081/mcp")


def _token() -> str | None:
    """The bearer token to send, or None to send no ``Authorization`` header.

    Read per call, not captured at import, so a token can be exported from a notebook
    cell and picked up without restarting the kernel.
    """
    return (os.getenv("YADA_MCP_TOKEN") or "").strip() or None


def _leaves(exc: BaseException) -> list[BaseException]:
    """Every non-group exception inside ``exc``, however deeply nested.

    Both ``streamable_http_client`` and ``ClientSession`` open anyio task groups, so a
    one-line server rejection surfaces as a ~40-line traceback of two nested
    ``ExceptionGroup``s with the actual message on the last line. This exists so
    `_with_session` can find that message and re-raise it on its own.
    """
    if isinstance(exc, BaseExceptionGroup):
        return [leaf for sub in exc.exceptions for leaf in _leaves(sub)]
    return [exc]


def _caller(name: str, **extra: Any) -> dict[str, Any]:
    """Identify which helper issued a request, for the server's log.

    ``list_mcp_tools`` and ``show_tool_schema`` are the same protocol call --
    ``tools/list`` -- and differ only in what this module does with the response, so
    the server cannot tell them apart and logs two identical lines. MCP lets a request
    carry ``_meta``, which the server sees as ``ctx.meta`` and yada's request log
    prints with the rest of the params, so saying who called is enough to separate them.

    Purely diagnostic: ``_meta`` never reaches a tool's arguments.
    """
    return {"caller": name, **{k: v for k, v in extra.items() if v is not None}}


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
    # mcp 2.x removed the `headers=` keyword: a caller that needs headers supplies the
    # whole client. `create_mcp_http_client` is the transports' own factory, so this
    # keeps their timeouts (30s, 300s read) and redirect handling rather than inventing
    # new ones -- the only difference is the Authorization header.
    token = _token()
    headers = {"Authorization": f"Bearer {token}"} if token else None
    try:
        async with create_mcp_http_client(headers=headers) as http_client:
            # 2.x yields (read, write); 1.x yielded a third get_session_id callable.
            async with streamable_http_client(MCP_URL, http_client=http_client) as (read, write):
                async with ClientSession(read, write) as session:
                    await session.initialize()
                    return await fn(session)
    except BaseExceptionGroup as group:
        for leaf in _leaves(group):
            if isinstance(leaf, MCPError):
                raise RuntimeError(
                    f"{leaf} [{MCP_URL}, YADA_MCP_TOKEN "
                    f"{'set' if token else 'unset'}]") from None
        raise


async def list_mcp_tools(prefix: str | tuple[str, ...] | None = None) -> None:
    """Print the server's tools, optionally only those whose name starts with ``prefix``.

    Print-only: the notebooks call this as a bare expression, so returning a
    value would echo the list underneath the printed output.
    """
    prefixes = (prefix,) if isinstance(prefix, str) else prefix
    tools = await _with_session(lambda s: s.list_tools(
        params=PaginatedRequestParams(meta=_caller("list_mcp_tools", prefix=prefix))))
    for tool in tools.tools:
        if prefixes and not tool.name.startswith(tuple(prefixes)):
            continue
        first_line = (tool.description or "").strip().split(". ")[0]
        print(f"{tool.name}: {first_line}.")


def _schema_type(spec: dict[str, Any]) -> str:
    return str(spec.get("type") or ("enum" if "enum" in spec else "any"))


async def show_tool_schema(tool_name: str, raw: bool = False) -> dict[str, Any] | None:
    """Print one tool's arguments compactly: type, required/optional, default.

    ``raw=True`` dumps the tool **as ``tools/list`` carries it** -- name, description,
    ``inputSchema``, ``outputSchema`` and ``_meta`` -- not just the argument schema.
    That distinction cost real time: ``description`` and ``_meta`` are *siblings* of
    ``inputSchema``, not nested inside it, so dumping the argument schema alone hid
    both. ``_meta`` is where the MCP App binding lives, and a wrong nested
    ``_meta["ui"]`` shape is exactly what made ``plot_series`` render collapsed in
    Goose -- a field this helper previously could not show at all.

    Worth knowing while reading the argument schema: this server writes **no**
    descriptions into it, at either level. Every argument is documented in prose
    inside the tool description instead, so ``properties`` carries bare
    ``{'title', 'type'}`` entries and ``title`` is the SDK's generated
    ``<tool>Arguments``, not anything anyone wrote. A client building input fields
    from the schema has no help text to render.

    The two branches return different things, on purpose. The default returns the
    argument schema, which the notebooks call as a bare expression so the dict echoes
    underneath the rendered table -- the compact view and the shape it was rendered
    from, in one cell. ``raw=True`` returns nothing: it has already printed the whole
    object, and echoing a second copy of a 90-to-290-line dump underneath the first
    one helps no one.
    """
    listed = await _with_session(lambda s: s.list_tools(
        params=PaginatedRequestParams(meta=_caller("show_tool_schema", tool=tool_name))))
    tools = {tool.name: tool for tool in listed.tools}
    if tool_name not in tools:
        raise RuntimeError(f"no tool {tool_name!r} on the server. Available: {sorted(tools)}")
    tool = tools[tool_name]
    if raw:
        # by_alias: the wire spells these `inputSchema`/`outputSchema`/`_meta`, and the
        # wire spelling is what a client parses -- python_case here would misreport the
        # contract. exclude_none drops the fields this server never sets, which is most
        # of them, rather than padding the dump with nulls.
        print_json_vertical(tool.model_dump(by_alias=True, exclude_none=True))
        return None
    schema = dict(tool.input_schema or {})
    required = set(schema.get("required") or [])
    print(f"{tool_name}\n  {tool.description}\n")
    for name, spec in (schema.get("properties") or {}).items():
        flag = "required" if name in required else "optional"
        default = spec.get("default")
        suffix = "" if default is None else f", default={default!r}"
        print(f"  {name:20} {_schema_type(spec):8} {flag}{suffix}")
    return schema


async def call_tool(tool_name: str, arguments: dict[str, Any] | None = None) -> CallToolResult:
    """Call a tool and return the raw result, images and all."""
    return await _with_session(lambda s: s.call_tool(
        tool_name, arguments or {}, meta=_caller("call_tool")))


def first_text(result: CallToolResult) -> str:
    """The first text block's text, or ``""`` when the result carries none.

    ``CallToolResult.content`` is a **union** -- ``TextContent | ImageContent |
    AudioContent | ResourceLink | EmbeddedResource`` -- and only ``TextContent`` has
    a ``.text`` attribute. So ``result.content[0].text``, the obvious thing to write,
    is four attribute errors waiting to happen and Pylance flags all four. It also
    assumes the text block is first, which is true of yada's plot tools (text, then
    image) and not a guarantee.

    Narrowing on the ``type`` discriminant is what makes this type-safe rather than
    merely quiet: every block type carries a ``Literal`` ``type``, so the checker
    knows ``block`` is a ``TextContent`` inside the branch. ``cast`` or
    ``# type: ignore`` would silence the warning without making it true.
    """
    for block in result.content:
        if block.type == "text":
            return block.text
    return ""


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
