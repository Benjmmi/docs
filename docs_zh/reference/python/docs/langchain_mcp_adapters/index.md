---
title: MCP 适配器
---

# :fontawesome-solid-down-left-and-up-right-to-center:{ .lg .middle } `langchain-mcp-adapters`

[![PyPI - 版本](https://img.shields.io/pypi/v/langchain-mcp-adapters?label=%20)](https://pypi.org/project/langchain-mcp-adapters/#history)
[![PyPI - 许可证](https://img.shields.io/pypi/l/langchain-mcp-adapters)](https://opensource.org/licenses/MIT)
[![PyPI - 下载量](https://img.shields.io/pepy/dt/langchain-mcp-adapters)](https://pypistats.org/packages/langchain-mcp-adapters)

[`langchain-mcp-adapters`](https://pypi.org/project/langchain-mcp-adapters/) 包的参考文档。

::: langchain_mcp_adapters.client
    options:
      members:
        - MultiServerMCPClient

::: langchain_mcp_adapters.tools
    options:
      members:
        - load_mcp_tools
        - MCPToolArtifact

::: langchain_mcp_adapters.prompts
    options:
      members:
        - load_mcp_prompt

::: langchain_mcp_adapters.resources
    options:
      members:
        - load_mcp_resources

::: langchain_mcp_adapters.interceptors
    options:
      members:
        - ToolCallInterceptor

::: langchain_mcp_adapters.callbacks
    options:
      members:
        - CallbackContext
        - Callbacks

::: langchain_mcp_adapters.sessions
    options:
      members:
        - Connection
        - SSEConnection
        - StdioConnection
        - StreamableHttpConnection
        - WebsocketConnection