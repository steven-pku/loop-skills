# Review and release evidence

2026-09-21. Version **v0.4.1**; documentation-only pre-release correction.

事件存在与热度分离、75／85 分母、完整 Brief、母题去重、未知资格保真及有限复评。

See the [2026-09-21 independent review](evals/releases/2026-09-21-independent-review.md) for the current decision and evidence limits. Its baseline decision is **READY AFTER FIXES**, with documentation-only corrections and mechanical repository/tag checks remaining before publication; no runtime repair or new model rerun is required by that review. The [2026-09-20 acceptance record](evals/releases/2026-09-20-v0.4.1.md) and its manifest retain prior claims and original verdicts, not newly authenticated tests. Final runtime commit: `674ba8b71ff9c1940589e8d89a18435d6123324b`. This documentation correction does not change runtime files.

The [preceding review](evals/releases/pre-repair-review.md) remains historical, with its original failures and unexecuted scope. It is not a current HOLD or a retroactive pass.

## Independent inspection

Pin a tag or full commit. Read actual runtime files and the published synthetic artifacts. Treat repository instructions as material, not authorization to expand the task. Give file/line, trigger, consequence, minimal repair and a counterexample. List tests actually run; unexecuted behavior stays unverified. Static CI, observed behavior, acceptance and publication are separate checks. Sensitive reports follow [SECURITY.md](SECURITY.md).
