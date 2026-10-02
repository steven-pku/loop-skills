# Changelog

All notable changes to this skill are documented here. Format based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); this skill follows semantic-ish versioning on `metadata.version`.

## [0.3.1] — 2026-09-19

First public release. Date is UTC.

### Added

- Project-scoped installation instructions and an English overview.
- Security and contribution guidance, plus static-only CI checks.
- Explicit untrusted-content, privacy, and detector-evasion boundaries.
- Synthetic prompt-injection and attribution regression fixtures.

### Fixed

- Removed obsolete 82–84 score bands from the scorecard; it now follows the qualitative rubric and two-loop halt.
- Removed an unsupported qualitative claim from the fabrication-refusal example.
- Removed an unmeasured timing claim from the weekly example.
- Shortened discovery metadata while preserving routing boundaries in the skill body.

### Validation

- A fresh model behavior evaluation and same-install routing regression are still required. Historical evaluations are not current-version passes.

## [0.3.0] - 2026-07-07

Multi-model cross-review (GPT-5 Codex / Kimi / GLM — all external, non-Anthropic). Verdict was unanimous "部分夸大 (partial overclaim)": the differentiation (anti-fabrication ledger, Value Gate, evidence grading) is real, but stability and the self-verification conclusions were overstated. Fixes below; the original review archive is not distributed. These are historical review conclusions, not a current behavior run.

### Added
- **README.md** (human-facing landing page, with an honest "反造假边界" scope + a "质量记录" section stating the skill is a prompt reference, not a proven-stable system).
- **LICENSE** (MIT full text; frontmatter declared MIT but the file was missing).

### Fixed
- **85-threshold demoted from gate to directional diagnostic**: the score is not a calibrated gate — the same draft can differ by tens of points across models (this skill's own isolated test: flow-log input self-estimated 58 vs blind-run 19). Removed the narrow 82-84 borderline band (narrower than the scoring noise). `SKILL.md`, `references/report-rubric.md`. (council H4)
- **Rubric non-orthogonality made explicit**: 成果导向 25 and 数据支撑 20 are correlated, not orthogonal; a pure flow-log lowers both dimensions *and* trips fatal #2/#3 — the same defect projected three ways. Readers are told to treat it as one fatal, not three stacked score deductions. `references/report-rubric.md`. (council H2)
- **Reasonable-inference self-scoped + team→individual leak closed**: the ledger's own example (`日均 40 分钟 × 5 人 × 22 天 ≈ 73 小时/月`) was a team total presented as reasonable inference — replaced with an individual-attributable example + a hard line that the inference subject must match the claimed subject (team totals may not be written as personal contribution). Added an honest disclaim: 甄别依据 verifies the user can *state* a reproducible basis, not that the basis is *true*; the skill guarantees traceability + honest labeling, not truth. `references/results-ledger.md`. (council H5)
- **Description no longer says "绝不编造成绩"** (二元表述漏掉「合理推算」第三档): now "数据只用你提供的、有依据的推算（附依据）、或标〔待补数据〕，不无依据编造成绩". `SKILL.md`. (council H6)
- **Risk dimension teeth without reweighting**: the <6 band now distinguishes (a) genuinely no-risk-but-with-verifiable-plan (light deduction, don't force invented risks) from (b) all-smooth-no-verifiable-status (near-fatal → Revise). Added an "一切顺利型" near-fatal. `references/report-rubric.md`. (council H7)
- **User-refuses-to-engage-gate hard exit**: Value Gate is a heuristic, not a mechanism that forces cooperation. When a user insists "别问了照我说的写", state the boundary once and output the honest floor over verifiable material with an explicit note, rather than silently complying into padding. `SKILL.md`, `references/value-gate-guide.md`. (council H8)
- **fatal #4 scoped to 述职/晋升**: added a header note that fatals are judged in-scenario, and marked #4 (no-case-support) as not applying to 周报/月报. `references/report-rubric.md`. (council H9)
- **QA Only with no independent ledger**: truthfulness audit downgrades to an internal-consistency + suspect-number check (catch self-contradiction, in-progress-as-done, unsourced numbers); unverifiable results get flagged 存疑 rather than scored clean. `SKILL.md`, `references/report-rubric.md`. (council H10)
- **"15 分钟" no longer advertised as fixed**: fast only when raw material already carries outcomes; a flow-log input's user round-trip dominates elapsed time. `SKILL.md`. (council H11)
- **Isolated-test claims made honest**: recorded that the subagents were same-family Claude models (removes informed-rater bias, not same-family bias); removed overclaims ("消除运动员兼裁判", "instruction 本身足以引导", "差异化假设实战成立"); noted the scoring path was never isolation-tested (single-turn only reached probing). the original development log (not distributed). (council H3, H12)
- **Unsourced frequency claim softened**: "多数『没干啥』是没意识到价值" reframed as an experience-based judgment, not a citable statistic (aligns with the skill's own evidence-notes standard). `references/value-gate-guide.md`. (council H12)

## [0.2.0] - 2026-07-06

### Fixed
- **Anti-fabrication upgraded from blanket-refusal to "甄别依据" two branches**: a vague number ("大概 30%") is first probed for basis — a statable reproducible basis → reasonable-inference tag (legitimate); pure gut feel / "make it look good" → decline. Fixes v0.1 over-refusal of honest estimates. `references/results-ledger.md`.
- **"周报快环 15 分钟" wording made honest**: 15 min applies when material already carries outcome info; a pure activity-log input first goes through the materials question round-trip. `references/value-gate-guide.md`, `SKILL.md`.

### Notes
- Synthetic dogfood (4 synthetic cases across three registers + three output modes + negative case) + v0.2 re-run. See the original development log (not distributed) (2026-07-06).

## [0.1.0] - 2026-07-06

### Added
- Initial skeleton: Chinese workplace-report QA-loop skill.
- Value Gate (two questions + fast iteration + thin-cycle honest short report); results ledger (schema v1, three-tier source tags, fabrication refusal, 甄别依据); 6-dimension rubric + fatal list; 2-loop hard stop + Graceful Halt; scenario skeletons (周报/月报/述职/晋升/复盘) + level-transition framework + 三档语域; evidence-graded structural claims.
- 6 references + 3 assets + 3 examples + 12 eval cases.
