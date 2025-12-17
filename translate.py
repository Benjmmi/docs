import os
import hashlib
from openai import OpenAI

# 初始化 DeepSeek 客户端
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"), 
    base_url="https://api.deepseek.com"
)

def translate_markdown(content, target_lang="中文"):
    prompt = f"""你是一位专业的技术文档翻译官。请将以下 Markdown 内容翻译成{target_lang}。
    要求：
    1. 保持所有的 Markdown 语法标记（如 #, 内容链接, 图片, 代码块）不动。
    2. 保持代码块中的内容不翻译。
    3. 技术术语请保持专业性，必要时保留英文原词（如 Runtime, Hook）。
    4. 仅返回翻译后的正文内容。
    
    内容如下：
    {content}"""

    response = client.chat.completions.create(
        model="deepseek-chat", # 或者使用 deepseek-reasoner (R1)
        messages=[
            {"role": "system", "content": "You are a helpful assistant that translates technical documentation."},
            {"role": "user", "content": prompt},
        ],
        stream=False
    )
    return response.choices[0].message.content
