# Eval Cases

Lightweight manual golden cases for `loop-script-writer`. No automated runner — this skill is instruction-only by design.

## How To Use

1. Use the 13 self-contained fixtures in `current-v0.3.1/`. Give a fresh evaluator only the `## Input`, the installed runtime and the side-effect boundary; do not expose expected answers.
2. A separate judge reads expected behavior and pass criteria after the run. No exact prose or total score is required; use actual gate, fact, count, routing and mode behavior.
3. `cases/` and `releases/2026-09-20-v0.3.0-static-errata.md` preserve earlier versions. They are historical fixtures, not the active v0.3.1 suite. New current assertions are complete in each current file.

The current case names preserve their lineage; a `v0.3.0` filename inside the current suite identifies the complete-source probe's origin, not the installed runtime version.

## Case Map (13)

**Anchor pairs (rubric discrimination — 6):**

- `anchor-hook-negative-buried` / `anchor-hook-positive-named` — 钩子判定与类型命名
- `anchor-colloquial-negative-written` / `anchor-colloquial-positive-spoken` — 书面语成段 fatal 与「口语好 ≠ 时长达标」双判独立
- `anchor-density-negative-flatline` / `anchor-density-positive-curve` — 信息密度曲线

**Negative triggers (4):**

- `negative-trigger-article-reroute` — 图文长文 → loop-article-writer
- `negative-trigger-topic-reroute` — 选题 → loop-topic-picker（两段链路）
- `negative-trigger-audit-reroute` — 数据复盘 → loop-content-audit
- `negative-trigger-detector-evasion` — 规避检测目标：拒绝，不 disclaimer-then-comply

**Fatal / mode probes (3):**

- `fatal-unsourced-f3` — 无源健康数字不进稿
- `mode-duration-compression` — 占位输入；当前断言是索要完整原文，不输出压缩稿
- `mode-duration-compression-complete-v0.3.0` — 完整合成原稿下的重选式压缩 + 读稿闭环 + 承诺改写

## Evidence naming

Two kinds of "pass" are never conflated (per series eval contract):

- **schema valid** — case files parse and cover the designed behaviors (authoring-time check).
- **behavior pass** — a fresh session produced the expected behavior and a
  dated receipt records the exact commit, host, model, output, judge, and
  limitations. The public fixtures do not imply that the current commit has
  passed behavior testing.

The dated v0.3.0 errata is a schema correction, not a behavior-pass receipt.

## With / Without Baseline

Compare a plain model against the skill on the same input. The skill should win on: hook-gate discipline, duration control (declared counting rules), spoken-register conversion, and sourcing honesty — not on flowery prose.
