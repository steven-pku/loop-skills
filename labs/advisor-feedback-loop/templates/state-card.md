# Loop State Card

```markdown
## LOOP_STATE
- case_id:
- skill: advisor-feedback-loop
- skill_version: 0.1.0
- current_phase:
- user_goal:
- deadline:
- scope_verdict:
- confirmed_facts:
- assumptions:
- unknowns:
- evidence_received:
- feedback_ids:
- open_fatal_issues:
- open_major_issues:
- completed_actions:
- next_actions:
- artifacts:
- current_score:
- revision_round:
- max_rounds: 3
- stop_reason:
- updated_at:
```

`revision_round` 记已完成的「用户修订 → 评审 → 评分」次数；只完成诊断与计划时记 0。

恢复规则：

1. 先检查 Skill 名称和版本；
2. 重建 Facts／Assumptions／Unknowns；
3. 核对 Feedback ID 和证据是否仍存在；
4. 不信任卡片中声称已完成但没有证据的状态；
5. `current_score` 与 `revision_round` 按本轮证据重算，不直接采信卡片数值；
6. 从 `next_actions` 的最高优先级继续。
