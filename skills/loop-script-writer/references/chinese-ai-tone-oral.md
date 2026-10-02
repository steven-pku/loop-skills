# Chinese AI-Tone Patterns — Oral Subset

Adapted from a reviewed Chinese AI-tone pattern library. This file is self-contained and keeps only the patterns that are **instantly audible** in a spoken script—the ear catches what the eye forgives. If a suspected pattern is not listed here, judge it in context instead of depending on another repository.

## 听感即死（高频高害 · 口播加重）

| 模式 | 为什么口播里更致命 | 检测 | 修法 |
|---|---|---|---|
| 排比三连（「不是…不是…而是…」「从…到…到…」） | 书面扫过去 1 秒，念出来占 8 秒且节奏假 | 三个以上同构短语连用 | 留最强一个，其余删 |
| 「X 不仅是 Y，更是 Z」递进套话 | 听众等到「更是」就知道下一句是空话 | 模板匹配 | 直接说 Z，或给 Z 一个具体画面 |
| 列举式结尾（「无论是…还是…都…」收尾） | 口播结尾要 CTA，列举收尾 = 没有结尾 | 结尾段出现枚举 | 换成一个具体动作指令 |
| 匀速无停顿 | 纸面看不出，念出来像 TTS | read-aloud pass 无一处停顿标记 | 揭晓/转折前加停顿；长短句交替 |
| 定义句起手（「X，是一种…」） | 前 3 秒最贵，定义句 = 自杀式开场 | 首句是「是什么」句式 | 砍掉，从冲突或结果开始 |
| 每段总分总 | 听众听得出「作文感」，完播崩 | 段段先总述 | 信息密度曲线重排（每 10 秒一个点） |

## 听感存疑（中频 · 上下文判断）

| 模式 | 口播处理 |
|---|---|
| 「与此同时」「然而」桥接词 | 换口语转场（「另一边」「结果呢」）——见 `colloquial-craft.md` 替换表 |
| 万能程度副词堆叠（非常/极其/十分连用） | 口语允许一个，堆叠删 |
| 「正如 X 所言」伪引经 | 口播引用必须真实且口语化转述；查无出处直接删（F 纪律管辖） |
| 逗号流水句过长 | 按呼吸单元拆行（`colloquial-craft.md`） |

## 使用边界

- 本子集只管「念出来才暴露」的模式，不企图覆盖所有中文写作问题。
- AI 腔是「对真人听众的质量问题」，不是检测器博弈——detector-evasion 边界声明见 SKILL.md Operating Principles。
