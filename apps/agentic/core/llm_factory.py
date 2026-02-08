import os
import yaml

from dataclasses import dataclass, field
from typing import Iterable, Protocol, runtime_checkable, Any

from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.language_models.chat_models import BaseChatModel
from langgraph.graph import END
from langchain_core.tracers.langchain import LangChainTracer
from langchain.callbacks.manager import CallbackManager


def _build_tracer():
    if os.environ.get("LANGCHAIN_TRACING_V2", "").lower() != "true":
        return None
    api_key = os.environ.get("LANGCHAIN_API_KEY") or os.environ.get("LANGSMITH_API_KEY")
    if not api_key:
        return None

    # LangChainTracer reads credentials from environment variables; ensure they're set.
    os.environ.setdefault("LANGCHAIN_API_KEY", api_key)

    project = os.environ.get("LANGCHAIN_PROJECT")
    tracer = LangChainTracer(project_name=project)
    return CallbackManager([tracer])


@dataclass(frozen=True)
class LLMSettings:
    provider: str              # e.g. "openai", "anthropic", "bedrock"
    model: str
    temperature: float = 0.7
    extra: dict[str, Any] = field(default_factory=dict)


@runtime_checkable
class LangsmithLLMFactory(Protocol):
    """“Create an LLM wired up to LangSmith tracing.”"""
    provider: str

    def build(
        self,
        settings: LLMSettings,
        callbacks: CallbackManager | None = None,
    ) -> BaseChatModel:
        ...

class OpenAILLMFactory(LangsmithLLMFactory):
    provider = "openai"

    def build(self, settings: LLMSettings, callbacks=None):
        return ChatOpenAI(
            model=settings.model,
            temperature=settings.temperature,
            callbacks=callbacks,
            **settings.extra,
        )

class AnthropicLLMFactory(LangsmithLLMFactory):
    provider = "anthropic"

    def build(self, settings: LLMSettings, callbacks=None):
        return ChatAnthropic(
            model_name=settings.model,
            temperature=settings.temperature,
            callbacks=callbacks,
            **settings.extra,
        )


_factories: dict[str, LangsmithLLMFactory] = {
    "openai": OpenAILLMFactory(),
    "anthropic": AnthropicLLMFactory(),
}


def register_llm_factory(factory: LangsmithLLMFactory) -> None:
    _factories[factory.provider] = factory


def build_llm(provider: str = "openai", model: str = "gpt-4.1", **kwargs):
    callbacks = _build_tracer()
    settings = LLMSettings(provider=provider, model=model, extra=kwargs)
    try:
        factory = _factories[provider]
    except KeyError:
        raise ValueError(f"No factory registered for '{provider}'")
    return factory.build(settings, callbacks=callbacks)