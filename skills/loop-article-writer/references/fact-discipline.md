# Fact Discipline

Use this reference when an article contains numbers, dates, named people, direct quotes, report findings, platform claims, or any assertion that could damage credibility if wrong.

This skill does not promise factual accuracy. It applies **graded fact discipline**: sort each claim into one of four risk levels (F0–F3) and handle it according to its level. The goal is not to make opinion essays timid; it is to protect the author's credibility while keeping judgment alive.

To run a structured verification of these claims (claim ledger + per-claim check + fix list), use `references/fact-check-pass.md`.

## Four-Level Ladder (F0–F3)

Sort every factual-looking claim into one level. The level decides how it is handled and how `references/fact-check-pass.md` routes it.

### F0 — Opinion, judgment, analogy, experience, common knowledge

State directly. Never needs a marker. Not in the verification check surface.

- `短视频改变了很多人的信息消费习惯。`
- `这种写法对读者不尊重。`
- `我合作过的几个品牌，对 AI 写作的态度都很矛盾。`

Do not turn an F0 judgment into a disclaimer. Protecting the author's stance comes first.

### F1 — Facts the user supplied

Facts given in the user's brief, notes, sources, or prior drafts. Trust them as provided — do not invent beyond what was given. The only check is **internal consistency**: the claim must not contradict another statement in the same draft.

- A figure the user pasted from their own backend data.
- A quote the user supplied with its source.

If the user-given fact is itself high-risk for publication, the author still owns it; flag it, do not silently launder it into the model's voice.

### F2 — Checkable third-party claim, moderate risk

A verifiable claim where being wrong is embarrassing but not load-bearing. Verify, or mark `〔待核验〕` at the end of the sentence.

Triggers:

- specific numbers, percentages, rankings, amounts, or counts
- exact dates or specific month/year event claims
- full names, concrete places, institutions, companies, policies, or laws
- direct quotes attributed to a person or organization
- statistics, survey results, research findings, report conclusions

Examples:

- `2025 年 Q1 微信月活 13.8 亿〔待核验〕`
- `某报告显示，短视频用户日均使用时长已达 151 分钟〔待核验〕`
- `某人在某日期指出“……”〔待核验〕`

### F3 — High-risk, load-bearing claim

A claim the argument leans on, where being wrong damages credibility or misleads the reader. **It must carry a real source.** If it cannot be sourced or verified, do not publish it: cut it, or downgrade it to a clearly-marked judgment (F0). An unsourced F3 claim is a fatal issue in QA — it blocks the draft.

- a headline statistic the whole article is built around
- a named study used to prove the core stance
- a direct quote that, if fabricated, would be a serious credibility failure

(Exact claims about platform rules — recommendation weights, folding, penalties — are time-sensitive and use the separate `〔待核·上线前实测〕` marker; see below.)

### Disguised hard data

If a sentence uses `据我观察`, `很多人`, `大部分`, `普遍`, `几乎都`, or similar wording to imply a statistical claim, strip the wrapper and reclassify the real claim. If it contains specific numbers or can be turned into a measurable claim, it is F2 or F3, not F0.

- `据我观察，90% 的 AI 写作工具其实没人用。` -> F2/F3 (has a number)
- `现在大部分公众号头条打开率已经不到 2%。` -> F2/F3 (has a number)
- `很多写作者开始反思 AI 工具的价值。` -> F0 unless the article leans on it as data

## Boundary Test (F2 vs F3)

Ask:

1. If this sentence is removed, does the core argument still hold?
2. Does the core argument depend on the factual accuracy of this sentence?

If the argument still holds without it, it is F2 at most (verify or mark). If the argument leans on it being accurate, treat it as F3 (must carry a source, or do not publish it).

## Wording Strategy

Use this attitude in the final article:

> This is not about tying the author's hands. It is about protecting trust.

Do not turn every paragraph into a disclaimer. Mark only the claims that truly require verification.

## QA Order

In QA:

1. Run Chinese AI-tone checks first.
2. Run fact-discipline checks second.
3. Quote the original sentence for every fact-risk deduction.

## Marker Distinction

Use two different markers:

- `〔待核验〕`: a hard factual claim in the article body needs verification before publication.
- `〔待核·上线前实测〕`: a time-sensitive platform-guide claim, such as current recommendation behavior, folding behavior, or CTA treatment, should be checked before release.

Do not merge these markers. They flag different risks.
