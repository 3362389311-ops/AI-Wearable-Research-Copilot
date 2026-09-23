import os
import json

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

product_text = input("请输入产品资料：\n> ").strip()

if not product_text:
    raise ValueError("产品资料不能为空")

system_prompt = """
你是一名健康可穿戴产品研究助手。

请根据用户提供的产品资料进行分析。

要求：
1. 只依据用户提供的资料，不要编造不存在的信息。
2. 只输出 JSON，不要输出 Markdown，不要输出额外解释。
3. JSON 必须严格包含以下四个字段：

{
  "features": [],
  "evidence": [],
  "risks": [],
  "questions": []
}

字段含义：
features：产品的主要功能或特征。
evidence：支持这些判断的原始资料证据。
risks：资料中存在的风险、局限或尚未验证的问题。
questions：为了进一步研究产品，还需要回答的问题。
"""

messages = [
    {
        "role": "system",
        "content": system_prompt
    },
    {
        "role": "user",
        "content": product_text
    }
]

response = client.chat.completions.create(
    model="deepseek-flash",
    messages=messages,
    response_format={
        "type": "json_object"
    }
)

content = response.choices[0].message.content

result = json.loads(content)

# 临时观察 API → JSON字符串 → Python字典 的类型变化
print(type(response))
print(type(content))
print(type(result))
print(result["features"])

print("\n=== AI Wearable Research Copilot v0.2 ===")

print(
    json.dumps(
        result,
        ensure_ascii=False,
        indent=2
    )
)

with open(
    "result.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(
        result,
        f,
        ensure_ascii=False,
        indent=2
    )

print("\n分析结果已保存到 result.json")