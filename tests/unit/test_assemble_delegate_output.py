"""Unit tests for the orchestrator's verbatim delegate-output assembly.

_content_to_text flattens Anthropic content-block lists; assemble_delegate_output
selects the right tool results from the current turn (all parallel results vs the
last result of a dependent chain).
"""

from langchain_core.messages import AIMessage, HumanMessage, ToolMessage

from apps.agentic.agents.orchestrator import _content_to_text, assemble_delegate_output


def _ai_tools(*names):
    """AIMessage carrying one tool_call per name, ids '1','2',..."""
    calls = [{"name": n, "args": {}, "id": str(i + 1), "type": "tool_call"} for i, n in enumerate(names)]
    return AIMessage(content="", tool_calls=calls)


# ---------- _content_to_text ----------

def test_content_to_text_plain_string():
    assert _content_to_text("hello world") == "hello world"


def test_content_to_text_anthropic_block_list():
    content = [{"type": "text", "text": "line one"}, {"type": "text", "text": "line two"}]
    assert _content_to_text(content) == "line one\nline two"


def test_content_to_text_block_without_text_falls_back_to_repr():
    content = [{"type": "image", "source": "x"}]
    assert "image" in _content_to_text(content)


# ---------- assemble_delegate_output ----------

def test_parallel_results_all_included_in_order():
    msgs = [
        HumanMessage(content="do two things"),
        _ai_tools("delegate_a", "delegate_b"),
        ToolMessage(content="RESULT A", tool_call_id="1"),
        ToolMessage(content="RESULT B", tool_call_id="2"),
    ]
    assert assemble_delegate_output(msgs) == "RESULT A\n\nRESULT B"


def test_dependent_chain_returns_only_last_result():
    msgs = [
        HumanMessage(content="fetch then plot"),
        _ai_tools("fetch"),
        ToolMessage(content="RAW DATA", tool_call_id="1"),
        _ai_tools("plot"),
        ToolMessage(content="THE PLOT", tool_call_id="1"),
    ]
    assert assemble_delegate_output(msgs) == "THE PLOT"


def test_pure_conversational_falls_back_to_ai_message():
    msgs = [HumanMessage(content="hi"), AIMessage(content="hello there")]
    assert assemble_delegate_output(msgs) == "hello there"


def test_no_assistant_message_returns_none():
    assert assemble_delegate_output([HumanMessage(content="hi")]) is None


def test_scoped_to_current_turn_ignores_prior_turn():
    msgs = [
        HumanMessage(content="old request"),
        _ai_tools("delegate_a"),
        ToolMessage(content="OLD RESULT", tool_call_id="1"),
        HumanMessage(content="new request"),
        _ai_tools("delegate_b"),
        ToolMessage(content="NEW RESULT", tool_call_id="1"),
    ]
    assert assemble_delegate_output(msgs) == "NEW RESULT"


def test_tool_result_with_anthropic_block_content():
    msgs = [
        HumanMessage(content="go"),
        _ai_tools("delegate_a"),
        ToolMessage(content=[{"type": "text", "text": "<img src=x>"}], tool_call_id="1"),
    ]
    assert assemble_delegate_output(msgs) == "<img src=x>"
