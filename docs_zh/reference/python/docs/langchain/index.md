---
title: LangChain 概述
hide:
  - toc
---

欢迎来到 [LangChain](https://github.com/langchain-ai/langchain) 包参考文档！

大多数用户主要会与主包 [`langchain`](./langchain/index.md) 进行交互，它提供了构建 LLM 应用所需的完整实现。以下包构成了 LangChain 生态系统的基础，每个包在架构中都有特定的用途：

<div class="grid cards" markdown>

- :simple-langchain:{ .lg .middle } __`langchain`__

    ---

    包含构建 LLM 应用所需的所有实现的主要入口点。

    [:octicons-arrow-right-24: 参考文档](./langchain/index.md)

- :material-atom:{ .lg .middle } __`langchain-core`__

    ---

    LangChain 生态系统中使用的核心接口和抽象。

    [:octicons-arrow-right-24: 参考文档](../langchain_core/index.md)

- :material-format-text:{ .lg .middle } __`langchain-text-splitters`__

    ---

    用于文档处理的文本分割工具。

    [:octicons-arrow-right-24: 参考文档](../langchain_text_splitters/index.md)

- :fontawesome-solid-down-left-and-up-right-to-center:{ .lg .middle } __`langchain-mcp-adapters`__

    ---

    使 MCP 工具可在 LangChain 和 LangGraph 应用中使用。

    [:octicons-arrow-right-24: 参考文档](../langchain_mcp_adapters/index.md)

- :material-test-tube:{ .lg .middle } __`langchain-tests`__

    ---

    用于验证 LangChain 集成包实现的标准测试套件。

    [:octicons-arrow-right-24: 参考文档](../langchain_tests/index.md)

- :fontawesome-solid-building-columns:{ .lg .middle } __`langchain-classic`__

    ---

    传统的 `langchain` 实现和组件。

    [:octicons-arrow-right-24: 参考文档](../langchain_classic/index.md)

</div>

!!! info "集成包"

    正在寻找与特定提供商和服务的集成？请查看 [集成参考文档](../integrations/index.md)，了解与热门 LLM 提供商、向量存储、工具及其他服务连接的包。