---
title: LangChain Core 主页
---

# :material-atom:{ .lg .middle } `langchain-core`

[![PyPI - 版本](https://img.shields.io/pypi/v/langchain-core?label=%20)](https://pypi.org/project/langchain-core/#history)
[![PyPI - 许可证](https://img.shields.io/pypi/l/langchain-core)](https://opensource.org/licenses/MIT)
[![PyPI - 下载量](https://img.shields.io/pepy/dt/langchain-core)](https://pypistats.org/packages/langchain-core)

[`langchain-core`](https://pypi.org/project/langchain-core/) 包的参考文档。

`langchain-core` 包含了 LangChain 生态系统中使用的核心接口与抽象。大多数用户主要会与主包 [`langchain`](../langchain/langchain/index.md) 交互，该包构建在 `langchain-core` 之上，并为所有核心接口提供了具体实现。

- [缓存](caches.md): 缓存机制。
- [回调](callbacks.md): 回调处理器与管理。
- [文档](documents.md): 文档抽象。
- [嵌入](embeddings.md): 嵌入抽象。
- [异常](exceptions.md): 常见的 LangChain 异常类型。
- [语言模型](language_models.md): 语言模型的基础接口。
- [序列化](load.md): 序列化与反序列化组件。
- [输出解析器](output_parsers.md): 解析模型输出。
- [提示](prompts.md): 提示模板及相关工具。
- [速率限制器](rate_limiters.md): 速率限制工具。
- [检索器](retrievers.md): 检索器接口与实现。
- [可运行对象](runnables.md): 可运行对象及相关抽象。
- [工具](utils.md): 各种实用函数和类。
- [向量存储](vectorstores.md): 向量存储接口与实现。