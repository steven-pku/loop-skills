# Loop Article Writer

![Loop Article Writer — scored QA loop](assets/og-card.jpg)

[![validate](https://github.com/steven-pku/loop-article-writer/actions/workflows/validate.yml/badge.svg)](https://github.com/steven-pku/loop-article-writer/actions/workflows/validate.yml)
![version](https://img.shields.io/badge/version-0.3.0-blue)
![license](https://img.shields.io/badge/license-MIT-green)
![type](https://img.shields.io/badge/skill-instruction--only-orange)
![scope](https://img.shields.io/badge/Chinese--first-公众号%20%2F%20小红书-red)

[← 中文 README](README.md) · **English (overview)**

> **This is a Chinese-only writing skill.** Its rubrics, AI-tone pattern library, and platform rules are built for Chinese opinion writing (公众号 / 小红书) and are not a translation of an English rule set. Other requested output languages have no dedicated pattern library or evaluation coverage in this package. This page exists so English-speaking developers can understand what the skill does before installing — the working language is Chinese.

A Chinese-first **QA-loop writing system** for 公众号/小红书 opinion longform: it grades each draft against a rubric and keeps revising until the stance is real and rebuttable. Removing the 「AI 味」(去 AI 味 / de-AI-ifying the prose) is a built-in loop step, backed by an evidence-graded Chinese AI-tone pattern library — not a one-shot humanizer bolted on top.

It turns article work into a loop:

```text
Define -> Research -> Source Map -> Outline -> Draft -> QA Loop -> Polish -> Publish Check
```

**Contents**: [Modes](#pick-your-mode-you-do-not-have-to-run-the-whole-loop) · [Not a humanizer](#why-not-just-call-it-a-humanizer) · [For](#what-it-is-for)/[Not for](#what-it-is-not-for) · [Features](#core-features) · [Demo](#demo-what-one-qa-loop-looks-like) · [Instruction-only](#why-instruction-only) · [Install](#installation) · [Examples](#usage-examples) · [Validation](#validation-internal-smoke-tests-not-a-benchmark) · [Evidence](#evidence-basis--limits) · [License](#license)

## Pick your mode (you do not have to run the whole loop)

- **Just diagnose my draft** → QA Only — paste a draft, get a scorecard + fixes, no rewrite.
- **Clean up / 去 AI 味 an existing piece** → Rewrite Only or Platform Polish.
- **Write a publishable longform from scratch** → Full Loop.
- **Quick draft + check** → Fast Loop.

Lightweight modes are first-class; the full loop is for when depth matters.

## Why not just call it a "humanizer"?

Because it does a different job. A humanizer takes finished AI text and rewrites it to look less AI. This skill runs a QA loop on your *argument*: it first checks whether a rebuttable stance even exists (Stance Gate), scores the draft against a rubric, and only then cleans AI-tone — as one step, in service of the writing, not to beat a detector. De-AI-tone here is a craft step, not the product.

The focus is **scoring the argument first, then iterating against explicit criteria**, rather than replacing phrases in a single pass.

## What It Is For

- 公众号 opinion essays and practical longform
- 小红书 notes that need sharper structure and less generic writing
- X longform and threads as secondary supported platforms, not the default
- Zhihu longform, newsletters, research notes, and thought-leadership drafts
- QA-only diagnosis of existing drafts
- rewrite and polish work with fact-discipline checks

Platform guides currently cover 公众号 / 小红书 / X; other platforms (Zhihu, newsletters) run the same loop with the generic polish rules.

## What It Is Not For

- fiction or poetry
- ads and sales copy
- generic SEO articles
- platform-growth hacks
- unverified platform-rule claims
- **English writing** — this skill's rules are Chinese-specific by design

## Core Features

- Chinese-first defaults for 公众号 and 小红书
- separate rubrics for opinion essays and practical method articles
- stance sharpness gate for opinion essays
- **去 AI 味 (de-AI-ify) as a loop step**: an evidence-graded Chinese AI-tone pattern library that diagnoses syntax, structure, and punctuation — a loop-integrated step, not a standalone humanizer
- graded fact discipline (F0–F3): from pure opinion to high-risk claims that must carry a source
- lightweight eval cases for rubric calibration

## Demo: what one QA loop looks like

The value is the loop, not a magic before/after. The illustration below shows how scores and issues can guide revision:

```text
Draft v1  ->  QA: Stance Gate FAIL (no rebuttable stance)      ->  stance-only iteration
Draft v2  ->  QA: 71/100 · fatal: generic ending · AI-tone: 不仅…也…, era-framing  ->  revise
Draft v3  ->  QA: 86/100 · PASS · QA loop 2/2
```

What the reader watches is the same draft getting *graded and pushed*, not a one-shot rewrite. The opening line, for example, moves from generic to rebuttable across the loop:

- v1: `AI 的出现正在深刻改变写作……总之，拥抱变化，才能保持竞争力。`
- v3: `别再说「AI 改变了写作」——这句话正确得毫无信息量。真正变的是判断力：你得一眼看出哪一段是「正确的废话」，然后删掉它。`

Illustrative, not a benchmark — actual scores and quality depend on the host model.

## Why instruction-only?

No scripts, no runner — every behavior is plain text you can read. That is deliberate, not an unfinished MVP:

- **Auditable** — read every instruction and know exactly how the skill will treat your draft. No black-box code.
- **Portable** — the same skill runs on Claude Code, Codex, or any compatible agent. No platform lock-in.
- **Supply-chain safe** — zero runtime dependencies, nothing auto-executes, nothing to `npm install`; install (npx / git clone) and CI checks still inherit the npm / Git / GitHub trust chain, with CI pinned to commit SHAs and fixed versions.

The fact-checking / web steps run only if your host agent already exposes a web tool; otherwise the skill degrades gracefully and says so.

## Installation

Version **0.3.0**. All 16 golden inputs were exercised: 15 pass and one partial for conservative fact classification. Additional checks cover the full loop, scope, new patterns, first use and same-install routing. See the [release evaluation](evals/releases/2026-09-19.md).

**Project scope (Claude Code)**: run in your own project without `--global`.

```bash
npx skills@1.7.0 add https://github.com/steven-pku/loop-article-writer/tree/v0.3.0 --skill loop-article-writer --agent claude-code --yes
```

For Codex, replace `--agent claude-code` with `--agent codex`. See the [official skills CLI scope documentation](https://github.com/vercel-labs/skills#installation-scope).

**Local release package**: extract it, then run from your project. The source path must contain `SKILL.md`.

```bash
npx skills@1.7.0 add ./loop-article-writer --skill loop-article-writer --agent claude-code --yes
```

**Manual (Claude Code, current project)**: the destination must not exist.

```bash
mkdir -p .claude/skills
git clone --branch v0.3.0 --depth 1 https://github.com/steven-pku/loop-article-writer.git .claude/skills/loop-article-writer
```

The entrypoint is `SKILL.md`; all required references and templates are bundled. No other writing skill is required. Start a new session and try:

```text
Use loop-article-writer, QA Only. Do not rewrite:
“AI 正在改变世界。我们应积极拥抱变化，与时俱进，共同走向美好未来。”
```

Expected: identify the missing rebuttable stance, quote the draft, and return a diagnosis and material gaps without claiming publish readiness. This checks the workflow, not writing quality.

## Usage Examples

```text
Use loop-article-writer to write a 公众号 opinion essay.
Topic: 为什么 AI 写作越来越像正确废话
Reader: 用 AI 辅助写作但觉得文章越来越空的中文写作者
Core stance: AI 写作最容易失败的地方不是生成正文，而是没有检查观点是否成立
Output: Full Loop
```

```text
Use loop-article-writer QA Only mode for 小红书.
下面是一篇我写的小红书笔记。不要重写，先做 QA，指出 AI 腔、节奏和事实风险。
[paste draft]
```

More examples live in `assets/prompt-examples.md` and `examples/`.

## Validation (internal smoke tests, not a benchmark)

Validation is manual. The historical evaluation (2026-07-10) was an **internal manual smoke test**: 16 golden cases in `evals/cases/`, run by fresh-context AI agents as evaluators — not human reviewers, and not on real published articles. Read "cases pass" as "the instructions reproduce the intended diagnosis," not as a proven quality benchmark. Human review and real-user validation are pending and welcome.

**Historical and current evidence are separate.** The [current release evaluation](evals/releases/2026-09-19.md) records the 16 golden inputs, additional checks and known limits. It makes no complete-suite, calibrated-score or real-user-effectiveness claim.

To run a case:

1. Paste an input case into the skill in QA mode.
2. Check whether the output hits the expected diagnosis.
3. Do not require exact scores; require the correct fatal issues, dimensions, source quotes, and revision rules.

See `evals/README.md` for the with/without-baseline method and the build-time measurements; the original dated reports remain in the development repository.

## Evidence basis & limits

Evidence-graded is **not** the same as "scientifically proven":

- The Chinese AI-tone library has **27 patterns**: 4 anchored on a primary corpus study (朱君辉 et al., CCL 2023), 1 partial, 2 from rhetorical tradition (a Substack essay, not peer-reviewed), and **20 honestly marked `〔待核〕` experience rules**. The uncertainty is labeled, not hidden.
- The corpus figures come from a **GPT-3.5-era** comparison; gaps may narrow on newer models.
- Platform tactics are unverified practitioner lore. Agent-facing guides give only qualitative craft direction; unverified numbers are not usage rules in this package.
- The hallucination-guard pass reduces and flags risk; it does **not** guarantee factual correctness, and its offline layer has documented blind spots.

## Scope and Limits

- **Not an AI-detector-evasion tool.** It removes AI-tone for human readers and does not target, optimize for, or guarantee bypassing any AI detector. If your goal is to pass a detector or "lower the AI rate," it declines and offers an honest quality revision instead. 本 skill 不针对、不优化、不保证规避任何 AI 检测器。
- **Platform tactics are qualitative.** The platform guides give craft direction, not algorithm numbers — unverified operator figures are kept out of the instructions (retained only in historical development notes).
- **Fact discipline is graded, not guaranteed** — see "Evidence basis & limits" above.
- **Out of scope:** fiction, poetry, ads, generic SEO articles, platform-growth hacks, and English writing (Chinese-specific rules by design).

## License

MIT. See `LICENSE`.
