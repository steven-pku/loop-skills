# Decision Memo Template

The memo is the anti-hindsight artifact: it freezes what was knowable at decision time so the retrospective judges the process fairly. Memory rewrites itself; the memo does not.

```markdown
# 决策备忘录：〔决策问题一句话〕

- **日期**：YYYY-MM-DD
- **Status**：Proposed / 待决定   <!-- only explicit user confirmation changes this to Decided -->
- **Gate**：Type 1 / Type 2 + 理由
- **建议选择**：选项 X（用户确认后才改为「最终选择」）
- **当时的真选项**：（含各自「理性人理由」与主观概率——照抄 brief，不美化）
- **载重证据**（F 标签保留）：
- **当时明确未知的**：
- **红队结论**：幸存反对意见含否决条件原样保留；若为零，保留四条攻击线的检验依据、排除理由与残留未知：
- **止损位**：信号 / owner / 动作
- **预设复盘日期**：YYYY-MM-DD（写进你真会看到的地方——日历/任务系统）
- **决策时刻状态**：（时间压力/情绪，照抄 brief）
```

## Lifecycle rules

- **Proposed / 待决定**：模型完成分析或给出建议，但用户尚未明确确认。偏好、已付成本、索取建议或模型高置信度都不等于决定。
- **Decided**：用户明确确认选择后才进入；模型不得代用户推进此状态。
- **Under review**：到达复盘日期或止损信号触发。
- **Confirmed**：复盘后维持；**Reversed**：执行了止损/回滚；**Superseded**：被新决策替代（链接新备忘录）。
- Status 变更只追加不改写历史（append a dated line, never edit the frozen sections）。

## Retrospective hooks

Keep planned review dates, evidenced actual reviews, and the present retrospective date separate. Missing execution records leave completion timing unknown; a later retrospective request alone does not prove a missed checkpoint or delay.

复盘模式（SKILL.md · Retrospective Mode）依赖本模板的三个字段工作：

1. 「当时明确未知的」——区分「不可知」与「没去查」，复盘时最常见的翻案点
2. 「红队结论」——对照幸存意见及否决条件，或无新增发现时的检验依据与残留未知，检查红队是否攻在要害
3. 「主观概率」——校准原料：说 70% 的事发生了没有？跨多份备忘录看系统性偏差

**过程／结果分离提醒**：先沿用原 Gate——Type 1 才用 Full Loop rubric；Type 2 默认只复盘当时的 1-3 个因素、建议、退出条件与是否按信号回退，不因缺 steelman／premortem／三选项扣分。结果尚未知时先完成过程评估，再揭结果。结果已经泄露时，outcome blindness 无法恢复：第一句先声明污染，不先给总判词、安慰、责备或分数；把「决策时已知」与「事后才知」分栏，后者不得倒灌过程扣分。缺字段只能写「所给 memo 未记录」，不能断言当时没做。合同／书面承诺的法律效力未经专业核验一律标 F3／未知。完成过程证据段后才单独讨论结果，并把评估标为「hindsight-exposed」。
