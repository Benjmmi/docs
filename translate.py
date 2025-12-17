import os
import hashlib
import json
from openai import OpenAI
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 配置
client = OpenAI(api_key=os.getenv("DEEPSEEK_API_KEY"), base_url="https://api.deepseek.com")
SOURCE_DIR = BASE_DIR
TARGET_DIR = "docs_zh"
CACHE_FILE = "translation_cache.json"

def get_hash(text):
    return hashlib.md5(text.encode('utf-8')).hexdigest()

def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, 'r') as f: return json.load(f)
    return {}

def save_cache(cache):
    with open(CACHE_FILE, 'w') as f: json.dump(cache, f, indent=2)

def translate_text(text):
    prompt = f"You are a professional technical translator. Translate the following Markdown content into Chinese. Keep markdown structure, links, and code blocks unchanged.\n\nContent:\n{text}"
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def main():
    cache = load_cache()
    if not os.path.exists(TARGET_DIR): os.makedirs(TARGET_DIR)

    for root, dirs, files in os.walk(SOURCE_DIR):
        for file in files:
            if file.endswith(".md"):
                source_path = os.path.join(root, file)
                rel_path = os.util.relpath(source_path, SOURCE_DIR)
                target_path = os.path.join(TARGET_DIR, rel_path)
                
                os.makedirs(os.path.dirname(target_path), exist_ok=True)

                with open(source_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                curr_hash = get_hash(content)
                if cache.get(source_path) == curr_hash:
                    print(f"Skipping {source_path} (No changes)")
                    continue

                print(f"Translating {source_path}...")
                translated_content = translate_text(content)
                
                with open(target_path, 'w', encoding='utf-8') as f:
                    f.write(translated_content)
                
                cache[source_path] = curr_hash

    save_cache(cache)

if __name__ == "__main__":
    main()
