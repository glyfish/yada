#!/bin/bash
cd "$(dirname "$0")"
export YADA_MCP_TRANSPORT=streamable-http
export YADA_MCP_HOST=127.0.0.1
export YADA_MCP_PORT=8081
~/.pyenv/versions/yada-3.14.7/bin/python -m mcp_server.server
