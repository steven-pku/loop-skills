# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.3.1] - 2026-09-20

### Fixed

- Replaced unsupported causal and guaranteed-outcome claims in the Full Loop
  teaching example; checked facts across the whole draft, not only its hook.
- Defined one explicit duration adjustment: deviations above 15% through 30%
  cap the rhythm score at 17 without a second band deduction.
- Separated diagnostic drafts with unresolved facts from ready-to-voice scripts.
- Clarified promise-fatal deduplication and counted targeted agent rewrites
  within the same two-revision budget, with bounded explicit continuation.
- Added self-contained current test fixtures; preserved earlier cases and
  errata as versioned history rather than rewriting prior evidence.

## [0.3.0] - 2026-09-20

### Changed

- Made the runtime package self-contained: the oral AI-tone reference no
  longer points to a private or separately installed repository, and the
  main instructions no longer load a contributor-only upgrade log.
- Reclassified platform evidence so platform statements, reported statements,
  platform-site external contributions, and craft heuristics are not conflated.
- Recast the 240-350 characters-per-minute profiles as overrideable planning
  assumptions rather than official or universal speech-rate standards.
- Added explicit privacy, external-action, human-review, and no-guarantee
  boundaries to the runtime instructions and public documentation.
- Shortened the skill description to 203 characters while preserving the
  main triggers and routing exclusions.
- Capped hook-only rewrites at two attempts, made QA Only strictly diagnostic,
  and clarified that iteration limits are not time-to-completion promises.
- Standardized the duration fatal boundary as deviation greater than 30%.
- Required complete source text for adaptation and compression; summaries,
  placeholders, and unreadable attachments cannot be reconstructed as source.
- Replaced unverified CLI install claims with a project-scoped, tag-pinned
  v0.3.0 path explicitly marked pending post-release verification.

### Fixed

- Recast the Full Loop example as an explicitly hypothetical, editorially
  corrected teaching example without inventing user experience; fixed its
  spoken-count convention and distinguished illustration from runtime evidence.
- Corrected the QA Only removal count to 72 characters and kept diagnostic
  follow-ups outside the revision counter.
- Added the missing short-digression density anchor; corrected the example
  score to its stated band without combining separate passages into a plateau.
- Replaced unsupported numerical claims in the two-column format example.

- Removed a fact-discipline example that could induce a fabricated first-person
  experience when the user had not supplied one.
- Added a dated v0.3.0 eval errata for frozen legacy fixtures and a complete
  synthetic compression probe.

### Added

- A self-contained QA Only example that demonstrates a duration verdict
  flipping between 260 and 300 characters-per-minute assumptions.
- A fuller Full Loop example with score evidence, counting-range disclosure,
  and before/after revision evidence.

## [0.2.0] - 2026-07-13

### Changed

- Pre-release validation surfaced and fixed five spec ambiguities: explicit
  character-counting rules for the duration fatal
  (Arabic numerals and English abbreviations count by spoken length,
  punctuation excluded) plus a borderline-sensitivity protocol; the 15-30%
  duration deviation now lands as one band down in 口语化与节奏； QA Only
  must state its assumed pace tier and confirm when the verdict flips
  across tiers; a two-candidate rule for self-drafted hooks (a from-scratch
  opening grades itself too kindly); the promise-unkept fatal covers only
  made-but-unkept promises (a promise-less opening is covered by no-hook).
- Description tightened for series routing: article-writer and topic-picker
  now defer spoken-script requests to this skill.

### Added

- `evals/`: 12 manual golden cases (3 anchor pairs, 4 negative triggers,
  unsourced-F3 + compression-mode probes) with a README documenting the
  schema-valid vs behavior-pass evidence contract.
- `examples/60s-douyin-full-loop.md`.

## [0.1.0] - 2026-07-12

### Added

- Initial build: `SKILL.md` with Hook Gate (seven-type taxonomy), two-column
  draft format （口播 × 画面提示）, read-aloud pacing simulation with four
  duration tiers, six-dimension rubric (Hook 强度 / 口语化与节奏 / 信息密度
  曲线 / 结构完整 / 中文 AI 腔 / 事实纪律), and four output modes (Full /
  Fast / QA Only / 时长压缩).
- `references/`: hook taxonomy with evidence tiers, pacing anchors and
  conversion table, colloquial craft tables, self-contained AI-tone oral
  subset, F0-F3 fact discipline, platform notes with a do-not-cite folklore
  list, and scoring rubric.
