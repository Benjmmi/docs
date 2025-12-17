# :material-account-supervisor:{ .lg .middle } `langgraph-supervisor`

[![PyPI - 版本](https://img.shields.io/pypi/v/langgraph-supervisor?label=%20)](https://pypi.org/project/langgraph-supervisor/#history)
[![PyPI - 许可证](https://img.shields.io/pypi/l/langgraph-supervisor)](https://opensource.org/licenses/MIT)
[![PyPI - 下载量](https://img.shields.io/pepy/dt/langgraph-supervisor)](https://pypistats.org/packages/langgraph-supervisor)

!!! note

    目前我们建议在大多数使用场景中**直接通过工具使用监督者模式**，而非使用此库。工具调用方式能让你更好地控制上下文工程，这也是 [LangChain 多智能体指南](https://docs.langchain.com/oss/python/langchain/multi-agent)中推荐的模式。

    请参阅我们的[监督者教程](https://docs.langchain.com/oss/python/langchain/supervisor)获取逐步指导。

    我们正在将此库适配 LangChain 1.0 以帮助用户升级现有代码。如果你发现此库能解决手动监督者模式难以处理的问题，我们很乐意了解你的使用场景！

更多详情请参阅[项目描述](https://pypi.org/project/langgraph-supervisor/)。

::: langgraph_supervisor.supervisor
    options:
      members:
        - create_supervisor

::: langgraph_supervisor.handoff
    options:
      members:
        - create_handoff_tool
        - create_forward_message_tool