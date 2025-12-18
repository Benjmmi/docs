# LangChain 统一文档概述

本仓库包含 LangChain 产品与服务的完整文档，托管于 Mintlify 平台。文档按产品划分为不同章节。这是一套共享的指导原则，旨在确保所有内容的一致性与质量。

## 适用范围

**本指南仅适用于手动编写的文档，不适用于以下内容：**

- `**/reference/**` 目录中的文件（自动生成的 API 参考文档）
- 构建产物和生成文件

关于参考文档，请参阅 `.github/instructions/reference-docs.instructions.md`。

## 协作原则

- 你可以对想法提出质疑——这有助于产出更好的文档。提出质疑时请引用来源并说明理由
- **始终**请求澄清，而非自行假设
- **绝不**撒谎、猜测或编造信息

## 项目背景

- 格式：使用 YAML frontmatter 的 MDX 文件，遵循 Mintlify 语法
- 配置：docs.json 用于导航、主题和设置
- 组件：Mintlify 组件

## 内容策略

- 文档内容以用户成功为目标——不多不少，恰到好处
- 优先保证信息的准确性和可用性
- 尽可能保持内容的长期有效性
- 添加新内容前先搜索现有信息。避免重复，除非出于战略考虑。尽可能引用现有内容
- 检查现有模式以保持一致性
- 从最合理的微小改动开始

## docs.json

- 构建 docs.json 文件和站点导航时，请参考 [docs.json 模式](https://mintlify.com/docs.json)
- 若添加新分组，请确保根目录 `index.mdx` 包含在 `pages` 数组中，例如：

```json
{
  "group": "新分组",
  "pages": ["new-group/index", "new-group/other-page"]
}
```

如果省略末尾的 `/index`（不包含扩展名），Mintlify 解析器会发出警告，但站点仍能正常构建。

## 页面 Frontmatter 要求

- title：清晰、描述性强、简洁的页面标题
- description：用于 SEO/导航的简洁摘要

## 自定义代码语言标记

我们为 Python 和 JavaScript/TypeScript 实现了自定义代码语言标记。这些标记用于标识特定于该语言的内容。使用 `:::python` 或 `:::js` 来标记特定语言的内容。两者均以 `:::` 标记结束。

如果代码页面存在此类标记，则会生成两个输出（每种语言一个）。例如，如果 `/concepts/foo.mdx` 页面中包含此语法，则会创建两个页面：`/python/concepts/foo.mdx` 和 `/javascript/concepts/foo.mdx`。

有关实现细节，请参阅 `pipeline/preprocessors/markdown_preprocessor.py`。

## 代码片段

`src/snippets/` 中的片段文件是可重用的 MDX 内容，可导入多个页面。这些片段在构建过程中会经过特殊的链接预处理，将绝对路径 `/oss/` 链接转换为相对路径。

**重要提示：** 在片段中编写链接时，请注意路径结构。请阅读 `pipeline/core/builder.py` 中 `_process_snippet_markdown_file` 方法（第 807-872 行）的文档字符串和注释，以了解片段链接预处理的工作原理以及为何需要特定的路径结构。

## 风格指南

总体上遵循 [Google 开发者文档风格指南](https://developers.google.com/style)。您也可以通过 [Vale 兼容实现](https://github.com/errata-ai/Google) 访问此风格指南。

- 使用第二人称（“你”）
- 操作指南开头列出先决条件
- 发布前测试所有代码示例
- 与现有页面的风格和格式保持一致
- 包含基础与高级使用案例
- 所有代码块添加语言标签
- 所有图片添加替代文本
- 内部链接使用根相对路径
- 拼写正确
- 语法正确
- 标题使用句子大小写
- 确保使用美式英语拼写

## 禁止事项

- 不要在 MDX 文件中省略 frontmatter
- 内部链接不要使用绝对 URL
- 不要审查代码块（以 ``` 标记），因为它们通常不是完整片段
- 不要包含未经测试的代码示例
- 不要自行假设——始终请求澄清
- 相对链接中不要包含本地化路径（例如 `/python/` 或 `/javascript/`）——这些由构建管道自动解析
- 代码示例中不要使用模型别名（例如 "claude-sonnet-4-5"）；始终使用完整的模型名称/标识符（例如 "claude-sonnet-4-5-20250929"）

如有疑问，请参阅 Mintlify 文档（可通过 MCP 访问，如可用）或访问 [Mintlify 文档](https://docs.mintlify.com/docs/introduction)。

## 拉取请求指南

- 描述变更的“原因”，说明为何所提方案是合适的
- 突出显示需要仔细审查的变更部分
- 始终在 PR 描述中添加免责声明，说明 AI 智能体如何参与本次贡献