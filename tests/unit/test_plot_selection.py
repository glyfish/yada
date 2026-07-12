"""Unit tests for the deterministic report-plot selection rules (no LLM).

_select_plot_type keys off series count + distinct units; _axis_type_for switches to
a log axis when the global value span exceeds one order of magnitude.
"""

import pytest

from lib.plots import PlotType
from apps.agentic.agents.plots.time_series_report_plot_agent import (
    _axis_type_for,
    _select_plot_type,
)


# ---------- _select_plot_type ----------

@pytest.mark.parametrize("units,expected", [
    (["USD"], "single"),                          # one series
    (["USD", "USD"], "comparison"),               # same unit -> overlay
    (["USD", "USD", "USD"], "comparison"),        # same unit, 3 series
    (["USD", "EUR"], "twinx"),                     # 2 series, 2 units
    (["USD", "EUR", "USD"], "twinx_comparison"),   # >2 series, 2 units
    (["USD", "EUR", "USD", "EUR", "USD"], "twinx_comparison"),
    (["USD", "EUR", "GBP"], "stack"),              # 3 distinct units
    (["A", "B", "C", "D"], "stack"),               # many distinct units
])
def test_select_plot_type(units, expected):
    assert _select_plot_type(units) == expected


# ---------- _axis_type_for ----------

def test_axis_linear_for_narrow_span():
    assert _axis_type_for([[1.0, 5.0, 9.0]]) == PlotType.LINEAR


def test_axis_ylog_for_wide_positive_span():
    assert _axis_type_for([[1.0, 100.0]]) == PlotType.YLOG


def test_axis_ylog_across_multiple_groups():
    assert _axis_type_for([[2.0, 4.0], [100.0, 400.0]]) == PlotType.YLOG


def test_axis_linear_when_min_is_zero_or_negative():
    # log axis is undefined for <= 0, so those spans stay linear regardless of range
    assert _axis_type_for([[0.0, 1000.0]]) == PlotType.LINEAR
    assert _axis_type_for([[-5.0, 1000.0]]) == PlotType.LINEAR


def test_axis_linear_for_empty():
    assert _axis_type_for([]) == PlotType.LINEAR
    assert _axis_type_for([[]]) == PlotType.LINEAR


def test_axis_boundary_exactly_one_order_is_linear():
    # ratio == 10 is not strictly greater than 10 -> linear
    assert _axis_type_for([[1.0, 10.0]]) == PlotType.LINEAR
