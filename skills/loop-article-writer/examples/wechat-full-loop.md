# WeChat Full Loop Example

Dogfood example from Round 3.

Topic: `为什么大多数人用 AI 写出来的中文文章，一眼就能看出是 AI 写的`

## Article Brief

- Topic: 为什么大多数人用 AI 写出来的中文文章，一眼就能看出是 AI 写的
- Platform: 公众号
- Reader: 已在用 AI 辅助写作的中文写作者
- Reader's current state: 能生成初稿，也会手动改几遍，但发出去还是被读者一眼识破
- Reader's current misunderstanding: 以为是用词太华丽或提示词不够细，实际问题是中文 AI 写作有独特的句法和结构指纹
- Desired result after reading: 能识别自己文章里的 AI 句法指纹，知道该改骨架而非换皮
- Core stance: 中文 AI 文章被一眼看穿，不是因为用词，是因为句法骨架和结构节奏有统一指纹；改词不动骨，白改
- Article type: opinion
- Platform target: 公众号深度长文，保留判断感，不写成教程
- Fact risk: medium
- Supporting materials: `chinese-ai-tone-patterns.md` 的 25 条模式；自身作为 AI 写作本文的元体验；行业公开讨论
- Required sections: hook, target, core stance, evidence, objection, turn, ending judgment
- Exclusions: 空泛概念、AI 腔、连续排比、百科解释、SEO 套路
- Tone: 经验分享，直接，有判断，承认自身也是 AI 在写
- Output mode: Full Loop
- Success criteria: QA >= 85, no fatal issues, stance sharpness >= 18/30
- Assumptions: 25 条 AI 指纹模式多为经验性观察；维度级特征有实证支撑但正文引用需核验
- Missing materials: 读者真实被识破的稿件、A/B 对比测试数据

## Source Map

| Article Function | Material To Use | Claim / Evidence | Fact Risk | Platform Function | Status |
|---|---|---|---|---|---|
| Hook | 改了三遍的 AI 稿还是被读者说像 AI | 经验性观察 | low | create recognition | ready |
| Core stance | 改词不动骨，白改 | 判断 | low | tell reader why this matters | ready |
| Problem | 读者误以为是用词问题 | 观察+类比 | low | show why old way fails | ready |
| Evidence / case | 四层指纹 + before/after 对照 | 经验法则；维度级实证需核验 | medium | make believable | ready |
| Framework / template | 自检三步法：立场、节奏、个人例子 | 方法 | low | make usable | ready |
| Objection / mistake | 人类也会用排比 | 判断 | low | prevent shallow agreement | ready |
| Ending judgment | 真问题不是像 AI，而是没有立场和毛刺 | 判断 | low | leave stance | ready |

## Outline

1. Hook: 改了三遍，读者还是说像 AI 写的。
2. Target: 大多数人以为问题是用词，于是只改华丽词和套话。
3. Core stance: 指纹在句法骨架和结构节奏，不在单个词。
4. Evidence: 句法、结构、标点、组合分布。
5. Objection: 人类也会排比、总结、用逗号。
6. Turn: AI 文章不是写得差，而是太正确、太光滑。
7. Ending judgment: 先看立场、短段和真实经验，别只改词。

## Draft v1 QA

- Article type: Opinion Essay
- QA loop: 1/2
- Stance Gate: Restatement test Pass | Rebuttability test Pass
- Meta-article exemption: Applied

| Dimension | Score | Evidence / Deduction | Revision Rule |
|---|---:|---|---|
| Stance Sharpness /30 | 24 | 立场清晰可反驳，但“改骨架”缺具体 before/after。 | 增加全段 before/after 对照。 |
| Argument Structure /20 | 16 | 模式“evidence 段连续堆四层指纹”+ 段落范围“证据段”。 | 拆证据段，中间加短停。 |
| Fact Discipline /15 | 12 | 未标注 25 条模式多为经验性观察。 | 加 `据：经验法则，非频率实证`。 |
| Hook Strength /10 | 8 | Hook 具体，但读者内心反应不足。 | 加一句“不服气”。 |
| Material Density /10 | 6 | 缺全段对照案例。 | 增加改词 vs 改骨架案例。 |
| Chinese AI-Tone Cleanup /8 | 5 | 元文章例示句豁免；作者承载句仍有三连排比。 | 拆三连，保留必要例示句。 |
| Structural Variation / Rhythm /5 | 3 | 证据段内部格式太齐。 | 加独句段和节奏变化。 |
| Ending /1 | 1 | 有判断。 | - |
| Title /1 | 0 | 原题像问题说明，无立场。 | 改成判断式标题。 |

Total: 75  
Decision: Revise  
Fatal Issues: Material density close to fatal due to missing concrete case.

## Revision Rules

1. Add a full before/after paragraph showing word-level edits versus structure edits.
2. Split evidence into syntax, structure, punctuation, and distribution with rhythm changes.
3. Apply meta-article exemption only to quoted examples; revise carrier sentences that still sound templated.
4. Mark pattern claims as experience rules unless using verified empirical references.
5. Change the title into a stance.

## Polished Version

### AI 写作最大的破绽不在用词，在骨架

改了三遍，还是被一眼识破。

你用 ChatGPT 写了篇公众号文章，自己读了觉得还行，改了几处措辞，删掉几个“赋能”和“破局”。你觉得应该没问题了——结果发出去，评论区第一条：“这是 AI 写的吧？”

不服气。你明明改过了。

问题不在词。

大多数人以为 AI 文章的破绽在“用词太华丽”。把“赋能”换成“帮忙”，把“破局”改成“打破僵局”，删掉几个“毋庸置疑”和“不言而喻”，就算去过 AI 味了。

去掉的是皮。骨架一点没动。

中文 AI 文章真正的指纹，不在某个词用得多，而在句法骨架和结构节奏。

**先看句法。**

AI 特别爱用几副句式骨架。

排比三连。三个结构相似的从句排在一起，像口号：“它改变了我们的生活方式，改变了我们的工作模式，改变了我们的思维方式。”人类偶尔排比，是蓄意强调。AI 排比，是因为这个模板太顺了，不用白不用。

“不是 A 而是 B”的万能对比。“真正的挑战不是技术，而是人心。”听起来有力量，但你仔细看，这个句式可以套进任何文章：真正的挑战不是 X，而是 Y。它不传递信息，只传递“我在对比”的姿态。

“在……中”开头。“在数字化转型中，企业面临着诸多挑战。”删掉这个开头，意思完全不变。它只是占了个位置。

还有“不仅是……更是……”的递进套话、“正如 X 所言”的伪引经、“与此同时”的机械桥接。这些句式不是不能用，但 AI 用的频率和均匀度暴露了它（据：经验法则，非频率实证）。人类用一次是为了效果，AI 用三次是因为模板就在那里。

**再看结构。**

AI 的文章有个更深的指纹：每个段落都是总分总。先说一个论点，展开两句，再回到论点。每段长度差不多。例子全是正面的，转折全在段尾，结尾一定总结。全文没有一个独句段——那种只放一句话、故意让读者停一下的段落。

读起来“正确”。但没有呼吸。

**标点也是指纹。**

AI 用逗号做一切停顿，偶尔句号，几乎没有破折号、冒号、分号。节奏像节拍器：嗒、嗒、嗒、嗒。人类写文章会急——一个破折号打断自己，一个冒号抛出结论，一个感叹号表示这事我真在意。

AI 不急。因为它没有在意的事情。

所以，任何单条特征，排比、总分总、逗号多，人类也会有。但 AI 的指纹不在单点，在组合和均匀度。三个句式指纹叠在一起，每段结构雷同，标点节奏平坦。组合起来就像笔迹鉴定：不用读内容，看运笔就知道是同一只手。

有人会说：人类也会排比，也会总结，也会用逗号啊。对。但人类用排比是一篇文章里用一次，AI 用三次。人类段落长短交错，AI 每段差不多。人类会偏心——某个论点展开三段，另一个一笔带过。AI 端水，每个论点分到的篇幅差不多。指纹在分布，不在单点。

**给你看一个具体的对照。**

下面这段话，是典型的 AI 生成：

> 在 AI 写作日益普及的今天，越来越多的内容创作者开始反思：AI 究竟是提升了写作效率，还是降低了内容质量？这个问题值得深思。

你改词试试：“在 AI 写作越来越普遍的当下，不少内容创作者开始思考：AI 到底提高了写作效率，还是拉低了内容质量？这个问题值得认真想想。”

没区别。骨架没变：开头“在……中”，中间设问，结尾“值得深思”。你只是换了皮。

换成改骨架：

> AI 时代的内容创作者，效率确实上去了。但内容质量呢？很多人在装没看见。

开头去掉了“在……中”，拆成两个短句，设问变成了短促的反问，“值得深思”变成了“装没看见”——一个有态度的判断。字数少了，但信息密度和人的语气出来了。

这就是改词和改骨架的区别。

**再深一层。**

AI 文章的问题不是“写得差”，是“太正确”。段落完整，转折丝滑，观点端水。像一面打磨过的墙——光滑，但没有抓手。

人写东西有犹豫，有偏心，有没想清楚就写出来的句子，有一段话明显比别人长因为作者真的在意那件事。那些“毛刺”，才是人味。AI 帮你把毛刺都磨掉了——顺便把你的人味也磨掉了。

所以别再改词了。改词是最省力的假动作。你真正该做的是三件事。

第一，你的文章有没有一个能被反驳的立场？如果没有，你写的不是文章，是材料。

第二，有没有一段话是短的？哪怕只有一句话独占一行。如果没有，你的节奏就是 AI 的节奏。

第三，有没有一个例子是你自己的经历里拿出来的，不是 AI 编的通用案例？如果有，把它放进去，别换。

三样都有，AI 的壳就碎了。

## Final QA

- Article type: Opinion Essay
- QA loop: 2/2
- Stance Gate: Restatement test Pass | Rebuttability test Pass
- Meta-article exemption: Applied

| Dimension | Score | Evidence / Deduction | Revision Rule |
|---|---:|---|---|
| Stance Sharpness /30 | 24 | Passes the /30 integer stance scale: specific and rebuttable, but not a 30/30 counterintuitive anchor. | - |
| Argument Structure /20 | 18 | Structure now moves hook -> target -> evidence -> objection -> case -> turn -> ending. | - |
| Fact Discipline /15 | 13 | Pattern claims are marked as experience rules; no hard data is presented as verified. | - |
| Hook Strength /10 | 9 | Opening creates recognition and emotion quickly. | - |
| Material Density /10 | 8 | Full before/after contrast added; still no real external case. | - |
| Chinese AI-Tone Cleanup /8 | 6 | Meta-article examples exempted; carrier sentences mostly avoid high-impact patterns. | - |
| Structural Variation / Rhythm /5 | 5 | Paragraph length and punctuation rhythm now vary. | - |
| Ending /1 | 1 | Ends with action and judgment. | - |
| Title /1 | 1 | Title carries a stance. | - |

Total: 85  
Decision: Pass  
Fatal Issues: None

## Publish Check

- Suitable for platform: Yes
- Best audience: 已在用 AI 辅助写作、觉得“改了还是像”的中文写作者
- Strongest part: before/after 对照段
- Weakest remaining part: 无真实作者案例；组合指纹判断缺中文单句式频率实证
- Fact-risk status: medium; 25 条 AI 指纹模式多为经验性观察，维度级特征可补实证但需核验
- Suggested title / opening line: `AI 写作最大的破绽不在用词，在骨架` / `改了三遍，还是被一眼识破。`
- Should publish as: 公众号深度长文
