# Xiaohongshu Rewrite QA Example

A worked example of **Rewrite Only** mode on a mediocre 小红书 opinion note.

The user pasted an existing note and said: 「这条没人收藏，帮我重写一下，小红书发的。」 That is an existing draft plus an explicit ask to fix it, so the mode is **Rewrite Only**: diagnosis summary, revision rules, rewritten version, publish check. We still run a QA scorecard inside the diagnosis so the deductions are evidenced, not asserted.

Platform: 小红书. Article type: Opinion Essay (the note is arguing a position about how to use AI for writing, not teaching a fixed template). The 小红书 platform guide is loaded for craft direction only — we do not cite algorithm numbers, title-length rules, or interaction weights, because those are unpublished and time-sensitive.

---

## Original Draft

> **标题：AI 写作的那些事，你真的了解吗？**
>
> 在这个 AI 飞速发展的时代，越来越多的人开始使用 AI 来辅助写作。
>
> 不可否认，AI 写作确实给我们带来了诸多便利。它不仅能提升我们的写作效率，更能激发我们的创作灵感。从选题到成稿，AI 正在重新定义内容创作的方式。
>
> 然而值得思考的是，AI 写作真的万能吗？答案显然是否定的。很多人发现，用 AI 写出来的东西虽然很流畅，但总是缺少一点东西，读起来不够打动人。
>
> 其实，想要用好 AI，关键在于掌握正确的方法。我们需要不断学习，不断实践，不断总结。只有这样，才能真正发挥 AI 的价值，让它成为我们创作路上的得力助手。
>
> 与此同时，我们也要保持独立思考，不能过度依赖 AI。毕竟，真正优秀的内容，永远离不开人的温度和思考。
>
> 总之，AI 是工具，人是核心。希望大家都能在 AI 时代找到属于自己的写作之道，一起加油！

---

## Diagnosis

This note reads smoothly and has zero typos. That is exactly the problem: it is smooth, complete, and says nothing a reader could disagree with. On 小红书, a note that nobody can disagree with is also a note nobody saves — there is no rule, no contrast, no 「啊这说的就是我」moment to screenshot.

The note is built almost entirely out of high-impact Chinese AI-tone skeletons stacked on top of each other, and its stance — 「AI 是工具，人是核心」— is the single most common filler conclusion in this entire topic. It passes the Stance Gate on a technicality (you can restate it) but fails on rebuttability, which short-circuits full scoring and triggers a stance-only fast iteration before we touch anything else.

### QA Scorecard

- Article type: Opinion Essay
- Core stance: 「AI 是工具，人是核心，要保持独立思考别过度依赖」
- Stance Gate: Restatement test (Pass) | Rebuttability test (**Fail**)
- Meta-article exemption: Not applied — this note is *committing* the AI-tone patterns in its own carrier sentences, not quoting them as exhibits. (Topic is AI writing, but the author is not pointing at the patterns as examples; they are writing in them. No exemption.)
- QA loop: 1/2 (hard stop at 2/2 → Graceful Halt: output best version + unresolved flaws, hand to user)

**Stance Gate fails on the Rebuttability test.** If a reader says 「我不同意，因为……」 they have nothing to push against: nobody believes AI should *replace* human thinking, so 「人是核心」 rebuts a position no one holds. Per the rubric, a failed Stance Gate means we skip the full 9-dimension scorecard and go straight to a stance-only fast iteration — but we still report the Stance Sharpness anchor and name the fatal patterns so the rewrite has concrete targets.

| Dimension | Score | Evidence / Deduction | Revision Rule |
|---|---:|---|---|
| Stance Sharpness /30 | 6 | Gate failed (Rebuttability). Anchor 6/30: restatable but it is correct filler — 「AI 是工具，人是核心」 is the default conclusion of this topic, not a position. | Replace with a stance a competent writer could actually argue against. |
| Chinese AI-Tone Cleanup /8 | — | Not fully scored (Gate failed). Flagged fatal: 6 高频高害 / 中频中害 patterns stacked (2.1 / 2.11 / 2.14 / 2.6 / 2.13 / 2.15). See Deduction Evidence. | Rebuild carrier sentences, not just swap words. |
| Structural Variation / Rhythm /5 | — | Not fully scored. Flagged: 2.7 匀速无停顿 across the whole note; every paragraph is the same length and temperature, no stand-alone line, no scannable block. | Vary paragraph length; add line breaks and one save-worthy block. |

Total: **not computed — Stance Gate failed, full scoring skipped per rubric.**
Decision: **Stance-only fast iteration**, then rebuild for 小红书.
Fatal Issues:

1. Opinion essay has no rebuttable stance (Stance Gate Rebuttability fail).
2. Obvious high-impact Chinese AI-tone patterns (≥3 高频高害 hit → automatic AI-Tone fatal).
3. Ending has no judgment (列举/口号式收尾).

### Deduction Evidence

1. 【扣分项】Stance Sharpness: 原文「总之，AI 是工具，人是核心」（第 7 段）-> anchor 6/30，原因：可复述但无法反驳，是本话题的缺省正确结论，没人会反对「人是核心」，立场对一个无人持有的观点开火。
2. 【扣分项】Chinese AI-Tone (2.14 「不仅…更是…」递进套话): 原文「它不仅能提升我们的写作效率，更能激发我们的创作灵感」（第 3 段）-> 高频高害命中，原因：后半句听起来更大但不更准，把弱观点包装成大主张。
3. 【扣分项】Chinese AI-Tone (2.1 排比三连 + 2.11 万能程度副词堆叠): 原文「我们需要不断学习，不断实践，不断总结」（第 5 段）-> 高频高害命中，原因：等权同构三连滑梯，「不断」三连堆叠不推进任何信息。
4. 【扣分项】Chinese AI-Tone (2.6 伪转折「然而值得思考的是」): 原文「然而值得思考的是，AI 写作真的万能吗？答案显然是否定的」（第 4 段）-> 中频中害命中，原因：像报告小标题而非论证里真实的转折，且「万能吗 / 答案显然是否定的」在打一个稻草人——没人说过 AI 万能。
5. 【扣分项】Chinese AI-Tone (2.13 「与此同时」桥接词): 原文「与此同时，我们也要保持独立思考」（第 6 段）-> 中频中害命中，原因：只命名关系而不制造关系，纯机械过段。
6. 【扣分项】Chinese AI-Tone (2.15 列举/口号式结尾 + 3.6 结尾无判断): 原文「希望大家都能在 AI 时代找到属于自己的写作之道，一起加油！」（第 7 段）-> 高频高害命中，原因：用祝福和号召替代判断，读者读完没有任何可执行的东西。
7. 【扣分项】Structural Variation / Rhythm: 模式「匀速无停顿、每段等长、全文无独句段无断行」+ 段落范围「第 2-7 段」-> 原因：六段长度与温度高度接近，没有短句冲刺、没有可截图收藏的规则块，违背 小红书 可扫读、可收藏的体感（craft 判断，非平台数值规则）。

注：第 1 段标题「AI 写作的那些事，你真的了解吗？」属 2.10 起手式设问 + 无立场标题，扣在 Title 维度逻辑下；此处随 Stance Gate 失败一并指出。

---

## Fact-Risk Findings

Almost nothing here is checkable — the note is pure F0 opinion and filler, so fact discipline barely applies. One line to watch when rewriting:

- 「在这个 AI 飞速发展的时代，越来越多的人开始使用 AI 来辅助写作」 — this is F0 common-knowledge framing as written (no number), so it needs no `〔待核验〕`. But if the rewrite sharpens it into a quantified claim (e.g. 「八成写作者都在用 AI」), that becomes a disguised hard-data F2 claim and must be verified or marked. Keep the rewrite on the F0 side: state it as the author's observation, not as a statistic.

No `〔待核·上线前实测〕` markers needed: the note makes no claim about 小红书 distribution rules.

---

## Revision Rules

1. **Kill the filler stance, install a rebuttable one.** Drop 「AI 是工具，人是核心」. Take a position a smart writer could actually argue with — e.g. *用 AI 写作真正拉垮你的，不是文笔，是你舍不得删它写得最顺的那段*. A reader can disagree (「我觉得问题是提示词不行」), which is the test of a real stance.
2. **Front-load the title with the strongest phrase, no vague labels.** Cut 「你真的了解吗」 设问。Lead with the pain or the contradiction in the first few characters so it is legible at a glance and findable in search — that is legibility, not keyword stuffing. No 「干货」「必看」「深度」.
3. **Open on the reader's scene or a blunt diagnosis, not on 「在这个……时代」.** First line must trigger 「这说的就是我」 within one breath.
4. **Rebuild carrier sentences — don't swap words.** Remove every AI-tone skeleton: no 「不仅…更是…」, no 「不断 X，不断 Y，不断 Z」, no 「然而值得思考的是」, no 「与此同时」. Replace with short, uneven, first-person sentences that each carry one concrete observation.
5. **Add rhythm and one save-worthy block.** Vary paragraph length; use line breaks to separate the turn and the warning; give the reader exactly one screenshot-able rule (a 3-line self-check), because 小红书 readers save rules, not paragraphs.
6. **End on a judgment or a real question, not a 口号.** No 「一起加油」, no 「希望大家越来越好」. Close with one self-check or one question that invites an actual reply.
7. **Keep the author's voice — don't over-sanitize into neutrality.** The note should still sound like a person with an opinion who has done this, including a small admission of their own mistake. De-AI is not flattening to safe and bland.

---

## Rewritten Version

> **标题：用 AI 写作，最该删的是它写得最顺的那段**
>
> 你用 AI 写完一篇笔记，自己读着挺顺，发出去，没人收藏。
>
> 我之前也这样。后来发现，问题根本不在提示词。
>
> AI 给你的初稿，最大的特点是「哪儿都对，哪儿都不疼」。它写得最顺的那几句——「不仅提升效率，更能激发灵感」那种——恰恰是最该删的。因为顺，是因为它谁都不得罪；谁都不得罪，就没人记得住。
>
> 我现在改 AI 稿，只盯一件事：把它最四平八稳的那段拎出来，逼自己写一句会被人反驳的话。
>
> 它写「AI 是工具，人是核心」，我改成「AI 写得越顺，你越该怀疑自己在偷懒」。前一句没人会反对，后一句有人会跳出来说「我不同意」——能被反驳，才算你说了句话。
>
> 给你一个我每次都过的三步自检 👇
>
> 1️⃣ 这段有没有一句话，是有人会不同意的？没有 = 还是 AI 在替你说场面话。
> 2️⃣ 有没有一句是短的？短到能单独成行那种。全程匀速长句 = AI 的节奏。
> 3️⃣ 有没有一个例子是我自己踩过的坑，不是它编的？有 = 留下，别换。
>
> 三条都过，这稿才像人写的。
>
> 你最近一次发出去没人收藏的稿子，是不是也栽在「太顺」上？评论区告诉我，我帮你看是哪一步。

---

## Publish Check

- Suitable for platform: **Yes** — 小红书-appropriate: short, scannable, one save-worthy self-check block, first-person scene opening, ends on a real question.
- Best audience: 已经在用 AI 写笔记 / 公众号、但发出去「很顺却没人收藏」的中文写作者。
- Strongest part: 把 filler 立场「AI 是工具，人是核心」当场改写成可反驳立场的那一段——直接示范了「能被反驳才算说了话」。
- Weakest remaining part: 仍是单人经验视角，无外部案例或对照数据；属 F0 经验分享定位下可接受，但若要更有说服力可补一个真实改稿前后对照（待补案例）。
- Fact-risk status: low。全文 F0 经验与判断，无 F2/F3 硬事实；未对 小红书 分发规则做任何断言，无需 `〔待核·上线前实测〕` 标记。
- Suggested title / opening line: `用 AI 写作，最该删的是它写得最顺的那段` / `你用 AI 写完一篇笔记，自己读着挺顺，发出去，没人收藏。`
- Should publish as: 小红书图文笔记（可扫读、含一个可截图收藏的三步自检）。

---

## What This Example Demonstrates

- **Rewrite Only mode** still diagnoses with an evidenced scorecard before it rewrites — it does not jump straight to a new draft.
- **A failed Stance Gate short-circuits scoring.** When 「AI 是工具，人是核心」 fails the Rebuttability test, we do not score all nine dimensions; we report the anchor (6/30), name the fatal patterns, run a stance-only fast iteration, then rebuild. This is the rubric working as designed.
- **Smoothness is not quality.** A typo-free, complete note scored near the floor because it had no rebuttable stance and was built from stacked AI-tone skeletons.
- **Platform craft without platform numbers.** Every 小红书 instruction here is qualitative (front-load the strongest phrase, keep it scannable, one save-worthy block, end on a real question). No CES weights, no character-count rule, no traffic claims — those stay out of agent-facing guidance.
- **De-AI is not over-sanitizing.** The rewrite keeps a strong first-person opinion and a personal admission; it removes the machine skeletons without flattening the author's voice into safe neutrality.
