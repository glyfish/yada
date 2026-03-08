# Cost per 1M tokens in USD.
# "input"  = tokens sent TO the model (prompt, system message, conversation history, retrieved docs)
# "output" = tokens the model generates in its response
_PRICING = {
    "gpt-4.1":           {"input": 2.00,  "output": 8.00},
    "gpt-4.1-mini":      {"input": 0.40,  "output": 1.60},
    "gpt-4o":            {"input": 2.50,  "output": 10.00},
    "gpt-4o-mini":       {"input": 0.15,  "output": 0.60},
    "gpt-3.5-turbo":     {"input": 0.50,  "output": 1.50},
    "claude-opus-4-6":   {"input": 15.00, "output": 75.00},
    "claude-sonnet-4-6": {"input": 3.00,  "output": 15.00},
    "claude-sonnet-4-5": {"input": 3.00,  "output": 15.00},
    "claude-haiku-4-5":  {"input": 0.80,  "output": 4.00},
}


def estimate_cost(model: str, input_tokens: int, output_tokens: int) -> float | None:
    """Return estimated cost in USD, or None if the model is not in the pricing table."""
    p = _PRICING.get(model)
    if p is None:
        return None
    return (input_tokens * p["input"] + output_tokens * p["output"]) / 1_000_000
