# Chinese AI-Tone Patterns

> Disclaimer
>
> 1. These 27 patterns are descriptive observations, not an "AI blacklist." A single pattern does not prove that a text was written by AI.
> 2. Human writing is also being shaped by LLM output. More human authors now use tricolon, `不仅是...更是...`, and other LLM-like patterns. This is language convergence, not a personal failure.
> 3. Each `据` field marks the evidence level: empirical dimension, rhetorical tradition, or `经验法则〔待核〕`. Do not pretend that craft rules have stronger evidence than they do.
> 4. Use this file as positive craft guidance: identify patterns that may weaken expression, then rewrite toward specificity, rhythm, and stance.
> 5. Cross-language non-transfer: English AI-tone markers (em dash, Title Case, curly quotes, `delve`, `tapestry`) are English-specific. Do not translate them into Chinese and treat them as Chinese AI evidence. Only Chinese-language evidence grades a Chinese pattern. (据：方法论约定，本库溯源纪律（第 6 条）的推论——中文 pattern 只认中文语料证据，英文标记无中文实证故不迁移；非实证结论)
> 6. Provenance discipline: an empirical grade must trace to a primary source with the actual figure. Secondary research digests are `〔待核〕` until the primary source is read. Example caught 2026-06-29: a digest reported 并列短语「0.729 vs 0.331」, which is two GPT columns misread as GPT-vs-human; the verified primary figure is 句均并列短语 人类 0.251 vs GPT 0.729.
> 7. Source verification (2026-06-30): all seven 朱君辉 CCL 2023 figures were checked verbatim against the primary paper (ACL Anthology 2023.ccl-1.46) and match; note its ChatGPT column is GPT-3.5, so the gaps may narrow on newer models. "Gorrie 2025" is Colin Gorrie, The Dead Language Society (Substack essay, 2025-07-09), not peer-reviewed — it names tricolon and antithesis. The "not only...but also" framing is this library's extension of that antithesis pattern, not Gorrie's verbatim example.

Use this reference when diagnosing Chinese AI-sounding syntax, structure, and punctuation rhythm.

This file is instruction-only. Detection signals are human/LLM judgment heuristics, not automation promises.

## Priority Tiers

### 高频高害

Check these first. If 3 or more hit in one draft, deduct in Chinese AI-Tone Cleanup without waiting for a second pass.

| ID | Pattern | Why It Matters |
|---|---|---|
| 2.1 | 排比三连 | One of the most visible Chinese AI-tone skeletons. |
| 2.4 | 每段总分总 | Makes each paragraph repeat itself and drain information density. |
| 2.7 | 匀速无停顿节奏 | Low structural variation is a stable machine-text signal at the discourse level. |
| 2.14 | 「不仅是...更是...」递进套话 | Mechanical escalation makes claims sound grand but imprecise. |
| 2.15 | 列举式结尾 | Replaces judgment with categories. |
| 3.6 | 结尾无判断/无态度 | Fatal for opinion essays. |
| 3.1 | 钩子-论点-论据-论点复现 | Whole-article template that often combines with paragraph templates. |

### 中频中害

Check after the high-impact pass. Deduct when the pattern affects meaning, rhythm, or credibility.

| ID | Pattern |
|---|---|
| 2.2 | 「不是 A 而是 B」滥用 |
| 2.3 | 「从 X 到 Y」框架句 |
| 2.5 | 逗号流水句过长 |
| 2.6 | 伪转折「然而值得思考的是」 |
| 2.10 | 定义句起手 |
| 2.11 | 万能程度副词堆叠 |
| 2.13 | 「与此同时」桥接词 |
| 2.16 | 伪独家洞察起手 |
| 2.17 | 伪分析尾巴 |
| 3.2 | 每段等长 |
| 3.3 | 例子全部正面、全部顺利 |
| 4.1 | 逗号代替一切停顿 |

### 低频/需上下文判断

Use these as supporting signals. Usually deduct only when they stack with stronger patterns.

| ID | Pattern |
|---|---|
| 2.8 | 「在...中」万能状语开头 |
| 2.9 | 被动泛化 |
| 2.12 | 「正如 X 所言」伪引经 |
| 3.4 | 无断行/无独句段 |
| 3.5 | 全文无直接引语 |
| 4.2 | 省略号滥用 |
| 4.3 | 感叹号缺失 |
| 4.4 | 引号缺失 |

## Four Layers

| Layer | Name | Scope | Use |
|---|---|---|---|
| L1 | Word layer | words and phrases | Challenge generic all-purpose words; keep the phrase list in `anti-ai-style-guide.md`. |
| L2 | Sentence layer | single sentence or compound sentence | Find reusable AI-sounding sentence skeletons. |
| L3 | Structure layer | paragraph or whole article | Find template-like argument flow and rhythm. |
| L4 | Punctuation layer | punctuation sequence | Find flat or unnatural Chinese pacing. |

## L1 Word Layer

Do not maintain this file as a pure banned-word list. The principle is:

> Any all-purpose word that can be inserted into almost any article is suspicious.

Examples: `毋庸置疑`, `不言而喻`, `至关重要`, `深刻`, `赋能`, `破局`, `底层逻辑`.

Maintain L1 as a small challenge list, not as a growing blacklist. Add a word only when it hides a more concrete observation in real use.

## L2 Sentence Layer

### 2.1 排比三连 [高频高害]

- Pattern: Three similarly structured clauses line up as a slogan.
- Before: 它改变了我们的生活方式，改变了我们的工作模式，改变了我们的思维方式。
- After: 它最先改写的是工作方式——远程和协同突然变得理所当然；生活方式和思维方式的改变，反倒是后来才跟上的。
- Judgment heuristic: Several neighboring clauses share the same subject, verb, or object skeleton and feel equally weighted.
- 据：实证维度 C1 + 修辞传统 E2。实证 = 朱君辉等 CCL 2023（北语·ACL Anthology 2023.ccl-1.46, pp.523-534）句法复杂性维度：句均并列短语 人类 0.251 vs ChatGPT 0.729（约 2.9×），并列短语总数 0.813 vs 4.600，「并列短语数」属分类模型高贡献特征（占重要特征 6.5%）。修辞 = Gorrie 2025 rule-of-three/tricolon。
- 不应触发：并列本身不是病。三项若各自推进信息、长度不齐、收在判断上，保留。只罚「等权、同构、不递进」的滑梯式排比。

### 2.2 「不是 A 而是 B」滥用 [中频中害]

- Pattern: `不是...而是...` is used as a universal contrast frame.
- Before: 真正的挑战不是技术，而是人心。
- After: 人心才是难关——技术问题反而好解。
- Judgment heuristic: The contrast is made of abstract nouns and could be dropped into many unrelated essays.
- 据：修辞传统 E2（Gorrie 2025: antithesis；E1: "not X but Y" pattern）

### 2.3 「从 X 到 Y」框架句 [中频中害]

- Pattern: `从 A 到 B` opens a broad narrative without real movement.
- Before: 从工具到伙伴，AI 正在重新定义人与技术的关系。
- After: AI 先是工具；后来它开始能接话了——关系的性质就变了。
- Judgment heuristic: Both sides of `从...到...` are abstract labels, not observable changes.
- 据：经验法则〔待核〕（英文 "from X to Y" 在 E1 列举，中文频率无实证）

### 2.4 每段总分总 [高频高害]

- Pattern: A paragraph starts with a topic sentence, explains it, then restates the same idea.
- Before: 创新需要勇气。很多企业不敢尝试新方向，总等别人先走。所以，没有勇气就没有创新。
- After: 很多公司不敢碰新方向——都在等别人先趟雷。可第一个趟的，往往最后才被记得。
- Judgment heuristic: The first and last sentence say almost the same thing, and the middle adds little.
- 据：经验法则〔待核〕（结构模板化属 E3 维度，但中文首尾复现频率无实证）

### 2.5 逗号流水句过长 [中频中害]

- Pattern: A sentence keeps extending with commas instead of making clear stops.
- Before: 我们需要重新审视这个问题，因为它涉及多个维度，而且每个维度都有不同的影响，所以不能一概而论。
- After: 这事得拆开看。它牵着好几头——定价、渠道、用户预期，每头拉的方向还不一样。想一句话下结论，多半翻车。
- Judgment heuristic: One sentence carries too many logical moves and would read better split into stops or a stronger connector.
- 据：经验法则〔待核〕（中文逗号链长度无实证；句法规整度属 E3 维度）

### 2.6 伪转折「然而值得思考的是」 [中频中害]

- Pattern: `然而/但是/不过` plus `值得思考/深思/关注的是`.
- Before: 然而值得思考的是，这种增长是否可持续。
- After: 可这种增长能持续吗？
- Judgment heuristic: The transition sounds like a report label rather than a live turn in the argument.
- 据：经验法则〔待核〕（英文 "it's worth noting" 在 E1 列举，中文等价表达频率无实证）

### 2.7 匀速无停顿节奏 [高频高害]

- Pattern: Sentence length and tone stay too even for too long.
- Before: 技术正在重塑行业格局。企业需要找到新的增长点。用户的需求也在不断变化。市场的竞争变得更加激烈。
- After: 行业格局在变。用户在变。竞争在变。不变的企业——出局。
- Judgment heuristic: A passage has no short punch, no long build, and no intentional pause.
- 据：实证维度 E3 + C1。E3 = Kim et al. ACL 2024（AI discourse structure shows lower variation than human writing）。中文佐证 = 朱君辉 CCL 2023 §4.1：人类回答的句长标准差高于 ChatGPT，最长/最短句字数差更大，长短句使用更灵活多变（机器文本句长更匀质）。

### 2.8 「在...中」万能状语开头 [低频/需上下文判断]

- Pattern: `在 N 中` opens a sentence where N is an abstract scene.
- Before: 在数字化转型中，企业面临着诸多挑战。
- After: 企业数字化转型，挑战不少。
- Judgment heuristic: The opening phrase can be deleted without changing meaning.
- 据：经验法则〔待核〕（中文翻译腔观察；与汉语意合到形合的学理推论相印证，但非单条实证）

### 2.9 被动泛化 [低频/需上下文判断]

- Pattern: Passive phrasing replaces a clearer actor, especially `被广泛/被深入/被深刻`.
- Before: 这一现象被广泛讨论。
- After: 我那个三十来人的同行群，这两周全在吵这件事。
- Judgment heuristic: The actor is hidden even though naming the actor would make the sentence clearer.
- 据：经验法则〔待核〕（中文被字句泛滥属翻译腔观察，C1 描述 AI 中文偏离但未单列此模式）

### 2.10 定义句起手 [中频中害]

- Pattern: The article opens like a textbook definition.
- Before: 数字化转型是指企业利用数字技术重塑业务流程的过程。
- After: 你的公司要活过这五年，大概率绕不过数字化转型——把线下流程搬上线只是第一步。
- Judgment heuristic: The first sentence defines instead of creating tension, recognition, or a concrete problem.
- 据：经验法则〔待核〕（中文观点文起兴传统 vs AI 下定义起手属工艺观察，无实证）

### 2.11 万能程度副词堆叠 [中频中害]

- Pattern: Several degree adverbs stack without adding information.
- Before: 市场在日益激烈的竞争中不断发展，企业需要进一步持续创新。
- After: 竞争越来越硬，企业只能不停试新。
- Judgment heuristic: Words like `日益`, `不断`, `持续`, `进一步`, `愈发`, `越发` appear together and do not sharpen the claim.
- 据：实证维度 C1（朱君辉等 CCL 2023: AI 中文词频偏差含描述性/常用度偏离）+ 经验法则〔待核〕（堆叠频率无单列实证）

### 2.12 「正如 X 所言」伪引经 [低频/需上下文判断]

- Pattern: A famous name is used as generic backing.
- Before: 正如德鲁克所言，管理是一种实践。
- After: 德鲁克说过“管理是实践”——但多数公司把它当成了流程。
- Judgment heuristic: The quote does not do argumentative work, or the source would require verification before publication.
- 据：经验法则〔待核〕（E1 列举 "as X noted" 类模式，中文频率无实证）

### 2.13 「与此同时」桥接词 [中频中害]

- Pattern: `与此同时/在此背景下/在这种趋势下` bridges paragraphs mechanically.
- Before: 与此同时，行业也在加速整合。
- After: 另一头，行业整合也在加速。
- Judgment heuristic: The transition names relation but does not create real relation.
- 据：部分佐证 + 经验法则〔待核〕。佐证 = 朱君辉 CCL 2023 表5：ChatGPT 更倾向用「和、与」作连接（和：人类 4.13 vs ChatGPT 11.76），连词密度 GPT 高（0.036 vs 0.013）；人类更常用「跟、同」。但「与此同时/在此背景下」这类具体桥接词的中文频率无单列实证。

### 2.14 「X 不仅是 Y，更是 Z」递进套话 [高频高害]

- Pattern: `不仅是...更是...` turns a weak idea into a grand claim.
- Before: AI 不仅是工具，更是伙伴。
- After: 说 AI 是工具没错，但它偶尔也像个能接话的搭档。
- Judgment heuristic: The second half sounds bigger but not more precise.
- 据：修辞传统 E2（Gorrie 2025: antithesis / negation-contrast「it's not X, it's Y」；`不仅...更是...` 为本库据此延伸，非 Gorrie 原文点名；E1 同列）

### 2.15 列举式结尾 [高频高害]

- Pattern: The ending lists categories instead of making a judgment.
- Before: 综上所述，我们需要在技术创新、人才培养和制度保障三个方面共同发力。
- After: 三个方向都得动，但最不能等的是制度——技术和人会自己找路，制度不会。
- Judgment heuristic: The last paragraph begins with summary language and avoids taking a position.
- 据：经验法则〔待核〕（英文 "In conclusion" 在 E1 列举，中文结尾频率无实证）

### 2.16 伪独家洞察起手 [中频中害]

- Pattern: A claim is framed as secret knowledge the crowd lacks: `没人告诉你`, `大多数人都搞错了`, `99% 的人不知道`, `真正懂行的人都明白`.
- Before: 大多数人都忽略了一点：分发才是真正的护城河。
- After: 分发才是护城河——产品好坏反而是第二位的。
- Judgment heuristic: Deleting the setup does not weaken the claim; the setup only flatters the writer as the lone expert. In platform hook slots (小红书首行) this is a designed convention — judge body prose, not the hook slot.
- 据：经验法则〔待核〕（英文对应模式 "faux-insight setups" 在 petergyang/no-ai-slop（2026, MIT）列举；依本库跨语言不迁移纪律不作中文证据，中文频率无实证）

### 2.17 伪分析尾巴 [中频中害]

- Pattern: A fact carries a trailing clause that pretends to explain its significance: `，凸显了...`, `，彰显了...`, `，标志着...`, `，反映出...`, `，折射出...`.
- Before: 该功能本周上线，彰显了团队对创作者体验的重视。
- After: 该功能本周上线——用户不用离开编辑器就能找旧稿了。
- Judgment heuristic: The tail names significance without mechanism or consequence; replace it with what actually changes and the sentence carries weight. `标志着` can be literal in a concrete milestone — keep it there.
- 据：经验法则〔待核〕（英文对应模式 "superficial analysis"（trailing -ing clauses）在 petergyang/no-ai-slop（2026, MIT）列举；依本库跨语言不迁移纪律不作中文证据，中文频率无实证）

## L3 Structure Layer

### 3.1 钩子-论点-论据-论点复现 [高频高害]

- Before: 开头提现象 -> 中间铺三个论据 -> 结尾复现开头论点。
- After: 开头提矛盾 -> 中间走一段弯路或反例 -> 结尾翻一层判断。
- Judgment heuristic: The final paragraph only repeats the opening claim instead of moving it forward.
- 据：实证维度 E3 + C1。E3 = Kim et al. ACL 2024（AI discourse motif repetition higher than human）。中文佐证 = 朱君辉 CCL 2023 表8 语篇凝聚力：相邻句实词重复 人类 0.481 vs ChatGPT 0.831，全文词语重复 0.380 vs 0.519，机器文本重复性显著更高。

### 3.2 每段等长 [中频中害]

- Before: 全文每段长度接近，视觉节奏平均。
- After: 有短句冲刺段、长段展开、一句话断行。
- Judgment heuristic: The paragraph rhythm looks machine-cut rather than topic-driven.
- 据：经验法则〔待核〕（E3 维度覆盖结构变异，但未单列段长方差）

### 3.3 例子全部正面、全部顺利 [中频中害]

- Before: Three success cases are listed.
- After: One success, one failure, and a judgment about what really matters.
- Judgment heuristic: The article has no failure, constraint, misuse, or counterexample.
- 据：经验法则〔待核〕（AI 词汇趋同有英文大样本实证，案例趋同为类比推论）

### 3.4 无断行/无独句段 [低频/需上下文判断]

- Before: Every paragraph carries multiple sentences.
- After: Occasional one-sentence paragraphs create emphasis and pause.
- Judgment heuristic: No sentence is ever allowed to stand alone, even when the argument turns.
- 据：经验法则〔待核〕

### 3.5 全文无直接引语 [低频/需上下文判断]

- Before: Everything is indirect narration.
- After: At least one direct line, reader thought, or spoken sentence appears where it helps.
- Judgment heuristic: The draft has no quoted phrase, no reader voice, and no scene-level speech.
- 据：经验法则〔待核〕

### 3.6 结尾无判断/无态度 [高频高害]

- Before: 让我们共同期待 / 未来充满可能。
- After: End with a specific stance the reader can accept or reject.
- Judgment heuristic: The ending gestures toward possibility but avoids a position.
- Repair caution: when cutting an empty ending, do not rewrite it into a fancier aphorism or metaphor — an upgraded 金句 is still a stance-free ending. Land on a concrete judgment or fact already in the draft.
- 据：经验法则〔待核〕（属 rubric Ending 维度逻辑，非句法实证）

## L4 Punctuation Layer

### 4.1 逗号代替一切停顿 [中频中害]

- Before: The draft mostly uses commas and periods.
- After: Use dashes for interruption or turn, colons for setup, semicolons for parallel contrast.
- Judgment heuristic: Punctuation rhythm is flat and does not match argument movement.
- 据：经验法则〔待核〕（标点节奏属 E3 变异度维度，但中文标点模式无专项实证）

### 4.2 省略号滥用 [低频/需上下文判断]

- Before: Ellipses repeatedly create fake emotional depth.
- After: Use ellipses only when something is genuinely unfinished.
- Judgment heuristic: `...` or `……` appears as a mood marker rather than a meaning marker.
- 据：经验法则〔待核〕

### 4.3 感叹号缺失 [低频/需上下文判断]

- Before: The whole opinion essay has no forceful sentence.
- After: Use occasional emphasis when the stance needs emotion.
- Judgment heuristic: The article is making a sharp claim but every sentence has the same temperature.
- 据：经验法则〔待核〕

### 4.4 引号缺失 [低频/需上下文判断]

- Before: Key concepts are never framed.
- After: Put at least one contested term, reader phrase, or core concept in quotes when useful.
- Judgment heuristic: The draft never marks a phrase as a term of art, quoted reader thought, or disputed label.
- 据：经验法则〔待核〕

## Positive Moves (Reverse Rules)

De-AI is not only deletion. Several AI-tone patterns are best fixed by adding human-side moves the model underuses:

- Add subordination and nesting where the logic is layered. 据：朱君辉 CCL 2023 表6——人类最大句子依存距离 29.452 vs ChatGPT 23.991，人类长短句更灵活，AI 倾向平铺并列而弱于长程从属。去 AI 味可主动把「A，B，C」并列改成有主从、有让步、有插入的句子，而不只是删并列。
- Vary sentence length on purpose: one short punch, one long build, one stand-alone line. Guard: build rhythm from words already in the draft — inserting stock fragments (`对。`, `真的。`), canned `说实话`, or self-answered Q&A pairs is itself a current machine tell（工程化人味）. 据：经验法则〔待核〕（英文对应 "dramatic fragmentation / rhetorical setups" 见 petergyang/no-ai-slop，中文频率无实证）
- Raise content-word richness over function-word padding. 据：朱君辉 CCL 2023 表4——人类实词丰富度 0.822 vs ChatGPT 0.647，同等篇幅人类信息量更大。
- Let at least one example fail, get constrained, or push back, instead of all-positive cases.

## Quick QA Checklist

### First Pass: 高频高害 7 条

- [ ] 排比三连: neighboring clauses share structure and equal weight.
- [ ] 每段总分总: paragraph opening and ending repeat the same idea.
- [ ] 匀速无停顿: several sentences in a row have similar length and temperature.
- [ ] `不仅是...更是...`: second half sounds bigger but not more precise.
- [ ] 列举式结尾: ending uses categories instead of judgment.
- [ ] 结尾无态度: ending gestures at possibility without a stance.
- [ ] 论点复现: ending repeats the opening instead of moving the argument forward.

If 3 or more hit, deduct in Chinese AI-Tone Cleanup.

### Second Pass: 中频中害 12 条

- [ ] `不是 A 而是 B`万能转折
- [ ] `从 X 到 Y`叙事起手
- [ ] comma-stream sentence
- [ ] `然而值得思考的是`伪转折
- [ ] definition opening
- [ ] degree-adverb stacking
- [ ] mechanical transition words
- [ ] equal-length paragraphs
- [ ] all-positive examples
- [ ] comma-only punctuation rhythm
- [ ] 伪独家洞察起手（没人告诉你 / 大多数人都搞错了）
- [ ] 伪分析尾巴（凸显了 / 彰显了 / 标志着 无机制无后果）

### Third Pass: 低频/上下文 8 条

- [ ] `在...中`万能状语
- [ ] passive generalization
- [ ] fake authority quote
- [ ] no one-sentence paragraphs
- [ ] no direct quote or reader voice
- [ ] excessive ellipses
- [ ] no forceful punctuation where stance needs force
- [ ] no quotation marks around contested terms or reader phrases

## Meta-Article Exemption

When the article's topic itself is AI writing, AI tone, or AI text characteristics, quoted AI-sounding sentences used as examples or critique targets do not count as AI-Tone deductions.

Rule: judge only carrier sentences: the sentences where the author advances their own argument, not the sentences where the author points at AI patterns as exhibits.

Example: An article titled `AI 写作最大的破绽不在用词，在骨架` will naturally include sentences like `AI 喜欢排比三连：A，B，C`. That sentence is pointing at the pattern, not committing it. Score the carrier argument, not the exhibit.

## Evidence Count

The 27 patterns are graded as follows (recalibrated 2026-06-29 against primary Chinese sources; `2.16`/`2.17` added 2026-07-24 from a petergyang/no-ai-slop cross-reference):

- Empirical dimension (incl. primary Chinese corpus): 4 patterns (`2.1`, `2.7`, `2.11`, `3.1`) — anchored on 朱君辉 et al. CCL 2023 (北语, ACL Anthology 2023.ccl-1.46) and/or Kim et al. ACL 2024.
- Partial corroboration: 1 pattern (`2.13`) — connective over-use has 朱君辉 表5 support, but specific bridge phrases are unmeasured.
- Rhetorical tradition: 2 patterns (`2.2`, `2.14`) — Gorrie 2025, an English-tradition source.
- Experience rules `〔待核〕`: 20 patterns.

This count is a credibility boundary. Do not present experience rules as if they had direct Chinese frequency evidence. When a primary figure is cited it must match the source verbatim (see Disclaimer 6: a digest's 「0.729 vs 0.331」 was a misread; the verified figure is 人类 0.251 vs ChatGPT 0.729).
