import os
import json
import time
import logging

from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel, ValidationError, ConfigDict

class ResearchResult(BaseModel):
    model_config = ConfigDict(extra="forbid")

    features: list[str]
    evidence: list[str]
    risks: list[str]
    questions: list[str]

logging.basicConfig(
    filename="copilot.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    encoding="utf-8"
)

load_dotenv()

api_key = os.getenv("DEEPSEEK_API_KEY")

if not api_key:
    raise ValueError("没有找到 DEEPSEEK_API_KEY")


client = OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com"
)

def analyze_product(client, messages, max_retries=3):
    for attempt in range(1, max_retries + 1):

        try:
            logging.info("analysis_start attempt=%s", attempt)

            response = client.chat.completions.create(
                model="deepseek-flash",
                messages=messages,
                response_format={
                    "type": "json_object"
                }
            )

            content = response.choices[0].message.content

            raw_result = json.loads(content)

            validated_result = ResearchResult.model_validate(raw_result)

            result = validated_result.model_dump()

            logging.info("analysis_success attempt=%s", attempt)

            return result

        except json.JSONDecodeError as e:
            logging.warning(
                "json_decode_failed attempt=%s error=%s",
                attempt,
                e
            )

            print(f"第 {attempt} 次失败：JSON 解析错误")

        except ValidationError as e:
            logging.warning(
                "schema_validation_failed attempt=%s error=%s",
                attempt,
                e
            )

            print(f"第 {attempt} 次失败：Schema 校验错误")

        except Exception as e:
            logging.error(
                "api_or_unexpected_failed attempt=%s error=%s",
                attempt,
                e
            )

            print(
                f"第 {attempt} 次失败："
                f"API、网络或其他错误：{e}"
            )

        if attempt < max_retries:
            print("2 秒后自动重试...")
            time.sleep(2)

    raise RuntimeError(
        f"连续 {max_retries} 次失败，请检查 copilot.log"
    )

def main():
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

    result = analyze_product(
        client,
        messages
    )

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


if __name__ == "__main__":
    main()