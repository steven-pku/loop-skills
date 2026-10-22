# QA-Only Bad Draft Example

A worked example of **QA Only** mode on a weak 公众号 opinion draft.

QA Only means **diagnose, do not rewrite.** The user handed over a finished draft and asked for a verdict, not a new version. So this file ends at revision rules and a decision — there is no rewritten article. (Per the skill: in QA Only, produce the rewritten version *only if the user explicitly asks*. Here they did not.)

The point of this example: a draft can be grammatical, complete, and confident-sounding, and still fail — because the stance is vague and the prose is built from AI-tone skeletons. Smooth ≠ good.

---

## User Request

> 「这是我写的一篇公众号，主题是远程办公。你帮我打个分，看看问题在哪，先别动笔改。」

Mode inferred: **QA Only** (existing draft + explicit 「先别动笔改」). Platform: 公众号. Article type: Opinion Essay (the draft is taking a position on whether remote work is good, not teaching a method).

---

## Bad Draft

> **标题：关于远程办公的一些思考**
>
> （第 1 段）在当今这个数字化时代，远程办公正在变得越来越普遍。随着科技的不断进步，越来越多的企业开始采用远程办公的模式。
>
> （第 2 段）不可否认，远程办公有着诸多优势。它不仅能够节省通勤时间，更能够提升员工的工作幸福感。从大型科技公司到初创企业，远程办公正在重新定义现代职场。据相关研究表明，采用远程办公的企业，员工效率平均提升了 40%。
>
> （第 3 段）然而值得思考的是，远程办公真的完美无缺吗？答案当然是否定的。远程办公也面临着沟通成本上升、团队凝聚力下降、员工容易产生孤独感等一系列挑战。
>
> （第 4 段）那么，我们应该如何看待远程办公呢？我认为，关键在于平衡。企业需要在灵活性与协作性之间找到平衡点，员工也需要在自由与自律之间做好平衡。只有这样，才能真正发挥远程办公的价值。
>
> （第 5 段）与此同时，我们也要看到，远程办公并不适合所有的行业和岗位。对于一些需要紧密协作的团队来说，线下办公可能仍然是更好的选择。因此，我们不能一概而论。
>
> （第 6 段）总而言之，远程办公既有机遇，也有挑战。它是大势所趋，但也需要我们理性看待。未来，相信随着技术的不断发展和管理模式的不断完善，远程办公一定会越来越好。让我们拭目以待。

---

## QA Diagnosis

This draft is fluent and organized, and that fluency is hiding the core failure: **it never takes a position.** Every claim is immediately balanced by its opposite — 有优势但也有挑战、要灵活但也要协作、是趋势但要理性看待、不适合所有岗位所以不能一概而论. The conclusion 「关键在于平衡」 is the single most common non-stance in Chinese opinion writing. A reader finishes it and cannot tell you what the author actually believes, beyond 「凡事要平衡」, which nobody disagrees with.

On top of the empty stance, the draft stacks high-impact AI-tone skeletons (排比/递进套话/伪转折/桥接词/列举式结尾) and carries an unsourced load-bearing statistic. Two of these are independently fatal.

### QA Scorecard

- Article type: Opinion Essay
- Core stance (as written): 「远程办公既有机遇也有挑战，关键在于平衡，要理性看待」
- Stance Gate: Restatement test (**Pass**) | Rebuttability test (**Pass, but barely**)
- Meta-article exemption: Not applied (topic is remote work, not AI writing — no exemption available; AI-tone patterns here are the author's own carrier sentences and are fully chargeable).
- QA loop: 1/2 (hard stop at 2/2 → Graceful Halt: output best version + unresolved flaws, hand to user)

**Stance Gate notes.** Restatement passes: you can compress it to 「远程办公要平衡」. Rebuttability technically passes — someone *could* say 「我不同意，远程办公就是全面更好」— so we do not short-circuit to a stance-only iteration on the Gate. We proceed to full scoring. But the stance is so hedged that it lands at the 12/30 anchor (direction exists, too vague to refute meaningfully), which itself is below the 18/30 floor and would trigger a stance-only fast iteration if we were revising. Because this is QA Only, we record that trigger and hand it back as a revision rule rather than executing it.

| Dimension | Score | Evidence / Deduction | Revision Rule |
|---|---:|---|---|
| Stance Sharpness /30 | 12 | Anchor 12/30: direction exists (远程办公), but 「关键在于平衡」 is too vague to refute. Every claim is canceled by its opposite. See Evidence 1. | Pick one side and defend it; name what you are willing to be wrong about. |
| Argument Structure /20 | 9 | Structure is 现象 → 优点 → 缺点 → 平衡 → 例外 → 展望, with no turn that moves the position forward. Objection (第 5 段) is folded back into 「不能一概而论」 instead of sharpening the stance. | Replace the balanced survey with target → stance → strongest objection → turn → judgment. |
| Fact Discipline /15 | 5 | **Unsourced F3 statistic** carrying the 优势 case (Evidence 2). Plus a disguised-authority phrase 「据相关研究表明」 with no named source. This is a fatal-level deduction, not cosmetic. | Cut the 40% claim or attach a real, named source; remove 「据相关研究表明」 unless a source is given. |
| Hook Strength /10 | 3 | Opening is a definition/scene-setting cliché (Evidence 3), creates no recognition, tension, or contradiction. | Open on a concrete pain or a contrarian claim, not 「在当今这个数字化时代」. |
| Material Density /10 | 4 | No concrete case, no named company, no scene, no personal observation — only abstract pros/cons lists. The one specific number is the unsourced 40%. | Add at least one real, specific case or first-hand observation; let one example fail or push back. |
| Chinese AI-Tone Cleanup /8 | 2 | ≥3 高频高害 patterns hit (2.14 / 2.6 / 2.15) plus 中频 2.13, 2.11. Fluent but machine-shaped at sentence level. See Evidence 4. | Rebuild carrier sentences: drop 不仅…更是…, 然而值得思考的是, 与此同时, 总而言之+展望. |
| Structural Variation / Rhythm /5 | 2 | 模式: 匀速无停顿 + 每段等长 + 无独句段（第 1-6 段六段长度高度接近，全程同温度陈述句，无短句冲刺、无断行）。 | Vary paragraph length; add at least one short stand-alone line at the turn. |
| Ending /1 | 0 | 「让我们拭目以待」 is possibility-gesturing with no judgment (Evidence 5). | End on a position the reader can accept or reject. |
| Title /1 | 0 | 「关于远程办公的一些思考」 is a topic label with no stance or promise (Evidence 6). | Rewrite the title to carry the chosen stance. |

Total: **37 / 100**
Decision: **Revise** (score < 82, and three independent fatal issues). Because mode is QA Only, we stop at diagnosis + revision rules; no rewrite is produced unless the user asks.
Fatal Issues:

1. **Empty / vague stance** — opinion essay whose position reduces to 「要平衡」, refutable only trivially (Stance Sharpness anchor 12/30).
2. **Unsourced F3 claim** — the 40% efficiency statistic is load-bearing for the 优势 case and carries no source; per fact discipline this blocks the draft.
3. **Ending has no judgment** — 「让我们拭目以待」.
4. (Near-fatal) **Obvious high-impact Chinese AI-tone patterns** — ≥3 高频高害 stacked.

---

## Deduction Evidence

1. 【扣分项】Stance Sharpness: 原文「我认为，关键在于平衡。企业需要在灵活性与协作性之间找到平衡点，员工也需要在自由与自律之间做好平衡」（第 4 段）-> anchor 12/30，原因：「关键在于平衡」是中文观点文最高频的非立场，每个主张都被它的反面对冲，读者读完不知道作者到底主张什么。
2. 【扣分项】Fact Discipline: 原文「据相关研究表明，采用远程办公的企业，员工效率平均提升了 40%」（第 2 段）-> 扣 10 分（致命级），原因：F3 承重统计——整个「优势」论证压在这个数字上，却无来源、无机构、无时间，且用「据相关研究表明」伪权威包装。按 fact-discipline，无源 F3 必须删除或补真实出处，否则阻断发布。
3. 【扣分项】Hook Strength: 原文「在当今这个数字化时代，远程办公正在变得越来越普遍」（第 1 段）-> 扣 7 分，原因：2.8「在…中」万能状语 + 定义式起手，删掉整句意思不变，不制造任何识别感或张力。
4. 【扣分项】Chinese AI-Tone:
   - (2.14 「不仅…更是…」) 原文「它不仅能够节省通勤时间，更能够提升员工的工作幸福感」（第 2 段）-> 高频高害，后半句更大不更准。
   - (2.6 伪转折) 原文「然而值得思考的是，远程办公真的完美无缺吗？答案当然是否定的」（第 3 段）-> 高频高害，报告腔伪转折 + 打稻草人（没人说远程办公完美无缺）。
   - (2.15 列举式结尾 + 2.13 与此同时桥接) 原文「与此同时，我们也要看到……」（第 5 段）/「总而言之，远程办公既有机遇，也有挑战」（第 6 段）-> 高频高害，机械桥接 + 用分类替代判断。
   - 合并扣分：高频高害命中 ≥3 条，按 chinese-ai-tone-patterns「3 条以上直接扣」，Chinese AI-Tone Cleanup 仅留 2/8。
5. 【扣分项】Ending: 原文「未来……远程办公一定会越来越好。让我们拭目以待」（第 6 段）-> 扣 1 分（清零），原因：3.6 结尾无判断，用「会越来越好 / 拭目以待」朝向可能性而回避立场。
6. 【扣分项】Title: 原文「关于远程办公的一些思考」-> 扣 1 分（清零），原因：纯主题标签，无立场、无具体承诺；对照 rubric 负向锚点（话题罗列型 0/30 立场）。
7. 【扣分项】Structural Variation / Rhythm: 模式「匀速无停顿 + 每段等长 + 全文无独句段」+ 段落范围「第 1-6 段」-> 扣 3 分，原因：六段长度与温度高度接近，全程陈述句无短句冲刺、无断行停顿，机器切割感而非话题驱动的节奏。

（QA 顺序遵循 rubric：先跑 Chinese AI-tone 检查，再跑 fact-discipline 检查；每条事实风险扣分均引用原句。）

---

## Revision Rules

This is the handoff. In QA Only mode the loop stops here — these are instructions for the author (or for a later Rewrite Only / Full Loop pass), not edits applied now.

1. **Choose a side before anything else (stance-only fast iteration first).** The draft scores 12/30 on stance, below the 18/30 floor — so the *first* move is not a full rewrite, it is a stance-only fast iteration: rewrite only the target, the core stance, and the objection. Pick a defensible position, e.g. *远程办公对大多数公司不是「要不要」的问题，而是「先改管理还是先改工位」的问题——不改管理，远程只会放大原有的失序*. Re-run the Stance Gate on that before touching the body.
2. **Cut or source the 40% statistic.** Either attach a real, named, dated source (then it is a sourced F3, allowed), or delete it and rebuild the 优势 case on a concrete observation. Remove 「据相关研究表明」 entirely unless a source follows it. Until this is fixed, the draft cannot publish — it is a fatal issue, not a deduction to weigh against others.
3. **Replace the balanced survey structure with an argued one.** Move from 现象→优缺点→平衡 to target → stance → strongest objection → turn → judgment. The 第 5 段 「不适合所有岗位」 should *sharpen* the stance (narrow it to where it holds), not dissolve it into 「不能一概而论」.
4. **Add one concrete case.** Name a real situation, team, or first-hand observation; let one example fail or push back, instead of abstract pros/cons. This lifts Material Density and gives the stance something to stand on.
5. **Rebuild the AI-tone carrier sentences.** Remove 不仅…更是…, 然而值得思考的是, 与此同时, 总而言之 + 展望式收尾. Vary sentence length; add one short stand-alone line at the turn.
6. **Rewrite the ending into a judgment.** Drop 「会越来越好 / 让我们拭目以待」. Close on a position the reader can accept or reject — ideally a self-check or a decision rule.
7. **Retitle to carry the stance.** 「关于远程办公的一些思考」 → a title that states the chosen position or a concrete promise.

---

## Decision

- **Verdict:** Revise. Total 37/100 with three independent fatal issues (empty stance, unsourced F3 statistic, judgment-free ending).
- **Mode boundary respected:** QA Only — diagnosis and revision rules delivered; **no rewrite produced.** If the user wants the fix executed, the next step is a Rewrite Only or Full Loop pass, which would *start* with the stance-only fast iteration in Rule 1.
- **Sequencing for the author:** fix stance (Rule 1) and the F3 statistic (Rule 2) first; those two gate everything else. Re-running QA after a full rewrite without first settling the stance would just produce another smooth, positionless draft.
- **Missing-material flag:** the draft needs (a) a real source for any efficiency claim and (b) at least one concrete case or first-hand observation. If the author cannot supply either, the honest path is to narrow the article to pure first-person judgment (F0) rather than dress up unsourced numbers as evidence.

---

## What This Example Demonstrates

- **QA Only = diagnose, don't rewrite.** The deliverable is a scorecard, evidence, fatal issues, revision rules, and a decision — and it deliberately stops before producing a new draft, because the user did not ask for one.
- **A passing Stance Gate is not a passing stance.** Unlike a hard Gate failure (which short-circuits scoring), this draft *passes* the Gate yet still scores 12/30 on sharpness — so full scoring runs, and the low stance score is logged as a stance-only-iteration trigger handed back to the author, not executed.
- **Fluent prose can be fatal.** Three independent fatal issues survive in a draft with zero grammatical errors. Smoothness is not the metric.
- **Fact discipline has teeth.** An unsourced load-bearing statistic (F3) is a publish-blocker on its own, separate from style — and 「据相关研究表明」 is flagged as disguised authority, not accepted as a citation.
- **Sequencing matters.** The revision rules are ordered: settle the stance and the F3 fact first, because rewriting the body before the stance exists just regenerates the same positionless essay.
