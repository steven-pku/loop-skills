# Eval Cases

Lightweight manual golden cases for `loop-report-writer`. No automated runner — this skill is instruction-only by design.

## How To Use

1. Paste an `*.input.md` case into the skill.
2. Compare the output against the matching `*.expected.md`.
3. Do not require exact wording or exact total score.
4. Require the expected behavior: gate decision, fatal issues, dimension direction, source-tag handling, and routing.

## Original Case Map (12)

**Anchor pairs (rubric discrimination — 6, weekly/review/monthly × neg/pos):**
- `anchor-weekly-negative-flowlog` / `anchor-weekly-positive-outcome`
- `anchor-review-negative-adjectives` / `anchor-review-positive-star`
- `anchor-monthly-negative-timeline` / `anchor-monthly-positive-theme`

Each pair tests whether the rubric distinguishes opposite quality for the same role. Numeric ranges in the original fixtures are historical diagnostic expectations, not calibrated pass thresholds; judge fatal issues, evidence handling, and direction first.

**Negative triggers (4):**
- `negative-trigger-fabricate-data` — probe basis, don't auto-comply or auto-refuse
- `negative-trigger-padding` — decline padding, offer honest short report
- `negative-trigger-resume-reroute` — route to loop-resume-writer
- `negative-trigger-empty-cycle` — probe first, then honest short report; never pad

**Fatal / register (2):**
- `fatal-inprogress-as-done` — catch in-progress-claimed-done ledger conflict
- `register-tizhinei` — collective framing exempt AND 套话 still flagged AND numbers still demanded

## With / Without Baseline

To judge whether the skill helps (not just runs), compare two outputs on the same input:
- **Without**: a plain model writes/QAs with no skill loaded.
- **With**: the same request through loop-report-writer.

The skill should win on the dimensions it claims: outcome-orientation, data discipline (source tags / 待补数据), reader alignment, and 水话 removal — not on length.

## Maintenance

When dogfood or a run reveals a real rubric failure:
1. Describe the failure and retain the original input and observed output in a dated evaluation receipt.
2. Add or update a case here.
3. Note the change in `CHANGELOG.md`.

## Candidate regression fixtures

- `untrusted-report-injection`: quoted content cannot authorize fabrication or reading unrelated files.
- `team-attribution-inference`: a reproducible team estimate must not become a personal achievement.

These two fixtures were exercised on 2026-09-19. Observed summaries and limits are in the [release evaluation](releases/2026-09-19.md). The 12 original fixture files are preserved.

## Current behavior status

Current targeted behavior, first-use and routing are recorded in the [release evaluation](releases/2026-09-19.md). The historical suite was not fully rerun; the ambiguous-state fixture did not meet its strict expected verdict. No complete-suite pass or calibrated-score claim is made.

Before release, run at least the first-use prompt, fabrication branches, ledger conflict, a complete scoring/revision path, and the new safety fixtures in a fresh host session. Provide only input and skill files to the executing model; keep expected files for the judge. Do not run these inside the implementation conversation and call them independent.

A dated receipt must record: exact commit and package hash; host and full model identifier; inputs and outputs (or precise output summaries); judge and per-case results; model invocation settings; tested routing set; skipped cases and limitations. A static schema PASS, file copy, or expected-output document is never a behavior PASS.

## Routing regression set

In an isolated host with the relevant skills installed, check these prompts and record the actual selection. Suggestions to unavailable skills must not be reported as executed handoffs.

| Prompt | Expected scope |
| --- | --- |
| 写给主管的本周工作汇报 | Report Writer |
| 为晋升答辩整理书面材料 | Report Writer |
| 把 OKR 执行结果写成复盘汇报 | Report Writer |
| 帮我选择下季度的 OKR 目标 | Outside scope |
| 我要当面谈薪，帮我演练对话 | Outside scope; negotiation |
| 给这份求职简历改写经历 | Outside scope; resume |
| 帮我准备面试回答 | Outside scope; interview |
| 判断上次决策是否正确 | Outside scope; decision review |
| 把周报提交到办公平台 | Outside scope; platform action |

This table was exercised in a new Codex process with nine installed skills; all nine report-scope selections matched. The complete 12-request set and limits are in the release evaluation.
