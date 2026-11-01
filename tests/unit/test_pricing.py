"""
Unit tests for cost estimation.

The table's failure mode is not a wrong formula, it is sitting still while the configured
model changes around it. That is how `claude-opus-4-8` -- the model doing nearly all the
work -- came to have no price at all, returning `None` into a display with no log line.
So the test that matters is the one that reads the configured models and asserts they are
priced; the arithmetic is one multiplication.
"""

import os

import pytest

from apps.agentic.core import pricing

#: The env vars naming models whose cost gets reported.
CONFIGURED = ("AGENT_LLM_MODEL", "SCORING_LLM_MODEL")


def test_the_configured_models_are_priced():
    """
    The regression test for the actual defect.

    Skips rather than fails when the environment names no model: that means the test is
    running without `.env`, not that the table is wrong.
    """
    models = [os.environ.get(var) for var in CONFIGURED]
    if not any(models):
        pytest.skip(f"none of {', '.join(CONFIGURED)} is set")
    missing = pricing.unpriced_models([m for m in models if m])
    assert not missing, (
        f"configured but unpriced: {missing}. Any cost reported for these is blank, "
        f"and `estimate_cost` returns None rather than raising."
    )


def test_an_unknown_model_returns_none_and_warns(caplog):
    """None, never 0.0 -- a zero reads as "this was free" rather than "unknown"."""
    pricing._warned.discard("no-such-model")
    with caplog.at_level("WARNING", logger="YADA"):
        assert pricing.estimate_cost("no-such-model", 1000, 1000) is None
    assert "No price for model" in caplog.text


def test_the_warning_is_said_once_per_model(caplog):
    """It is called per request; a line per call would bury the log it sits in."""
    pricing._warned.discard("also-unknown")
    with caplog.at_level("WARNING", logger="YADA"):
        pricing.estimate_cost("also-unknown", 1, 1)
        pricing.estimate_cost("also-unknown", 1, 1)
    assert caplog.text.count("No price for model") == 1


@pytest.mark.parametrize("model,inp,out,expected", [
    # Verified against Anthropic's published table, 2026-11-01.
    ("claude-opus-4-8",  1_000_000, 0,         5.00),
    ("claude-opus-4-8",  0,         1_000_000, 25.00),
    ("claude-haiku-4-5", 1_000_000, 1_000_000, 6.00),
    ("claude-opus-5-5",  1_000_000, 1_000_000, 24.00),
    ("claude-haiku-5-5", 1_000_000, 1_000_000, 0.60),
    ("claude-opus-4-8",  0,         0,         0.00),
])
def test_cost_is_priced_per_million_tokens(model, inp, out, expected):
    assert pricing.estimate_cost(model, inp, out) == pytest.approx(expected)


def test_every_price_has_both_directions():
    """A half-filled row would estimate as a KeyError at the one moment it is needed."""
    for model, p in pricing._PRICING.items():
        assert set(p) == {"input", "output"}, model
        assert p["input"] > 0 and p["output"] > 0, model
