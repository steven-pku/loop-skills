# Loop Article Writer

![Loop Article Writer — scored QA loop](assets/og-card.jpg)

[![validate](https://github.com/steven-pku/loop-article-writer/actions/workflows/validate.yml/badge.svg)](https://github.com/steven-pku/loop-article-writer/actions/workflows/validate.yml)
![version](https://img.shields.io/badge/version-0.3.0-blue)
![license](https://img.shields.io/badge/license-MIT-green)
![type](https://img.shields.io/badge/skill-instruction--only-orange)
![scope](https://img.shields.io/badge/Chinese--first-公众号%20%2F%20小红书-red)

**中文（当前）** · [English overview →](README.en.md)

一篇文章可以写得流畅，却没有值得读者记住的观点。这个 Skill 从观点是否成立开始检查。

Loop Article Writer 反过来做——先给你的**观点**跑一遍评分闭环。第一关「立场闸」先问一句：这篇有没有一个能被反驳的核心观点？没有就打回，不给你润色。因为观点立不住，改得再顺也是「正确的废话」。

立场站住了，才按评分表打分、迭代到达标，最后才清中文 AI 腔。「去 AI 味」是闭环里的一道内置工序，不是单卖的一键改写器。

面向公众号 / 小红书的观点型长文。纯指令、无脚本，配合 Claude Code / Codex 这类 AI 助手使用。

它把写文章变成一个闭环：

```text
定义读者 → 查资料 → 资料地图 → 大纲 → 初稿 → QA 评分闭环 → 润色 → 发布前检查
```

**目录**：[挑模式](#挑一个模式不必每次都跑完整闭环) · [为什么不是 humanizer](#为什么不叫去-ai-味工具humanizer) · [适合](#适合)/[不适合](#不适合) · [核心特性](#核心特性) · [Demo](#demo一次-qa-闭环长什么样) · [纯指令](#为什么是纯指令) · [安装](#安装) · [示例](#用法示例) · [验证](#验证内部冒烟测试非基准) · [证据边界](#证据基础与边界) · [License](#license)

## 挑一个模式（不必每次都跑完整闭环）

- **只想给稿子做 QA** → QA Only：贴一篇稿，拿到评分表 + 修改点，不重写。
- **清理 / 去 AI 味一篇现成的** → Rewrite Only 或 Platform Polish。
- **从零写一篇能发的长文** → Full Loop。
- **快速起稿 + 检查** → Fast Loop。

轻量模式是一等公民；完整闭环留给需要深度的时候。

## 为什么不叫「去 AI 味工具」/「humanizer」

因为它干的是另一件事。humanizer 拿写完的 AI 文重写得不像 AI；这个 skill 的顺序前面说过——立场闸、评分、最后才清 AI 腔。要补的是没说过的那句：清 AI 腔是为了人类读者，不是为了骗过检测器——它是手艺环节，不是产品本体。

这套流程的重点是**先评观点、再按明确标准迭代**，而非一次性替换词句。

## 适合

- 公众号观点型长文和方法类实用长文
- 需要更硬的结构、少一点套话的小红书笔记
- X 长文和推文串（次级支持平台，非默认）
- 知乎长文、newsletter、研究笔记、观点署名文
- 给现成稿子做 QA 诊断
- 带事实纪律检查的改写和润色

平台指南目前覆盖公众号 / 小红书 / X；其他平台（知乎、newsletter）走同一套闭环和通用润色规则。

## 不适合

- 小说、诗歌
- 广告、销售文案
- 通用 SEO 文章
- 平台涨粉黑科技
- 未经核实的平台规则断言

## 核心特性

- 公众号 / 小红书的中文优先默认设置
- 观点文和方法文各一套评分表
- 观点文的立场锐度闸门
- **去 AI 味作为一道闭环工序**：一套带证据分级的中文 AI 腔句法库，从句法、结构、标点三层诊断——集成在闭环里，不是独立的一键改写器
- 分级事实纪律（F0–F3）：从纯观点到必须带来源的高风险声明
- 用于校准评分表的轻量 eval 案例

## Demo：一次 QA 闭环长什么样

价值在闭环，不在魔法般的 before/after。下面是流程示意，展示分数与问题如何引导修改：

```text
初稿 v1  →  QA：立场闸 FAIL（没有可反驳的立场）        →  只迭代立场
初稿 v2  →  QA：71/100 · 致命：结尾泛泛 · AI 腔：不仅…也…, 宏大时代叙事  →  改
初稿 v3  →  QA：86/100 · PASS · QA 闭环 2/2
```

读者看到的是同一篇稿被**打分、被推着改**，不是一次性重写。比如开头这句，就在闭环里从泛泛变成可反驳：

- v1：`AI 的出现正在深刻改变写作……总之，拥抱变化，才能保持竞争力。`
- v3：`别再说「AI 改变了写作」——这句话正确得毫无信息量。真正变的是判断力：你得一眼看出哪一段是「正确的废话」，然后删掉它。`

仅作示意，非基准；实际分数和质量取决于你的宿主模型。

## 为什么是纯指令

没有脚本、没有 runner——每一条行为都是你能读的纯文本。这是刻意设计，不是没做完的 MVP：

- **可审计**——读完每条指令，就知道这个 skill 会怎么处理你的稿子。没有黑盒代码。
- **可移植**——同一个 skill 跑在 Claude Code、Codex 或任何兼容 agent 上。不锁平台。
- **供应链安全**——运行时零依赖，不自动执行任何东西，没有 `npm install`；安装（npx / git clone）与 CI 校验仍继承 npm / Git / GitHub 的信任链，CI 已按 commit SHA 与固定版本 pin。

事实核查 / 联网这些步骤，只在你的宿主 agent 已经带联网工具时才跑；否则 skill 优雅降级并明说。

## 安装

当前版本为 **0.3.0**。16 条原有用例已执行，15 条符合预期、1 条存在事实分级偏保守的问题；另完成闭环、边界、新模式、首次使用和同装分流检查。详见[本次验收记录](evals/releases/2026-09-19.md)。

**按项目安装（Claude Code）**：在自己的项目目录执行，不加 `--global`。

```bash
npx skills@1.7.0 add https://github.com/steven-pku/loop-article-writer/tree/v0.3.0 --skill loop-article-writer --agent claude-code --yes
```

Codex 用户把 `--agent claude-code` 改为 `--agent codex`。安装范围与参数见 [skills CLI 官方说明](https://github.com/vercel-labs/skills#installation-scope)。

**本地发行包**：解压后，在自己的项目目录用本地路径安装；路径指向含 `SKILL.md` 的目录。

```bash
npx skills@1.7.0 add ./loop-article-writer --skill loop-article-writer --agent claude-code --yes
```

**手动安装（Claude Code，当前项目）**：目标目录须不存在，避免覆盖已有安装。

```bash
mkdir -p .claude/skills
git clone --branch v0.3.0 --depth 1 https://github.com/steven-pku/loop-article-writer.git .claude/skills/loop-article-writer
```

运行时入口是 `SKILL.md`，按需读取包内 `references/` 和 `assets/`；无需其他写作 Skill。安装后开启新会话，粘贴下面的最小用例：

```text
使用 loop-article-writer，QA Only，不要重写：
「AI 正在改变世界。我们应积极拥抱变化，与时俱进，共同走向美好未来。」
```

预期：指出缺乏可反驳的立场，引用原句，给出诊断与补充材料需求，不宣称已经可以发表。这个例子用于检查流程，不是质量基准。

## 用法示例

```text
用 loop-article-writer 写一篇公众号观点文。
选题：为什么 AI 写作越来越像正确废话
读者：用 AI 辅助写作但觉得文章越来越空的中文写作者
核心立场：AI 写作最容易失败的地方不是生成正文，而是没有检查观点是否成立
输出：Full Loop
```

```text
用 loop-article-writer 的 QA Only 模式做小红书。
下面是一篇我写的小红书笔记。不要重写，先做 QA，指出 AI 腔、节奏和事实风险。
[贴稿]
```

更多示例见 `assets/prompt-examples.md` 和 `examples/`。

## 验证（内部冒烟测试，非基准）

历史 eval（2026-07-10）是一次**内部手动冒烟测试**：`evals/cases/` 里 16 个 golden case，由全新上下文的 AI agent 当评估者跑——不是人工评审，也不是在真实已发表文章上跑。「cases pass」读作「指令复现出了预期诊断」，不是「已被证明的质量基准」。人工评审和真实用户验证仍待补，欢迎参与。

**历史结果与本次验证分开记录。** 当前版本的 16 条用例、附加检查及已知限制见[验收记录](evals/releases/2026-09-19.md)；不宣称完整用例全通过、评分已校准或真实用户效果已被证明。

跑一个 case：

1. 把一个输入 case 贴进 skill 的 QA 模式。
2. 检查输出是否命中预期诊断。
3. 不要求分数精确一致；要求命中正确的致命问题、维度、来源引文和修改规则。

with/without-baseline 方法和构建期测量见 `evals/README.md`；历史原始报告保留在开发仓，发行包只提供测试用例与验证边界。

## 证据基础与边界

「带证据分级」**不等于**「已被科学证明」：

- 中文 AI 腔句法库有 **27 条**：4 条锚定一手语料研究（朱君辉 等，CCL 2023），1 条部分支持，2 条来自修辞传统（一篇 Substack 文章，非同行评审），以及 **20 条老实标注 `〔待核〕` 的经验规则**。不确定性是标出来的，不是藏起来的。
- 语料数字来自 **GPT-3.5 时代** 的对照；在更新的模型上差距可能收窄。
- 平台打法是未经核实的从业者经验。面向 agent 的指南只给定性的手艺方向；没有重新核实的数字不作为本发行包的使用规则。
- 去幻觉工序只能降低并标出风险，**不保证**事实正确；离线层有哪些盲区，文档里写明了。

## 范围与边界

- **不是绕过 AI 检测器的工具。** 它为人类读者清理 AI 腔，不针对、不优化、不保证规避任何 AI 检测器。如果你的目标是过检测器或「降 AI 率」，它会拒绝，转而给你一份诚实的质量修改建议。
- **平台打法是定性的。** 给手艺方向，不给算法数字——出处与边界见上文「证据基础与边界」。
- **事实纪律是分级的，不是保证的**——见上文「证据基础与边界」。

## License

MIT。见 `LICENSE`。
