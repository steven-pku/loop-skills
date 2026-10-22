# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### 0.3.1 candidate

- Separate trusted task instructions from dataset and report text provenance,
  including both synthetic-to-real and real-to-synthetic injection directions.
- Scope scorecards to real-data diagnosis reports, report-text review, or
  arithmetic demonstrations; retain user-transcription verification limits.
- Preserve claim qualifiers without making them an exemption from scrutiny;
  replace a baseline-return forecast example with a testable observation goal.
- Use two default revision-and-regrade loops with explicit finite extensions
  and cumulative counters, and clarify permitted public-source read boundaries.
- Keep historical failed outputs, receipts, assertions, and release history
  unchanged. These are static repairs awaiting fresh behavior validation.

## [0.3.0] - 2026-09-20

### Changed

- Replaced absolute platform assertions with a current-primary-source gate:
  unverifiable rules are downgraded, marked `〔待核〕`, and removed from the
  causal path.
- Added explicit privacy, credential, untrusted-content, and no-account-action
  boundaries; tightened the skill description to under 300 characters.
- Corrected evidence grades, recommendation routing, and platform reference
  labels so media paraphrases cannot appear as official evidence.
- Separated evidence category from verification status; synthetic numbers,
  placeholders, unreadable screenshots, and remembered estimates no longer
  unlock attribution.
- Required comparable metric definitions, observation windows, and
  distribution stages before cross-post count or ratio judgments.
- Split spoken-video script routing from article/image-sequence routing and
  changed one-post regression hooks from "falsified" to "not supported yet".

### Added

- A public synthetic example covering the no-data quality-only downgrade and
  the refusal branch when a user requests attribution without metrics.
- A dated current-eval assertion file that corrects historical arithmetic,
  evidence, routing, and score-gap expectations without rewriting old runs.

## [0.2.0] - 2026-07-13

### Changed

- Clarified five behavior ambiguities: screenshot/export = B,
  hand-transcribed metrics = B with disclosure, and remembered values = C;
  dimension guidance is self-contained; batch mode is pattern-level; a gate
  refusal produces no scorecard; partial baselines leave uncovered dimensions
  at D instead of blocking the whole diagnosis.
- Description tightened for series routing: topic-picker now points 发布后
  归因 requests to this skill.

### Added

- Twelve manual golden cases covering evidence grades, no-data refusal,
  invented benchmarks, routing, throttling claims, and small samples.
- `examples/single-post-diagnosis.md` as a public synthetic worked example.

## [0.1.0] - 2026-07-12

### Added

- Initial build: `SKILL.md` with Data Gate (real metrics or explicit
  downgrade), per-dimension diagnosis (six dimensions), attribution honesty
  grading (A official / B data-backed / C consensus / D hypothesis),
  five attribution guards, executable improvement rules with routing tags,
  and regression hooks; three output modes (单条诊断 / 批量复盘 / 无数据质检).
- `references/`: attribution-honesty manual (with official-debunk list and
  the CES cautionary tale), four platform metric files with per-claim
  evidence grades, diagnosis dimensions manual, improvement-rule standard,
  diagnosis-quality rubric, upgrade log.
