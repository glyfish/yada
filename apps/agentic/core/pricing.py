"""
Per-token prices for the models this project calls, and the estimate derived from them.

This is the fallback behind LangSmith's own `total_cost`, used whenever a run has not
finished ingesting -- which is exactly when a cost has to be shown. A model missing from
the table silently produced `None`, and `None` reaching a display is a blank where a
number belongs, with nothing saying why. Hence `estimate_cost` now logs.

Prices are per 1M tokens in USD, checked against Anthropic's published table on
2026-11-01. They change; `unpriced_models()` is here so a check can run in a test or at
startup rather than waiting for a blank in the UI.
"""

from lib.logger import get_logger

logger = get_logger("YADA")

# Cost per 1M tokens in USD.
# "input"  = tokens sent TO the model (prompt, system message, conversation history, retrieved docs)
# "output" = tokens the model generates in its response
_PRICING = {
    "gpt-4.1":           {"input": 2.00,  "output": 8.00},
    "gpt-4.1-mini":      {"input": 0.40,  "output": 1.60},
    "gpt-4o":            {"input": 2.50,  "output": 10.00},
    "gpt-4o-mini":       {"input": 0.15,  "output": 0.60},
    "gpt-3.5-turbo":     {"input": 0.50,  "output": 1.50},
    # Claude 5 family.
    "claude-fable-5-1":  {"input": 10.00, "output": 50.00},
    "claude-fable-5":    {"input": 10.00, "output": 50.00},
    "claude-opus-5-5":   {"input": 4.00,  "output": 20.00},
    "claude-opus-5":     {"input": 5.00,  "output": 25.00},
    "claude-sonnet-5-5": {"input": 2.00,  "output": 10.00},
    "claude-sonnet-5":   {"input": 2.00,  "output": 10.00},
    "claude-haiku-5-5":  {"input": 0.10,  "output": 0.50},
    # Claude 4 family. opus-4-8 is AGENT_LLM_MODEL and was missing entirely, so the
    # model doing nearly all the work returned None. opus-4-6 was carrying 15/75 and
    # haiku-4-5 0.80/4.00; both were wrong, and haiku-4-5 is SCORING_LLM_MODEL, so
    # every ranker cost reported before today was about 20% low.
    "claude-opus-4-8":   {"input": 5.00,  "output": 25.00},
    "claude-opus-4-7":   {"input": 5.00,  "output": 25.00},
    "claude-opus-4-6":   {"input": 5.00,  "output": 25.00},
    "claude-sonnet-4-6": {"input": 3.00,  "output": 15.00},
    "claude-sonnet-4-5": {"input": 3.00,  "output": 15.00},
    "claude-haiku-4-5":  {"input": 1.00,  "output": 5.00},
}

#: Models already reported as unpriced, so the log says it once rather than per call.
_warned: set[str] = set()


def estimate_cost(model: str, input_tokens: int, output_tokens: int) -> float | None:
    """
    Estimated cost in USD, or None when the model is not priced.

    A None is logged once per model. The caller still has to handle it -- a missing
    price must not become a zero, which would read as "this was free" rather than
    "this is unknown".
    """
    p = _PRICING.get(model)
    if p is None:
        if model not in _warned:
            _warned.add(model)
            logger.warning(
                f"No price for model {model!r}; cost cannot be estimated. Add it to "
                f"apps/agentic/core/pricing.py."
            )
        return None
    return (input_tokens * p["input"] + output_tokens * p["output"]) / 1_000_000


def is_priced(model: str) -> bool:
    """Whether a price is known for this model."""
    return model in _PRICING


def unpriced_models(models: list[str]) -> list[str]:
    """
    Which of these models have no price, so a test or a startup check can say so.

    The table goes stale by sitting still while the configured model changes around it,
    which is a silent failure in a module whose whole job is to produce a number.
    """
    return [m for m in models if m and m not in _PRICING]
