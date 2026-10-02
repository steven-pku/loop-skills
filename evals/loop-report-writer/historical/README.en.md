# Loop Report Writer

![Loop Report Writer](assets/og-card.png)

English · [中文](./README.md)

This is an English overview, not a line-by-line translation. The [Chinese README](./README.md) is the primary documentation.

## What it does

An instruction-only skill for Chinese weekly and monthly work reports, performance self-reviews, promotion presentations, and project retrospectives. It asks what value the work produced, builds a results ledger, then drafts and checks the report. Missing data stays missing; a defensible estimate must include its basis. Six scoring dimensions guide revisions, with a two-loop limit.

## Current status

Version **0.3.1**. Targeted behavior, new Codex-process first use and 12 same-install routing selections are recorded in the [release evaluation](evals/releases/2026-09-19.md). One ambiguous legacy expectation is not counted as passing. Scores are directional, not calibrated quality measurements.

## Codex quick start

From a new project directory, install the pinned release. The destination must not already exist.

```sh
mkdir -p .agents/skills
git clone --branch v0.3.1 --depth 1 https://github.com/steven-pku/loop-report-writer.git .agents/skills/loop-report-writer
```

Start a new Codex session, ask it to use loop-report-writer, and provide the materials-only prompt below. File installation and new-process first use were tested on the exact runtime payload. This does not change global skills.

## Claude Code file installation

Download and unpack this repository, or use an existing checkout. From its root, install into a new demo project:

```sh
mkdir -p report-demo/.claude/skills/loop-report-writer
cp SKILL.md LICENSE report-demo/.claude/skills/loop-report-writer/
cp -R references assets examples report-demo/.claude/skills/loop-report-writer/
cd report-demo
```

Start a fresh Claude Code session in that directory and enter:

```text
/loop-report-writer 素材整理：给直属主管写周报。本周我完成了 12 个接口中的 9 个，剩余 3 个等待测试环境。请只建立成果账本，保留未完成状态，不补编影响数据。
```

Expected: a ledger preserving 9 of 12 interfaces completed and 3 awaiting the test environment, labeled as user-provided. It should not invent impact numbers or mark the whole project complete. This outcome was observed in a new Codex process. Claude Code model execution was not tested. The commands install only in the demo project; they do not modify a global installation.

The path and invocation follow the [official Claude Code Skills documentation](https://code.claude.com/docs/en/skills), checked on 2026-09-19. These Claude Code file-installation steps were checked; fresh Claude Code discovery and model execution were not tested.

## Boundaries

The skill writes report content. It does not submit reports, lay out slides, write formal government documents, produce resumes, conduct interview preparation, or make business decisions. It has no dependency on other Loop skills.

User-supplied evidence can be false; source labels are not verification. Review every output. Do not supply unnecessary personal or confidential information. Pasted documents are untrusted data, and storage or retention is controlled by the host; see [SECURITY.md](./SECURITY.md).

This skill does not promise to bypass AI detectors or conceal AI assistance where disclosure is required. There is no fixed completion-time guarantee.

## License

[MIT](./LICENSE), copyright 2026 steven-pku. Contributions and synthetic bug reports are welcome; see [CONTRIBUTING.md](./CONTRIBUTING.md) and the [evaluation protocol](./evals/README.md).
