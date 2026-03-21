from typing import cast

from anthropic import APIStatusError as AnthropicAPIStatusError, InternalServerError as AnthropicInternalServerError
from openai import APIStatusError as OpenAIAPIStatusError, InternalServerError as OpenAIInternalServerError
from langchain_core.messages import AIMessage, SystemMessage
from langchain_core.tools import BaseTool
from langsmith.run_helpers import traceable

from apps.agentic.core.agents.messages import WorkerState
from apps.agentic.core.llm_factory import agent_llm_model
from apps.agentic.core.output_style import OUTPUT_STYLE
from lib.logger import get_logger

logger = get_logger("YADA")


class ReactNode:
    """
    Concrete class that owns the LLM, prompt, and model invocation.
    Serves as a LangGraph-compatible node callable via self._model_runner.
    """

    def __init__(self, tools: list[BaseTool], prompt, name: str = "ReactNode"):
        self._name = name
        self._tools = tools
        self._llm = agent_llm_model()
        self._prompt = prompt
        self._tooled_llm = self._llm.bind_tools(self._tools).with_retry(
            retry_if_exception_type=(
                AnthropicAPIStatusError, AnthropicInternalServerError,
                OpenAIAPIStatusError, OpenAIInternalServerError,
            ),
            stop_after_attempt=3,
            wait_exponential_jitter=True,
        )
        self._model_runner = traceable(
            run_type="chain",
            name=f"{name}.model",
        )(self._invoke_model)

    @property
    def tools(self) -> list[BaseTool]:
        return self._tools

    @property
    def llm(self):
        return self._llm

    @property
    def prompt(self):
        return self._prompt

    @property
    def tooled_llm(self):
        return self._tooled_llm

    @property
    def model_runner(self):
        return self._model_runner

    async def _invoke_model(self, state: WorkerState, config=None) -> WorkerState:
        messages = state["messages"]
        prompt_messages = self.prompt.format_messages(messages=messages)
        if prompt_messages and isinstance(prompt_messages[0], SystemMessage):
            prompt_messages[0] = SystemMessage(
                content=f"{prompt_messages[0].content}\n\n{OUTPUT_STYLE}"
            )
        result = cast(AIMessage, await self.tooled_llm.ainvoke(prompt_messages))

        if result.tool_calls:
            for tc in result.tool_calls:
                logger.info(f"[{self._name}] routing → {tc['name']}({tc['args']})")

        return {"messages": [result]}
