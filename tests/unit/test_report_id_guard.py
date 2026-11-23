"""A malformed report_id is a miss, not a crash.

`uuid.UUID("GDP Overview")` raises ValueError, and the parse sat inline in three
ReportCache methods. LangGraph's default tool-error handler re-raises anything that is
not a ToolInvocationError, so "delete the GDP Overview report" ended the chat turn --
and both tools' descriptions positively invite a title. On the HTTP side the same parse
turned GET /api/reports/<title> into a 500 instead of a 404.

A malformed id matches no row, which is the same answer this store already gives for a
report owned by someone else. These pin that, and the tools' replies, which must name
the next step rather than claim no such report exists.
"""
import pytest

from apps.agentic.db.report_cache import ReportCache

VALID = "24c23e96-5e97-4c3d-bb4a-c85116839d36"
MALFORMED = ["GDP Overview", "", "not-a-uuid", "24c23e96-5e97", None, 7]


def test_a_real_uuid_parses():
    assert str(ReportCache._as_report_id(VALID)) == VALID


@pytest.mark.parametrize("bad", MALFORMED)
def test_malformed_ids_are_none_not_an_exception(bad):
    assert ReportCache._as_report_id(bad) is None


@pytest.mark.parametrize("bad", MALFORMED)
def test_the_store_never_raises_on_one(bad):
    """No database needed: the guard returns before the engine is touched."""
    assert ReportCache._get_by_report_id_sync(bad) is None
    assert ReportCache._delete_report_sync(bad) is False


@pytest.mark.parametrize("tool_name, must_mention", [
    ("delete_time_series_report", "list_time_series_reports"),
    ("get_time_series_report", "list_time_series_reports"),
])
def test_the_chat_tools_answer_a_title_with_the_next_step(tool_name, must_mention):
    from apps.agentic.agents.plots.time_series_report_agent import TimeSeriesReportAgent

    tool = getattr(TimeSeriesReportAgent, tool_name)
    reply = tool.invoke({"report_id": "GDP Overview"})
    assert "is not a report_id" in reply
    assert must_mention in reply
    # Not "no such report" -- the report may well exist under that title.
    assert "No report found" not in reply
