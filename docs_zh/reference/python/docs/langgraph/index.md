---
title: LangGraph 概述
hide:
  - toc
---

[![PyPI - 版本](https://img.shields.io/pypi/v/langgraph?label=%20)](https://pypi.org/project/langgraph/#history)
[![PyPI - 许可证](https://img.shields.io/pypi/l/langgraph)](https://opensource.org/licenses/MIT)
[![PyPI - 下载量](https://img.shields.io/pepy/dt/langgraph)](https://pypistats.org/packages/langgraph)

欢迎来到 LangGraph 参考文档！

这些页面详细介绍了使用 LangGraph 构建应用时会用到的核心接口。每个部分涵盖了生态系统的不同组成部分。

## :simple-langgraph:{ .lg .middle } `langgraph`

LangGraph 开源库的核心 API。

- [图](graphs.md)：主图抽象与使用。
- [函数式 API](func.md)：图的函数式编程接口。
- [Pregel](pregel.md)：受 Pregel 启发的计算模型。
- [检查点](checkpoints.md)：保存与恢复图状态。
- [存储](store.md)：存储后端与选项。
- [缓存](cache.md)：性能缓存机制。
- [类型](types.md)：图组件的类型定义。
- [运行时](runtime.md)：运行时配置与选项。
- [配置](config.md)：配置选项。
- [错误](errors.md)：错误类型与处理。
- [常量](constants.md)：全局常量。
- [通道](channels.md)：消息传递与通道。

!!! tip "模型上下文协议 (MCP) 支持"

    要在 LangGraph 应用中使用 MCP 工具，请查看 [`langchain-mcp-adapters`](../langchain_mcp_adapters/index.md)。

## :material-package-check:{ .lg .middle } 预构建组件

针对常见工作流、智能体及其他模式的高级抽象。

- [智能体](agents.md)：内置智能体模式。
- [监督器](supervisor.md)：编排与委派。
- [集群](swarm.md)：多智能体协作。