# Loop Script Writer

> **v0.3.1** · [Evaluation record](evals/releases/2026-09-20-v0.3.1.md) · [Review scope and limits](REVIEW.md)

![Loop skill cover](assets/cover.jpg)

![version](https://img.shields.io/badge/version-0.3.1-blue)
![license](https://img.shields.io/badge/license-MIT-green)
![type](https://img.shields.io/badge/skill-instruction--only-orange)
![scope](https://img.shields.io/badge/Chinese--first-spoken--video--scripts-red)

[← 中文 README](README.md) · **English (overview)**

> This is an overview, not a line-by-line translation. The complete documentation is the [Chinese README](README.md). The skill works in Chinese and its planning assumptions are designed for Chinese spoken-video narration （抖音 / 视频号 / B站 / 小红书）.

## What it does

Turns Chinese spoken-video scriptwriting into a scored quality loop:

```text
Brief -> Hook Gate -> two-column draft (speech × visual cues) -> read-aloud pass -> rubric QA -> iterate -> ship check
```

- **Hook Gate first**: the opening three lines are judged (against a seven-type hook taxonomy) before any body drafting; a failed gate loops on the opening only.
- **Read-aloud simulation**: expected duration computed from declared pace profiles (240-350 cpm planning assumptions, not official standards); user-measured pace wins, and borderline verdicts show sensitivity across plausible profiles.
- **Duration as a hard constraint**: four tiers (30s / 60s / 3min / 10min); deviation greater than 30% is fatal.
- **Honest numbers**: no official source for platform "pass lines" has been verified for this release. The skill refuses to fabricate thresholds and ships an explicit do-not-cite list for popular folklore figures.
- **Self-contained AI-tone oral subset**: patterns that are instantly audible (parallel triads, escalation clichés, list-style endings), with no runtime dependency on another repository.
- **Fact discipline (F0-F3)**: unsourced high-stakes claims are fatal — a spoken claim can't be footnoted after it ships.

## Not an AI-detector-evasion tool

This skill improves spoken-script quality and removes AI-tone for human listeners; it does not target, optimize for, or guarantee bypassing any AI detector.

## Safety and privacy

The skill drafts and reviews scripts only. It does not manage accounts, upload, publish, message, or buy ads. Unpublished drafts stay offline by default; when the user explicitly requests a web fact check, only the minimum claim should leave the draft. Human review is required before publication, and no performance outcome is guaranteed.

## Install

Run in the target project root; the destination must not already exist:

```bash
mkdir -p .agents/skills
git clone --branch v0.3.1 --depth 1 \
  https://github.com/steven-pku/loop-script-writer.git \
  .agents/skills/loop-script-writer
```

Start a fresh Codex conversation in that project and try the QA Only example in
the Chinese README. Verification used Codex CLI 0.155.1 with configured model
`gpt-6-astra` and reasoning `xhigh`; see the evaluation record for the exact
runtime identity, results, and limitations.

For Claude Code, the analogous project directory is
`.claude/skills/loop-script-writer`; Claude Code behavior was not tested for this
release. Other hosts require their own validation. Preserve local modifications
before replacing an existing installation.

## License

MIT © Steven CHAN
