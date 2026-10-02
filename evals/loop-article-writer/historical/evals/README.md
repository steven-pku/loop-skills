# Eval Cases

These are lightweight manual golden cases for `loop-article-writer`.

There is no automated runner; this skill is instruction-only by design.

## Current release evaluation — 2026-09-19

The [dated release receipt](releases/2026-09-19.md) records commit and runtime hashes, hosts, models, per-case observed summaries, judge decisions, routing and limits. All 16 golden inputs were exercised: 15 pass, one partial for overclassifying a personal observation. Additional scope, pattern, full-loop and first-use checks are listed separately. No expectation was rewritten to hide the partial result.

The previous full behavior exercise was on 2026-07-10: 14 cases on 357af9b, then two positive-anchor reruns after the rubric fix recorded in 15db9b1. Those AI-run historical smoke results are not a current pass claim. Human editor and real-user validation remain unclaimed.

## How To Use

1. Paste an `*.input.md` case into the skill in QA mode.
2. Compare the output with the matching `*.expected.md`.
3. Do not require exact wording or exact total score.
4. Require the expected article type, stance diagnosis, fatal issues, quoted evidence, and revision direction.

## With / Without Baseline

To judge whether the skill actually helps — not just whether it runs — compare two outputs on the same input:

- **Without**: a plain model writes or QAs the piece with no skill loaded.
- **With**: the same request runs through loop-article-writer.

Compare on the dimensions the skill claims: stance sharpness, concrete evidence, Chinese AI-tone, fact marking, and structural variation. The skill should win on those, not on length.

## Negative-Trigger Cases

Some inputs should NOT trigger normal write/polish behavior:

- requests to make text "pass AI detectors" or 降 AI 率 to fool a checker — see `cases/negative-trigger-detector-evasion.*`
- fiction, poetry, ads, generic SEO articles, platform-growth hacks

Expected behavior: the skill states the boundary, then declines or redirects to in-scope help. It does not silently comply with an out-of-scope or detector-gaming request.

## Build-Time Measurements (measure on the real host; do not conclude from analysis)

Measure these before trusting the hallucination-guard pass (`references/fact-check-pass.md`):

1. Per-article token cost and latency of the pass — sets the default claim-count cap for the offline layer.
2. Chinese cited-source query recall — Chinese sources often lack a clean author+year.
3. Whether the host's WebSearch actually separates true from false Chinese factual claims — do not assume the SAFE paper's ~72% (arXiv:2403.18802) transfers here.
4. What Citation Padding detection degrades to under pure instruction — likely only "疑似同源·待核".
5. CoVe hallucination hit-rate on the host model for Chinese text — the offline layer leans entirely on it.

## Maintenance

When dogfood reveals a real rubric failure:

1. Add the failure to `references/upgrade-log.md`.
2. Add or update a case here.
3. Note the change in `CHANGELOG.md`.
