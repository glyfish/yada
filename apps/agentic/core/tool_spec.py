from dataclasses import dataclass, field

from langchain_core.tools import tool


@dataclass
class PositiveExample:
    input: str


@dataclass
class NegativeExample:
    input: str
    reason: str


@dataclass
class ToolSpec:
    primary_function: str
    positive_examples: list[PositiveExample] = field(default_factory=list)
    negative_examples: list[NegativeExample] = field(default_factory=list)
    requires_context: list[str] = field(default_factory=list)
    suggests_followup: list[str] = field(default_factory=list)


def build_tool_description(metadata: ToolSpec) -> str:
    parts = [metadata.primary_function.strip()]

    if metadata.positive_examples:
        examples = "\n".join(f'  - "{ex.input}"' for ex in metadata.positive_examples)
        parts.append(f"Use when the user says things like:\n{examples}")

    if metadata.negative_examples:
        examples = "\n".join(f'  - "{ex.input}" ({ex.reason})' for ex in metadata.negative_examples)
        parts.append(f"Do NOT use when the user says things like:\n{examples}")

    if metadata.requires_context:
        context = "\n".join(f"  - {item}" for item in metadata.requires_context)
        parts.append(f"Always include in your request:\n{context}")

    if metadata.suggests_followup:
        followup = "\n".join(f"  - {item}" for item in metadata.suggests_followup)
        parts.append(f"Consider chaining with:\n{followup}")

    return "\n\n".join(parts)


def tool_spec(args_schema=None, metadata: ToolSpec = None):
    """
    Decorate a function as a LangChain tool with a description built from ToolSpec.

    Pass args_schema=None to let LangChain infer the schema from the function
    signature. That path is required when the tool declares an InjectedState (or
    other injected) parameter, since an explicit args_schema prevents LangGraph's
    ToolNode from recognizing and filling the injected argument.
    """
    def decorator(func):
        description = build_tool_description(metadata)
        if args_schema is None:
            return tool(description=description)(func)
        return tool(args_schema=args_schema, description=description)(func)
    return decorator
