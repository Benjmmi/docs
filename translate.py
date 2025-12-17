import openai
import os

def translate_text(text, target_lang="Chinese"):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": f"You are a professional tech translator. Translate the following markdown content to {target_lang}, preserving all markdown tags and code blocks."},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content
