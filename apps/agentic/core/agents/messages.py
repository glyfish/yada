from dataclasses import dataclass
from typing import Annotated, Sequence
from typing_extensions import NotRequired, TypedDict

from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages
from langgraph.graph import END

class Annotation:
    """
    Annotation class to define a reducer and a default value for a state field.
    This class is used to annotate fields in the state with a reducer function
    """
    
    def __init__(self, reducer, default):
        self.reducer = reducer
        self.default = default

    @classmethod
    def Root(cls, annotations):
        # This inner class will serve as our state container
        class Root:
            def __init__(self):
                # Initialize each field with its default value
                for key, annotation in annotations.items():
                    setattr(self, key, annotation.default())
            
            def update(self, key, value):
                if key in annotations:
                    # Get the annotation definition for this key
                    annotation = annotations[key]
                    current_value = getattr(self, key)
                    # Use the reducer to compute the new value
                    new_value = annotation.reducer(current_value, value)
                    setattr(self, key, new_value)
                else:
                    raise KeyError(f"No annotation defined for key: {key}")

            def __repr__(self):
                # Provide a convenient string representation of the state
                state = {key: getattr(self, key) for key in annotations}
                return f"<AgentState {state}>"
                
        return Root

"""
Implementation of Annotated Agent State Model implementing with a concatenating 
reducer and a default value of END for the next field.
"""
AgentStateModel = Annotation.Root({
    "messages": Annotation(
        reducer=lambda x, y: x + y,   # Concatenates lists
        default=lambda: []            # Default is an empty list
    ),
    "next": Annotation(
        reducer=lambda x, y: y if y is not None else x if x is not None else END,
        default=lambda: END           # Default value is END
    )
})


@dataclass
class RetrievedChunk:
    """
    One retrieved chunk, kept whole across a node boundary.

    The graph passed retrieved documents as text in a SystemMessage, so everything a
    chunk knew about itself -- which repository, which file, what the ranker scored it
    -- survived only as far as it could be written into a header and parsed back out.
    The score fared worst: `_grade_documents` had it as a float and could express it
    only as the string `[relevance: 0.95]` appended to the text.

    Nothing could consume that. A structured result needs the score as a number, the
    path as a path, and the metadata as fields, which is why the chunks now travel
    beside the messages rather than inside them.
    """

    index: int                  # 1-based, matching the "Document N:" label the grader reads
    text: str
    metadata: dict
    score: float | None = None  # set by the ranker; None before grading

    @property
    def path(self) -> str:
        return self.metadata.get("path") or self.metadata.get("title") or ""


class WorkerState(TypedDict):
    """
    WorkerState is a TypedDict that defines the structure of the worker's state.
    It includes a list of messages annotated with the add_messages reducer.

    `hits` is NotRequired because most graphs here never retrieve; those that do
    overwrite it wholesale at each node, which is the default reducer for an
    un-annotated field and the behaviour wanted -- grading narrows the set rather than
    adding to it.
    """

    messages: Annotated[Sequence[BaseMessage], add_messages]
    hits: NotRequired[list[RetrievedChunk]]


def get_last_message(state) -> BaseMessage:
    """
    Get the last message from a list of messages.
    """
    
    if not isinstance(state, dict) or "messages" not in state:
        raise ValueError("Invalid state format. Expected a dictionary with 'messages' key.")
    if not state["messages"]:
        raise ValueError("No messages found in the state.")
    if not isinstance(state["messages"], list):
        raise ValueError("Messages should be a list of BaseMessage objects.")
    if len(state["messages"]) == 0:
        raise ValueError("No messages found in the state.")
    if not isinstance(state["messages"][-1], BaseMessage):
        raise ValueError("The last message is not a BaseMessage object.")
    
    return state["messages"][-1]


