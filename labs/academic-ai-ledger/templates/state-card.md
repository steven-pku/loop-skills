# Loop State Card

```markdown
## LOOP_STATE
- case_id:
- skill: academic-ai-ledger
- skill_version: 0.1.0
- current_phase:
- user_goal:
- deadline:
- scope_verdict:
- policy_status:
- applicable_policies:
- confirmed_facts:
- assumptions:
- unknowns:
- evidence_received:
- event_ids:
- last_event_id:
- correction_events:
- open_fatal_issues:
- open_major_issues:
- remediation_actions:
- disclosure_status:
- completed_actions:
- next_actions:
- artifacts:
- current_score:
- revision_round:
- max_rounds: not_applicable
- stop_reason:
- updated_at:
```

`max_rounds` 固定为 `not_applicable`：Compliance Ledger 不设总轮次上限，每次新增事件只做一次审计。

`current_score` 只在适用政策存在时填写，否则填 `Cannot Assess`。

恢复规则：

1. 先检查 Skill 名称和版本；
2. 以账本文件中实际存在的 Event 为准，与 `event_ids` 不一致时把差异写进 Unknowns；
3. 重建 Facts／Assumptions／Unknowns；
4. 核对 `applicable_policies` 的版本与适用对象是否仍然成立；
5. 不信任卡片中声称已核验但没有证据的字段；
6. 从 `next_actions` 的最高优先级继续。
