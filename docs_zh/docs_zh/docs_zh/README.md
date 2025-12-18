# LangChain 文档

🦜 **欢迎！** 本仓库包含 LangChain 项目的文档构建流水线。

* 🏠 [`docs.langchain.com`](https://docs.langchain.com) 是我们的文档主页，集中了 LangChain、LangGraph、LangSmith 和 LangChain Labs（Deep Agents、Open SWE、Open Agent Platform）的文档。该站点托管在 [Mintlify](https://mintlify.com) 上。
* 🛠️ `reference.langchain.com` 是 LangChain、LangGraph、LangSmith 和 LangChain 集成包（例如 [`langchain-anthropic`](https://pypi.org/project/langchain-anthropic/)、[`langchain-openai`](https://pypi.org/project/langchain-openai/)）的 API 参考文档主页。这些是从源代码构建并部署到 [Vercel](https://vercel.com) 的静态站点。
  * [`Python 参考`](https://reference.langchain.com/python/)
  * [`JavaScript/TypeScript 参考`](https://reference.langchain.com/javascript/)

---

**目录：**

- [LangChain 文档](#langchain-文档)
  - [贡献](#贡献)
  - [参考](#参考)
    - [仓库结构](#仓库结构)
      - [`docs.langchain.com`](#docslangchaincom)
      - [`reference.langchain.com`](#referencelangchaincom)
    - [文件格式](#文件格式)
    - [可用命令](#可用命令)
  - [故障排除](#故障排除)
    - [`docs dev` 无法工作/运行](#docs-dev-无法工作运行)
    - [Mintlify `.venv` 解析错误](#mintlify-venv-解析错误)
    - [警告：页面不存在](#警告页面不存在)
    - [一般 Mintlify 错误](#一般-mintlify-错误)

---

## 贡献

要为 LangChain 文档做出贡献，请遵循[贡献指南](https://docs.langchain.com/oss/python/contributing/overview)中概述的步骤。该指南还解释了我们的文档类型及其编写和质量标准。

有关设置开发环境和贡献文档的详细信息，请参阅[文档贡献指南](https://docs.langchain.com/oss/python/contributing/documentation)。

> [!重要]
> 关于贡献参考文档，请参阅 `/reference/python` 和 `/reference/javascript` 目录中的 `README.md` 文件。

## 参考

### 仓库结构

```text
# --- docs.langchain.com ----------------------------------------------
build/                    # 构建的文档（请勿编辑）
pipeline/                 # 构建流水线源代码
scripts/                  # 辅助脚本
src/                      # 源文档文件（< 在此编辑内容）
    langsmith/            # LangSmith 文档
    oss/                  # LangChain、LangGraph、Deep Agents 和集成文档
    docs.json             # Mintlify 站点配置和导航
tests/                    # 流水线的测试文件
Makefile                  # 构建目标
pyproject.toml            # 依赖项

# --- reference.langchain.com -----------------------------------------
reference/                # 参考文档构建流水线
    dist/                 # 构建的文档（请勿编辑）
    javascript/           # JS/TS 参考构建流水线
    python/               # Python 参考构建流水线和源代码
    package.json          # Vercel 命令和依赖项
    vercel.json           # Vercel 配置/重定向
```

#### `docs.langchain.com`

Mintlify 文档流水线的结构是：`.mdx` 源文件位于 `/src` 中，构建产物位于 `/build` 中。Mintlify 从 `/build` 文件夹部署，该文件夹由预处理逻辑生成。

> [!重要]
> 切勿直接编辑 `/build`。

`/src/docs.json` 文件用于配置 Mintlify 站点导航和设置。有关详细语法和组件用法，请参阅 [Mintlify 文档](https://www.mintlify.com/docs/organize/navigation)。

文档更改遵循 PR 工作流程，所有测试必须在合并前通过。更多详情请参阅[贡献指南](/oss/contributing/documentation)。

#### `reference.langchain.com`

每种语言在 `/reference/<language>` 中都有自己的构建流水线。参考文档通过自动文档字符串提取和手动编写内容相结合的方式构建。有关如何构建和贡献的详细信息，请参阅每个文件夹中的 `README.md`。

构建的文件存储在 `/reference/dist/{LANGUAGE}` 中，然后部署到 Vercel。构建过程在推送到 `main` 分支时自动触发，也可以通过 Vercel 仪表板手动触发。

### 文件格式

* **Markdown 文件** (`.md`, `.mdx`) - 标准文档内容
* **代码片段** (`src/snippets/`) - 可重用的 MDX 内容，可以导入到多个页面中。**重要提示：** 代码片段经过特殊的链接预处理。在代码片段中编写链接时，请注意路径段。
* **Jupyter 笔记本** (`.ipynb`) - 在构建过程中转换为 markdown，但**不建议用于新内容！** 除非维护者要求，否则如果您尝试添加 Jupyter 笔记本，您的 PR 很可能会被拒绝。
* **资源文件** - 图像和其他文件被复制到构建目录

### 可用命令

**Make 命令：**

* `make dev` - 启动开发模式，包含文件监视和实时重建
* `make build` - 将文档构建到 `./build` 目录
* `make mint-broken-links` - 检查构建文档中的损坏链接（不包括集成）
* `make mint-broken-links-all` - 检查构建文档中的损坏链接（包括所有目录）
* `make build-references` - 构建参考文档
* `make preview-references` - 使用 vercel 预览参考文档
* `make install` - 安装所有依赖项
* `make clean` - 删除构建产物
* `make test` - 运行测试套件
* `make lint` - 检查代码风格和格式
* `make format` - 自动格式化代码
* `make lint_md` - 对 markdown 文件进行 lint 检查
* `make lint_md_fix` - 对 markdown 文件进行 lint 检查和修复
* `make help` - 显示所有可用命令

**`docs` CLI 工具：**

`docs` 命令（安装为 `uv run docs`）提供附加功能：

* **`docs migrate <path>`** - 将 MkDocs markdown/笔记本文件转换为 Mintlify 格式
  * `--dry-run` - 预览更改而不写入文件
  * `--output <path>` - 指定输出位置（默认：原地）
  * 支持 `.md`、`.markdown`、`.ipynb` 文件

* **`docs migrate-docusaurus <path>`** - 将 Docusaurus markdown/笔记本文件转换为 Mintlify 格式
  * `--dry-run` - 预览更改而不写入文件
  * `--output <path>` - 指定输出位置（默认：原地）
  * 支持 `.md`、`.markdown`、`.mdx`、`.ipynb` 文件
  * 转换 Docusaurus 特定语法（提示框、标签页、导入等）

* **`docs mv <old_path> <new_path>`** - 移动文件并更新交叉引用
  * `--dry-run` - 预览更改而不移动文件

这些可以通过 `Makefile` 直接使用，也可以通过 `docs` CLI 工具使用：

* **`docs dev`** - 启动开发模式，包含文件监视和热重载
  * 自动将 `src/` 中更改的文件重建到 `build/`
  * 在 <http://localhost:3000> 启动 Mintlify 开发服务器
  * 文件更改时提供自动浏览器刷新
  * `--skip-build` - 跳过初始构建并使用现有构建目录

* **`docs build`** - 构建文档文件
  * `--watch` - 构建后监视文件更改

## 故障排除

### `docs dev` 无法工作/运行

重新执行[设置本地开发环境的步骤](#set-up-a-local-dev-environment)，确保您已激活虚拟环境并安装了所有依赖项。

### Mintlify `.venv` 解析错误

**问题**：从项目根目录运行 `mint broken-links` 或其他 Mintlify 命令会导致解析错误，例如：

```txt
无法解析 .venv/lib/python3.13/site-packages/soupsieve-2.7.dist-info/licenses/LICENSE.md
- 3:48: 名称中出现意外字符 '@' (U+0040)
```

**根本原因**：Mintlify 尝试解析目录中的所有文件，包括包含无效 MDX 语法的 Python 虚拟环境文件。

**解决方案**（按偏好顺序）：

1. **使用安全的 Make 命令**（推荐）：

   ```bash
   make mint-broken-links  # 先构建文档，然后检查链接（不包括集成）
   ```

2. **从构建目录运行 Mintlify 命令**：

   ```bash
   cd build               # 切换到构建目录，最终文档在此
   mint broken-links      # 现在可以安全运行
   ```

**为什么有效**：该解决方案确保 Mintlify 命令从 `build/` 目录运行，最终文档在此生成，这是检查损坏链接的正确位置。这避免了扫描项目根目录中的 Python 虚拟环境。

**预防措施**：始终使用提供的 Make 命令，而不是从项目根目录运行原始的 `mint` 命令。

### 警告：页面不存在

如果添加新组，请确保根 `index.mdx` 包含在 `pages` 数组中，例如：

```json
{
  "group": "新组",
  "pages": ["new-group/index", "new-group/other-page"]
}
```

如果省略了尾随的 `/index`（不包含扩展名），即使站点仍能构建，Mintlify 解析器也会发出警告。

### 一般 Mintlify 错误

在某些情况下，我们使用仅在最新 Mintlify CLI 中可用的新功能。如果遇到错误，请确保安装了最新版本：

```bash
mint update

# 或

npm install -g mint
```