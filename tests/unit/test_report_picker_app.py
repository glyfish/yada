"""The report-picker App: registered, bound, and fed a payload it can read.

Companion to `test_series_picker_app.py`, pinning the same silent failures one surface
over, plus two that are specific to this page.

The first is drift. `list_reports` and `open_plot_report_view` return the same rows and
differ only in the App binding, because the client reads that binding off its cached
`tools/list` entry and cannot decide it per result -- so a flag on `list_reports` could
not open a view and a second tool is the only shape available. Two tools returning one
projection is exactly the arrangement that drifted five plot tools apart before they
were consolidated, so the equality is asserted rather than trusted.

The second is the payload contract. The page draws a column per field name; a field
renamed in `_row` would blank that column with no error anywhere, so the page is checked
to mention every field it reads.

The page's behaviour is not covered: there is no harness for an App page, and the
`ui/message` hand-off can only be verified by clicking it in a client.
"""
import pytest

import mcp_server.server as S
import mcp_server.report_tools as report_tools

from mcp.server.mcpserver import MCPServer

#: Every field the page's `applyFilter`/`members` read out of a row.
ROW_FIELDS = ("report_id", "report_title", "report_description", "series",
              "series_count", "time_range_from", "time_range_to")


@pytest.fixture(scope="module")
def tools():
    import asyncio
    return {t.name: t for t in asyncio.run(S.server.list_tools())}


@pytest.fixture(scope="module")
def resource_uris():
    import asyncio
    return [str(r.uri) for r in asyncio.run(S.server.list_resources())]


# ---------- the page exists and is served ----------

def test_the_picker_page_is_registered(resource_uris):
    assert S.REPORT_PICKER_URI in resource_uris


def test_all_three_app_pages_are_served(resource_uris):
    assert {S.PLOT_URI, S.SERIES_PICKER_URI,
            S.REPORT_PICKER_URI} <= set(resource_uris)


def test_every_registered_page_is_stamped_with_its_own_build():
    """A restart that picked up only some of three pages must be visible."""
    builds = set()
    for uri, html, *_ in S._APP_PAGES:
        stamped = S._stamp(html)
        assert "__BUILD__" not in stamped, f"{uri} still carries the placeholder"
        builds.add(stamped)
    assert len(builds) == len(S._APP_PAGES), "two pages stamped identically"


# ---------- the binding Goose actually reads ----------

def test_the_opener_is_bound_to_the_report_picker_page(tools):
    """`get_tool_resource_uri` reads _meta['ui']['resourceUri'] and nothing else."""
    meta = tools["open_plot_report_view"].meta or {}
    assert meta.get("ui") == {
        "resourceUri": S.REPORT_PICKER_URI, "visibility": ["model", "app"],
    }


def test_the_three_pages_are_not_crossed(tools):
    """Three (uri, meta) pairs threaded through three register() calls."""
    expected = {
        "open_plot_report_view": S.REPORT_PICKER_URI,
        "open_create_report_view": S.SERIES_PICKER_URI,
        "plot": S.PLOT_URI,
        "plot_report": S.PLOT_URI,
        "plot_series": S.PLOT_URI,
    }
    for name, uri in expected.items():
        meta = tools[name].meta or {}
        assert (meta.get("ui") or {}).get("resourceUri") == uri, name


def test_the_plain_report_tools_advertise_no_page(tools):
    """Only the opener may mount the picker. `list_reports` returning the same rows
    with a binding would mount it on every ordinary listing."""
    for name in ("list_reports", "search_reports", "create_report", "delete_report"):
        assert not ((tools[name].meta or {}).get("ui") or {}).get("resourceUri"), name


def test_binding_an_unregistered_page_is_refused():
    with pytest.raises(ValueError, match="not a registered App page"):
        S._bind("ui://yada/report-pickr")


# ---------- the opener exists only when a page is bound ----------

def test_without_a_bound_page_the_opener_is_not_registered():
    """Registered unconditionally it would advertise a page the client cannot resolve,
    which fails silently at render time rather than erroring."""
    import asyncio
    bare = MCPServer("test", version="0")
    report_tools.register(bare)
    names = {t.name for t in asyncio.run(bare.list_tools())}
    assert "open_plot_report_view" not in names
    assert "list_reports" in names


def test_with_a_bound_page_the_opener_is_registered():
    import asyncio
    bound = MCPServer("test", version="0")
    report_tools.register(bound, S.REPORT_PICKER_URI, S._bind(S.REPORT_PICKER_URI))
    names = {t.name for t in asyncio.run(bound.list_tools())}
    assert "open_plot_report_view" in names


# ---------- the payload the page reads ----------

def test_the_opener_publishes_an_output_schema(tools):
    """Without one the reply is text-only and the App's structuredContent is None."""
    assert tools["open_plot_report_view"].output_schema is not None


def test_the_opener_steers_the_model_off_plotting_it_itself(tools):
    """The view asks for the plot once the user picks. A model that also calls
    plot_report charts a report nobody chose, and says nothing about having done so."""
    d = tools["open_plot_report_view"].description or ""
    assert "plot_report" in d
    assert "STOP" in d


def test_the_opener_and_list_reports_cannot_drift():
    """Same rows, one body. The only difference is the binding on the definition."""
    import asyncio
    from apps.core import identity
    with identity.scoped(identity.Caller(user_id="00000000-0000-0000-0000-000000000000",
                                         name="nobody")):
        a = asyncio.run(S.server.call_tool("list_reports", {}))
        b = asyncio.run(S.server.call_tool("open_plot_report_view", {}))
    assert a.structured_content == b.structured_content


def test_the_rows_carry_every_column_the_table_draws():
    import asyncio
    from apps.core import identity
    with identity.scoped(identity.Caller(user_id="ee4981fd-0692-4d3b-8da2-3839f5db372e",
                                         name="troy")):
        r = asyncio.run(S.server.call_tool("open_plot_report_view", {}))
    sc = r.structured_content or {}
    assert sc.get("status") == "ok"
    rows = sc.get("reports") or []
    if not rows:
        pytest.skip("no saved reports in this environment")
    for field in ROW_FIELDS:
        assert field in rows[0], field


def test_the_envelope_key_is_the_one_the_page_reads():
    """`rowsFrom` accepts a result only if it carries `reports`; anything else leaves
    the table empty with no error."""
    import asyncio
    from apps.core import identity
    with identity.scoped(identity.Caller(user_id="00000000-0000-0000-0000-000000000000",
                                         name="nobody")):
        r = asyncio.run(S.server.call_tool("open_plot_report_view", {}))
    assert "reports" in (r.structured_content or {})
    assert "reports" in S.REPORT_PICKER_HTML


@pytest.mark.parametrize("field", ROW_FIELDS)
def test_the_page_mentions_every_field_it_reads(field):
    """A field renamed in `_row` would blank a column silently."""
    assert field in S.REPORT_PICKER_HTML


# ---------- the hand-off, as far as it can be checked without a client ----------

def test_the_page_hands_off_through_ui_message_not_a_proxied_call():
    """A page cannot mount another page: mounting is decided from _meta.goose.mcpApp,
    which goosed synthesizes, and a proxied tools/call runs no mount logic at all. So
    the chart has to come from the ordinary path, driven by ui/message."""
    assert "ui/message" in S.REPORT_PICKER_HTML
    assert "tools/call" not in S.REPORT_PICKER_HTML


def test_the_page_leaves_fullscreen_before_handing_off():
    """The chart mounts as a new transcript row UNDER this page, so staying in the
    overlay would hide the thing the user asked for. The frame itself cannot be torn
    down -- Goose never sends a teardown and never calls teardownResource."""
    assert "'inline'" in S.REPORT_PICKER_HTML
