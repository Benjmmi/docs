---
title: Google (GenAI)
---

# :simple-googlegemini:{ .lg .middle } `langchain-google-genai`

[![PyPI - 版本](https://img.shields.io/pypi/v/langchain-google-genai?label=%20)](https://pypi.org/project/langchain-google-genai/#history)
[![PyPI - 许可证](https://img.shields.io/pypi/l/langchain-google-genai)](https://opensource.org/licenses/MIT)
[![PyPI - 下载量](https://img.shields.io/pepy/dt/langchain-google-genai)](https://pypistats.org/packages/langchain-google-genai)

LangChain 与 Google 生成式 AI 模型的集成，通过 **Gemini 开发者 API** 和 **Vertex AI** 提供对 Gemini 模型的访问。

!!! note "Vertex AI 整合"

    自 `langchain-google-genai` 4.0.0 版本起，本包使用整合后的 [`google-genai`](https://googleapis.github.io/python-genai/) SDK，取代了旧的 [`google-ai-generativelanguage`](https://googleapis.dev/python/generativelanguage/latest/) SDK。

    此次迁移带来了通过 Gemini 开发者 API 和 Vertex AI 中的 Gemini API 对 Gemini 模型的支持，取代了 `langchain-google-vertexai` 中的某些类，例如 `ChatVertexAI`。更多信息请参阅 [提供者文档](https://docs.langchain.com/oss/python/integrations/providers/google) 和 [发布说明](https://github.com/langchain-ai/langchain-google/discussions/1422)。

## 模块

!!! note "使用文档"
    关于如何使用每个模块的高级指南，请参阅 [文档](https://docs.langchain.com/oss/python/integrations/providers/google)。这些参考页面包含每个模块的自动生成的 API 文档，侧重于“是什么”而不是“如何”或“为什么”（即不包含端到端教程或概念概述）。

<div class="grid cards" markdown>

- :material-message-text:{ .lg .middle } __`ChatGoogleGenerativeAI`__

    ---

    Gemini 聊天模型。

    [:octicons-arrow-right-24: 参考](./ChatGoogleGenerativeAI.md)

- :material-message-text:{ .lg .middle } __`GoogleGenerativeAI`__

    ---

    （旧版）Google 文本补全抽象。

    [:octicons-arrow-right-24: 参考](./GoogleGenerativeAI.md)

- :fontawesome-solid-layer-group:{ .lg .middle } __`GoogleGenerativeAIEmbeddings`__

    ---

    Gemini 嵌入模型。

    [:octicons-arrow-right-24: 参考](./GoogleGenerativeAIEmbeddings.md)

</div>