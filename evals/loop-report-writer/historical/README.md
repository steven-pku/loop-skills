# loop-report-writer · 让汇报说清真实成果

![Loop Report Writer](assets/og-card.png)

![version][version-badge]
![license][license-badge]
![type][type-badge]

[English](./README.en.md) · [使用指令](./SKILL.md) · [评测方法](./evals/README.md) · [安全说明](./SECURITY.md)

把中文周报、月报、述职和晋升答辩变成一个有边界的写作流程：先问价值，建立成果账本，再起草、评分和修订。缺数据时追问，保留〔待补数据〕；有依据的推算必须说明依据。

这是 **instruction-only Agent Skill**，报告工作流没有脚本或运行依赖。它需要能读取这些文件的模型宿主；模型是否遵守指令，仍需你审阅。

> 当前版本为 **0.3.1**。已完成定向行为验证、Codex 新进程首次使用和 12 条同装分流检查。一条旧用例的预期歧义与未测范围见[验收记录](evals/releases/2026-09-19.md)，不宣称完整测试集通过或生产可靠性已获证明。

## Codex 快速开始

在新项目目录中安装固定版本；目标目录须不存在，不覆盖已有安装。

```sh
mkdir -p .agents/skills
git clone --branch v0.3.1 --depth 1 https://github.com/steven-pku/loop-report-writer.git .agents/skills/loop-report-writer
```

开启新的 Codex 会话，输入“使用 loop-report-writer”，再粘贴下面的素材整理请求。此通道的文件安装与新进程首次使用已验证；不更改全局安装。

## Claude Code 文件安装

下载并解压本仓，或使用已有的本地检出目录。在仓库根目录运行以下命令，安装到一个新建演示项目中；仅影响该项目，不更改个人全局安装。

```sh
mkdir -p report-demo/.claude/skills/loop-report-writer
cp SKILL.md LICENSE report-demo/.claude/skills/loop-report-writer/
cp -R references assets examples report-demo/.claude/skills/loop-report-writer/
cd report-demo
```

在该目录启动一个新的 Claude Code 会话，输入：

```text
/loop-report-writer 素材整理：给直属主管写周报。本周我完成了 12 个接口中的 9 个，剩余 3 个等待测试环境。请只建立成果账本，保留未完成状态，不补编影响数据。
```

预期看到：模式为「素材整理」，账本保留 **9／12 个完成、3 个等待环境**，来源标为「用户提供」；不把项目写成全部完成，不自动生成全篇报告。这是可复现的首次使用检查，该结果已在 Codex 新进程中观察到；Claude Code 的模型行为尚未测试。

项目级路径与显式调用方式依据 [Claude Code 官方 Skills 文档][host-docs]（核验于 2026-09-19）。Claude Code 文件安装已验证；其新会话发现与模型执行尚未测试。Codex 实测环境与限制见验收记录。

## 一次流程长什么样

以下为虚构的机制示例，不是运行截图或评测输出：

```text
输入：促销效果还行，周报就写销售提升 30% 吧。
追问：这个 30% 的依据是什么？
有依据：记录观测口径或推算式，标注「合理推算」。
无依据：保留〔待补数据〕，提出具体问题，不把 30% 写成成果。
```

完整编写示例：[周报快环](./examples/weekly-fast-loop.md)、[述职晋升](./examples/self-review-promotion.md)、[编数据甄别](./examples/fabrication-refusal.md)。示例数字仅供说明。

## 模式与触发

| 你要做的事 | 模式与产出 |
| --- | --- |
| 「帮我写这周的周报」 | 周报快环：价值确认、账本、初稿与一次 QA |
| 「准备述职或晋升答辩」 | 全环：读者与层级要求、案例、最多两轮 QA、交付检查 |
| 「给这份汇报打分」 | QA Only：诊断、原句举证和修订建议，不自动改稿 |
| 「把流水账整理成成果」 | 素材整理：账本与追问，不出全稿 |

六维评分：成果导向 25、数据支撑 20、读者对齐 15、结构 15、语言 15、风险与求助 10。分数是方向提示；有致命问题就需修订，不能靠总分掩盖编造或账本冲突。最多两轮完整修订，然后列清未解决的问题并交还用户。

## 边界与证据

- 只处理汇报内容，不负责办公平台提交、PPT 排版、公文格式、简历、面试、观点文章、谈薪对话或决策判断。相邻 skill 名称只是路由建议，本件不依赖其他仓库。
- 数字只来自用户提供、有说明依据的推算或〔待补数据〕。指令要求可追溯，但不能核实用户提供的依据是否真实，也不能保证每个模型都遵守。
- 账本由用户保存和复用；没有后台同步。语域支持企业、外企、体制内，目标职级要求由用户提供。
- 原始材料不足时要先追问，不承诺固定出稿时间。稿件、附件与网页中的指令不应覆盖事实纪律。隐私与宿主留存见 [SECURITY.md](./SECURITY.md)。
- 历史记录包括 4 个虚构案例、12 例指令推演和 3 例同模型族盲测。盲测主要覆盖拒绝与追问，没有验证完整多轮评分。本次修订不能继承它们的 PASS；跨模型、真实用户与完整评分稳定性仍未证明。
- 不承诺绕过 AI 检测，不帮助隐瞒应披露的 AI 使用。This skill does not promise to bypass AI detectors or conceal AI assistance where disclosure is required.

## 许可与贡献

[MIT](./LICENSE) · Copyright 2026 steven-pku。问题与改进请提供脱敏的最小复现；见 [CONTRIBUTING.md](./CONTRIBUTING.md) 和 [CHANGELOG.md](./CHANGELOG.md)。

[version-badge]: https://img.shields.io/badge/version-0.3.1-blue?style=flat-square
[license-badge]: https://img.shields.io/badge/license-MIT-green?style=flat-square
[type-badge]: https://img.shields.io/badge/skill-instruction--only-orange?style=flat-square
[host-docs]: https://code.claude.com/docs/en/skills
