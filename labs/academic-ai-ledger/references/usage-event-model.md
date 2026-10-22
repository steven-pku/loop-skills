# 使用事件模型

## 15 个字段

| 字段 | 内容 | 缺失时 |
|---|---|---|
| Event ID | 唯一编号，格式 `EV01`、`EV02` | 不允许缺失 |
| Date | 日期与时间范围 | 标 `Unknown`，写入缺失记录清单 |
| Tool | 工具名称 | 标 `Unknown` |
| Version／Model | 版本或模型名 | 标 `Unknown`，不按记忆猜测 |
| Purpose | 使用目的 | 标 `Unknown` |
| Paper Stage | 选题、检索、整理、方法、数据、分析、写作、润色、翻译、格式 | 标 `Unknown` |
| Input Summary | 输入内容摘要，不必粘贴原始提示词 | 标 `Unknown` |
| Output Summary | 输出内容摘要 | 标 `Unknown` |
| Adopted Content | 实际采用进论文的内容与位置 | 标 `Unknown`，并降低可追踪性评分 |
| Human Verification | 人工核验方式与结论 | 标 `Not verified`，不写成已核验 |
| Final Modification | 用户在采用后做的修改 | 标 `Unknown` |
| Policy Basis | 对应规则条款与原文位置 | 标 `Policy Missing` |
| Risk Level | `Low`／`Medium`／`High`／`Prohibited` | 无政策时标 `Unassessed` |
| Evidence | 对话、版本、截图、文件、时间戳 | 标 `Unknown`，按 `E0` 处理 |
| Disclosure Needed | `Yes`／`No`／`Need Confirmation` | 无政策时标 `Need Confirmation` |

## 记录纪律

- 只记录用户能确认的事实；
- 记忆模糊时记录区间，例如“5 月中旬某天”，不编造具体日期；
- 不反向补造不存在的时间、版本、提示词、对话或证据；
- 不为了让账本看起来完整而合并或拆分事件；
- 一次连续会话内的同一目的使用记为一个事件，跨目的或跨阶段分开记。

## 追加规则

账本是追加式记录：

1. 新事件追加到表尾，Event ID 递增，不复用；
2. 已有行的字段内容不直接改写；
3. 表头、frontmatter 与历史行保持原样；
4. `updated` 覆盖为当前日期；
5. 追加后逐项检查：Event ID 唯一、时间顺序可读、披露引用的 Event 存在。

## 更正规则

发现记录有误时，追加一条 `Correction Event`：

```markdown
| EV07-C1 | 2026-07-28 | — | — | 更正 EV07 的 Version／Model | — | — | — | — | — | — | — | — | 用户当日截图 | — |
- corrects: EV07
- 原记录：Version／Model 记为 Unknown
- 更正为：某工具 2026 年 5 月版本
- 更正依据：用户当日截图
- 更正时间：2026-07-28
```

规则：

- 原 Event 行保留，只在其备注中标 `已被 EV07-C1 更正`；
- 更正必须写明依据，没有依据就不更正，只标 `Unknown`；
- 更正不能把时间往前改，也不能删除已披露过的事件；
- 静默改写历史等同伪造记录，判 Fatal。

## 缺失记录清单

每轮输出一张缺失表：

| Event ID | 缺失字段 | 影响 | 可补方式 | 是否可补 |
|---|---|---|---|---|

“可补方式”只列真实可行动作：翻查工具历史记录、找回文档版本、查邮件时间戳、请导师确认。不包括“凭印象补写”。

## 与状态卡的关系

状态卡记录 `event_ids` 与 `last_event_id`。恢复会话时先核对账本中实际存在的 Event，与状态卡不一致时以账本文件为准，并把差异写进 Unknowns。
