from typing import Annotated, Sequence
from typing_extensions import TypedDict

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


class WorkerState(TypedDict):
    """
    WorkerState is a TypedDict that defines the structure of the worker's state.
    It includes a list of messages, which are annotated with the add_messages function.
    """

    messages: Annotated[Sequence[BaseMessage], add_messages]


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


