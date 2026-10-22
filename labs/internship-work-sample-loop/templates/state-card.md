# Loop State Card

```markdown
## LOOP_STATE
- case_id:
- skill: internship-work-sample-loop
- skill_version: 0.1.0
- current_phase:
- user_goal:
- deadline:
- scope_verdict:
- target_role_family:
- confirmed_facts:
- assumptions:
- unknowns:
- evidence_received:
- jd_item_ids:
- selected_gap:
- selected_project:
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

恢复规则：

1. 先检查 Skill 名称和版本；
2. 重建 Facts／Assumptions／Unknowns；
3. 核对证据编号对应的产物是否仍然存在；
4. 不信任卡片中声称已完成但没有产物的状态，缺产物一律重开；
5. 核对 `selected_project` 是否仍在 5–7 天可完成范围内，剩余时间不足时缩小范围而非提速；
6. 从 `next_actions` 的最高优先级继续；
7. `revision_round` 已达 `max_rounds` 时不再开新轮，输出最佳现状与未解决问题。
