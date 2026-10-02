# Writing Rubric

Use this rubric for QA Loop.

Before scoring, classify the article as:

- Opinion Essay: the article should make a clear, rebuttable stance.
- Practical Method: the article should teach a repeatable method or template.

If the user's brief already specifies the article type, use that. Otherwise infer it from the draft and state the inference.

## Deduction Format

Every deduction must cite the original text. The citation format depends on the problem type.

Sentence-level problems such as wording, AI tone, factual risk, weak hook, or weak ending:

```markdown
【扣分项】Dimension: 原文「...」（第 X 段）-> 扣 Z 分，原因：...
```

Structure or rhythm problems such as paragraph pacing, repetitive patterns, or section balance:

```markdown
【扣分项】Dimension: 模式「...」+ 段落范围「第 X-Y 段」-> 扣 Z 分，原因：...
```

Pattern examples:

- `第 3-6 段均为总分总结构，段长差异很小`
- `全文 8 段中 5 段以问句开头`
- `论证段段落长度均等，无节奏变化`

## Opinion Essay Rubric

Total: 100 points.

| Dimension | Points | What To Check |
|---|---:|---|
| Stance Sharpness | 30 | Can the core stance be restated in one sentence, and is it meaningfully rebuttable? |
| Argument Structure | 20 | Does the article move through target -> argument -> objection -> turn -> ending judgment? |
| Fact Discipline | 15 | Are claims graded F0–F3 (`references/fact-discipline.md`), with checkable claims verified or marked `〔待核验〕` and judgments left alive? An unsourced F3 (load-bearing) claim is a fatal issue, not just a deduction. |
| Hook Strength | 10 | Do the first lines create recognition, tension, or contradiction? |
| Material Density | 10 | Are there cases, observations, details, or useful examples? |
| Chinese AI-Tone Cleanup | 8 | Does the draft avoid high-impact Chinese AI-tone syntax and punctuation patterns? Apply the meta-article exemption below when relevant. |
| Structural Variation / Rhythm | 5 | Is structure varied rather than homogeneous — varied paragraph length, some clause nesting and subordination (not only flat parallel lists), intentional rhythm? |
| Ending | 1 | Does the ending carry a judgment rather than polite filler? |
| Title | 1 | Does the title carry a stance or concrete promise? |

### Stance Gate

Run these two checks before any full scoring. They are pass/fail entry gates, not scored dimensions.

1. Restatement test: Can the article's core stance be restated in one sentence?
2. Rebuttability test: If someone says "I disagree because...", would that disagreement be meaningful?

If either test fails, skip full scoring entirely. Go directly to stance-only fast iteration. Do not proceed to the 9-dimension scorecard. (Still report the Stance Sharpness anchor score — 0, 6, or 12 — as a one-line explanation of why the gate failed; just do not run the other eight dimensions.)

If both tests pass, proceed to full scoring.

### Stance Sharpness Scoring

Score directly on the /30 scale as an integer. Do not use decimals or intermediate /5 scores.

| Score (/30) | Standard |
|---:|---|
| 0 | No core stance; the article is a pile of materials. |
| 6 | Restatable, but it is common sense or correct filler. |
| 12 | Direction exists, but the stance is too vague to refute. |
| 18 | Specific and rebuttable, but the argument is thin. |
| 24 | Sharp stance with layered argument and meaningful objection handling. |
| 30 | Counterintuitive but convincing, and every section serves the stance. |

### Stance-Only Fast Iteration

Triggers:

1. Stance Gate failed: restatement test or rebuttability test failed.
2. Stance Sharpness score is below 18/30 in full scoring.

When triggered:

1. Do not rewrite the whole article.
2. Rewrite only the core stance, target, and objection.
3. Re-run Stance Gate.
4. If Gate passes, proceed to full scoring.
5. If Gate still fails after one iteration, stop and return diagnosis plus missing-material list. Do not loop.

## Practical Method Rubric

Total: 100 points.

| Dimension | Points | What To Check |
|---|---:|---|
| Practical Value | 25 | Can the reader copy a process, checklist, or template after reading? |
| Structure Clarity | 20 | Is the method sequenced and easy to follow? |
| Material Density | 15 | Are there examples, cases, observations, or details? |
| Hook Strength | 10 | Does the opening make the method feel necessary? |
| Fact Discipline | 10 | Are hard facts verified or marked `〔待核验〕`? |
| Chinese AI-Tone Cleanup | 10 | Does the draft avoid high-impact Chinese AI-tone patterns? Apply the meta-article exemption below when relevant. |
| Structural Variation / Rhythm | 5 | Is structure varied and the pacing clear — not visually heavy, not homogeneous? |
| Ending Judgment | 5 | Does the ending give a self-check, decision rule, or next action? |

## Passing Standard

Additional requirement: no fatal issue exists.

| Score Range | Decision | Action |
|---|---|---|
| >= 85 | Pass | Publish check may proceed. |
| 82-84 | Borderline | Author reviews the 2 lowest-scoring dimensions and makes 1 targeted revision, then resubmits for re-check. |
| < 82 | Revise | Full revision loop. |

## Fatal Issues

A fatal issue forces another revision loop even if the score looks acceptable.

Fatal issues:

1. No concrete case or evidence. This blocks when the draft offers the reader nothing concrete at all — no case, no observation, no worked example. For an opinion draft that passes both Stance Gate tests and argues through specific observation, treat a missing case as a Material Density deduction plus a required revision note, not as a block.
2. Empty concepts.
3. Encyclopedia tone.
4. Obvious high-impact Chinese AI-tone patterns.
5. Weak opening.
6. No practical template in a method article.
7. Unsourced F3 claim: a high-risk, load-bearing factual claim with no source and no way to verify it.
8. Reader cannot act or repeat the core stance after reading.
9. Ending has no judgment.
10. Opinion essay has no rebuttable stance.

## Meta-Article Rule

When the article's topic is AI writing, AI tone, or AI text characteristics:

- AI-sounding sentences used as quoted examples or critique targets do not count as AI-Tone deductions.
- The author is showing the reader what to look for, not necessarily producing those lines as their own voice.
- Only judge carrier sentences: the sentences where the author advances their own argument and narrative voice.
- Mark the exemption in the QA scorecard: `元文章：例示句不计 AI-Tone 扣分。`

Example: An article titled `AI 写作最大的破绽不在用词，在骨架` will naturally contain sentences like `AI 喜欢排比三连——A，B，C`. That sentence points at the pattern as an exhibit. Score the carrier argument, not the exhibit.

## Anchor Examples

Use these anchors to calibrate Stance Sharpness. Full eval cases live in `evals/cases/`.

Negative anchors:

- 0/30: `2025 年 AI 写作工具大盘点：10 款你该知道的` — listicle, no stance.
- 6/30: `内容质量为王：为什么好内容永远不过时` — true but empty.
- 12/30: `AI 正在改变写作，你准备好了吗` — direction exists, but the claim is too vague.

Positive anchors:

- 18/30: `公众号改版后，深度长文的打开率反而涨了——流量逻辑变了` — specific and rebuttable, argument may be thin.
- 24/30: `别学网红做小红书——长文作者的平台红利在公众号，不在小红书` — counter-position with layered reasoning.
- 30/30: `AI 写作的敌人不是 AI，是中文互联网的内容通胀` — surprising, specific, and structurally supported.

Anchors are binding pins for the stance itself — how sharp and rebuttable the core claim is — not for the volume of supporting material. When a draft's core stance sits at an anchor's sharpness level, score Stance Sharpness at that anchor even if the essay is short or thin on cases; charge thin evidence under Material Density and Argument Structure instead of discounting Stance Sharpness. The anchor rationales ("layered reasoning", "structurally supported") describe why that stance earns its tier; they are not an extra evidence requirement to re-verify against the draft.

## QA Format

```markdown
## QA Scorecard

- Article type: Opinion Essay / Practical Method
- Core stance:
- Stance Gate: Restatement test (Pass / Fail) | Rebuttability test (Pass / Fail)
- Meta-article exemption: Applied / Not applied
- QA loop: N/2 (hard stop at 2/2 → Graceful Halt: output best version + unresolved flaws, hand to user)

| Dimension | Score | Evidence / Deduction | Revision Rule |
|---|---:|---|---|
| ... |  |  |  |

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

## Scoring Discipline

- Do not give a score without citing the text or structure pattern that caused deductions.
- For structure/rhythm problems, use pattern description plus paragraph range.
- Dimension ownership (do not double-charge one pattern): score rhythm and length-variation tells (匀速无停顿, 段落等长, hook/structure repetition) under Structural Variation / Rhythm; score sentence-, punctuation-, and word-level tells (parallelism, 不是A而是B, lexical patterns) under Chinese AI-Tone Cleanup. Charge each pattern in one dimension only.
- Do not reward a smooth essay if the stance is empty.
- Do not punish a strong opinion merely because it contains judgment or analogy.
- Do not turn all fact risk into disclaimers; mark only hard factual claims that need verification.
- Run Chinese AI-tone checks before fact-discipline checks.
- When the article topic is AI writing itself, apply the meta-article rule: quoted AI-text examples are exempt from AI-tone deductions.
