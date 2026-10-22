# Loop State Card

```markdown
## LOOP_STATE
- case_id:
- skill: survey-preflight-loop
- skill_version: 0.1.0
- current_phase:
- user_goal:
- deadline:
- scope_verdict:
- release_verdict:
- confirmed_facts:
- assumptions:
- unknowns:
- evidence_received:
- construct_coverage:
- audited_items:
- open_fatal_issues:
- open_major_issues:
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

- `scope_verdict`：`IN_SCOPE`、`OUT_OF_SCOPE`、`PROHIBITED`；
- `release_verdict`：`可发`、`修改后可发`、`暂停发放`；
- `construct_coverage`：核心变量覆盖率与未覆盖变量名；
- `audited_items`：已审计题号范围；
- `artifacts`：本轮已产出的交付物名称。

恢复规则：

1. 先核对 Skill 名称与版本；
2. 重建 Facts／Assumptions／Unknowns；
3. 核对卡片声称的修复在修订版问卷中是否真的存在；
4. 没有修订版问卷佐证的 `Fixed` 一律重开为 `Open`；
5. `revision_round` 已达 `max_rounds` 且仍有 Fatal 时，直接输出 `暂停发放` 并停止，不开新一轮；
6. 从 `next_actions` 的最高优先级继续。
