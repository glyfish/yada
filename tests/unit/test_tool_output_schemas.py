"""Every report tool must publish an output schema, or structured_content is None.

A tool annotated `-> dict` generates no output schema. The server then sends its reply
as text only, and a client reading `result.structured_content` gets None -- no error,
no warning, just a TypeError the first time something subscripts it. That is how the
plotting notebook failed on its first real run against the server: the cells had only
ever been verified in process, calling the Python functions directly, which never
exercises the wire.

`-> dict[str, Any]` generates the schema. The difference is invisible at the call site
and silent at registration, so it is pinned here.

The plot tools are deliberately exempt: they return content blocks (text + image), not
structured data, and a schema for those would be wrong.
"""

import pytest

from mcp.server.mcpserver import MCPServer

import mcp_server.report_tools as report_tools


#: The report tools registered unconditionally. `open_plot_report_view` is deliberately
#: absent: it is registered only when an App page is bound to it, so a server with no
#: picker page does not advertise a view the client cannot resolve.
REPORT_TOOLS = [
    "create_report",
    "list_reports",
    "search_reports",
    "delete_report",
    "add_series_to_report",
    "remove_series_from_report",
    "set_report_metadata",
]


@pytest.fixture(scope="module")
def registered():
    """The report tools on a real MCPServer, as the live server registers them."""
    server = MCPServer("test", version="0")
    report_tools.register(server)
    import asyncio
    return {t.name: t for t in asyncio.run(server.list_tools())}


def test_every_report_tool_registers(registered):
    """Spelled out rather than counted, so adding a tool is a deliberate edit here and
    a tool that silently stopped registering is a failure."""
    assert sorted(registered) == sorted(REPORT_TOOLS)


@pytest.mark.parametrize("name", REPORT_TOOLS)
def test_the_tool_publishes_an_output_schema(name, registered):
    """Without this the caller's structured_content is None and nothing says why."""
    schema = registered[name].output_schema
    assert schema is not None, (
        f"{name} has no output schema -- it is probably annotated '-> dict' rather "
        f"than '-> dict[str, Any]'. structured_content will arrive as None.")
    assert schema.get("type") == "object"


@pytest.mark.parametrize("name", REPORT_TOOLS)
def test_the_tool_has_a_description_a_model_can_act_on(name, registered):
    """These are chosen by an LLM from the description alone."""
    assert len(registered[name].description or "") > 100


def test_a_bare_dict_annotation_really_is_the_difference():
    """Pins the cause, so the rule above does not become folklore."""
    from typing import Any

    server = MCPServer("probe", version="0")

    def bare() -> dict:
        return {}

    def parameterised() -> dict[str, Any]:
        return {}

    server.add_tool(bare, name="bare", description="x")
    server.add_tool(parameterised, name="parameterised", description="x")

    import asyncio
    tools = {t.name: t for t in asyncio.run(server.list_tools())}
    assert tools["bare"].output_schema is None
    assert tools["parameterised"].output_schema is not None
