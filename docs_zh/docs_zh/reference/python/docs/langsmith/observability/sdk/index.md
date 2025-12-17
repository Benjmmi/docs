---
title: LangSmith SDK
---

[![PyPI - 版本](https://img.shields.io/pypi/v/langsmith?label=%20)](https://pypi.org/project/langsmith/#history)
[![PyPI - 许可证](https://img.shields.io/pypi/l/langsmith)](https://opensource.org/licenses/MIT)
[![PyPI - 下载量](https://img.shields.io/pepy/dt/langsmith)](https://pypistats.org/packages/langsmith)

欢迎查阅 LangSmith Python SDK 参考文档！这些页面详细介绍了在使用 LangSmith 的观测与评估工具进行开发时所需的核心接口。

如需用户指南、教程和概念概述，请访问 [LangSmith 文档](https://docs.langchain.com/langsmith/home)。

## 快速参考

| 类/函数 | 描述 |
| :- | :- |
| [`Client`](client.md) | 用于与 LangSmith API 交互的同步客户端。 |
| [`AsyncClient`](async_client.md) | 用于与 LangSmith API 交互的异步客户端。 |
| [`traceable`](run_helpers.md) | 用于追踪任意函数的包装器/装饰器。 |
| [`@pytest.mark.langsmith`](testing.md) | LangSmith 的 `pytest` 集成。 |
| [`wrap_openai`](wrappers.md) | OpenAI 客户端的包装器，添加 LangSmith 追踪功能。 |
| [`wrap_anthropic`](wrappers.md) | Anthropic 客户端的包装器，添加 LangSmith 追踪功能。 |

## 核心 API

LangSmith SDK 的主要接口。

- [`Client`](client.md): LangSmith API 的同步客户端。
- [`AsyncClient`](async_client.md): LangSmith API 的异步客户端。
- [运行辅助工具](run_helpers.md): 如 `traceable`、`trace` 及追踪上下文管理等函数。
- [运行树](run_trees.md): 用于表示运行及嵌套运行的树形结构。
- [评估](evaluation.md): 用于在数据集上评估函数和模型的工具。

## 附加 API

- [模式定义](schemas.md): 数据模式与类型定义。
- [实用工具](utils.md): 实用类，包括错误类型和线程池执行器。
- [包装器](wrappers.md): 为流行 LLM 提供商提供的追踪包装器。
- [匿名化工具](anonymizer.md): 用于匿名化敏感数据的工具。
- [测试](testing.md): 测试工具及 pytest 集成。
- [期望 API](expect.md): 用于测试的断言与期望功能。