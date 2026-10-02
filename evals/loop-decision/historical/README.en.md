# Loop Decision

> **v0.3.1** · [Evaluation record](evals/releases/2026-09-20-v0.3.1.md) · [Review scope and limits](REVIEW.md)

![Loop skill cover](assets/cover.jpg)

![version](https://img.shields.io/badge/version-0.3.1-blue)
![license](https://img.shields.io/badge/license-MIT-green)
![type](https://img.shields.io/badge/skill-instruction--only-orange)

[中文](./README.md) | English

> This is an overview, not a line-by-line translation. The Chinese [README](./README.md) is canonical. The skill is Chinese-first: its templates, rubric anchors, and examples target Chinese-language decision briefs.

## What it does

Turns important decisions into a scored quality loop instead of a one-shot "sounds reasonable" answer:

```text
Hard Stops -> Reversibility Gate -> Decision Brief -> rubric QA -> premortem + red team -> Decision Memo (preset review date) -> outcome-blind retrospective
```

- **Reversibility Gate**: Type 2 (two-way door) decisions get a fast triage and are waved through — the gate protects against over-processing as much as under-processing. Only Type 1 (one-way door) decisions enter the full loop.
- **Short Type 2 response**: verdict, 1-3 factors, suggested call, and exit condition only—no Decision Brief, three-option table, or invented weighted scorecard.
- **Real-alternatives discipline**: the Full Loop requires >= 3 live options including "do nothing"; Type 2 fast triage does not require a third option or a score.
- **Evidence grading (F0-F3)**: opinion / party-provided / checkable / high-stakes. An unverified load-bearing F2 without an effective pre-commitment verification plan is fatal; calling it a guess does not remove that requirement.
- **Premortem + red team as scored passes**: Klein's original HBR 2007 protocol; steelman-then-attack. The pass should change the brief or explain a verifiable null result.
- **Decision memo**: freezes what was knowable at decision time. A model-authored memo stays `Proposed` until the user explicitly confirms the choice; the model never decides on the user's behalf.
- **Retrospective separation**: preserve the original Gate—Type 2 defaults to a proportional review without /100 or Full Loop deductions. If the outcome is already known, disclose contamination in the first sentence, keep later facts out of process findings, and only then discuss the result without claiming the bias was removed.

## Why instruction-only

No scripts, no runner, zero runtime dependencies. Every behavior is plain markdown you can read before installing. Web access, if any step wants it, goes through your host agent's own tools under your permission model.

## Honest sourcing

Every framework used is cited with its evidence tier in `references/anchors-and-sources.md` — including a correction of the widely circulated "premortem improves accuracy by 30%" misquote (the 1989 study measured the *number* of reasons generated, not accuracy) and a popular Kahneman quote that has no traceable primary source and is therefore not used.

## Project-local installation

These commands pin `v0.3.1` and affect only the current project. Use an absent destination and preserve any existing local changes. Verification used Codex CLI 0.155.1, configured model `gpt-6-astra`, reasoning `xhigh`; see the dated record for actual evidence and limits.

**Codex**:

```bash
mkdir -p .agents/skills
git clone --branch v0.3.1 --depth 1 https://github.com/steven-pku/loop-decision.git .agents/skills/loop-decision
```

**Claude Code directory example (behavior not tested on this host)**:

```bash
mkdir -p .claude/skills
git clone --branch v0.3.1 --depth 1 https://github.com/steven-pku/loop-decision.git .claude/skills/loop-decision
```

## First-success check

In a fresh session, ask the installed skill to fast-triage a choice between two cancellable software trials. It should classify the choice as Type 2 and return only the decisive factors, a suggested call, and an exit condition — no /100 rubric, premortem, or red-team loop. A 快判 request involving a Type 1 decision must instead return the gate verdict and request materials for the Full Loop.

## Boundaries

This skill supports decision process; it does not provide legal, tax, medical, mental-health, or licensed financial advice, and it cannot guarantee a correct outcome. Redact sensitive decision material before sharing it. Your host, model provider, logs, or chat history may retain submitted content.

Starting, stopping, tapering, switching, skipping, or changing the dose of prescription or psychiatric medication is a hard stop before the Gate. The skill must not run option comparison, scoring, premortem, red team, or a risk table for that request, even under a “safety analysis” disclaimer; it may only provide brief prescriber/pharmacist or urgent-support guidance.

## Repair verification

The dated record separates a 20-case first round from a 10-case targeted retest.
Five initial red-team scoring errors and one service-capacity failure remain in
the evidence. The corrected candidate distinguishes pending assessment from
observed poor work without excusing strawmen or sham no-findings claims.

See the [evaluation record](evals/releases/2026-09-20-v0.3.1.md) for exact runtime
identities, actual synthetic outputs, continuation and installation checks, and
remaining limitations. Historical scores are not current-candidate proof.

## License

MIT © Steven CHAN
