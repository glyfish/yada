"""Shared pytest fixtures / environment for the yada test suite.

Some modules (e.g. the orchestrator) instantiate the full agent tree at import
time, which builds LLM clients and therefore needs a provider + API key in the
environment. Unit tests must stay hermetic and never touch a real key or the
network, so we seed harmless placeholders here — client construction is offline,
so a dummy key is enough to let the imports succeed.

Integration / llm-marked tests that genuinely call a model should load the real
.env themselves (or run with real keys exported); setdefault leaves any real
values already present in the environment untouched.
"""

import logging
import os

# Agents dump their prompts at DEBUG on construction; keep test output readable.
logging.getLogger("YADA").setLevel(logging.WARNING)

os.environ.setdefault("LLM_MODEL_PROVIDER", "anthropic")
os.environ.setdefault("AGENT_LLM_MODEL", "claude-sonnet-5")
os.environ.setdefault("ANTHROPIC_API_KEY", "test-key-not-used")
os.environ.setdefault("OPENAI_API_KEY", "test-key-not-used")
# Some agents build API clients at construction that validate a key's presence.
os.environ.setdefault("TAVILY_API_KEY", "test-key-not-used")
