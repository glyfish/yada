"""Unit tests for the id -> name key an MCP client gets beside a chart.

Why the key exists at all: a chart's legend carries bare series ids, because it has to.
Measured at yada's figure size, a legend entry gets ~18 characters before it covers a
quarter of the plot; the median FRED title is 81 characters and 99.4% of the catalogue
is over 30, so a full-name legend would cover the chart it labels. The browser resolves
the ids with an HTML table above the plot, but only the <img> survives a trip to an MCP
client, so that door needs the same mapping as text.

The format is a markdown pipe table. Space-padded columns were the first attempt and
align nothing in the App, which renders the text in a proportional font; the pipes are
what survive, and `plot_app.py` rebuilds them as a real <table>. The cells are padded
anyway so the same string still reads as a table in a plain-text client.
"""

import re

import pytest

from mcp_server.server import _series_key_text


def _row(native_id, units, title, axis=""):
    return {"native_id": native_id, "units": units, "title": title, "axis": axis}


def _cells(line):
    """Split a row the way plot_app.py's cellsOf does: on UNESCAPED pipes only."""
    body = line.strip()
    body = body[1:] if body.startswith("|") else body
    body = body[:-1] if body.endswith("|") else body
    return [c.strip().replace(r"\|", "|")
            for c in re.split(r"(?<!\\)\|", body)]


def _parse(text):
    """(header, rule, rows) the way plot_app.py's renderNote reads it."""
    lines = text.splitlines()
    return _cells(lines[0]), lines[1], [_cells(line) for line in lines[2:]]


OIL = [
    _row("DCOILWTICO", "$ per Barrel",
         "Crude Oil Prices: West Texas Intermediate (WTI) - Cushing, Oklahoma", "left"),
    _row("DCOILBRENTEU", "$ per Barrel", "Crude Oil Prices: Brent - Europe", "left"),
    _row("DHHNGSP", "$ Per Mil. BTU", "Henry Hub Natural Gas Spot Price", "right"),
]

ONE_AXIS = [
    _row("GDP", "Bil. of $", "Gross Domestic Product"),
    _row("GNP", "Bil. of $", "Gross National Product"),
]


def test_empty_key_renders_nothing():
    """No key means no blank table stapled under the summary."""
    assert _series_key_text([]) == ""


def test_the_header_names_the_columns():
    header, _, _ = _parse(_series_key_text(ONE_AXIS))
    assert header == ["ID", "Units", "Series"]


def test_every_series_gets_a_row():
    _, _, rows = _parse(_series_key_text(OIL))
    assert [r[0] for r in rows] == ["DCOILWTICO", "DCOILBRENTEU", "DHHNGSP"]


def test_each_row_carries_its_title_and_units():
    _, _, rows = _parse(_series_key_text(OIL))
    assert rows[2] == ["DHHNGSP", "$ Per Mil. BTU", "right",
                       "Henry Hub Natural Gas Spot Price"]


# ---------- the markdown contract plot_app.py relies on ----------

def test_a_separator_rule_follows_the_header():
    """Without it the App renders the header as an ordinary row, and so does markdown."""
    _, rule, _ = _parse(_series_key_text(OIL))
    assert rule.startswith("|") and rule.endswith("|")
    assert set(rule) <= set("|-")
    assert "-" in rule


def test_every_line_is_a_pipe_row():
    for line in _series_key_text(OIL).splitlines():
        assert line.startswith("|") and line.endswith("|")


def test_the_rule_has_one_cell_per_column():
    header, rule, rows = _parse(_series_key_text(OIL))
    assert len(_cells(rule)) == len(header)
    for row in rows:
        assert len(row) == len(header)


# ---------- the axis column ----------

def test_the_axis_column_appears_only_on_a_twin_axis_plot():
    """Which scale a curve reads against is the thing a legend of ids cannot express."""
    assert "Axis" in _parse(_series_key_text(OIL))[0]
    assert "Axis" not in _parse(_series_key_text(ONE_AXIS))[0]


def test_axis_values_reach_the_rows():
    _, _, rows = _parse(_series_key_text(OIL))
    assert [r[2] for r in rows] == ["left", "left", "right"]


# ---------- robustness ----------

def test_a_very_long_title_does_not_disturb_the_other_columns():
    """Titles run to 482 characters, so the unbounded column has to be last."""
    long_title = "Total Unemployed, " + "Plus All Persons " * 12
    key = [_row("U6RATE", "%", long_title), _row("UNRATE", "%", "Unemployment Rate")]
    _, _, rows = _parse(_series_key_text(key))
    assert rows[0] == ["U6RATE", "%", long_title.strip()]
    assert rows[1] == ["UNRATE", "%", "Unemployment Rate"]


def test_a_pipe_inside_a_title_cannot_forge_a_column():
    """2,363 FRED titles contain a '|'. Unescaped it splits one cell into two."""
    title = "39) How Has the Volume of Disputes with Clients | Dealers Changed"
    header, _, rows = _parse(_series_key_text([_row("ALLQ39EDCNR", "%", title)]))
    assert len(rows[0]) == len(header)
    assert rows[0] == ["ALLQ39EDCNR", "%", title]      # survives the round trip


def test_a_pipe_is_escaped_on_the_wire():
    """The App splits on unescaped pipes, so the escape has to actually be there."""
    out = _series_key_text([_row("X", "%", "Clients | Dealers")])
    assert r"Clients \| Dealers" in out


@pytest.mark.parametrize("field", ["native_id", "units", "title", "axis"])
def test_a_missing_field_renders_blank_rather_than_crashing(field):
    """The key is built from cache rows, and any of these can be absent or None."""
    for absent in (True, False):
        row = _row("X", "%", "A thing")
        if absent:
            del row[field]
        else:
            row[field] = None
        out = _series_key_text([row])
        assert len(out.splitlines()) == 3          # header + rule + the one row
        assert "None" not in out                   # a None must not print as text
