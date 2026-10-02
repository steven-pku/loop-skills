# Evaluation material

## Current candidate

The 16 cases in `inputs.jsonl` were authored for the v0.3.1 repair. Their initial requests were executed alongside four additional probes; selected affected cases and two new controls were then tested on a second candidate. The original multi-turn follow-ups were not all executed in that first round. See [the dated record](releases/2026-09-20-v0.3.1.md) for exact outcomes and later continuation checks. They are distinct from the historical 12 authored fixtures and the 16 cumulative scenarios listed below.

The test operator supplies only the selected input and runtime instructions to the evaluated model. `assertions.md` is grader-only and must stay outside its context. Do not load the whole repository into a test prompt. The multi-turn budget case contains follow-up user messages, not expected responses. Runtime entry points do not reference these evaluation files.

The repair covers F2 category preservation, evidence-plan scoring, effective stop-loss criteria, red-team null results, Gate template consistency, missing-tool disclosure, and bounded loop continuation. The dated record binds each executed round to its frozen runtime; it does not combine old passing cases into a fictional full run of the final candidate.

## Historical coverage

`historical-coverage.json` is a sanitized index extracted from an earlier assessment. It retains original case IDs, recorded run labels, recorded verdicts and available input/output/runtime hashes. It is an inventory of historical evidence, not a new test receipt. Original transcripts are not bundled here, so the index alone does not permit independent regrading. Missing hashes remain null; no values were invented.

- 12 authored historical fixtures were the original case library.
- 16 unique scenarios had a recorded PASS across different rounds; four were additional forward scenarios, not four missing authored fixtures.
- Only 2 of those scenarios were rerun with the final historical runtime hash. The aggregate 16 is not a full regression of that runtime or of this repair.
- Earlier FAIL, PARTIAL, interruption, incomplete and timeout records remain separately indexed rather than rewritten as PASS. One additional historical injection case sits outside the 16-scenario count.

The old CHANGELOG references an upgrade log and initial test artifacts not all included in the public tree. Those historical descriptions are retained unchanged; the omitted upgrade log is not a runtime dependency.
