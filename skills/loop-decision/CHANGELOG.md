# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.3.1] - 2026-09-20

### Fixed

- Distinguish unassessed initial red-team work from observed poor red-team work; omit a total instead of assigning a strawman score to missing records. Align the worked example.

- Preserve F2 claim category independently of verification state; qualifying a
  checkable claim as a guess cannot bypass the load-bearing evidence gate.
- Align verified, pending-with-effective-plan, and pending-without-plan evidence
  bands; retain the offer example's 16/20 evidence score and 87/100 total with an
  explicit pre-commitment verification plan and feasible fallback.
- Define effective stop-loss signals, owners, and actions consistently across
  the rubric, fatal rules, and example; decorative placeholders remain fatal.
- Score red-team coverage and evidence rather than requiring a quota of surviving
  objections; allow documented, evidence-based null results in the memo.
- Align the Brief Gate field, disclose unavailable source-checking tools, and
  preserve cumulative loop counts through explicitly bounded user extensions.
- Add separated repair inputs and grader expectations, plus a sanitized
  historical coverage index, and a dated current evaluation record that preserves first-round failures and targeted retests.
- Preserve historical changelog entries and explain omitted historical artifacts
  without treating them as current runtime dependencies.

## [0.2.1] - 2026-09-20

### Changed

- Shortened the routing description to fit host skill-index limits while
  preserving the Type 2 fast path, full-loop triggers, retrospective mode,
  and exclusions.
- Aligned QA-loop labels across the runtime instructions and rubric, clarified
  that Borderline can mean one or two weak dimensions, and added confidence
  anchors to the premortem protocol.
- Corrected the worked example to run all four live options and added its
  initial/revised scorecard excerpt.
- Added evidence-tier labels to red-team sources and removed internal eval
  provenance from the public example.
- Tightened bilingual README installation, first-success, privacy, and
  unpublished-sibling boundaries.
- Made the Gate authoritative over mode words: a Type 1 request cannot bypass
  the Full Loop merely by asking for a fast triage.
- Clarified that a revealed outcome cannot become outcome-blind again; the
  process assessment stays separate but is labeled hindsight-exposed.
- Replaced global installation examples with pinned, project-local commands
  explicitly marked for post-publication verification, and hardened public
  security-reporting guidance.
- Added a pre-Gate hard stop for prescription and psychiatric medication
  changes; disclaimers and “safety analysis” labels cannot resume the loop.
- Made Type 2 output intentionally short and prohibited Decision Briefs,
  forced three-option tables, and invented numeric weighting matrices.
- Required hindsight-contamination disclosure as the first sentence whenever
  the outcome is already known, before any verdict, reassurance, or score.
- Added a retrospective evidence firewall: later events cannot become
  decision-time deductions, missing records are not proof of missing process,
  and unverified contract effects remain F3/unknown.
- Preserved Gate proportionality during review, so Type 2 decisions are not
  scored against Full Loop artifacts unless the user requests an optional
  diagnostic—and even then those artifacts were not historical requirements.
- Made decision ownership explicit: model recommendations remain `Proposed`
  until the user confirms, and cannot be recorded as `Decided` by inference.
- Tightened premortem credibility so unsupported plausible assumptions remain
  Medium/F2-pending at most; High requires direct evidence or a relevant
  precedent.

## [0.2.0] - 2026-07-13

### Changed

- Fresh-context validation surfaced and fixed five spec
  ambiguities: fatal #4 (Type 1 premortem) now applies at memo stage only,
  not on the pre-premortem initial scorecard; load-bearing F2 with a
  precondition-style verification plan no longer trips the hearsay fatal;
  QA-loop counting clarified (one full loop = score → passes → revise →
  re-score, both scorecards share the number); spoiled-outcome and
  claimed-memo-without-text fallbacks added to Retrospective Mode; the
  reversibility gate is explicitly non-overridable by a single insistent
  request (cost-based re-classification stays legitimate).
- Description tightened for series routing: added let-through pointers so
  negotiation / report-writer defer decision-proper questions correctly.

### Added

- Twelve golden cases covering rubric discrimination, routing, Type 2
  fast-path behavior, conclusion-first detection, and outcome-blind review.
- `examples/offer-decision-full-loop.md`.

## [0.1.0] - 2026-07-12

### Added

- Initial build: `SKILL.md` with reversibility gate (Type 1/2), decision brief,
  six-dimension rubric (选项充分性 / 证据强度 / 对立面强度 / 失败预案 /
  利益相关方 / 时机), premortem pass, red team pass, decision memo with preset
  review date, and outcome-blind retrospective mode.
- `references/`: brief template, scoring rubric, premortem protocol, red team
  protocol, memo template, F0-F3 evidence grading, full source anchors with
  misquote corrections, upgrade log.
- Process/outcome score separation and outcome-blind retrospective ordering as
  structural anti-resulting guards.
