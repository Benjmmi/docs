---
applyTo: "src/oss/**"
---

> **注意：** 前置元数据中的 `applyTo` 字段指定了以下说明和指南适用于所有匹配模式 `src/oss/**` 的文件和目录。此指令由我们的文档工具使用，以针对代码库的特定部分应用这些指南。
LangChain 和 LangGraph 的文档位于 `src/oss` 文件夹中，并指代开源的 LangChain 和 LangGraph 框架。每个仓库都是一个单体仓库。各自仓库中的每个库都位于 `libs/` 下的一个子目录中。

# LangChain 和 LangGraph 项目的全局开发指南

## 核心开发原则

### 1. 保持稳定的公共接口 ⚠️ 关键

**始终尝试保留导出/公共方法的函数签名、参数位置和名称。**

❌ **不好 - 破坏性变更：**

```python
def get_user(id, verbose=False):  # 从 `user_id` 更改而来
    pass
```

✅ **好 - 稳定接口：**

```python
def get_user(user_id: str, verbose: bool = False) -> User:
    """根据 ID 检索用户，可选择详细输出。"""
    pass
```

**在对公共 API 进行任何更改之前：**

- 检查函数/类是否在 `__init__.py` 中导出
- 查看测试和示例中现有的使用模式
- 对新参数使用仅关键字参数：`*, new_param: str = "default"`
- 使用文档字符串警告（使用 reStructuredText，例如 `.. warning::`）明确标记实验性功能

🧠 *自问：*“如果用户上周使用了这个代码，这个更改会破坏他们的代码吗？”

### 2. 代码质量标准

**所有 Python 代码必须包含类型提示和返回类型。**

❌ **不好：**

```python
def p(u, d):
    return [x for x in u if x not in d]
```

✅ **好：**

```python
def filter_unknown_users(users: list[str], known_users: set[str]) -> list[str]:
    """过滤掉不在已知用户集合中的用户。

    Args:
        users: 要过滤的用户标识符列表。
        known_users: 已知/有效用户标识符的集合。

    Returns:
        不在 known_users 集合中的用户列表。
    """
    return [user for user in users if user not in known_users]
```

**风格要求：**

- 使用描述性的、**自解释的变量名**。避免使用过短或晦涩的标识符。
- 尝试将复杂函数（>20 行）在合理的情况下拆分为更小、更专注的函数
- 避免不必要的抽象或过早优化
- 遵循你正在修改的代码库中的现有模式

### 3. 测试要求

**每个新功能或错误修复必须包含单元测试。**

**测试组织：**

- 单元测试：`tests/unit_tests/`（不允许网络调用）
- 集成测试：`tests/integration_tests/`（允许网络调用）
- 使用 `pytest` 作为测试框架

**测试质量检查清单：**

- [ ] 当你的新逻辑被破坏时，测试会失败
- [ ] 覆盖了正常路径
- [ ] 测试了边界情况和错误条件
- [ ] 对外部依赖使用夹具/模拟
- [ ] 测试是确定性的（没有不稳定的测试）

检查清单问题：

- [ ] 如果你的新逻辑被破坏，测试套件是否会失败？
- [ ] 是否练习了所有预期行为（正常路径、无效输入等）？
- [ ] 测试在需要时是否使用了夹具或模拟？

```python
def test_filter_unknown_users():
    """测试从列表中过滤未知用户。"""
    users = ["alice", "bob", "charlie"]
    known_users = {"alice", "bob"}

    result = filter_unknown_users(users, known_users)

    assert result == ["charlie"]
    assert len(result) == 1
```

### 4. 安全与风险评估

**安全检查清单：**

- 不对用户控制的输入使用 `eval()`、`exec()` 或 `pickle`
- 适当的异常处理（不使用裸 `except:`），并使用 `msg` 变量存储错误消息
- 提交前删除无法访问/已注释的代码
- 检查竞态条件或资源泄漏（文件句柄、套接字、线程）
- 确保适当的资源清理（文件句柄、连接）

❌ **不好：**

```python
def load_config(path):
    with open(path) as f:
        return eval(f.read())  # ⚠️ 切勿对配置使用 eval
```

✅ **好：**

```python
import json

def load_config(path: str) -> dict:
    with open(path) as f:
        return json.load(f)
```

### 5. 文档标准

**对所有公共函数使用带有 Args 部分的 Google 风格文档字符串。**

❌ **文档不足：**

```python
def send_email(to, msg):
    """向收件人发送电子邮件。"""
```

✅ **完整文档：**

```python
def send_email(to: str, msg: str, *, priority: str = "normal") -> bool:
    """
    以指定优先级向收件人发送电子邮件。

    Args:
        to: 收件人的电子邮件地址。
        msg: 要发送的消息正文。
        priority: 电子邮件优先级级别（``'low'``、``'normal'``、``'high'``）。

    Returns:
        如果电子邮件发送成功则为 True，否则为 False。

    Raises:
        InvalidEmailError: 如果电子邮件地址格式无效。
        SMTPConnectionError: 如果无法连接到电子邮件服务器。
    """
```

**文档指南：**

- 类型放在函数签名中，而不是文档字符串中
- 在描述中关注“为什么”而不是“是什么”
- 记录所有参数、返回值和异常
- 保持描述简洁但清晰
- 在文档字符串中使用 reStructuredText 以实现丰富的格式

📌 *提示：* 保持描述简洁但清晰。仅在非显而易见时记录返回值。

### 6. 架构改进

**当你遇到可以改进的代码时，建议更好的设计：**

❌ **不良设计：**

```python
def process_data(data, db_conn, email_client, logger):
    # 函数做了太多事情
    validated = validate_data(data)
    result = db_conn.save(validated)
    email_client.send_notification(result)
    logger.log(f"Processed {len(data)} items")
    return result
```

✅ **更好的设计：**

```python
@dataclass
class ProcessingResult:
    """数据处理操作的结果。"""
    items_processed: int
    success: bool
    errors: List[str] = field(default_factory=list)

class DataProcessor:
    """处理数据验证、存储和通知。"""

    def __init__(self, db_conn: Database, email_client: EmailClient):
        self.db = db_conn
        self.email = email_client

    def process(self, data: List[dict]) -> ProcessingResult:
        """处理并存储数据，附带通知。"""
        validated = self._validate_data(data)
        result = self.db.save(validated)
        self._notify_completion(result)
        return result
```

**设计改进领域：**

如果存在**更清晰**、**更可扩展**或**更简单**的设计，请突出显示它，并建议以下方面的改进：

- 通过共享工具减少代码重复
- 使单元测试更容易（例如，通过依赖注入）
- 改善关注点分离（单一职责）
- 在不增加复杂性的情况下提高清晰度
- 对于结构化数据，优先使用数据类

## 开发工具与命令

### 包管理

```bash
# 添加包
uv add package-name

# 同步项目依赖
uv sync
uv lock
```

### 测试

```bash
# 运行单元测试（无网络）
make test

# 不要运行集成测试，因为必须设置 API 密钥

# 运行特定测试文件
uv run --group test pytest tests/unit_tests/test_specific.py
```

### 代码质量

```bash
# 代码检查
make lint

# 代码格式化
make format

# 类型检查
uv run --group lint mypy .
```

### 依赖管理模式

**本地开发依赖：**

```toml
[tool.uv.sources]
langchain-core = { path = "../core", editable = true }
langchain-tests = { path = "../standard-tests", editable = true }
```

**对于工具，使用来自 `langchain_core.tools` 的 `@tool` 装饰器：**

```python
from langchain.tools import tool

@tool
def search_database(query: str) -> str:
    """在数据库中搜索相关信息。

    Args:
        query: 搜索查询字符串。
    """
    # 在此处实现
    return results
```

## 快速参考检查清单

提交代码更改前：

- [ ] **破坏性变更**：确认没有公共 API 更改
- [ ] **类型提示**：所有函数都有完整的类型注解
- [ ] **测试**：新功能已完全测试
- [ ] **安全**：没有危险模式（eval、静默失败等）
- [ ] **文档**：公共函数使用 Google 风格文档字符串
- [ ] **代码质量**：`make lint` 和 `make format` 通过
- [ ] **架构**：在适用的情况下提出了改进建议
- [ ] **提交消息**：遵循 Conventional Commits 格式