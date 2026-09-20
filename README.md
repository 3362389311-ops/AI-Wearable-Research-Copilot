# AI 可穿戴研究助手
# AI Wearable Research Copilot

> 面向健康可穿戴产品研究、用户研究与 AI 产品探索的轻量研究助手。  
> A lightweight AI-assisted research copilot for wearable product research, user research, and AI product exploration.

---

## 1. 项目概述
## 1. Project Overview

**AI Wearable Research Copilot** 是一个围绕健康可穿戴设备研究构建的长期项目。

**AI Wearable Research Copilot** is a long-term project built around research on wearable and health-tech products.

本项目的目标并不是简单“调用一个大模型”，而是把真实的产品研究流程做成一个可验证、可迭代的 AI 工作流。

The goal of this project is not simply to “call an LLM,” but to turn a real product research workflow into a verifiable and iterative AI-assisted system.

**中文流程：**

产品资料 / 参数 / 评论 / 问卷 / 访谈记录  
→ 结构化提取  
→ 用户需求与痛点分析  
→ 竞品矩阵与 JTBD  
→ 证据引用  
→ 产品机会点与研究摘要

**English Workflow:**

Product materials / specifications / reviews / surveys / interview notes  
→ Structured extraction  
→ User needs and pain-point analysis  
→ Competitor matrix and JTBD  
→ Evidence citation  
→ Product opportunity identification and research brief

最终希望形成一个可以公开访问的 Web Demo，并通过 Evaluation、用户测试、成本 / 延迟记录等方式证明它不仅“能跑”，而且能够被验证和持续改进。

The final goal is to build a publicly accessible Web Demo and prove, through evaluation, user testing, and cost / latency tracking, that the product not only “runs” but can also be validated and continuously improved.

---

## 2. 为什么做这个项目
## 2. Why This Project

健康、运动与可穿戴设备正在逐渐融合。

Health, sports, and wearable devices are increasingly converging.

我长期关注运动场景、开放式音频和可穿戴设备，也在科研中持续使用 Python、机器学习和 AI 工具完成数据分析、文献研究与复杂任务拆解。

I have a long-term interest in sports scenarios, open-ear audio, and wearable devices, and I also use Python, machine learning, and AI tools in research for data analysis, literature research, and complex task decomposition.

这个项目希望进一步完成一次能力迁移：

This project aims to complete a further capability transition:

**中文：**

AI-native 科研工作流  
→ AI 辅助产品研究  
→ 可被真实用户使用和验证的 AI 产品 Demo

**English:**

AI-native research workflow  
→ AI-assisted product research  
→ An AI product demo that can be used and validated by real users

因此，本项目重点训练和展示以下能力：

Therefore, this project focuses on developing and demonstrating the following capabilities:

- Git / GitHub 工程化协作  
  Git / GitHub engineering workflow and collaboration
- Python 数据处理  
  Python-based data processing
- LLM API 调用  
  LLM API integration
- 结构化输出 / JSON Schema  
  Structured Output / JSON Schema
- Prompt 设计  
  Prompt design
- 用户研究与 JTBD  
  User research and JTBD
- 竞品研究  
  Competitor research
- 基于证据的研究  
  Evidence-based research
- LLM Evaluation  
  LLM evaluation
- 轻量 RAG / Citation  
  RAG Lite / Citation
- Web Demo 构建  
  Web Demo development
- 产品定义 / MVP  
  Product definition / MVP
- 用户测试与迭代  
  User testing and iteration

---

## 3. 目标用户
## 3. Target Users

本项目初始目标用户包括：

The initial target users of this project include:

- 健康可穿戴产品经理  
  Wearable and health-tech product managers
- 用户研究员  
  User researchers
- AI 产品经理 / AI 应用工程师  
  AI product managers / AI application engineers
- 运动健康与消费电子行业研究人员  
  Researchers in sports health and consumer electronics

这些用户通常需要同时处理大量不同类型的信息。

These users often need to process large amounts of heterogeneous information.

**中文：**

- 产品参数
- 官方资料
- 用户评论
- 问卷数据
- 用户访谈
- 市场与行业信息

**English:**

- Product specifications
- Official product materials
- User reviews
- Survey data
- User interviews
- Market and industry information

真正困难的并不是“找到信息”，而是：

The real difficulty is not simply “finding information,” but rather:

**如何把分散证据转化为结构化、可追溯、可用于产品决策的研究结论。**

**How to transform scattered evidence into structured, traceable research conclusions that can support product decisions.**

---

## 4. 计划输入
## 4. Planned Inputs

### 4.1 结构化数据
### 4.1 Structured Data

- 产品参数 CSV  
  Product specification CSV
- 问卷 CSV  
  Survey CSV
- 可穿戴设备功能表  
  Wearable feature tables
- 基础用户画像数据  
  Basic user profile data

### 4.2 非结构化数据
### 4.2 Unstructured Data

- 产品描述  
  Product descriptions
- 用户评论  
  User reviews
- 访谈笔记  
  Interview notes
- 研究笔记  
  Research notes
- 公开报告与产品文档  
  Public reports and product documents

---

## 5. 计划输出
## 5. Planned Outputs

系统首先计划输出稳定、结构化的 JSON 结果。

The system will first focus on generating stable, structured JSON outputs.

```json
{
  "features": [],
  "evidence": [],
  "user_pain_points": [],
  "jtbd": [],
  "risks": [],
  "product_opportunities": [],
  "open_questions": []
}
```

更完整的产品输出包括：

More complete product outputs will include:

- 竞品矩阵  
  Competitor Matrix
- 用户分群摘要  
  User Segment Summary
- 用户痛点地图  
  Pain Point Map
- JTBD 假设  
  JTBD Hypotheses
- 证据与引用  
  Evidence & Citation
- 产品机会地图  
  Product Opportunity Map
- 研究简报  
  Research Brief
- 访谈问题建议  
  Interview Question Suggestions
- 产品研究摘要  
  Product Research Summary

---

## 6. 用户研究场景
## 6. Research Scenario

项目计划首先聚焦于：

The project will initially focus on:

**大学生 × 运动 × 可穿戴设备**

**University Students × Sports × Wearable Devices**

真实用户研究将优先覆盖：

Real-world user research will prioritize:

- 操场  
  Running tracks / sports fields
- 篮球场  
  Basketball courts
- 健身房  
  Gyms

计划通过匿名问卷和轻量访谈收集以下信息：

The project plans to collect the following information through anonymous surveys and lightweight interviews:

- 使用的穿戴设备品牌  
  Wearable device brands currently used
- 主要运动场景  
  Main sports and activity scenarios
- 高频功能  
  Frequently used features
- 使用习惯  
  Usage habits
- 核心关注点  
  Key decision factors
- 使用痛点  
  User pain points
- 购买 / 弃用原因  
  Reasons for purchase / abandonment
- 年龄与年级等基础分群信息  
  Basic segmentation information such as age and academic year

所有用户研究数据在进入公开仓库前均应进行匿名化处理，不上传可识别个人身份的信息。

All user research data should be anonymized before being uploaded to the public repository, and no personally identifiable information should be included.

---

## 7. 初始竞品范围
## 7. Initial Competitor Scope

第一阶段计划覆盖部分典型健康 / 运动可穿戴产品与品牌，例如：

The first stage plans to cover several representative health and sports wearable products and brands, including:

- Apple Watch
- Garmin
- COROS
- WHOOP
- Oura
- Huawei / 华为
- Shokz / 韶音

本项目的目的不是做简单参数罗列，而是逐步建立以下关系：

The goal is not to create a simple specification list, but to gradually build the following relationship:

**中文：**

产品能力  
→ 使用场景  
→ 用户需求  
→ 用户痛点  
→ 产品机会

**English:**

Product capabilities  
→ Usage scenarios  
→ User needs  
→ User pain points  
→ Product opportunities

---

## 8. 产品工作流
## 8. Product Workflow

本项目计划按照“原始资料 → 数据处理 → AI 分析 → 证据验证 → 产品洞察”的顺序构建完整流程。

The project is planned around a complete workflow from raw materials to data processing, AI analysis, evidence validation, and product insight generation.

```text
原始数据 / Raw Data
   │
   ├── 产品参数 / Product Specs
   ├── 用户评论 / Reviews
   ├── 问卷 CSV / Survey CSV
   ├── 访谈笔记 / Interview Notes
   └── 研究资料 / Research Documents
   │
   ▼
数据清洗与解析 / Data Cleaning & Parsing
   │
   ▼
LLM 结构化输出 / LLM Structured Output
   │
   ▼
证据提取 / Evidence Extraction
   │
   ▼
用户痛点与 JTBD / User Pain Points & JTBD
   │
   ▼
竞品分析 / Competitor Analysis
   │
   ▼
产品机会识别 / Product Opportunity Identification
   │
   ▼
研究简报 / Web Demo
Research Brief / Web Demo
```

---

## 9. 仓库结构
## 9. Repository Structure

项目初始仓库结构规划如下：

The initial repository structure is planned as follows:

```text
ai-wearable-research-copilot/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   └── sample_product.txt
│
├── src/
│   ├── api_demo.py
│   ├── product_analyzer.py
│   └── utils.py
│
├── outputs/
│
└── logs/
```

### 9.1 主要文件说明
### 9.1 Main Files

- `api_demo.py`  
  中文：最小化 LLM API 调用示例，用于验证 API 是否可以正常工作。  
  English: A minimal LLM API call demo used to verify that the API works correctly.

- `product_analyzer.py`  
  中文：核心产品研究与结构化分析逻辑。  
  English: Core logic for product research and structured analysis.

- `utils.py`  
  中文：通用工具函数，例如保存 JSON、日志记录等。  
  English: Shared utility functions, such as saving JSON and logging.

- `data/`  
  中文：输入数据与样例研究资料。  
  English: Input data and sample research materials.

- `outputs/`  
  中文：结构化模型输出与生成的研究结果。  
  English: Structured model outputs and generated research results.

- `logs/`  
  中文：运行日志，用于调试、错误定位和后续评测。  
  English: Runtime logs for debugging, error tracing, and later evaluation.

---

## 10. 六个月路线
## 10. Six-Month Roadmap

### 10.1 第一阶段：工程基础
### 10.1 Phase 1 — Engineering Foundation

**第 1–4 周**

**Week 1–4**

中文学习内容：

Chinese learning objectives:

- Git / GitHub 工作流  
  Git / GitHub workflow
- Python CSV / JSON / 函数 / 异常处理  
  Python CSV / JSON / functions / exception handling
- LLM API  
  LLM API
- Structured Output  
  Structured Output
- 日志系统  
  Logging
- 基础 Tool Calling  
  Basic tool calling

**中文里程碑：可复现的 CLI Demo。**

**English Milestone: A reproducible CLI Demo.**

### 10.2 第二阶段：产品研究与用户研究
### 10.2 Phase 2 — Product & User Research

**第 5–8 周**

**Week 5–8**

中文学习内容：

Chinese learning objectives:

- 竞品分析  
  Competitor analysis
- 用户画像  
  User personas
- JTBD  
  JTBD
- 问卷 / 访谈设计  
  Survey / interview design
- 用户痛点地图  
  Pain Point Map
- 证据分类  
  Evidence classification

**中文里程碑：《健康可穿戴研究报告 v1》。**

**English Milestone: Wearable Research Report v1.**

### 10.3 第三阶段：MVP 与 Evaluation
### 10.3 Phase 3 — MVP & Evaluation

**第 9–16 周**

**Week 9–16**

中文学习内容：

Chinese learning objectives:

- Streamlit / Gradio / 轻量 Web UI  
  Streamlit / Gradio / lightweight Web UI
- 小型 Evaluation 数据集  
  Small evaluation dataset
- 事实性 / 引用 / 格式 / 有用性评价  
  Factuality / Citation / Format / Usefulness evaluation
- Prompt 与模型对比  
  Prompt and model comparison
- 成本 / 延迟 / 可靠性 benchmark  
  Cost / latency / reliability benchmark
- RAG Lite  
  RAG Lite

**中文里程碑：具有可量化 Evaluation 结果的 Copilot MVP。**

**English Milestone: A Copilot MVP with measurable evaluation results.**

### 10.4 第四阶段：产品化
### 10.4 Phase 4 — Productization

**第 17–22 周**

**Week 17–22**

中文学习内容：

Chinese learning objectives:

- PRD Lite  
  PRD Lite
- 用户流程  
  User flow
- Backlog  
  Backlog
- 真实用户测试  
  Real user testing
- 产品迭代  
  Product iteration
- 异常处理  
  Error handling
- 隐私提示  
  Privacy notice
- 公开部署  
  Public deployment

**中文里程碑：公开 Demo v1.0。**

**English Milestone: Public Demo v1.0.**

### 10.5 第五阶段：作品集与面试
### 10.5 Phase 5 — Portfolio & Interview

**第 23–26 周**

**Week 23–26**

最终将整个项目压缩成一套完整的产品 Case：

The final project will be condensed into a complete product case:

**Problem → Insight → Build → Eval → Iteration → Impact**

最终交付物：

Final deliverables:

- 公开 GitHub 仓库  
  Public GitHub repository
- 在线 Demo  
  Online Demo
- 产品作品集 Case  
  Portfolio case
- 60–90 秒 Demo 视频  
  60–90 second demo video
- Evaluation 报告  
  Evaluation report
- 用户研究报告  
  User research report
- 2 分钟 / 5 分钟项目讲稿  
  2-minute / 5-minute project pitch

---

## 11. Evaluation 原则
## 11. Evaluation Principles

本项目不会把“看起来不错”作为唯一评价标准。

This project will not use “it looks good” as the only evaluation criterion.

计划评价维度包括：

Planned evaluation dimensions include:

- 结构化输出成功率  
  Structured output success rate
- 事实准确性  
  Factuality
- 证据可追溯性  
  Evidence traceability
- 引用质量  
  Citation quality
- 格式有效性  
  Format validity
- 用户有用性  
  User usefulness
- 错误率  
  Error rate
- Token 使用量  
  Token usage
- 单次运行成本  
  Cost per run
- P50 / P95 延迟  
  P50 / P95 latency

本项目希望最终可以回答三个问题：

The project ultimately aims to answer three questions:

**哪一个版本更好？为什么更好？仍然存在哪些失败情况？**

**Which version performs better? Why does it perform better? What failure modes still remain?**

---

## 12. 当前状态
## 12. Current Status

**版本：v0.1 — 项目基础阶段**

**Version: v0.1 — Project Foundation**

当前进度：

Current progress:

- [x] 已创建 GitHub 账户  
  GitHub account created
- [x] 已安装 Git  
  Git installed
- [x] 已完成初步 LLM API 探索  
  Initial LLM API exploration completed
- [x] 已定义项目范围  
  Project scope defined
- [ ] 初始化仓库结构  
  Repository structure initialized
- [ ] 完成第一次 CSV → JSON Python 工作流  
  First CSV → JSON Python workflow
- [ ] 完成稳定 Structured Output Demo  
  Stable structured output demo
- [ ] 完成第一次 20 次运行可靠性测试  
  First 20-run reliability test
- [ ] 建立可穿戴竞品数据集  
  Wearable competitor dataset
- [ ] 建立用户研究数据集  
  User research dataset
- [ ] 完成 Web Demo  
  Web Demo

---

## 13. 开发原则
## 13. Development Principles

### 13.1 证据优先
### 13.1 Evidence First

中文：任何研究结论都应尽可能保留来源，并能够追溯到原始资料。

English: Research conclusions should preserve their sources whenever possible and remain traceable to the original evidence.

### 13.2 事实、推断与假设必须区分
### 13.2 Facts, Inferences, and Hypotheses Must Be Distinguished

中文：产品研究中必须明确区分已验证事实、模型推断和研究假设。

English: Product research must clearly distinguish verified facts, model inferences, and research hypotheses.

### 13.3 先构建，再增加复杂度
### 13.3 Build Before Complexity

中文：优先从简单的 Python + API + JSON 开始，不为了“看起来高级”而堆叠复杂 Agent 框架。

English: Start with simple Python + API + JSON, and do not add complex agent frameworks merely to make the system look more advanced.

### 13.4 先评测，再展示
### 13.4 Evaluate Before Showcase

中文：一个 Demo 不应只追求视觉效果，而应能够通过 Evaluation 被量化验证。

English: A Demo should not only look impressive; it should also be quantitatively validated through evaluation.

### 13.5 人在回路
### 13.5 Human-in-the-loop

中文：AI 用于辅助研究、提取和综合信息，最终产品判断与决策仍由人完成。

English: AI is used to assist research, extraction, and synthesis, while final product judgments and decisions remain human decisions.

---

## 14. 项目最终目标
## 14. Project Goal

这个仓库最终希望证明一种完整能力：

This repository is ultimately intended to demonstrate one complete capability:

> **中文：我能够发现一个真实的产品研究问题，构建一个 AI 辅助解决方案，用证据进行 Evaluation，让真实用户测试，并基于反馈持续迭代成一个可使用的产品。**

> **English: I can identify a real product research problem, build an AI-assisted solution, evaluate it with evidence, test it with real users, and iterate it into a usable product.**

---

## 15. 免责声明
## 15. Disclaimer

中文：本项目目前属于学习与求职作品集项目，主要用于产品研究、数据分析与 AI 产品能力训练。

English: This project is currently an educational and portfolio project, mainly intended for product research, data analysis, and AI product development practice.

中文：本项目不提供医疗诊断或医疗建议。

English: This project does not provide medical diagnosis or medical advice.
