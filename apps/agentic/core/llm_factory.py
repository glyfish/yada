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


def _env_float(name: str, default: float) -> float:
    raw = os.getenv(name)
    if not raw or not raw.strip():
        return default
    try:
        return float(raw)
    except ValueError:
        return default


def _env_flag(name: str, default: bool = False) -> bool:
    raw = os.getenv(name)
    if raw is None:
        return default
    return raw.strip().lower() in ("1", "true", "yes", "on", "adaptive")


def _env_int(name: str, default: int | None = None) -> int | None:
    raw = os.getenv(name)
    if not raw or not raw.strip():
        return default
    try:
        return int(raw)
    except ValueError:
        return default


@dataclass(frozen=True)
class LLMSettings:
    """
    Factory for building LLMs with LangSmith tracing support.
    Supported values of `provider` and `model are:

    provider    model
    --------    ---------------------
    openai      gpt-4.1, gpt-4.1-mini, 
                gpt-3.5-turbo, gpt-4o,
                gpt-4o-mini
    anthropic   claude-opus-4-8,
                claude-opus-4-7,
                claude-opus-4-6,
                claude-sonnet-4-6,
                claude-sonnet-4-5,
                claude-haiku-4-5
    """

    provider: str
    model: str
    temperature: float = 0.7
    thinking: bool = False
    effort: str | None = None
    max_tokens: int | None = None
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
        kwargs = dict(settings.extra)
        if settings.max_tokens is not None:
            kwargs.setdefault("max_tokens", settings.max_tokens)
        return ChatOpenAI(
            model=settings.model,
            temperature=settings.temperature,
            callbacks=callbacks,
            **kwargs,
        )

# Anthropic models that reject sampling params (temperature/top_p/top_k); sending
# any of them returns a 400. Covers Opus 4.7+, Fable 5, and Mythos.
_ANTHROPIC_NO_SAMPLING_PARAMS = (
    "claude-opus-4-7",
    "claude-opus-4-8",
    "claude-fable-5",
    "claude-mythos-5",
    "claude-mythos-preview",
)

# Anthropic models that support adaptive thinking and the effort parameter.
# Haiku 4.5 and older Sonnets are excluded — they 400 on effort.
_ANTHROPIC_REASONING_MODELS = (
    "claude-opus-4-5",
    "claude-opus-4-6",
    "claude-opus-4-7",
    "claude-opus-4-8",
    "claude-sonnet-4-6",
    "claude-fable-5",
    "claude-mythos-5",
    "claude-mythos-preview",
)


class AnthropicLLMFactory(LangsmithLLMFactory):
    provider = "anthropic"

    def build(self, settings: LLMSettings, callbacks=None):
        kwargs = dict(settings.extra)
        if settings.model.startswith(_ANTHROPIC_NO_SAMPLING_PARAMS):
            # Opus 4.7+, Fable 5, and Mythos reject temperature/top_p/top_k.
            for param in ("temperature", "top_p", "top_k"):
                kwargs.pop(param, None)
        else:
            kwargs.setdefault("temperature", settings.temperature)

        if settings.model.startswith(_ANTHROPIC_REASONING_MODELS):
            if settings.thinking:
                kwargs.setdefault("thinking", {"type": "adaptive"})
            if settings.effort:
                model_kwargs = dict(kwargs.get("model_kwargs") or {})
                model_kwargs.setdefault("output_config", {"effort": settings.effort})
                kwargs["model_kwargs"] = model_kwargs

        if settings.max_tokens is not None:
            kwargs.setdefault("max_tokens", settings.max_tokens)

        return ChatAnthropic(
            model_name=settings.model,
            callbacks=callbacks,
            **kwargs,
        )


_factories: dict[str, LangsmithLLMFactory] = {
    "openai": OpenAILLMFactory(),
    "anthropic": AnthropicLLMFactory(),
}


def register_llm_factory(factory: LangsmithLLMFactory) -> None:
    _factories[factory.provider] = factory


def build_llm(
    provider: str = "openai",
    model: str = "gpt-4.1",
    temperature: float = 0.7,
    thinking: bool = False,
    effort: str | None = None,
    max_tokens: int | None = None,
    **kwargs,
):
    callbacks = _build_tracer()
    settings = LLMSettings(
        provider=provider,
        model=model,
        temperature=temperature,
        thinking=thinking,
        effort=effort,
        max_tokens=max_tokens,
        extra=kwargs,
    )
    try:
        factory = _factories[provider]
    except KeyError:
        raise ValueError(f"No factory registered for '{provider}'")
    return factory.build(settings, callbacks=callbacks)


def agent_llm_model(**kwargs):
    provider = os.getenv("LLM_MODEL_PROVIDER", "openai")
    model = os.getenv("AGENT_LLM_MODEL", "gpt-4.1")
    return build_llm(
        provider=provider,
        model=model,
        temperature=_env_float("LLM_TEMPERATURE", 0.7),
        max_tokens=_env_int("LLM_MAX_TOKENS"),
        thinking=_env_flag("AGENT_LLM_THINKING", False),
        effort=os.getenv("AGENT_LLM_EFFORT") or None,
        **kwargs,
    )


def scoring_llm_model(**kwargs):
    provider = os.getenv("LLM_MODEL_PROVIDER", "openai")
    model = os.getenv("SCORING_LLM_MODEL", "gpt-4.1-mini")
    return build_llm(
        provider=provider,
        model=model,
        temperature=_env_float("LLM_TEMPERATURE", 0.7),
        max_tokens=_env_int("LLM_MAX_TOKENS"),
        **kwargs,
    )


def filter_llm_model(**kwargs):
    provider = os.getenv("LLM_MODEL_PROVIDER", "openai")
    model = os.getenv("FILTER_LLM_MODEL", os.getenv("SCORING_LLM_MODEL", "gpt-4.1-mini"))
    return build_llm(
        provider=provider,
        model=model,
        temperature=_env_float("LLM_TEMPERATURE", 0.7),
        max_tokens=_env_int("LLM_MAX_TOKENS"),
        **kwargs,
    )