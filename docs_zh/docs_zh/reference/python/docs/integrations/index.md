---
title: 集成概览
hide:
  - toc
---

欢迎！这些页面包含了所有 `langchain-*` Python 集成包的参考文档。

要了解更多关于 LangChain 中的集成信息，请访问 [集成概览](https://docs.langchain.com/oss/python/integrations/providers/overview)。

!!! tip "模型上下文协议 (MCP)"
    LangChain 支持模型上下文协议 (MCP)。这使得外部工具可以通过标准接口与 LangChain 和 LangGraph 应用程序协同工作。

    要在您的项目中使用 MCP 工具，请参阅 [`langchain-mcp-adapters`](../langchain_mcp_adapters/index.md)。

---

## 热门提供商

<div class="grid cards" markdown>

- :fontawesome-brands-openai:{ .lg .middle } __`langchain-openai`__

    ---

    与 OpenAI（补全、响应）及 OpenAI 兼容的 API 进行交互。

    [:octicons-arrow-right-24: 参考文档](./langchain_openai/index.md)

- :simple-claude:{ .lg .middle } __`langchain-anthropic`__

    ---

    与 Claude (Anthropic) API 进行交互。

    [:octicons-arrow-right-24: 参考文档](./langchain_anthropic/index.md)

- :simple-googlegemini:{ .lg .middle } __`langchain-google-genai`__

    ---

    通过 Google Gen AI SDK 访问 Google Gemini 模型。

    [:octicons-arrow-right-24: 参考文档](./langchain_google_genai/index.md)

- :material-aws:{ .lg .middle } __`langchain-aws`__

    ---

    使用与 AWS 平台相关的集成，如 Bedrock、S3 等。

    [:octicons-arrow-right-24: 参考文档](./langchain_aws.md)

- :simple-huggingface:{ .lg .middle } __`langchain-huggingface`__

    ---

    在 LangChain 中访问 HuggingFace 托管的模型。

    [:octicons-arrow-right-24: 参考文档](./langchain_huggingface.md)

- :material-message:{ .lg .middle } __`langchain-groq`__

    ---

    连接至 Groq Cloud。

    [:octicons-arrow-right-24: 参考文档](./langchain_groq.md)

- :simple-ollama:{ .lg .middle } __`langchain-ollama`__

    ---

    通过 Ollama 使用本地托管的模型。

    [:octicons-arrow-right-24: 参考文档](./langchain_ollama.md)

</div>

其他提供商，包括 `langchain-community`，列在左侧边栏的导航部分中。

!!! question ""我没有找到想要的集成""
    LangChain 有数百个集成，但并非所有都记录在本站点。如果您没有找到所需的集成，请参考 [LangChain 文档中的提供商页面](https://docs.langchain.com/oss/python/integrations/providers/all_providers)。此外，许多社区维护的集成可在 [`langchain-community`](./langchain_community/index.md) 包中找到。

!!! note "创建新的集成"
    有关贡献新集成的信息，请参阅 [指南](https://docs.langchain.com/oss/python/contributing/integrations-langchain)。