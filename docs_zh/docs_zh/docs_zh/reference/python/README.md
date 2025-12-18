# LangChain Python 参考文档

本目录包含 Python 参考文档站点的源代码和构建流程，该站点托管于 [`reference.langchain.com/python`](https://reference.langchain.com/python)。此站点为 LangChain、LangGraph、LangSmith 以及 LangChain 集成包（如 [`langchain-anthropic`](https://pypi.org/project/langchain-anthropic/)、[`langchain-openai`](https://pypi.org/project/langchain-openai/) 等）提供参考文档。

该站点使用 [MkDocs](https://www.mkdocs.org/) 构建，采用 [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) 主题，并使用 [mkdocstrings](https://mkdocstrings.github.io/) 插件从文档字符串生成 API 参考文档。所有配置选项请参见 [`mkdocs.yml`](./mkdocs.yml) 文件。

`docs/` 目录包含站点的 Markdown 文件，主入口点为 `index.md`。在构建时，每个文件中的存根（stubs）会被 `mkdocstrings` 生成的 API 参考文档替换。这使我们能够在 Markdown 中设计内容排序、布局等，同时仍能从源代码自动生成 API 参考文档。因此，要对 API 参考本身进行内容更改，你需要在源代码（例如文档字符串、类/方法名称等）中进行更改，然后重新构建站点。

---

## 贡献

由于这些文档是从源代码构建的，最好的贡献方式是在**源代码本身进行更改**。这包括：

-   改进文档字符串
-   添加缺失的文档字符串
-   修复拼写错误
-   等等。

你会注意到每个页面的顶部都有两个图标：一个用于查看页面源代码，另一个用于编辑页面。“查看源代码”图标会将你带到该页面的 Markdown 文件，而“编辑页面”图标会将你带到 GitHub 中相关的源代码文件。使用这些链接可以帮助你导航到正确的位置进行贡献。

---

## 在你的项目中交叉引用

如果你维护一个依赖 LangChain 或 LangGraph 的项目，并希望引用这些文档中的类、方法、函数等，你可以这样做！这些页面包含一个 `objects.inv` 文件，某些文档平台（如 MkDocs）可以使用它来自动创建指向这些文档的链接。

要在你的项目中引用这些文档，请将以下内容添加到你的 `mkdocs.yml` 文件中：

```yaml
mkdocstrings:
handlers:
    python:
    import:
        - https://reference.langchain.com/python/objects.inv
        - ... # 你想包含的任何其他清单
```

---

## 待办事项

此站点目前正在从之前基于 Sphinx 的实现迁移过来，因此仍有一些粗糙之处需要改进。以下是一些已知问题和潜在的改进方向：

-   [ ] [反向链接](https://mkdocstrings.github.io/python/usage/configuration/general/#backlinks)
-   [ ] [更多交叉引用](https://github.com/analog-garage/mkdocstrings-python-xref)
-   [ ] [现代化注解](https://mkdocstrings.github.io/python/usage/configuration/signatures/#modernize_annotations)
    -   [ ] ???
-   [ ] 考虑使用[继承的文档字符串](https://mkdocstrings.github.io/griffe/extensions/official/inherited-docstrings/)
-   [ ] 修复 TOC 阴影溢出（已在 `reference/python/docs/stylesheets/toc.css` 中开始处理）但效果不佳
-   [ ] 修复 `mkdocs.yml` 中 `navigation.path` 功能/插件不工作的问题
    -   [ ] ???
-   [ ] 使用源文件提交时间戳或 MkDocs 插件 [git-revision-date-localized](https://github.com/timvink/mkdocs-git-revision-date-localized-plugin) 为模块页面自动生成“模块最后更新”时间
-   [ ] 修复深色模式下搜索放大镜图标的颜色
-   [ ] [在搜索窗口中显示键盘快捷键](https://github.com/squidfunk/mkdocs-material/issues/2574#issuecomment-821979698) - 同时添加 cmd + k 以匹配 Mintlify

---

## 路径

对于位于 `langchain-ai/langchain` 单体仓库中的包，包的路径应存在于 `https://reference.langchain.com/python/{PACKAGE}/`，其中 `PACKAGE` 是在 `pyproject.toml` 文件中定义的包名，连字符替换为下划线。例如，`langchain-openai` 包的文档应位于 `https://reference.langchain.com/python/langchain_openai/`。

## 本地开发

### 设置

本项目支持两种安装模式：

1.  **开发模式** (`pyproject.dev.toml`) - 使用从克隆的仓库中进行的本地可编辑安装
2.  **生产模式** (`pyproject.toml`) - 直接使用 git 源

### 开发工作流

使用本地源代码进行本地开发：

```bash
# 1. 确保仓库按预期结构克隆（见下文）

# 2. 切换到开发模式并安装
make dev-install

# 3. 本地提供文档服务
make serve-docs

# 随时检查当前配置
make config-status
```

当你编辑本地仓库中的源代码时，更改将立即反映，因为包是以可编辑模式安装的。

**工作原理：** `make dev-install` 命令：

1.  将 `pyproject.toml` 切换为使用本地可编辑安装（通过 `switch-config.sh`）
2.  将生产配置备份到 `pyproject.prod.toml`
3.  使用 `uv sync` 从本地仓库安装所有包

### 生产/CI 工作流

用于生产构建或 CI：

```bash
# 切换到生产模式并安装
make prod-install

# 构建文档
make build
```

**工作原理：** `make prod-install` 命令：

1.  将 `pyproject.toml` 恢复为使用 git 源
2.  使用 `uv sync` 从 git 安装所有包

### 手动配置切换

你也可以直接使用脚本：

```bash
# 切换到开发模式
./switch-config.sh dev

# 切换到生产模式
./switch-config.sh prod

# 检查当前模式
./switch-config.sh status
```

### 必需的仓库结构

`pyproject.dev.toml` 文件期望仓库按以下结构克隆：

```txt
/某个父文件夹/
  ├── docs/                  # 此仓库
  │   └── reference/python/
  ├── langchain/             # 主 LangChain 单体仓库
  ├── langgraph/             # 主 LangGraph 单体仓库
  ├── langchain-community/
  ├── langchain-mcp-adapters/
  ├── langchain-datastax/
  ├── langchain-ai21/
  ├── langchain-aws/
  ├── langchain-azure/
  ├── langchain-cerebras/
  ├── langchain-cohere/
  ├── langchain-ibm/
  ├── langchain-elastic/
  ├── langchain-google/
  ├── langchain-milvus/
  ├── langchain-neo4j/
  ├── langchain-nvidia/
  ├── langchain-pinecone/
  ├── langchain-postgres/
  ├── langchain-redis/
  ├── langchain-sema4/
  ├── langchain-snowflake/
  ├── langchain-tavily/      # (外部组织)
  ├── langchain-together/
  ├── langchain-unstructured/
  ├── langchain-upstage/
  ├── langchain-weaviate/
  ├── langgraph-supervisor-py/
  └── langgraph-swarm-py/
```

`langchain-mongodb` 未包含在内，因为它由 MongoDB 团队单独维护和托管。

如果你只需要处理特定的包，可以在 `pyproject.dev.toml` 中注释掉其他包。

### 构建整个参考站点的子集

为了更快地开发和测试特定部分，可以使用 `serve_subset.py` 脚本仅提供部分文档：

```bash
# 仅提供 LangGraph 文档
python serve_subset.py langgraph

# 使用自定义端口
python serve_subset.py langgraph --port 8080

# 构建时不进行脏重载（干净构建）
python serve_subset.py langgraph --clean
```

---

## MkDocs/mkdocstrings Python 交叉引用链接语法

### 基本语法

mkdocstrings 中交叉引用的一般格式为：

```markdown
[显示文本][python.path.to.object]
```

如果你想使用对象名作为显示文本，请使用反引号：

```markdown
[`object_name`][python.path.to.object]
```

### 链接到不同的 Python 对象

#### 模块

```markdown
[`langchain.agents`][langchain.agents]

# 或者

[agents 模块][langchain.agents]
```

#### 类

```markdown
[`ChatOpenAI`][langchain_openai.ChatOpenAI]

# 或者

[ChatOpenAI 类][langchain_openai.ChatOpenAI]
```

#### 函数

```markdown
[`init_chat_model`][langchain.chat_models.init_chat_model]

# 或者

[初始化函数][langchain.chat_models.init_chat_model]
```

#### 方法

```markdown
[`invoke`][langchain_openai.ChatOpenAI.invoke]

# 或者

[invoke 方法][langchain_openai.ChatOpenAI.invoke]
```

#### 类属性

```markdown
[`temperature`][langchain_openai.ChatOpenAI.temperature]

# 或者

[temperature 属性][langchain_openai.ChatOpenAI.temperature]
```

#### 函数/方法参数

**注意：** 参数链接需要在 `mkdocstrings` 配置（在 `mkdocs.yml` 中）中启用 `parameter_headings` 选项。这会为每个参数生成永久链接和 TOC 条目，因此不要禁用它。

使用 `(parameter_name)` 语法链接到特定参数：

```markdown
[`model_provider`][langchain.chat_models.init_chat_model(model_provider)]

# 或者

[model_provider 参数][langchain.chat_models.init_chat_model(model_provider)]
```

对于方法参数：

```markdown
[`max_tokens`][langchain_openai.ChatOpenAI.invoke(max_tokens)]
```

对于类的 `__init__` 参数（当使用 `merge_init_into_class` 时）：

```markdown
[`temperature`][langchain_openai.ChatOpenAI(temperature)]
```

对于可变参数：

```markdown
[`*args`][package.module.function(*args)]
[`**kwargs`][package.module.function(**kwargs)]
```

#### 返回值

不能直接链接，但可以链接到返回类型类：

```markdown
返回一个 [`ChatResult`][langchain_core.outputs.ChatResult] 对象。
```

#### 嵌套类

```markdown
[`Config`][langchain_core.runnables.Runnable.Config]
```

### 高级模式

#### 在同一模块内链接

如果你在同一模块内编写文档，可以使用相对路径：

```markdown
另请参见 [`.other_method`][.other_method]
```

#### 链接到异常

```markdown
如果输入无效，则引发 [`ValueError`][ValueError]。
引发 [`CustomError`][my_package.exceptions.CustomError]。
```

#### 链接到类型别名

```markdown
[`RunnableConfig`][langchain_core.runnables.config.RunnableConfig]
```

#### 在参数文档中使用多个链接

```python
def create_agent(
    model: BaseChatModel,
    tools: Sequence[BaseTool],
) -> AgentExecutor:
    """
    创建一个代理执行器。

    Args:
        model: 一个 [`BaseChatModel`][langchain_core.language_models.BaseChatModel]
            实例。你可以使用 [`init_chat_model`][langchain.chat_models.init_chat_model]
            从字符串标识符初始化（参见
            [`model_provider`][langchain.chat_models.init_chat_model(model_provider)]
            参数以获取可用的提供者）。
        tools: 一个 [`BaseTool`][langchain_core.tools.BaseTool] 实例的序列。
            使用 [`@tool`][langchain_core.tools.tool] 装饰器来创建工具。

    Returns:
        一个 [`AgentExecutor`][langchain.agents.AgentExecutor] 实例。
    """
```

### 最佳实践

#### 1. 对代码标识符使用反引号

```markdown
✅ [`init_chat_model`][langchain.chat_models.init_chat_model]
❌ [init_chat_model][langchain.chat_models.init_chat_model]
```

#### 2. 为清晰起见使用完整路径

```markdown
✅ [`BaseChatModel`][langchain_core.language_models.BaseChatModel]
❌ [`BaseChatModel`][BaseChatModel]  # 可能无法正确解析
```

#### 3. 仅链接到公共 API

仅链接到用户应与之交互的公共、导出的 API。避免链接到内部实现细节（例如，以 `_` 为前缀的对象）。

#### 4. 对复杂引用使用描述性文本

```markdown
✅ 参见 [`model_provider`][langchain.chat_models.init_chat_model(model_provider)]
   参数以获取可用的提供者。
❌ 参见 [`model_provider`][langchain.chat_models.init_chat_model(model_provider)]。
```

#### 5. 验证链接是否正确构建

构建并手动检查生成的 HTML，以确保链接正确解析。

### 快速参考表

| 对象类型 | 语法 | 示例 |
|------------|--------|---------|
| 模块 | `[text][module.path]` | ``[`agents`][langchain.agents]`` |
| 类 | `[text][module.Class]` | ``[`ChatOpenAI`][langchain_openai.ChatOpenAI]`` |
| 函数 | `[text][module.function]` | ``[`init_chat_model`][langchain.chat_models.init_chat_model]`` |
| 方法 | `[text][module.Class.method]` | ``[`invoke`][langchain_openai.ChatOpenAI.invoke]`` |
| 属性 | `[text][module.Class.attr]` | ``[`temperature`][langchain_openai.ChatOpenAI.temperature]`` |
| 函数参数 | `[text][module.function(param)]` | ``[`model_provider`][langchain.chat_models.init_chat_model(model_provider)]`` |
| 方法参数 | `[text][module.Class.method(param)]` | ``[`max_tokens`][langchain_openai.ChatOpenAI.invoke(max_tokens)]`` |
| 类参数 | `[text][module.Class(param)]` | ``[`temperature`][langchain_openai.ChatOpenAI(temperature)]`` |

### 测试链接

要测试链接是否有效：

1.  检查对象是否在 `__init__.py` 的导出中
2.  验证导入路径：`from module.path import Object`
3.  使用 `--strict` 模式构建文档
4.  检查生成的 HTML 中是否有损坏的链接

```bash
mkdocs build --strict
mkdocs serve  # 在 http://127.0.0.1:8000/ 预览
```

此语法适用于使用 Python 处理程序的 MkDocs `mkdocstrings` 插件。根据你的包结构和导出调整路径。

---

## 页面标题：导航、Frontmatter 和 H1 标题

MkDocs 使用多个来源的页面标题，每个来源服务于不同的目的。以下是理解它们如何交互的方法：

### 三种标题类型

#### 1. 导航标题（在 `mkdocs.yml` 中）

在 `mkdocs.yml` 的 `nav` 部分定义：

```yaml
nav:
  - Deployment:
    - SDK: langsmith/deployment/sdk.md
```

-   **目的**：侧边栏导航中的标签
-   **用法**：模板中的 `page.title`（见下文）
-   **范围**：导航菜单

#### 2. Frontmatter 标题（在 `.md` 文件中）

在每个 Markdown 文件顶部的 YAML frontmatter 中定义：

```markdown
---
title: LangSmith Deployment SDK
---
```

-   **目的**：SEO 元数据，HTML `<title>` 标签
-   **用法**：模板中的 `page.meta.title`（见下文）
-   **范围**：浏览器标签页、搜索引擎、社交分享

#### 3. H1 标题（在 `.md` 文件中）

Markdown 内容中的第一个 `#` 标题：

```markdown
# LangSmith Deployment SDK reference
```

-   **目的**：用户可见的页面标题
-   **用法**：在页面内容中渲染为 `<h1>`！
-   **范围**：主页面内容区域

### 它们如何交互

以 `langsmith/deployment/sdk.md` 文件为例：

```yaml
# 在 mkdocs.yml 中
nav:
  - Deployment:
    - SDK: langsmith/deployment/sdk.md
```

```markdown
# 在 langsmith/deployment/sdk.md 中
---
title: LangSmith Deployment SDK
---

# LangSmith Deployment SDK reference
```

**结果：**

-   **导航侧边栏**：显示 "SDK"（来自 nav）
-   **浏览器标签页/HTML `<title>`**：显示 "LangSmith Deployment SDK | LangChain Reference"（来自 frontmatter + 站点名称）
-   **页面标题**：显示 "LangSmith Deployment SDK reference"（来自 H1）

### HTML `<title>` 标签优先级

HTML `<title>` 标签（出现在浏览器标签页中的内容）在 `overrides/main.html` 中遵循以下优先级系统：

1.  **如果 `page.meta.title` 存在**（来自 YAML frontmatter）：
2.
    ```html
    <title>{{ page.meta.title }} | {{ config.site_name }}</title>
    ```
    示例：`LangSmith Deployment SDK | LangChain Reference`

3.  **否则，如果 `page.title` 存在**（来自导航或从文件名推断）：
4.
    ```html
    <title>{{ page.title | striptags }} | {{ config.site_name }}</title>
    ```
    示例：`SDK | LangChain Reference`

5.  **否则**（主页回退