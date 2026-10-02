# QA Scorecard Template

Use the opinion scorecard for opinion essays. Use the practical-method scorecard for how-to and workflow articles.

## Opinion Essay Scorecard

```markdown
## QA Scorecard

- Article type: Opinion Essay
- QA loop: 1/2 | 2/2
- Core stance:
- Stance Gate: Restatement test (Pass / Fail) | Rebuttability test (Pass / Fail)
- Meta-article exemption: Applied / Not applied
- Stance-only iteration needed: Yes / No

| Dimension | Score | Evidence / Deduction | Revision Rule |
|---|---:|---|---|
| Stance Sharpness /30 |  |  |  |
| Argument Structure /20 |  |  |  |
| Fact Discipline /15 |  |  |  |
| Hook Strength /10 |  |  |  |
| Material Density /10 |  |  |  |
| Chinese AI-Tone Cleanup /8 |  |  |  |
| Structural Variation / Rhythm /5 |  |  |  |
| Ending /1 |  |  |  |
| Title /1 |  |  |  |

Total:
Decision: Pass / Borderline / Revise / Stance-only iteration / Return to user for missing material
Fatal Issues:

## Deduction Evidence

1. 【扣分项】Dimension: 原文「...」（第 X 段）-> 扣 Z 分，原因：...
2. 【扣分项】Dimension: 模式「...」+ 段落范围「第 X-Y 段」-> 扣 Z 分，原因：...

## Next Revision Rules

1.
2.
3.
```

## Practical Method Scorecard

```markdown
## QA Scorecard

- Article type: Practical Method
- QA loop: 1/2 | 2/2
- Meta-article exemption: Applied / Not applied

| Dimension | Score | Evidence / Deduction | Revision Rule |
|---|---:|---|---|
| Practical Value /25 |  |  |  |
| Structure Clarity /20 |  |  |  |
| Material Density /15 |  |  |  |
| Hook Strength /10 |  |  |  |
| Fact Discipline /10 |  |  |  |
| Chinese AI-Tone Cleanup /10 |  |  |  |
| Structural Variation / Rhythm /5 |  |  |  |
| Ending Judgment /5 |  |  |  |

Total:
Decision: Pass / Borderline / Revise / Return to user for missing material
Fatal Issues:

## Deduction Evidence

1. 【扣分项】Dimension: 原文「...」（第 X 段）-> 扣 Z 分，原因：...
2. 【扣分项】Dimension: 模式「...」+ 段落范围「第 X-Y 段」-> 扣 Z 分，原因：...

## Next Revision Rules

1.
2.
3.
```

## Decision Threshold

Apply the Pass / Borderline / Revise bands from `references/writing-rubric.md` §Passing Standard (the single authority — do not restate the numbers here). On Borderline, review the 2 lowest-scoring dimensions and make 1 targeted revision.

## QA Loop Counter

Every scorecard carries the `QA loop` field. The first QA on Draft v1 counts as `1/2`; each re-check after a revision increments the counter. At `2/2` without a Pass, do not start a third loop — enter the Graceful Halt defined in `SKILL.md` (output the best version, list unresolved flaws and material gaps, hand control back to the user). A stance-only fast iteration does not increment the counter.
