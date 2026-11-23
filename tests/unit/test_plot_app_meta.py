"""The App binding a tool advertises must not depend on how it was registered.

`plot` and `plot_report` use `@apps.tool`; `plot_series` is added after `MCPServer`
is constructed and so uses `server.add_tool(meta=...)`. Those two paths produced
different `_meta` for a while -- the decorator stamps a nested ``ui`` entry that
`meta_for` cannot carry -- and the difference was invisible server-side: the tool
still advertised ``ui/resourceUri``, so every check passed while Goose, which reads
only the nested entry, rendered the chart as a collapsed tool result instead.

This pins the two paths together. It asserts equality rather than the presence of
one key on purpose: the failure mode is a shape the decorator adds and the helper
does not, whatever that shape turns out to be next.
"""
from mcp.server.apps import Apps

from mcp_server.plot_app import app_meta, meta_for

URI = "ui://yada/plot"
VISIBILITY = ["model", "app"]


def _decorated_meta() -> dict:
    """The `_meta` the SDK gives a tool bound with the decorator."""
    apps = Apps()
    apps.add_html_resource(URI, "<!doctype html><html></html>")
    apps.tool(resource_uri=URI, visibility=VISIBILITY,
              meta=meta_for(URI, VISIBILITY), name="probe")(lambda: None)
    return apps.tools()[0].meta


def test_app_meta_matches_the_decorator():
    assert app_meta(URI, VISIBILITY) == _decorated_meta()


def test_nested_entry_is_what_the_helper_adds():
    # Stated separately because it is the key Goose reads, and a regression here is
    # silent everywhere else.
    assert "ui" not in meta_for(URI, VISIBILITY)
    assert app_meta(URI, VISIBILITY)["ui"] == {
        "resourceUri": URI, "visibility": VISIBILITY,
    }
