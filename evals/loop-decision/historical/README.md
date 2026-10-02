# Loop Decision

> **v0.3.1** · [评测记录](evals/releases/2026-09-20-v0.3.1.md) · [审查范围与限制](REVIEW.md)

![Loop skill cover](assets/cover.jpg)

![version](https://img.shields.io/badge/version-0.3.1-blue)
![license](https://img.shields.io/badge/license-MIT-green)
![type](https://img.shields.io/badge/skill-instruction--only-orange)

[English](./README.en.md) | 中文

把重要决策从「拍脑袋 + 事后后悔」变成打分闭环：可逆性分诊 → 决策 brief → rubric 打分 → premortem 事前验尸 + 红队唱反调 → 决策备忘录（预设复盘日期）→ 复盘对照（先评过程再看结果）。

给 Claude Code / Codex 等 agent 用的纯指令 skill：先过可逆性 Gate；只有难逆决策进入完整质检环，可逆小事走快判。

## 挑一个模式（不必每次都跑完整闭环）

| 模式 | 什么时候用 | 跑什么 |
|---|---|---|
| **Full Loop** | 难逆决策（跳槽/大额/选型/战略） | 全流程 + 打分迭代 |
| **快判** | 可逆小决策（Gate 自动判） | 分诊理由 + 一页要点 + 建议 + 退出条件 |
| **复盘模式** | 手里有旧决策备忘录 | 沿用原 Gate 比例复盘；已知结果先声明污染并隔离事后信息 |

## 适合

- 跳槽 / offer 选择 / 职业方向这类「选错了退不回来」的决策
- 大额购买、长期合同、技术栈选型、合作与投资判断
- 已经想好了但想被认真挑战一轮（红队 + premortem）
- 手里有一堆过去的决定，想知道自己判断的系统性偏差（复盘模式）

## 不适合

- 谈薪、离职谈话、关键对话的**话术准备**（「要不要跳」归本 skill，「怎么谈」不归本 skill）
- 述职 / 晋升 / 汇报**材料写作** → [loop-report-writer](https://github.com/steven-pku/loop-report-writer)
- 可逆的日常小决策——Gate 会直接放行，这是设计（防过度流程化），不是偷懒
- 心理危机、医疗紧急决策——超出范围，请寻求专业帮助
- 处方药或精神科用药的开始、停用、减量、渐停、换药、漏服处理——不进 Gate、评分、premortem 或方案比较，只提供简短的医生／药师求助支持

## 核心特性

- **可逆性 Gate**：先分诊 Type 1（单向门）/ Type 2（双向门），只有难逆决策进全环——框架出自 Bezos 2015 年致股东信，双向校准（重流程压垮小决策、轻流程放跑大决策都点破）
- **短快判**：Type 2 只输出判定、1-3 个因素、建议与退出条件；不扩写 Decision Brief、三选项表或自造加权评分卡
- **真选项纪律**：Full Loop 要求 >= 3 个真选项含「不做」，每个选项过「理性人理由」测试；Type 2 快判不强制补第三选项或打分
- **证据分级 F0-F3**：观点 / 给定事实 / 可核事实 / 高风险断言分层；载重 F2 未核且无有效承诺前核实计划时为 fatal，改称「我猜」不能绕过
- **premortem + 红队**：Klein 原始协议（HBR 2007）+ steelman-then-attack；产出应改变 brief，若没有变化则必须给出可核的 null-result 理由
- **决策备忘录**：冻结决策时刻的已知/未知/概率/幸存反对意见；模型草案默认 `Proposed`，只有用户明确确认后才进入 `Decided`
- **复盘分离**：Type 2 不因缺 Full Loop 构件扣分；结果已知时第一句先披露污染，把当时证据与事后信息分栏，事后原因不得倒灌过程评分，完成过程段后才讨论结果
- **引用可查**：rubric 每个锚点给出处和证据层级（`references/anchors-and-sources.md`），流传甚广的「premortem 提升准确率 30%」误引在本仓有考证与正确表述

## 为什么是纯指令

没有脚本、没有 runner——每一条行为都是你能读的纯文本：

- **可审计**——读完指令就知道它会怎么处理你的决策材料，没有黑盒
- **可移植**——使用同一组运行文件；各宿主的兼容性以实测为准
- **供应链安全**——运行时零依赖，不自动执行任何东西；安装与 CI 校验继承 npm / Git / GitHub 的信任链，CI 已按 commit SHA 与固定版本 pin

## 项目级安装

以下命令固定版本 `v0.3.1`，只写当前项目；目标目录须不存在。发布验证使用 Codex CLI 0.155.1、配置模型 `gpt-6-astra`／`xhigh`。实际结果与未测范围见评测记录。

**Codex**：

```bash
mkdir -p .agents/skills
git clone --branch v0.3.1 --depth 1 https://github.com/steven-pku/loop-decision.git .agents/skills/loop-decision
```

**Claude Code 目录示例（本版未执行该宿主行为验证）**：

```bash
mkdir -p .claude/skills
git clone --branch v0.3.1 --depth 1 https://github.com/steven-pku/loop-decision.git .claude/skills/loop-decision
```

运行时入口是 `SKILL.md`，按需读取 `references/` 和 `examples/`。安装后在该项目开启新会话。不要覆盖已有安装；先保留自己的修改。

## 30 秒首次成功

安装后在一个新会话中输入：

```text
用 loop-decision 快判：周末先试 A 还是 B 两款可退订的软件？两款都能随时取消。
```

检查输出先判为 **Type 2（可逆）**，只给分诊理由、1-3 个关键因素、建议与退出条件；不启动 /100 rubric、premortem 或红队全环。若 host 没有加载到本 skill，请先核对安装目录名是否为 `loop-decision`。

## 用法示例

```text
用 loop-decision 帮我过一个决策。
问题：要不要接受 B 公司的 offer（8 月底前要答复）
背景：现公司稳定但成长放缓；B 给了涨薪但业务线较新
输出：Full Loop
```

```text
用 loop-decision 的复盘模式。
下面是我三个月前写的决策备忘录，结果暂不提供。
请先按备忘录原文评过程；完成后我再提供结果。
[贴备忘录]
```

## 证据基础与边界

每个框架的出处和证据层级见 `references/anchors-and-sources.md`：Klein premortem（HBR 2007 一手）、Bezos Type 1/2（2015 股东信一手 PDF）、Farnam Street decision journal（原站一手）、SPADE / DACI / ADR（原作者一手）。找不到一手出处的流行说法（如某句 Kahneman 语录）明确标注不使用。

本 skill 提供决策**过程**支持，不构成法律、税务、医疗或持牌财务建议——这些领域的载重事实需要执业者确认（F3 纪律）。

它也不保证「最佳决定」或结果正确；输出需要由实际决策人复核。敏感材料应先去除姓名、联系方式、薪资、合同与账号信息，并注意 host / 模型服务商可能保留会话内容。

## 修复与验证

已执行 20 例首轮验证及 10 例定向复测；首轮的 5 处初评误扣分和 1 次服务容量失败均保留原始记录。新候选区分「红队待评」与「已观察到的低质量红队」，不把缺记录直接判作稻草人，也不让真实问题借待评免扣分。

[评测记录](evals/releases/2026-09-20-v0.3.1.md) 分列各轮候选、实际输出、连续会话与安装路由检查。示例分数是说明用的诊断，不能当成用户已接受决策或事实已核验。其他宿主未实跑；复盘加载提示等残余限制照实披露。

## License

MIT © Steven CHAN
