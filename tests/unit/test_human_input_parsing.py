"""Unit tests for HumanInputNode's message-scanning helpers.

These pure helpers pull the form_type / prefill / tool_call_id out of a prior
request_human_form call (from normalized tool_calls or raw Anthropic content
blocks), and deterministically parse a GitHub owner/repo out of the user's
request when the model left the load_github_repo prefill blank.
"""

from types import SimpleNamespace

from langchain_core.messages import AIMessage, HumanMessage

from apps.agentic.core.agents.human_input_node import HumanInputNode

node = HumanInputNode()


def _state(*messages):
    return {"messages": list(messages)}


def _hf_ai(form_type, prefill=None, tool_id="call-1"):
    args = {"form_type": form_type}
    if prefill is not None:
        args["prefill"] = prefill
    return AIMessage(
        content="",
        tool_calls=[{"name": "request_human_form", "args": args, "id": tool_id, "type": "tool_call"}],
    )


# ---------- _find_form_type ----------

def test_find_form_type_from_normalized_tool_calls():
    st = _state(HumanMessage(content="x"), _hf_ai("create_time_series_report"))
    assert node._find_form_type(st) == "create_time_series_report"


def test_find_form_type_from_raw_anthropic_block():
    block_msg = SimpleNamespace(content=[{
        "type": "tool_use", "name": "request_human_form",
        "input": {"form_type": "load_github_repo"}, "id": "call-9",
    }])
    st = _state(HumanMessage(content="x"), block_msg)
    assert node._find_form_type(st) == "load_github_repo"


def test_find_form_type_additional_kwargs_fallback():
    st = _state(HumanMessage(content="{}", additional_kwargs={"form_type": "create_time_series_report"}))
    assert node._find_form_type(st) == "create_time_series_report"


def test_find_form_type_absent_returns_none():
    st = _state(HumanMessage(content="just a question"))
    assert node._find_form_type(st) is None


# ---------- _find_prefill ----------

def test_find_prefill_returns_prefill_dict():
    prefill = {"searches": [{"source": "etf", "query": "VanEck"}]}
    st = _state(HumanMessage(content="x"), _hf_ai("create_time_series_report", prefill=prefill))
    assert node._find_prefill(st) == prefill


def test_find_prefill_absent_returns_none():
    st = _state(HumanMessage(content="x"), _hf_ai("create_time_series_report"))
    assert node._find_prefill(st) is None


# ---------- _find_tool_call_id ----------

def test_find_tool_call_id():
    st = _state(HumanMessage(content="x"), _hf_ai("create_time_series_report", tool_id="call-42"))
    assert node._find_tool_call_id(st) == "call-42"


# ---------- _augment_github_prefill ----------

def test_github_prefill_complete_is_passthrough():
    st = _state(HumanMessage(content="load glyfish/other"))
    assert node._augment_github_prefill(st, {"account": "a", "repo": "b"}) == {"account": "a", "repo": "b"}


def test_github_prefill_from_slug():
    st = _state(HumanMessage(content="load the glyfish/meida repo"))
    assert node._augment_github_prefill(st, None) == {"account": "glyfish", "repo": "meida"}


def test_github_prefill_from_url():
    st = _state(HumanMessage(content="add https://github.com/glyfish/meida to my store"))
    assert node._augment_github_prefill(st, None) == {"account": "glyfish", "repo": "meida"}


def test_github_prefill_skips_validated_form_message():
    genuine = HumanMessage(content="load glyfish/meida")
    validated = HumanMessage(content='{"account":"x"}', additional_kwargs={"form_type": "load_github_repo"})
    # validated is most recent and must be skipped in favour of the genuine request
    st = _state(genuine, validated)
    assert node._augment_github_prefill(st, None) == {"account": "glyfish", "repo": "meida"}
