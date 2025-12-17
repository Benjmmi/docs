# 文档编写者 IDE 设置指南

本仓库包含配置文件，以确保文档编写者使用的不同编辑器和 IDE 保持一致的格式。

在进行大量文档修改之前，请确保完成以下步骤并配置到位。

## 自动配置

### VSCode

如果您使用 Visual Studio Code，打开此项目时，`.vscode/settings.json` 中的设置应自动应用。无需额外设置。

### 其他 IDE

大多数现代 IDE 都支持 EditorConfig。根目录中的 `.editorconfig` 文件将自动配置：

- IntelliJ IDEA / PyCharm / WebStorm
- Sublime Text
- Atom
- Vim
- Emacs
- 以及其他许多 IDE

## 格式标准

### 缩进

- **1 个制表符 = 4 个空格**，适用于所有文件，除了：
  - JSON 文件：2 个空格
  - YAML 文件：2 个空格
  - CSS/HTML 文件：2 个空格

### 行长度

- **Markdown 文件不设硬换行**
- 启用自动换行，但不插入硬换行符
- 长行在视觉上会换行，但在文件中仍保持为单行

### 行尾

- 所有文件使用 **Unix 风格的行尾**（`\n`）
- 自动修剪尾部空格
- 自动插入最终换行符

### Markdown 特定设置

- 保留 Markdown 中的尾部空格（用于换行）
- 保存时不自动格式化
- 启用自动换行以提高可读性
- 不显示标尺/列参考线

## 手动 IDE 设置（如需要）

如果您的 IDE 未自动应用这些设置，请手动配置：

### 通用设置

```text
制表符大小：4 个空格
插入空格：是（非制表符）
自动换行：开启
保存时自动格式化：关闭
修剪尾部空格：是
插入最终换行符：是
```

### Markdown 设置

```text
自动换行：开启
硬换行：关闭
保留尾部空格：是
最大行长度：无限制
```

### 代码示例

```text
Python：4 个空格
JavaScript/TypeScript：4 个空格
JSON：2 个空格
YAML：2 个空格
```

## VSCode 扩展（推荐）

为了在 VSCode 中获得最佳写作体验，建议安装：

- **EditorConfig for VS Code** - 自动应用 .editorconfig 设置
- **markdownlint** - Markdown 编辑增强
- **Markdown All in One** - Markdown 编辑增强
- **MDX** - 为 `.mdx` 文件提供语法高亮
- **Prettier - Code formatter**（在我们的设置中已针对 Markdown 禁用）

## 为什么采用这些设置？

### 无硬换行

- 允许内容在不同设备上灵活显示
- 防止编辑内容时出现尴尬的换行
- 更利于协作编辑和版本控制
- 适应不同屏幕尺寸

### 缩进使用 4 个空格

- 与 Python 惯例一致（用于代码示例）
- 嵌套内容可读性更好
- 符合大多数编程语言的标准

### 无自动格式化

- 防止对精心编写的 Markdown 进行不必要的更改
- 避免破坏自定义格式（如表格或代码块）
- 给予编写者对内容结构的完全控制权

## 故障排除

### VSCode 未应用设置

1. 打开项目后重启 VSCode
2. 检查您是否在 docs 文件夹中（而非父目录）
3. 确认项目根目录中存在 `.vscode/settings.json`

### 其他 IDE 未应用设置

1. 确保您的 IDE 支持 EditorConfig
2. 如需，安装 EditorConfig 插件
3. 检查项目根目录中是否存在 `.editorconfig`
4. 重启您的 IDE

### 设置未生效

如果自动配置无效，请使用上述列出的设置手动配置您的 IDE。