---
title: Anthropic 中间件
---

# :simple-claude:{ .lg .middle } Anthropic 中间件

!!! note "参考文档"

    本页面包含 Anthropic 中间件的**参考文档**。关于使用 Anthropic 中间件的概念指南、教程和示例，请参阅[官方文档](https://docs.langchain.com/oss/python/langchain/middleware/built-in#anthropic)。

针对 Anthropic Claude 模型的特定提供商中间件：

| 类 | 描述 |
| ----- | ----------- |
| [`AnthropicPromptCachingMiddleware`](#langchain_anthropic.middleware.AnthropicPromptCachingMiddleware) | 通过缓存重复的提示前缀来降低成本 |
| [`ClaudeBashToolMiddleware`](#langchain_anthropic.middleware.ClaudeBashToolMiddleware) | 通过本地命令执行 Claude 原生 bash 工具 |
| [`StateClaudeTextEditorMiddleware`](#langchain_anthropic.middleware.StateClaudeTextEditorMiddleware) | 为基于状态的文件编辑提供 Claude 文本编辑器工具 |
| [`FilesystemClaudeTextEditorMiddleware`](#langchain_anthropic.middleware.FilesystemClaudeTextEditorMiddleware) | 为基于文件系统的文件编辑提供 Claude 文本编辑器工具 |
| [`StateClaudeMemoryMiddleware`](#langchain_anthropic.middleware.StateClaudeMemoryMiddleware) | 为基于状态的持久化智能体记忆提供 Claude 记忆工具 |
| [`FilesystemClaudeMemoryMiddleware`](#langchain_anthropic.middleware.FilesystemClaudeMemoryMiddleware) | 为基于文件系统的持久化智能体记忆提供 Claude 记忆工具 |
| [`StateFileSearchMiddleware`](#langchain_anthropic.middleware.StateFileSearchMiddleware) | 为基于状态的文件系统提供搜索工具 |

<!-- TODO: `ignore_init_summary` 似乎不起作用。 -->

<!-- `"^__init__$"` 用于排除 `__init__` 之外的所有内容 -->

::: langchain_anthropic.middleware.AnthropicPromptCachingMiddleware
    options:
      docstring_options:
        ignore_init_summary: true
      merge_init_into_class: true
      filters: ["^__init__$"]

::: langchain_anthropic.middleware.ClaudeBashToolMiddleware
    options:
      docstring_options:
        ignore_init_summary: true
      merge_init_into_class: true
      filters: ["^__init__$"]

::: langchain_anthropic.middleware.StateClaudeTextEditorMiddleware
    options:
      docstring_options:
        ignore_init_summary: true
      merge_init_into_class: true
      filters: ["^__init__$"]

::: langchain_anthropic.middleware.FilesystemClaudeTextEditorMiddleware
    options:
      docstring_options:
        ignore_init_summary: true
      merge_init_into_class: true
      filters: ["^__init__$"]

::: langchain_anthropic.middleware.StateClaudeMemoryMiddleware
    options:
      docstring_options:
        ignore_init_summary: true
      merge_init_into_class: true
      filters: ["^__init__$"]

::: langchain_anthropic.middleware.FilesystemClaudeMemoryMiddleware
    options:
      docstring_options:
        ignore_init_summary: true
      merge_init_into_class: true
      filters: ["^__init__$"]

::: langchain_anthropic.middleware.StateFileSearchMiddleware
    options:
      docstring_options:
        ignore_init_summary: true
      merge_init_into_class: true
      filters: ["^__init__$"]

<!-- 为每个新条目复制并粘贴上述内容 -->
<!-- (不要使用 "members") -->