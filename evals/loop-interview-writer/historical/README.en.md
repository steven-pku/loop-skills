# loop-interview-writer · Chinese Interview Preparation

> **v0.2.3 — INSTRUCTION-ONLY INTERVIEW PREPARATION.** Historical synthetic outputs provide limited behavioral evidence, not factual verification, automated hiring, or a guarantee of employment outcomes. See [REVIEW.md](REVIEW.md) for the independent review dated 2026-09-21, its limits, and retained historical findings. This text does not claim that tagging or publication has occurred.

English | [中文](README.md)

An instruction-only candidate for Chinese interview preparation: selling-point gate, career-facts ledger, story bank, answers, scoring, and mock follow-ups. A separate mode supports interviewer question design.

The version in `SKILL.md` is `0.2.3`. The reviewed runtime baseline is `0fbf48eb7fb2e29d5c62af2ae720872178510f42`; the release-documentation repair does not change runtime files. Source tracking, refusal to fabricate, and bounded revision are requirements, not guarantees about model behavior, factual truth, or hiring outcomes.

## Review first

The runtime covers non-story applicability, qualitative and honest-failure outcomes, source and verification states, input trust, privacy, and cumulative revision limits. Independent review found the six r2 cases and three actual user turns in `conversations-final` passing within their visible-output and contract scope. All executions predate this review; none is a new test in this review. The old word-count PARTIAL remains historical. All 13 distributed files match the r2 installed snapshot byte-for-byte, so documentation-only changes do not require repeating this behavior set.

Read [SKILL.md](SKILL.md), relevant `references/`, blank `assets/` templates, [REVIEW.md](REVIEW.md), and [SECURITY.md](SECURITY.md). The repository workflow checks skill format only. This review checked archive bytes, installed snapshots, historical outputs, and local documentation patches; it did not start a model or install into a real host. Model names and reported file-read lists do not independently authenticate backend identity or tool access. File availability and static checks do not prove effective loading or correct behavior.

## Paired use

`loop-resume-writer` is an optional ledger-handoff companion, not a release dependency. This repository includes `references/career-facts-ledger.md` and can be used independently. The companion repository is absent from this evidence package; this review does not certify paired byte identity or its release state.

The user explicitly carries the same ledger between skills; no automatic synchronization service is provided. Check both schemas and hashes separately for paired use. This independent repository review is not joint-workflow acceptance, and an unreviewed companion does not indefinitely block this repository.

Salary holding responses remain in scope. Offer negotiation is out of scope; the [fixed loop-negotiation candidate](https://github.com/steven-pku/loop-negotiation/tree/383096ca0b0c201315814ded67ca22224be8c1f9) is a historical reference whose current state is not asserted, and is not a required runtime dependency.

## Evidence and privacy

This repository does not store a candidate's real resume or career ledger. The separate review package contains public candidate files and synthetic historical execution records. Read-only/no-network host restrictions contributed to containment; native events and thread IDs are omitted. Passing visible outputs does not prove Skill-only defense with broad permissions, hiring fairness, cross-model reliability, or real interview outcomes.

Use synthetic or adequately de-identified review inputs. Do not submit identity documents, contact details, exact compensation, or identifiable third-party histories. The host and model provider may retain inputs or write files. Source tags cannot verify user-provided truth, and scores cannot replace hiring judgment or predict success. Instruction requirements and static checks are not guarantees of model behavior.

## License

[MIT](LICENSE), copied byte-for-byte from the source repository.

## Installation preparation

The project-local paths below follow the supplied installation conventions; cross-host compatibility was not newly certified. Run only after the maintainer creates `v0.2.3` and publishes the final commit and archive SHA-256. Stop if the tag is absent, the destination exists, or hashes differ; do not substitute a moving branch or overwrite an existing installation. A tag is not a content hash. Run inside the target project.

Codex:

```bash
test ! -e .agents/skills/loop-interview-writer || exit 1
mkdir -p .agents/skills
git clone --branch v0.2.3 --depth 1 \
  https://github.com/steven-pku/loop-interview-writer.git \
  .agents/skills/loop-interview-writer
```

Claude Code:

```bash
test ! -e .claude/skills/loop-interview-writer || exit 1
mkdir -p .claude/skills
git clone --branch v0.2.3 --depth 1 \
  https://github.com/steven-pku/loop-interview-writer.git \
  .claude/skills/loop-interview-writer
```

After cloning, compare `git rev-parse HEAD` with the final commit in the release receipt and verify the hashes of `SKILL.md`, `references/`, `assets/`, and `LICENSE`. Reload the skill using the host's loading mechanism. Discovery problems require checking the directory and loading setup; do not claim installation success or erase prior behavioral evidence merely because another host has not been tested.
