from __future__ import annotations

from langchain_core.messages import HumanMessage
from langgraph.types import interrupt

from apps.agentic.agents.forms import validate_form, FORM_REGISTRY
from apps.agentic.core.agents.messages import WorkerState
from lib.logger import get_logger

logger = get_logger("YADA")


class HumanInputNode:
    """
    LangGraph node that suspends execution to collect structured form input
    from the user via the interrupt/resume mechanism.

    On first pass the node calls interrupt() with a form schema dict, which
    suspends the graph and returns the schema to the caller. On resume the
    graph passes the submitted form data as the interrupt return value, which
    is validated and injected into state as a HumanMessage so the model node
    can continue.

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
            Current graph state. The last message is expected to carry the
            form type to request in its ``additional_kwargs["form_type"]``.

        Returns
        -------
        WorkerState
            State update containing the validated form data as a HumanMessage.
        """
        last_message = state["messages"][-1]
        form_type = (last_message.additional_kwargs or {}).get("form_type")

        if not form_type or form_type not in FORM_REGISTRY:
            raise ValueError(
                f"HumanInputNode: invalid or missing form_type '{form_type}'. "
                f"Available: {list(FORM_REGISTRY.keys())}"
            )

        model_cls = FORM_REGISTRY[form_type]
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

        logger.debug(f"HumanInputNode: interrupting for form '{form_type}'")

        form_data: dict = interrupt(schema)

        logger.debug(f"HumanInputNode: resumed with data {form_data}")

        validated = validate_form({"type": form_type, **form_data})

        return {
            "messages": [
                HumanMessage(
                    content=validated.model_dump_json(),
                    additional_kwargs={"form_type": form_type, "form_data": validated.model_dump()},
                )
            ]
        }
