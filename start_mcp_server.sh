#!/bin/bash
cd "$(dirname "$0")"
export YADA_MCP_TRANSPORT=streamable-http
export YADA_MCP_HOST=127.0.0.1
export YADA_MCP_PORT=8081
# INFO: one line per request and result. DEBUG adds response bodies, the
# extraction the model performed, and the agent prompts.
export YADA_LOG_LEVEL="${YADA_LOG_LEVEL:-INFO}"
~/.pyenv/versions/yada-3.14.7/bin/python -m mcp_server.server
