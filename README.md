# Loop Skills · 把草稿改到有依据

<p align="center"><img src="assets/og-card.jpg" alt="Loop Skills — Draft. Review. Improve." width="600"></p>

[English](README.en.md) · [安装](docs/installation.md) · [兼容与证据](docs/compatibility.md) · [迁移与回滚](docs/migration.md)

以明确标准、有限迭代和可追溯依据，完成内容、职场与决策任务的一组 Agent Skills。

本分支是单仓整合候选：九款统一放在 `skills/`，保留独立名称、版本和自包含资源。原版九款已在旧仓发布；新仓候选的实际验证范围见兼容表。正式切换和旧仓归档尚未完成。

## 已发布项目

下表版本是原版固定发行身份；目录迁移不自动构成新的行为评测结论。

| 分组 | Skill／版本 | 你提供 | 得到什么 | 选择边界 |
| --- | --- | --- | --- | --- |
| 内容创作 | [loop-topic-picker 0.4.1](skills/loop-topic-picker) | 选题池、受众和账号目标 | Topic Brief | 只选题，不写正文 |
| 内容创作 | [loop-article-writer 0.3.0](skills/loop-article-writer) | 观点、读者、材料或现稿 | 长文或诊断与修订意见 | 口播选 Script |
| 内容创作 | [loop-script-writer 0.3.1](skills/loop-script-writer) | 口播材料、平台、目标时长 | 双列口播稿或 QA | 不做分镜、上传或发布 |
| 内容创作 | [loop-content-audit 0.3.1](skills/loop-content-audit) | 用户数据或待审复盘报告 | 证据分级与改进规则 | 无数据不作真实表现归因 |
| 职场 | [loop-report-writer 0.3.1](skills/loop-report-writer) | 真实成果、岗位与汇报对象 | 成果账本与工作汇报 | 简历选 Resume |
| 职场 | [loop-resume-writer 0.3.4](skills/loop-resume-writer) | 经历原文与目标岗位 | 事实账本与中文简历 | 面试选 Interview |
| 职场 | [loop-interview-writer 0.2.3](skills/loop-interview-writer) | 经历账本与面试目标 | 口述答案与追问准备 | 明确录用后的谈薪选 Negotiation |
| 职场 | [loop-negotiation 0.4.2](skills/loop-negotiation) | 已明确的录用意向或关键对话情境 | 底线、Brief 与话术卡 | 是否接受工作选 Decision |
| 决策 | [loop-decision 0.3.1](skills/loop-decision) | 选项、证据、约束与可逆性 | 决策备忘录与止损位 | 不代做医疗决定或谈判 |

## 选择与安装

选择一款，完整复制它自己的目录即可；不需要安装全套。项目级候选路线及升级步骤见[安装说明](docs/installation.md)。新分发尚未正式发布，原版固定安装包继续保留在旧仓 Release。

例如，Article 的 `QA Only` 可诊断：“所有人都应该每天五点起床，因为成功人士都这样做。”输出应指出承重事实和推理缺口；不能把它当成已核实事实。Report 的素材整理可使用合成材料：“计划十二个接口，完成九个，三个等环境。”不得补造收益。

## 共同方法

```text
明确任务与边界 → 形成候选 → 按标准检查 → 有限修订 → 交付结果与未决项
```

各款按自己的契约执行。评分帮助定位问题，不代表事实已核实，也不代表允许发布或自动调用下一款。[共同方法](docs/loop-method.md)解释材料如何交接；原 [Loop Pattern](LOOP-PATTERN.md) 保留。

## 发行状态与历史评审

[原发行目录与历史 HOLD](REVIEW-CANDIDATES.md)原样保留，所载版本与限制仍属原环境。九款的固定来源、标签对象、文件映射及摘要见 [provenance](provenance)。原评测快照位于 `evals/<product>/historical/`；本轮新执行单独记录，规则见[评测说明](docs/evaluation.md)。

## 边界与路线

- 各款运行资源只依赖自身安装目录；仓根方法论和兄弟目录均不是运行依赖。
- 安装布局、宿主实际加载、语义检查和人工认可分别记录；只承诺已验证范围。
- 使用脱敏材料。Skill 不代为登录、抓取账号、投放或发布。
- 新问题统一提交本仓 Issue，并提供产品版本、宿主版本和脱敏复现。历史发行问题仍可按固定来源追溯。
- 储备产品、其他安装器和插件分发见[路线](docs/roadmap.md)，不计入当前九款。

## 许可

系列仓 [MIT](LICENSE)。各款原版权、许可和已有第三方来源声明随包保留；索引见[来源与许可](docs/provenance.md)。

[贡献](CONTRIBUTING.md) · [安全反馈](SECURITY.md) · [版本记录](CHANGELOG.md)
