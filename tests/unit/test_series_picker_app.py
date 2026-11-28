"""The report-builder App: registered, bound, and fed a payload it can read.

Every failure this pins is silent server-side. A page that is not registered still
lets its tool register and advertise an App, and fails only at render time in the
client. A tool whose `_meta` lacks the nested `ui` entry still answers normally, and
Goose just prints rows into a collapsed accordion instead of mounting the picker. A
tool with no output schema still returns rows, and `structuredContent` arrives as None
in the App -- the same defect that broke the plotting notebook, one surface over.

So these assert the wiring, not the behaviour of the search, which `search_fred`
already owns. The page's own JavaScript is not covered: there is no harness for an App
page, and verifying it means opening it in a client.
"""
import pytest

import mcp_server.server as S
from mcp_server.fred_tools import MAX_LIMIT


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
    assert S.SERIES_PICKER_URI in resource_uris


def test_both_app_pages_are_served(resource_uris):
    """The registry replaced four single-App constants; this is what it bought."""
    assert {S.PLOT_URI, S.SERIES_PICKER_URI} <= set(resource_uris)


def test_every_registered_page_is_stamped_with_its_own_build():
    """Two pages means a restart that picked up only one is now possible, and a stale
    build must be visible rather than read as a code bug."""
    builds = set()
    for uri, html, *_ in S._APP_PAGES:
        stamped = S._stamp(html)
        assert "__BUILD__" not in stamped, f"{uri} still carries the placeholder"
        builds.add(stamped)
    assert len(builds) == len(S._APP_PAGES), "two pages stamped identically"


# ---------- the binding Goose actually reads ----------

def test_the_opener_is_bound_to_the_picker_page(tools):
    """`get_tool_resource_uri` reads _meta['ui']['resourceUri'] and nothing else."""
    meta = tools["open_create_report_view"].meta or {}
    assert meta.get("ui") == {
        "resourceUri": S.SERIES_PICKER_URI, "visibility": ["model", "app"],
    }


def test_the_chart_tools_are_still_bound_to_the_chart_page(tools):
    """Threading a second (uri, meta) pair through register() must not cross them."""
    for name in ("plot", "plot_report", "plot_series"):
        meta = tools[name].meta or {}
        assert (meta.get("ui") or {}).get("resourceUri") == S.PLOT_URI, name


def test_binding_an_unregistered_page_is_refused():
    """`@apps.tool` raises for a missing resource; `add_tool(meta=...)` does not, so a
    typo would advertise an App that renders nothing. _bind is that missing check."""
    with pytest.raises(ValueError, match="not a registered App page"):
        S._bind("ui://yada/does-not-exist")


@pytest.mark.parametrize("uri", [S.PLOT_URI, S.SERIES_PICKER_URI])
def test_binding_a_registered_page_is_allowed(uri):
    assert S._bind(uri)["ui"]["resourceUri"] == uri


# ---------- the payload the page reads ----------

def test_the_opener_publishes_an_output_schema(tools):
    """Without one the reply is text-only and the App's structuredContent is None."""
    assert tools["open_create_report_view"].output_schema is not None


def test_the_opener_description_steers_the_model_off_the_write_tools(tools):
    """The view saves the report itself. A model that also calls create_report makes a
    duplicate, and the proxied save is invisible to it, so the description is the only
    place that can say so."""
    d = tools["open_create_report_view"].description or ""
    assert "create_report" in d and "fetch_fred_series" in d
    assert "category" in d


# ---------- the limit, which a picker pushes much harder than chat does ----------

@pytest.mark.parametrize("asked,effective", [
    (0, 1),            # returned no rows and said "Nothing matched" -- a wrong answer
    (-5, 1),           # reached the SQL layer and escaped as a protocol error
    (1, 1),
    (100, 100),
    (MAX_LIMIT + 1, MAX_LIMIT),
    (10 ** 9, MAX_LIMIT),
])
def test_the_limit_is_clamped(asked, effective):
    import asyncio
    r = asyncio.run(S.server.call_tool("open_create_report_view",
                                       {"category": "commodities", "limit": asked}))
    assert (r.structured_content or {})["limit"] == effective


# ---------- the rows carry what the table renders ----------

def test_the_rows_carry_every_column_the_table_draws():
    """The page renders id, title, units, frequency_class, popularity and the two
    observation dates. A field renamed in FredSeries would blank a column silently."""
    import asyncio
    r = asyncio.run(S.server.call_tool("open_create_report_view",
                                       {"category": "commodities", "limit": 3}))
    sc = r.structured_content or {}
    assert sc.get("status") == "ok"
    rows = sc.get("series") or []
    assert rows, "the commodities category should not be empty"
    for field in ("series_id", "title", "units", "frequency_class", "popularity",
                  "observation_start", "observation_end"):
        assert field in rows[0], field


def test_the_envelope_carries_the_total_the_heading_shows():
    """The page prints "N of M matches"; M is what distinguishes the top 100 of 1,969
    from the whole answer."""
    import asyncio
    r = asyncio.run(S.server.call_tool("open_create_report_view",
                                       {"category": "commodities", "limit": 5}))
    sc = r.structured_content or {}
    assert sc["total"] > sc["limit"]
