---
title: Google (VertexAI)
---

# :simple-googlecloud:{ .lg .middle } `langchain-google-vertexai`

[![PyPI - 版本](https://img.shields.io/pypi/v/langchain-google-vertexai?label=%20)](https://pypi.org/project/langchain-google-vertexai/#history)
[![PyPI - 许可证](https://img.shields.io/pypi/l/langchain-google-vertexai)](https://opensource.org/licenses/MIT)
[![PyPI - 下载量](https://img.shields.io/pepy/dt/langchain-google-vertexai)](https://pypistats.org/packages/langchain-google-vertexai)

用于 Google Vertex AI 平台的 LangChain 集成。

!!! note "Vertex AI 整合"

    自 `langchain-google-vertexai` 3.2.0 版本起，部分类已被弃用，转而使用 `langchain-google-genai` 4.0.0 中的等效类，后者基于整合后的 [`google-genai`](https://googleapis.github.io/python-genai/) SDK。

    更多信息请参阅 [提供商文档](https://docs.langchain.com/oss/python/integrations/providers/google) 和 [发布说明](https://github.com/langchain-ai/langchain-google/discussions/1422)。

## 模块

!!! note "使用文档"
    关于如何使用每个模块的高级指南，请参阅 [文档](https://docs.langchain.com/oss/python/integrations/providers/google)。这些参考页面包含每个模块的自动生成的 API 文档，侧重于“是什么”而非“如何”或“为什么”（即不包含端到端教程或概念概述）。

<div class="grid cards" markdown>

- :material-message-text:{ .lg .middle } **`ChatVertexAI`**

    ---

    **已弃用：** 请改用 `langchain-google-genai` 中的 `ChatGoogleGenerativeAI`。

    [:octicons-arrow-right-24: 参考](./ChatVertexAI.md)

- :material-message-text:{ .lg .middle } **`VertexAI`**

    ---

    **已弃用：** 请改用 `langchain-google-genai` 中的 `GoogleGenerativeAI`。

    [:octicons-arrow-right-24: 参考](./VertexAI.md)

- :fontawesome-solid-layer-group:{ .lg .middle } **`VertexAIEmbeddings`**

    ---

    **已弃用：** 请改用 `langchain-google-genai` 中的 `GoogleGenerativeAIEmbeddings`。

    [:octicons-arrow-right-24: 参考](./VertexAIEmbeddings.md)

- **其他**

    ---

    [:octicons-arrow-right-24: 参考](./other.md)

</div>