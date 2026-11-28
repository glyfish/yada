"""User-supplied report metadata: reachable from a request, and not silently erased.

Two independent failures are pinned here, and both were real before this feature.

The first is reachability. A model chooses a tool call from `inputSchema` alone, so a
field that is not in the schema cannot be sent -- not through `arguments`, and not
through the protocol's `_meta` sidecar either, which is filled by the client
implementation and never by the model. `tags` and `note` being in `inputSchema` IS the
feature; everything else here only keeps what arrives.

The second is erasure. `metadata` is rebuilt from the member series on every write --
`report_metadata_from_series` takes only the series list, so it cannot carry anything
forward -- and `_update_report_sync` assigns the column rather than merging it. Before
the carry-forward, adding a series to a tagged report silently untagged it, and so did
renaming one through the REST route. Those are asserted against the real store, because
the defect was invisible to every read that did not go through a write first.
"""
import asyncio

import pytest

import mcp_server.server as S
from apps.agentic.core.agents.series_metadata import (
    USER_METADATA_KEY, report_metadata_from_series, user_metadata_block,
    user_metadata_of,
)
from apps.agentic.db.report_cache import ReportCache
from apps.core import identity


@pytest.fixture(scope="module")
def tools():
    return {t.name: t for t in asyncio.run(S.server.list_tools())}


# ---------- the part the model can actually see ----------

@pytest.mark.parametrize("field", ["tags", "note"])
def test_create_report_advertises_the_field(tools, field):
    """The model picks arguments from inputSchema. A field absent from it cannot be
    sent at all, which is why metadata was unreachable however it was stored."""
    assert field in tools["create_report"].input_schema["properties"], field


def test_tags_is_typed_as_a_list_of_strings(tools):
    """A bare string fails validation and the model is told, which is the half of
    drift a schema can catch. The other half -- an invented KEY -- is why these are
    named arguments rather than one free-form dict."""
    schema = tools["create_report"].input_schema["properties"]["tags"]
    options = schema.get("anyOf") or [schema]
    arrays = [o for o in options if o.get("type") == "array"]
    assert arrays and arrays[0]["items"]["type"] == "string"


def test_neither_field_is_required(tools):
    """The picker page calls this tool with a literal argument object, so a newly
    required field would break it on a server restart the page did not get."""
    required = tools["create_report"].input_schema.get("required") or []
    assert "tags" not in required and "note" not in required


def test_the_retag_tool_is_registered_with_a_schema(tools):
    t = tools["set_report_metadata"]
    assert t.output_schema is not None
    assert "report_id_or_title" in t.input_schema["properties"]
    assert len(t.description or "") > 100


def test_the_descriptions_tell_the_model_not_to_invent_tags(tools):
    d = tools["create_report"].description or ""
    assert "tags" in d and "note" in d
    assert "do not invent" in d.lower()


# ---------- the stored shape ----------

@pytest.mark.parametrize("given,expected", [
    (["Energy"], ["energy"]),                       # casefolded: @> is case-sensitive
    ([" energy "], ["energy"]),                     # stripped
    (["Energy", "energy", " ENERGY"], ["energy"]),  # deduped after normalizing
    (["energy", "macro"], ["energy", "macro"]),     # order preserved
    ([""], None),                                   # empty contributes nothing
    (None, None),
])
def test_tags_are_normalized(given, expected):
    block = user_metadata_block(given)
    assert block.get("tags") == expected


def test_a_note_is_stored_as_a_one_element_list():
    """Always a list, single values included. `@>` is shape-sensitive, so a scalar here
    would need a different predicate than a list, per key, chosen by whatever the caller
    happened to send."""
    assert user_metadata_block(note="Watch the spread.") == {
        "note": ["Watch the spread."]}


def test_an_empty_block_is_empty_not_a_shell():
    """So a create that mentioned no metadata does not write `{"user": {}}` and make
    every untagged report answer a has-user-metadata test."""
    assert user_metadata_block() == {}
    assert user_metadata_block([], "") == {}


def test_user_metadata_of_tolerates_every_wrong_shape():
    for bad in (None, {}, {"user": None}, {"user": "energy"}, {"user": []}):
        assert user_metadata_of(bad) == {}


def test_the_authored_block_sits_beside_the_derived_one():
    info = [{"source": "fred", "metadata": {"fred": {"category_name": ["Commodities"]}}}]
    merged = report_metadata_from_series(info, user={"tags": ["energy"]})
    assert merged["fred"] == {"category_name": ["Commodities"]}
    assert merged[USER_METADATA_KEY] == {"tags": ["energy"]}


def test_a_source_named_user_is_refused():
    """`source_present` tests top-level keys, so a source called `user` would answer for
    the authored block and vice versa. Enforced, not documented: the collision is the
    one hazard of keeping authored data in the derived column."""
    info = [{"source": "user", "metadata": {"user": {"category_name": ["x"]}}}]
    with pytest.raises(ValueError, match="reserved"):
        report_metadata_from_series(info)


# ---------- the carry-forward, against the real store ----------

OWNER = "ee4981fd-0692-4d3b-8da2-3839f5db372e"


@pytest.fixture
def probe_report():
    """A throwaway report carrying tags and a note, deleted however the test ends."""
    caller = identity.Caller(user_id=OWNER, name="test")
    with identity.scoped(caller):
        existing = ReportCache._list_reports_sync(owner=OWNER)
        pool = [e["cache_id"] for r in existing for e in r["time_series_info"]]
        if len(pool) < 3:
            pytest.skip("needs three cached series in this environment")
        created = asyncio.run(S.server.call_tool("create_report", {
            "report_title": "ZZ carry-forward probe", "cache_ids": pool[:2],
            "tags": ["energy", "macro"], "note": "Watch the spread."}))
        report_id = (created.structured_content or {})["report_id"]
        try:
            yield caller, report_id, pool[2]
        finally:
            ReportCache._delete_report_sync(report_id, owner=OWNER)


def _call(caller, name, args):
    with identity.scoped(caller):
        return asyncio.run(S.server.call_tool(name, args)).structured_content or {}


def test_create_stores_the_normalized_block(probe_report):
    caller, report_id, _ = probe_report
    row = _call(caller, "search_reports", {"query": report_id})["reports"][0]
    assert row["tags"] == ["energy", "macro"]
    assert row["note"] == "Watch the spread."


def test_adding_a_series_keeps_the_tags(probe_report):
    """The write that used to erase them. `_write_membership` passes a freshly rebuilt
    catalogue, so nothing in its arguments carries the authored block."""
    caller, report_id, spare = probe_report
    out = _call(caller, "add_series_to_report",
                {"report_id_or_title": report_id, "cache_ids": [spare]})
    assert out["series_count"] == 3
    assert out["tags"] == ["energy", "macro"]
    assert out["note"] == "Watch the spread."


def test_removing_a_series_keeps_the_tags(probe_report):
    caller, report_id, spare = probe_report
    _call(caller, "add_series_to_report",
          {"report_id_or_title": report_id, "cache_ids": [spare]})
    out = _call(caller, "remove_series_from_report",
                {"report_id_or_title": report_id, "series": [spare]})
    assert out["tags"] == ["energy", "macro"]


def test_retagging_keeps_the_note(probe_report):
    """Merged per key, so one sentence about tags does not discard a note the user
    dictated separately."""
    caller, report_id, _ = probe_report
    out = _call(caller, "set_report_metadata",
                {"report_id_or_title": report_id, "tags": ["inflation"]})
    assert out["tags"] == ["inflation"]
    assert out["note"] == "Watch the spread."


def test_setting_the_note_keeps_the_tags(probe_report):
    caller, report_id, _ = probe_report
    out = _call(caller, "set_report_metadata",
                {"report_id_or_title": report_id, "note": "Revised."})
    assert out["tags"] == ["energy", "macro"]
    assert out["note"] == "Revised."


def test_a_retag_naming_nothing_changes_nothing(probe_report):
    caller, report_id, _ = probe_report
    out = _call(caller, "set_report_metadata", {"report_id_or_title": report_id})
    assert out["tags"] == ["energy", "macro"]
    assert out["note"] == "Watch the spread."


def test_an_unknown_report_is_refused_without_a_protocol_error(probe_report):
    caller, _, _ = probe_report
    out = _call(caller, "set_report_metadata",
                {"report_id_or_title": "no such report at all"})
    assert out["status"] == "error" and out.get("detail")


def test_the_derived_catalogue_is_still_there(probe_report):
    """Authored data must not displace what the column is for: `source_present` and
    `metadata_where` read the source keys, and a report that lost them would stop
    answering source='fred'."""
    caller, report_id, _ = probe_report
    with identity.scoped(caller):
        row = ReportCache._get_by_report_id_sync(report_id, owner=OWNER)
    assert "fred" in row["metadata"]
    assert USER_METADATA_KEY in row["metadata"]
    with identity.scoped(caller):
        titles = [r["report_title"]
                  for r in ReportCache._list_reports_sync(source="fred", owner=OWNER)]
    assert "ZZ carry-forward probe" in titles


# ---------- the create UI carries the same two fields ----------

@pytest.mark.parametrize("probe", ['id="tags"', 'id="note"', "tags:", "note:"])
def test_the_create_view_collects_them(probe):
    assert probe in S.SERIES_PICKER_HTML


def test_the_create_view_echoes_the_stored_tags_not_the_typed_ones():
    """They are lowercased and deduped on write, so "Energy, energy" is one tag and the
    page must show which one landed."""
    assert "rep.tags" in S.SERIES_PICKER_HTML
