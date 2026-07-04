from __future__ import annotations

import re

from langchain_core.messages import HumanMessage, ToolMessage
from langgraph.types import interrupt

from apps.agentic.agents.forms import validate_form, FORM_REGISTRY
from apps.agentic.core.agents.messages import WorkerState
from lib.logger import get_logger

logger = get_logger("YADA")

# A GitHub URL (https or ssh), capturing owner + repo, e.g.
# https://github.com/glyfish/meida(.git) or git@github.com:glyfish/meida.git
_GITHUB_URL_RE = re.compile(
    r"github\.com[/:]([A-Za-z0-9][\w.-]*?)/([A-Za-z0-9][\w.-]*?)(?:\.git)?(?:[\s/#?]|$)"
)
# The "owner/repo" shorthand a user types directly, e.g. "glyfish/meida".
_GITHUB_SLUG_RE = re.compile(
    r"\b([A-Za-z0-9](?:[A-Za-z0-9._-]*[A-Za-z0-9])?)/([A-Za-z0-9](?:[A-Za-z0-9._-]*[A-Za-z0-9])?)\b"
)


class HumanInputNode:
    """
    LangGraph node that suspends execution to collect structured form input
    from the user via the interrupt/resume mechanism.

    On first pass the node calls interrupt() with a form schema dict, which
    suspends the graph and returns the schema to the caller. On resume the
    graph passes the submitted form data as the interrupt return value, which
    is validated and injected into state as a HumanMessage so the model node
    can continue.

    The node finds the requested form_type by scanning back through state
    messages for the most recent AIMessage with a ``request_human_form``
    tool call, checking both the normalized ``tool_calls`` attribute and
    raw Anthropic ``content`` blocks.

    Usage in a graph
    ----------------
    Add an instance's ``__call__`` as a node::

        graph.add_node("human_input", HumanInputNode())
    """

    def __call__(self, state: WorkerState) -> WorkerState:
        """
        Suspend and collect form input, then validate and return it as a message.

        Parameters
        ----------
        state : WorkerState
            Current graph state. Scans messages in reverse for a
            ``request_human_form`` tool call to determine the form type.

        Returns
        -------
        WorkerState
            State update containing the validated form data as a HumanMessage.
        """
        form_type = self._find_form_type(state)

        if not form_type or form_type not in FORM_REGISTRY:
            logger.error(
                f"HumanInputNode: could not find form_type. "
                f"Last 3 messages: {[type(m).__name__ for m in state['messages'][-3:]]}"
            )
            raise ValueError(
                f"HumanInputNode: invalid or missing form_type '{form_type}'. "
                f"Available: {list(FORM_REGISTRY.keys())}"
            )

        model_cls = FORM_REGISTRY[form_type]
        prefill = self._find_prefill(state)
        if form_type == "load_github_repo":
            prefill = self._augment_github_prefill(state, prefill)
        schema = {
            "type": form_type,
            "fields": {
                name: {
                    "description": field.description,
                    "required": field.is_required(),
                }
                for name, field in model_cls.model_fields.items()
                if name != "type"
            },
        }
        if prefill:
            schema["prefill"] = prefill

        logger.debug(f"HumanInputNode: interrupting for form '{form_type}' prefill={prefill}")

        form_data: dict = interrupt(schema)

        logger.debug(f"HumanInputNode: resumed with data {form_data}")

        validated = validate_form({"type": form_type, **form_data})

        # Anthropic requires every tool_use block to be immediately followed by
        # a tool_result. Inject a ToolMessage answering request_human_form before
        # the HumanMessage so the model does not reject the conversation history.
        tool_call_id = self._find_tool_call_id(state)
        messages = []
        if tool_call_id:
            messages.append(
                ToolMessage(
                    content=f"Form submitted by user for form type: {form_type}",
                    tool_call_id=tool_call_id,
                )
            )

        messages.append(
            HumanMessage(
                content=validated.model_dump_json(),
                additional_kwargs={"form_type": form_type, "form_data": validated.model_dump()},
            )
        )

        return {"messages": messages}


    def _find_tool_call_id(self, state: WorkerState) -> str | None:
        """
        Return the tool_call_id of the most recent ``request_human_form``
        tool call so we can pair it with a ToolMessage on resume.
        """
        for msg in reversed(state["messages"]):
            tool_calls = getattr(msg, "tool_calls", None)
            if tool_calls:
                for tc in tool_calls:
                    name = tc.get("name") if isinstance(tc, dict) else getattr(tc, "name", None)
                    if name == "request_human_form":
                        return tc.get("id") if isinstance(tc, dict) else getattr(tc, "id", None)

            content = getattr(msg, "content", None)
            if isinstance(content, list):
                for block in content:
                    if isinstance(block, dict) and block.get("type") == "tool_use":
                        if block.get("name") == "request_human_form":
                            return block.get("id")

        return None


    def _find_form_type(self, state: WorkerState) -> str | None:
        """
        Scan messages in reverse for the form_type from a ``request_human_form``
        tool call. Checks three sources in order:

        1. Normalized ``tool_calls`` attribute (LangChain standard format, args key).
        2. Raw Anthropic ``content`` blocks (``tool_use`` type, input key).
        3. ``additional_kwargs["form_type"]`` on the last message (test fallback).
        """
        for msg in reversed(state["messages"]):

            # 1. Normalized tool_calls (LangChain standard)
            tool_calls = getattr(msg, "tool_calls", None)
            if tool_calls:
                for tc in tool_calls:
                    name = tc.get("name") if isinstance(tc, dict) else getattr(tc, "name", None)
                    if name == "request_human_form":
                        args = tc.get("args", {}) if isinstance(tc, dict) else getattr(tc, "args", {})
                        form_type = (args or {}).get("form_type")
                        if form_type:
                            return form_type

            # 2. Raw Anthropic content blocks (tool_use with input key)
            content = getattr(msg, "content", None)
            if isinstance(content, list):
                for block in content:
                    if isinstance(block, dict) and block.get("type") == "tool_use":
                        if block.get("name") == "request_human_form":
                            form_type = (block.get("input") or {}).get("form_type")
                            if form_type:
                                return form_type

        # 3. Fallback for tests that inject form_type via additional_kwargs directly
        last = state["messages"][-1]
        return (getattr(last, "additional_kwargs", None) or {}).get("form_type")


    def _find_prefill(self, state: WorkerState) -> dict | None:
        """Extract the prefill dict from the most recent request_human_form tool call."""
        for msg in reversed(state["messages"]):
            tool_calls = getattr(msg, "tool_calls", None)
            if tool_calls:
                for tc in tool_calls:
                    name = tc.get("name") if isinstance(tc, dict) else getattr(tc, "name", None)
                    if name == "request_human_form":
                        args = tc.get("args", {}) if isinstance(tc, dict) else getattr(tc, "args", {})
                        return (args or {}).get("prefill")

            content = getattr(msg, "content", None)
            if isinstance(content, list):
                for block in content:
                    if isinstance(block, dict) and block.get("type") == "tool_use":
                        if block.get("name") == "request_human_form":
                            return (block.get("input") or {}).get("prefill")

        return None

    def _augment_github_prefill(self, state: WorkerState, prefill: dict | None) -> dict | None:
        """
        Deterministic fallback for the load_github_repo form: fill any missing
        account/repo by parsing an ``owner/repo`` slug (or GitHub URL) out of the
        user's most recent request. Runs only for fields the model left blank, so
        an explicit LLM-supplied prefill always wins.
        """
        prefill = dict(prefill or {})
        if prefill.get("account") and prefill.get("repo"):
            return prefill

        for msg in reversed(state["messages"]):
            if not isinstance(msg, HumanMessage):
                continue
            # Skip validated-form messages we injected on a prior resume.
            if (getattr(msg, "additional_kwargs", None) or {}).get("form_type"):
                continue
            content = msg.content
            if not isinstance(content, str):
                continue
            match = _GITHUB_URL_RE.search(content) or _GITHUB_SLUG_RE.search(content)
            if match:
                prefill.setdefault("account", match.group(1))
                prefill.setdefault("repo", match.group(2))
            break  # only inspect the latest genuine user message

        return prefill or None
