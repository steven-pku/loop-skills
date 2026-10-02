# Expected: Fatal — 进行中写成已完成

- Skill must catch the internal contradiction: "完成订单系统重构并上线" vs 下周计划 "继续推进订单系统联调与压测"; "完成数据看板开发交付使用" vs 下周 "灰度测试收集反馈". Something claimed done cannot still need 联调/灰度 next week.
- This is a fatal issue: report contradicts reality (in-progress claimed as done) — the ledger-conflict fatal.
- Skill should require the item be rewritten as a milestone state (e.g. "重构完成，进入联调，预计 X 上线") rather than "完成上线".
- 数据支撑 should also flag "性能大幅提升" as unquantified (no number, no 〔待补数据〕).
- Pass condition: contradiction caught + flagged fatal + rewrite toward honest milestone state.
- Fail condition: skill accepts "完成上线" as a real result and scores it as strong 成果导向.
