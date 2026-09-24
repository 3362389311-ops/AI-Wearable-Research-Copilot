import csv
import time

from wearable_cli import client, analyze_product


SYSTEM_PROMPT = """
你是一名健康可穿戴产品研究助手。

只依据用户提供的信息分析，不要编造。

只输出 JSON，必须严格包含：

{
  "features": [],
  "evidence": [],
  "risks": [],
  "questions": []
}

四个字段都必须是字符串列表。
"""


TEST_CASES = [
    "一款开放式运动耳机，支持IP55，续航12小时，面向跑步用户。",
    "一款智能手表，支持心率监测、GPS和睡眠分析，续航7天。",
    "一款运动手环，重量25克，支持计步、血氧和消息提醒。",
    "一款开放式耳夹耳机，支持蓝牙5.4和无线充电。",
    "一款跑步手表，支持双频GPS、路线导航和训练负荷分析。",
    "一款睡眠戒指，可以记录心率、体温趋势和睡眠阶段。",
    "一款游泳耳机，支持IP68，可以离线播放音乐。",
    "一款骨传导耳机，面向骑行场景，支持双设备连接。",
    "一款儿童智能手表，支持定位、通话和电子围栏。",
    "一款健康手环，支持压力监测、睡眠记录和全天心率。",
    "一款运动耳机，官方宣称续航10小时，支持快充。",
    "一款户外手表，支持气压计、指南针和轨迹返航。",
    "一款健身手环，可记录力量训练和有氧训练数据。",
    "一款开放式办公耳机，支持双麦克风通话降噪。",
    "一款智能戒指，重量3克，支持睡眠和恢复状态分析。",
    "一款骑行码表，支持GPS、功率计连接和路线导航。",
    "一款运动手表，支持ECG功能和跌倒检测。",
    "一款耳夹式耳机，单次续航8小时，充电盒总续航32小时。",
    "一款户外运动耳机，支持防水、防汗和实体按键。",
    "一款健康监测设备，可记录静息心率、活动量和睡眠时长。"
]


results = []
success_count = 0


for index, product_text in enumerate(TEST_CASES, start=1):

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": product_text
        }
    ]

    start_time = time.time()

    try:
        result = analyze_product(
            client,
            messages
        )

        latency = round(time.time() - start_time, 2)

        success = True
        error = ""
        success_count += 1

        print(f"[{index:02d}/20] PASS | {latency}s")

    except Exception as e:
        latency = round(time.time() - start_time, 2)

        success = False
        error = str(e)

        print(f"[{index:02d}/20] FAIL | {error}")

    results.append({
        "run": index,
        "input": product_text,
        "success": success,
        "latency_seconds": latency,
        "error": error
    })


success_rate = success_count / len(TEST_CASES) * 100


with open(
    "gate_a_results.csv",
    "w",
    newline="",
    encoding="utf-8-sig"
) as f:

    writer = csv.DictWriter(
        f,
        fieldnames=[
            "run",
            "input",
            "success",
            "latency_seconds",
            "error"
        ]
    )

    writer.writeheader()
    writer.writerows(results)


print("\n==============================")
print("Gate A 20-run Test")
print("==============================")
print(f"Success: {success_count}/20")
print(f"Success rate: {success_rate:.1f}%")

if success_rate >= 90:
    print("Gate A: PASS")
else:
    print("Gate A: FAIL")

print("Results saved to gate_a_results.csv")