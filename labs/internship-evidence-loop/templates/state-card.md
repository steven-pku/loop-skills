# Loop State Card

```markdown
## LOOP_STATE
- case_id:
- skill: internship-evidence-loop
- skill_version: 0.1.0
- current_phase:
- user_goal:
- deadline:
- scope_verdict:
- week_index:
- internship_period:
- target_role:
- confirmed_facts:
- assumptions:
- unknowns:
- evidence_received:
- ledger_events:
- evidence_levels:
- attribution_flags:
- confidentiality_flags:
- open_fatal_issues:
- open_major_issues:
- completed_actions:
- next_actions:
- next_evidence_actions:
- artifacts:
- current_score:
- revision_round:
- max_rounds: 2
- stop_reason:
- updated_at:
```

字段说明：

- `week_index`：当前是第几周，跨周恢复的主键；
- `ledger_events`：已入账的 Event ID 列表，不含已作废条目；
- `evidence_levels`：各 Event ID 的当前等级，例如 `W02-01:E2`；
- `attribution_flags`：归因仍不清楚的 Event ID；
- `confidentiality_flags`：需脱敏或禁止外传的 Event ID；
- `next_evidence_actions`：下周补证动作，与账本表格一一对应；
- `max_rounds`：单次会话的修订上限，固定为 2，跨周运行不累计。

## 跨周恢复规则

1. 先核对 Skill 名称、版本与 `week_index`；
2. 重建 Facts／Assumptions／Unknowns；
3. 逐条核对 `ledger_events` 对应的证据现在是否仍能取得；
4. 不信任卡片中声称已有证据却拿不出材料的条目，等级降回 E1；
5. 检查上周 `next_evidence_actions` 的完成情况，未完成的写明原因，不静默删除；
6. 从最高优先级的 `next_actions` 继续，`revision_round` 在新一周归零。

## 累积检查

连续多周运行时，每周额外检查：

- 事件总数是否只增不减；
- 是否出现同一事实被重复入账；
- 是否有事件长期停在 E0 或 E1，需要重新评估是否值得补证；
- 归因或保密标记是否随新信息更新。
