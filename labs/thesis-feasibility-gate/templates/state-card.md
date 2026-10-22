# Loop State Card

```markdown
## LOOP_STATE
- case_id:
- skill: thesis-feasibility-gate
- skill_version: 0.1.0
- current_phase:
- user_goal:
- deadline:
- scope_verdict:
- feasibility_verdict:
- confirmed_facts:
- assumptions:
- unknowns:
- evidence_received:
- gate_scores:
- unknown_gates:
- open_fatal_issues:
- open_major_issues:
- scope_operators_used:
- completed_actions:
- next_actions:
- artifacts:
- current_score:
- revision_round:
- max_rounds: 2
- stop_reason:
- updated_at:
```

字段说明：

- `revision_round` 记缩题轮次，上限 2；
- `gate_scores` 按「问题／数据／测量／方法／资源／伦理」顺序填 0–5 或 `Unknown`；
- `feasibility_verdict` 只能是 `GO`、`GO WITH CONDITIONS`、`NO-GO`；
- `scope_operators_used` 记录每轮使用的缩题运算符。

恢复规则：

1. 先核对 Skill 名称与版本；
2. 重建 Facts／Assumptions／Unknowns；
3. 核对闸门分是否仍有证据支撑，没有证据的高分闸门降回 `Unknown`；
4. 核对缩题轮次，已达 2 轮时不得再开新轮；
5. 不信任卡片中声称已确认但没有来源的数据可得性；
6. 从 `next_actions` 的最高优先级继续。
