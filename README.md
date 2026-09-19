# Loop Skills · 把草稿改到有依据

<p align="center"><img src="assets/og-card.jpg" alt="Loop Skills — Draft. Review. Improve." width="600"></p>

![version][version-badge] ![license][license-badge] ![type][type-badge]

[English](README.en.md) | 中文 · [共同方法](LOOP-PATTERN.md) · [公开评审候选](REVIEW-CANDIDATES.md) · [版本记录](CHANGELOG.md)

把一次性生成变成可检查的写作闭环：先确认材料和目标，再起草、逐项评审，按问题修订，到达上限就把剩余问题交还给你。

这里汇总已经公开发布的独立 Skill。每件单独安装，完整用法、评测和限制以对应版本的文档为准。

## 已发布项目

| Skill | 用来做什么 | 固定版本 | Stars |
| --- | --- | --- | --- |
| [Article Writer][article] | 给中文观点长文检查立场、结构与事实，再按需要修订 | [v0.3.0][article-release] | [![Article stars][article-stars]][article] |
| [Report Writer][report] | 从真实成果账本整理周报、述职和晋升材料 | [v0.3.1][report-release] | [![Report stars][report-stars]][report] |

## 公开评审候选

另有 [13 个候选的独立评审入口](REVIEW-CANDIDATES.md)，按固定提交列出范围、REVIEW 与只读评审请求。它们全部维持 **HOLD**，不在上面的已发布产品表内；公开源码不表示正式发布、行为验证通过或推荐安装。

## 选择与安装

1. 修改观点文章，打开 [Article Writer 的安装说明][article-install]；整理工作成果，打开 [Report Writer 的安装说明][report-install]。
2. 选择文档中已验证的宿主与项目级安装方式。这个索引仓无需安装，不包含 `SKILL.md`。
3. 开启新会话，运行对应 README 的最小示例。先确认模式、事实边界和输出符合需要，再用于自己的材料。

例如，Article 的 QA Only 模式可以先诊断一句空泛的观点；Report 的素材整理模式先把“12 个接口完成 9 个、3 个等待环境”记成账本。具体检查方法与实际结果见各仓评测记录。

## 共同方法

```text
确认目标与材料 → 初稿 → 逐项评审 → 修订 → 达标或停下并列出剩余问题
```

评分帮助定位问题，不代表事实已经核实，也不是效果保证。各件的前置条件、评分表、轻量模式和停止规则不同；[Loop Pattern](LOOP-PATTERN.md) 解释共同思路。

## 边界与路线

- Skill 是给模型宿主读取的文本指令；具体执行效果取决于宿主、输入和人工复核。
- 各仓分别披露测试环境、通过范围和已知限制。安装成功、模型行为通过、真人认可分别判断。
- 使用脱敏材料；模型宿主可能保留输入和输出。第三方徽章会向其服务请求公开仓库信息。
- 已发布项目表只在产品实际发布、链接可访问后扩充；开发候选另列于评审目录，不作为可安装产品推荐。
- 反馈功能问题时，到对应项目提供脱敏的最小复现。索引问题可在本仓提出。

## 许可

[MIT](LICENSE) · Steven CHAN。每件 Skill 的许可及第三方来源说明以各自仓库为准。

[version-badge]: https://img.shields.io/badge/version-0.1.0-blue?style=flat-square
[license-badge]: https://img.shields.io/badge/license-MIT-green?style=flat-square
[type-badge]: https://img.shields.io/badge/type-skill%20index-orange?style=flat-square
[article]: https://github.com/steven-pku/loop-article-writer
[report]: https://github.com/steven-pku/loop-report-writer
[article-release]: https://github.com/steven-pku/loop-article-writer/releases/tag/v0.3.0
[report-release]: https://github.com/steven-pku/loop-report-writer/releases/tag/v0.3.1
[article-install]: https://github.com/steven-pku/loop-article-writer/blob/v0.3.0/README.md#安装
[report-install]: https://github.com/steven-pku/loop-report-writer/blob/v0.3.1/README.md#codex-快速开始
[article-stars]: https://img.shields.io/github/stars/steven-pku/loop-article-writer?style=social
[report-stars]: https://img.shields.io/github/stars/steven-pku/loop-report-writer?style=social
