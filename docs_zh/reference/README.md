# LangChain 参考文档

由于 Mintlify 平台的限制，参考文档未整合至我们的主 Mintlify 网站（[`docs.langchain.com`](https://docs.langchain.com)）。我们改为为 Python 和 JavaScript/TypeScript 参考文档部署了静态文档站点。

目前，一个 Vercel 项目负责托管构建自 `dist/language` 目录的 HTML 文件，访问地址为 [`reference.langchain.com/python`](https://reference.langchain.com/python) 和 [`reference.langchain.com/javascript`](https://reference.langchain.com/javascript)。

关于各语言参考文档的构建与部署详情，请参阅 [`reference/python/README.md`](./python/README.md) 和 [`reference/javascript/README.md`](./javascript/README.md) 文件。

## v0.3 Python HTML 参考文档

v0.3 Python HTML 参考文档托管在 `/v0.3/python` 路径下，通过 git 子模块指向 [`langchain-api-docs-html`](https://github.com/langchain-ai/langchain-api-docs-html) 仓库进行维护。

### 初始设置

首次克隆仓库或添加子模块时，需执行初始化：

```bash
git submodule update --init --recursive
```

### 更新 v0.3 Python HTML 参考文档

```bash
cd reference/external/html-docs
git pull origin main
cd ../..
git add external/html-docs
git commit -m "更新 v0.3 Python HTML 参考文档"
```

### 构建流程

部署过程中，构建脚本（`pnpm build:html-v03`）会将 `external/html-docs/api_reference_build/html/` 目录下的文件复制到 `dist/v0.3/python/` 目录。