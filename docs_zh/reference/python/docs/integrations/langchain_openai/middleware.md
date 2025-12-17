---
title: OpenAI 中间件
---

# :fontawesome-brands-openai:{ .lg .middle } OpenAI 中间件

!!! note "参考文档"

    本页面包含 OpenAI 中间件的**参考文档**。关于使用 OpenAI 中间件的概念指南、教程和示例，请参阅[文档](https://docs.langchain.com/oss/python/langchain/middleware/built-in#openai)。

针对 OpenAI 模型的特定提供商中间件：

| 类 | 描述 |
| ----- | ----------- |
| [`OpenAIModerationMiddleware`](#langchain_openai.middleware.OpenAIModerationMiddleware) | 使用 OpenAI 的审核端点来审核代理流量 |

<!-- TODO: `ignore_init_summary` 似乎不起作用。 -->

<!-- `"^__init__$"` 用于排除除 `__init__` 之外的所有内容 -->

::: langchain_openai.middleware.OpenAIModerationMiddleware
    options:
      docstring_options:
        ignore_init_summary: true
      merge_init_into_class: true
      filters: ["^__init__$"]

<!-- 为每个新条目复制并粘贴以上内容 -->
<!-- (不要使用 "members") -->