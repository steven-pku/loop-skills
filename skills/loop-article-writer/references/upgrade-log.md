# Upgrade Log

Use this file to record real failures and improvements after using the skill.

## Format

```markdown
## YYYY-MM-DD - [Article / Use Case]

### User Request

### Failure Observed

### Human Correction

### Rule To Add

### File To Update

### Status
- [ ] pending
- [ ] added
- [ ] tested
```

## 2026-06-29 - WeChat Full Loop Dogfood About AI Writing Tone

### User Request

Run the skill on a real 公众号 full-loop article: `为什么大多数人用 AI 写出来的中文文章，一眼就能看出是 AI 写的`.

### Failure Observed

1. Article Brief field names differed between `SKILL.md` and `assets/article-brief-template.md`.
2. Source Map `Platform Function` column had unclear semantics and no enum examples.
3. Stance Sharpness used a /5 qualitative scale while the scorecard used /30, allowing decimal scores.
4. Chinese AI-tone checks were a 25-item reference, not an operational checklist.
5. Structure/rhythm deductions could not always quote a single sentence.
6. Research and Source Map boundaries blurred during real use.
7. `〔待核验〕` and `〔待核·上线前实测〕` were both used but not distinguished.
8. "Stop after 2 QA loops" did not define what counts as a loop.
9. The 25 Chinese AI-tone patterns had no priority levels.
10. AI-writing meta articles had no rule for quoted AI examples versus the author's own carrier sentences.
11. The 7-part opinion outline was too rigid for analysis + method hybrids.
12. Draft v1 was expected to be rough, but QA immediately scored it strictly without saying this was intentional.
13. Stance Gate did not clearly say whether failed gates skip full scoring.
14. Rubric pass/fail behavior was noisy around 84-87, requiring a borderline band without moving the pass line above 85.

### Human Correction

Round-3 fixspec converted the failures into targeted changes: Stance Gate as entry gate, /30 integer stance scoring, two deduction formats, meta-article exemption, 85/82-84/<82 thresholds, prioritized AI-tone checklist, evidence-level tags, marker distinction, QA loop definition, and clearer Source Map / Draft v1 guidance.

Final Polish specifically fixed defect #1 by aligning the Required Brief field names in `SKILL.md` with `assets/article-brief-template.md` and the dogfood example.

### Rule To Add

Dogfood failures should update the smallest relevant runtime file: `SKILL.md` for workflow rules, `writing-rubric.md` for scoring behavior, `chinese-ai-tone-patterns.md` for AI-tone operations, templates for output contracts, and examples/evals for calibration.

### File To Update

- SKILL.md
- assets/article-brief-template.md
- assets/source-map-template.md
- assets/qa-scorecard-template.md
- references/writing-rubric.md
- references/chinese-ai-tone-patterns.md
- references/fact-discipline.md
- examples/wechat-full-loop.md

### Status

- [ ] pending
- [x] added
- [x] tested

## 2026-07-10 - Fresh-Context Eval Run: Positive Anchors Under-Scored

### User Request

Full 16-case fresh-context blind eval for the dated release receipt (historical receipt retained in the development repository).

### Failure Observed

Two independent fresh runners recognized that `anchor-positive-xhs-vs-wechat` and `anchor-positive-content-inflation` are the rubric's own 24/30 and 30/30 anchor essays, yet re-derived Stance Sharpness down to 18/30 — reading the anchor rationales ("layered reasoning", "structurally supported") as evidence properties to re-verify against the draft — and escalated the missing concrete case into the blocking fatal issue "no concrete case or evidence" → Revise. Golden verdicts flipped on the rubric's own anchor essays.

### Human Correction

Derived from the expected files' intent and the 2026-06-30 baseline run (pending owner review): anchors are calibration pins for the stance itself; evidence thinness belongs to Material Density / Argument Structure. Fatal issue 1 needs a severity boundary so it cannot block a gate-passing, observation-argued stance-anchor draft.

### Rule To Add

Anchor-binding note under Anchor Examples; severity boundary on fatal issue 1.

### File To Update

references/writing-rubric.md

### Status

- [x] added
- [x] tested (round-2 re-runs of both failed cases, recorded in the historical 2026-07-10 receipt)

## Upgrade Principle

Do not add rules because they sound good.

Only add a rule when:

1. The skill failed in a real use case.
2. The failure repeated or was serious.
3. The human correction can be turned into a concrete instruction.
4. The rule can be tested.

## Example

```markdown
## 2026-06-28 - X Longform About Loop Engineering

### User Request
Write an X longform article about how beginners can use Loop Engineering.

### Failure Observed
The first draft opened with a definition and sounded like an encyclopedia.

### Human Correction
Start with a contrast: most people ask AI for a full article, but the real issue is that they did not design the revision loop.

### Rule To Add
For X longform, never open with a definition. Start with a wrong common behavior, contradiction, or concrete pain point.

### File To Update
references/platform-x-guide.md

### Status
- [x] added
- [ ] tested
```
