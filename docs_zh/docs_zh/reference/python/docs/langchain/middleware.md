!!! note "参考文档"

    本页面包含中间件的**参考文档**。关于使用中间件的概念指南、教程和示例，请参阅[文档](https://docs.langchain.com/oss/python/langchain/middleware)。

## 中间件类

LangChain 为常见智能体用例提供了预构建的中间件：

| 类 | 描述 |
| ----- | ----------- |
| [`SummarizationMiddleware`](#langchain.agents.middleware.SummarizationMiddleware) | 在接近令牌限制时自动总结对话历史 |
| [`HumanInTheLoopMiddleware`](#langchain.agents.middleware.HumanInTheLoopMiddleware) | 暂停执行以等待人工批准工具调用 |
| [`ModelCallLimitMiddleware`](#langchain.agents.middleware.ModelCallLimitMiddleware) | 限制模型调用次数以防止过高成本 |
| [`ToolCallLimitMiddleware`](#langchain.agents.middleware.ToolCallLimitMiddleware) | 通过限制调用次数来控制工具执行 |
| [`ModelFallbackMiddleware`](#langchain.agents.middleware.ModelFallbackMiddleware) | 主模型失败时自动回退到替代模型 |
| [`PIIMiddleware`](#langchain.agents.middleware.PIIMiddleware) | 检测和处理个人身份信息 |
| [`TodoListMiddleware`](#langchain.agents.middleware.TodoListMiddleware) | 为智能体配备任务规划与跟踪能力 |
| [`LLMToolSelectorMiddleware`](#langchain.agents.middleware.LLMToolSelectorMiddleware) | 在调用主模型前使用 LLM 选择相关工具 |
| [`ToolRetryMiddleware`](#langchain.agents.middleware.ToolRetryMiddleware) | 以指数退避方式自动重试失败的工具调用 |
| [`LLMToolEmulator`](#langchain.agents.middleware.LLMToolEmulator) | 使用 LLM 模拟工具执行以用于测试目的 |
| [`ContextEditingMiddleware`](#langchain.agents.middleware.ContextEditingMiddleware) | 通过修剪或清除工具使用记录来管理对话上下文 |
| [`ShellToolMiddleware`](#langchain.agents.middleware.ShellToolMiddleware) | 为智能体提供持久化 shell 会话以执行命令 |
| [`FilesystemFileSearchMiddleware`](#langchain.agents.middleware.FilesystemFileSearchMiddleware) | 提供基于文件系统的 Glob 和 Grep 搜索工具 |
| [`AgentMiddleware`](#langchain.agents.middleware.AgentMiddleware) | 用于创建自定义中间件的基类 |

## 装饰器

使用以下装饰器创建自定义中间件：

| 装饰器 | 描述 |
| --------- | ----------- |
| [`@before_agent`](#langchain.agents.middleware.before_agent) | 在智能体执行开始前执行逻辑 |
| [`@before_model`](#langchain.agents.middleware.before_model) | 在每次模型调用前执行逻辑 |
| [`@after_model`](#langchain.agents.middleware.after_model) | 在每次模型收到响应后执行逻辑 |
| [`@after_agent`](#langchain.agents.middleware.after_agent) | 在智能体执行完成后执行逻辑 |
| [`@wrap_model_call`](#langchain.agents.middleware.wrap_model_call) | 包装并拦截模型调用 |
| [`@wrap_tool_call`](#langchain.agents.middleware.wrap_tool_call) | 包装并拦截工具调用 |
| [`@dynamic_prompt`](#langchain.agents.middleware.dynamic_prompt) | 基于请求上下文生成动态系统提示 |
| [`@hook_config`](#langchain.agents.middleware.hook_config) | 配置钩子行为（例如条件路由） |

## 类型与工具

构建中间件的核心类型：

| 类型 | 描述 |
| ---- | ----------- |
| [`AgentState`](#langchain.agents.middleware.AgentState) | 智能体执行的状态容器 |
| [`ModelRequest`](#langchain.agents.middleware.ModelRequest) | 传递给模型调用的请求详情 |
| [`ModelResponse`](#langchain.agents.middleware.ModelResponse) | 模型调用的响应详情 |
| [`ClearToolUsesEdit`](#langchain.agents.middleware.ClearToolUsesEdit) | 用于从上下文中清除工具使用历史的工具 |
| [`InterruptOnConfig`](#langchain.agents.middleware.InterruptOnConfig) | 人机交互中断的配置 |

[`SummarizationMiddleware`](#langchain.agents.middleware.SummarizationMiddleware) 类型：

| 类型 | 描述 |
| ---- | ----------- |
| [`ContextSize`](#langchain.agents.middleware.summarization.ContextSize) | 联合类型 |
| [`ContextFraction`](#langchain.agents.middleware.summarization.ContextFraction) | 在总上下文的指定比例处进行总结 |
| [`ContextTokens`](#langchain.agents.middleware.summarization.ContextTokens) | 在令牌阈值处进行总结 |
| [`ContextMessages`](#langchain.agents.middleware.summarization.ContextMessages) | 在消息阈值处进行总结 |

<!-- TODO: `ignore_init_summary` 似乎不起作用。  -->

::: langchain.agents.middleware.SummarizationMiddleware
    options:
      docstring_options:
        ignore_init_summary: true
      merge_init_into_class: true
      filters: ["^__init__$"]

::: langchain.agents.middleware.HumanInTheLoopMiddleware
    options:
      docstring_options:
        ignore_init_summary: true
      merge_init_into_class: true
      filters: ["^__init__$"]

::: langchain.agents.middleware.ModelCallLimitMiddleware
    options:
      docstring_options:
        ignore_init_summary: true
      merge_init_into_class: true
      filters: ["^(__init__|state_schema)$"]

::: langchain.agents.middleware.ToolCallLimitMiddleware
    options:
      docstring_options:
        ignore_init_summary: true
      merge_init_into_class: true
      filters: ["^(__init__|state_schema)$"]

::: langchain.agents.middleware.ModelFallbackMiddleware
    options:
      docstring_options:
        ignore_init_summary: true
      merge_init_into_class: true
      filters: ["^__init__$"]

::: langchain.agents.middleware.PIIMiddleware
    options:
      docstring_options:
        ignore_init_summary: true
      merge_init_into_class: true
      filters: ["^__init__$"]

::: langchain.agents.middleware.TodoListMiddleware
    options:
      docstring_options:
        ignore_init_summary: true
      merge_init_into_class: true
      filters: ["^(__init__|state_schema)$"]

::: langchain.agents.middleware.LLMToolSelectorMiddleware
    options:
      docstring_options:
        ignore_init_summary: true
      merge_init_into_class: true
      filters: ["^__init__$"]

::: langchain.agents.middleware.ToolRetryMiddleware
    options:
      docstring_options:
        ignore_init_summary: true
      merge_init_into_class: true
      filters: ["^__init__$"]

::: langchain.agents.middleware.LLMToolEmulator
    options:
      docstring_options:
        ignore_init_summary: true
      merge_init_into_class: true
      filters: ["^__init__$"]

::: langchain.agents.middleware.ContextEditingMiddleware
    options:
      docstring_options:
        ignore_init_summary: true
      merge_init_into_class: true
      filters: ["^__init__$"]

::: langchain.agents.middleware.ShellToolMiddleware
    options:
      docstring_options:
        ignore_init_summary: true
      merge_init_into_class: true
      filters: ["^__init__$"]

::: langchain.agents.middleware.FilesystemFileSearchMiddleware
    options:
      docstring_options:
        ignore_init_summary: true
      merge_init_into_class: true
      filters: ["^__init__$"]

::: langchain.agents.middleware.AgentMiddleware
    options:
      docstring_options:
        ignore_init_summary: true
      merge_init_into_class: true
      filters: ["^__init__$"]

::: langchain.agents.middleware.before_agent

::: langchain.agents.middleware.before_model

::: langchain.agents.middleware.after_model

::: langchain.agents.middleware.after_agent

::: langchain.agents.middleware.wrap_model_call

::: langchain.agents.middleware.wrap_tool_call

::: langchain.agents.middleware.dynamic_prompt

::: langchain.agents.middleware.hook_config

::: langchain.agents.middleware.AgentState
    options:
      merge_init_into_class: true

::: langchain.agents.middleware.ModelRequest
    options:
      merge_init_into_class: true

::: langchain.agents.middleware.ModelResponse
    options:
      merge_init_into_class: true

::: langchain.agents.middleware.ClearToolUsesEdit
    options:
      merge_init_into_class: true

::: langchain.agents.middleware.InterruptOnConfig
    options:
      merge_init_into_class: true

<!-- 总结类型 -->

::: langchain.agents.middleware.summarization.ContextSize
::: langchain.agents.middleware.summarization.ContextFraction
::: langchain.agents.middleware.summarization.ContextTokens
::: langchain.agents.middleware.summarization.ContextMessages

<!-- 为每个新条目复制并粘贴上述内容 -->
<!-- （不要使用 "members"） -->