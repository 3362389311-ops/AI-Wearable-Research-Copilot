import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

api_key = os.getenv("DEEPSEEK_API_KEY")

if not api_key:
    raise ValueError("没有找到 DEEPSEEK_API_KEY")


client = OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com"
)


response = client.chat.completions.create(
    model="deepseek-flash",
    messages=[
        {
            "role": "system",
            "content": "你是一名健康可穿戴产品研究助手。"
        },
        {
            "role": "user",
            "content": "用一句话解释开放式耳机是什么。"
        }
    ],
    stream=False,
    extra_body={
        "thinking": {
            "type": "disabled"
        }
    }
)


print(response.choices[0].message.content)