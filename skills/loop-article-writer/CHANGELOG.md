# Changelog

All notable changes to this skill are documented here. Format based on [Keep a Changelog](https://keepachangelog.com/); this project uses SemVer.

## [0.3.0] — 2026-09-19

First public release. Date is UTC.

### Added

- Hallucination-guard fact-check pass (`references/fact-check-pass.md`): claim ledger, CoVe-style independent verification, and a two-layer design — an offline foundation layer plus an enhanced layer that runs only when the host exposes a web tool. Adapts CoVe (arXiv:2309.11495) and SAFE (arXiv:2403.18802); documents its offline blind spots and a source-credibility ranking for the web layer.
- Structural Variation / Rhythm scoring dimension, with a dimension-ownership rule so AI-tone and rhythm patterns are not double-charged.
- Hard QA-loop circuit-breaker (loop counter + Graceful Halt) and mandatory file-read directives for the evidence references, guarding against the model reconstructing rubrics from memory.
- Platform craft guides for 公众号 and 小红书 (qualitative direction only; unverified operator numbers kept in development notes, deliberately out of the agent instructions).
- 16 golden eval cases (expanded from 7) covering both rubrics and the edge / F3-fatal / borderline / prompt-injection paths, plus eval methodology (with/without baseline, build-time measurements) and historical dated run reports retained in the development repository.
- Untrusted-content contract (external release audit, 2026-07-10): web pages, search results, linked sources, and drafts submitted for QA are data, not instructions — stated in `SKILL.md` Operating Principles, enforced as a trust boundary at the fact-check enhanced layer, documented in `SECURITY.md`, and covered by the new prompt-injection negative eval case.
- Bilingual AI-detector-evasion disclaimer; README badges, install commands, a QA-loop demo, mode routing, "Why instruction-only" / "Why not a humanizer" framing, a Chinese overview, and an Evidence basis & limits section.
- `license: MIT` and `metadata.version` in `SKILL.md` frontmatter.
- Thread QA defined as a five-item structure check in `references/platform-x-guide.md`, plus a Polish-step fallback for platforms without a dedicated guide (知乎, newsletters, blogs).
- Two experience-rule patterns in the Chinese AI-tone library — 2.16 伪独家洞察起手 (faux-insight setup) and 2.17 伪分析尾巴 (superficial trailing analysis) — cross-referenced from petergyang/no-ai-slop (EN, MIT) and graded 〔待核〕 under the cross-language non-transfer rule (library 25 → 27; README counts updated). Same source informed an engineered-humanity guard on Positive Moves (build rhythm from draft words only — stock fragments, canned 说实话, and self-answered Q&A pairs are themselves machine tells) and a repair caution on 3.6 (an empty ending must not be rewritten into a fancier aphorism).

### Changed

- SKILL.md de-duplication (2026-07-25, per Anthropic context-engineering guidance): the inline Article Brief template is replaced by a pointer to `assets/article-brief-template.md`, and the fatal-issues enumeration defers to the authoritative `references/writing-rubric.md` §Fatal Issues (removes a two-list drift risk; the rubric was already a mandatory read at QA time).
- Fact discipline reclassified from A/B/C tiers to a four-level ladder (F0–F3); an unsourced F3 (load-bearing) claim is now a fatal QA issue.
- Repositioned as a QA-loop writing system; 去 AI 味 framed as a loop step, not a standalone humanizer.
- Chinese AI-tone pattern library recalibrated with evidence grades and provenance; added cross-language non-transfer and positive-move (add subordination) rules.
- Strengthened the detector-evasion boundary from a property statement into an explicit decline-and-redirect instruction; removed the "unless explicitly adapting the loop" scope loophole.
- Relabeled the offline hallucination-guard verdict 已核实(内部自洽) → 未发现冲突(离线) to prevent reading offline self-consistency as external verification.
- Eval reframed as an internal manual smoke test run by AI evaluators (not a benchmark); human / real-user validation pending.
- Description tuned for public discovery: removed the step-by-step workflow enumeration (it can induce a shortcut run from the description alone), added humanize / 知乎 / natural Chinese diagnosis phrasings as triggers, and narrowed 中文长文 to 中文观点长文.
- Replaced an internal research citation in the cross-language non-transfer rule with a self-contained methodological rationale.

### Fixed

- First-release packaging: removed private drafting/review dependencies, made project-scoped installation explicit, reused the existing cover, and separated historical behavior evidence from current candidate checks.
- Added the upstream MIT notice for the no-ai-slop pattern adaptations.

- Release-audit fixes (external audit, 2026-07-10):
  - `borderline-83` golden no longer demands a targeted revision at a legitimate >= 85 Pass; expected behavior now branches exactly on the 82-84 / >= 85 decision thresholds.
  - `QA loop: n/2` counter added to both scorecard templates and the flagship example, with explicit counting semantics (the first QA on Draft v1 counts as `1/2`; stance-only iterations do not increment).
  - Platform-guide algorithm-causal claims (no length penalty, front-loaded keyword weight, interaction weighting, tag count, video tilt) now carry `〔待核·上线前实测〕` markers as the guides' own rules require.
  - CI actions pinned to full commit SHAs; `skills-ref` and `markdownlint-cli2` pinned to fixed versions; PR template validate command aligned with CI (`"$PWD"`, not `.`).
  - README supply-chain claim narrowed to runtime: install and CI still inherit the npm / Git / GitHub trust chain.
- Stance Sharpness anchors made binding (score at the anchor when the core stance sits at an anchor tier; thin evidence charges Material Density / Argument Structure instead), and fatal issue 1 ("no concrete case or evidence") given a severity boundary — a gate-passing stance argued through specific observation takes a deduction plus a revision note, not a block. Found by the 2026-07-10 fresh-context eval run (historical receipt, retained in the development repository): both positive-anchor golden cases failed round 1 on a stricter reader.

## [0.2]

- Reoriented default platform from X longform to Chinese-first 公众号 / 小红书 writing.
- Added 公众号 and 小红书 platform guides.
- Added Chinese AI-tone pattern reference with 25 sentence, structure, and punctuation patterns.
- Added fact-discipline reference with A/B/C classification.
- Added separate rubrics for opinion essays and practical method articles.
- Added stance sharpness gate and stance-only fast iteration for weak opinion essays.
- Changed Stance Sharpness to direct /30 integer scoring with Stance Gate as a pre-scoring entry gate.
- Added Borderline handling at 82-84 while keeping Pass at >=85.
- Added two deduction formats: sentence quotation and structure/rhythm pattern plus paragraph range.
- Added meta-article exemption for AI-writing articles that quote AI-like sentences as examples.
- Prioritized Chinese AI-tone patterns into high / medium / contextual tiers and added evidence-level tags.
- Added OSS shell files, dogfood example, and lightweight eval cases.

## [0.1]

- Initial instruction-only article loop: brief, research, source map, outline, draft, QA, polish, and publish check.
