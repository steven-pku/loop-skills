# loop-interview-writer · 中文面试准备

> **v0.2.3 · 指令型面试准备工具**。已有合成案例历史输出的有限行为证据，不是事实核验、自动招聘或求职结果保证。2026-09-21 独立复评的范围、限制及历史问题见 [REVIEW.md](REVIEW.md)；本文不声明标签或发布动作已经完成。

[English](README.en.md) | 中文

面向中文面试准备的纯指令候选：卖点检查 → 经历事实账本 → 故事库 → 答案草稿 → 评分与模拟追问。另有面试官侧出题模式。

`SKILL.md` 中的版本为 `0.2.3`。经复评的运行基线是 `0fbf48eb7fb2e29d5c62af2ae720872178510f42`；本次发布文档修正不改变运行文件。规则要求来源标注、拒绝编造和有限次修订；这些不是对模型行为、事实真实性或求职结果的保证。

## 先审什么

运行契约覆盖非 STAR 适配、定性／真实失败 Result、来源与核验状态、输入信任、隐私边界和累计修订预算。独立复评中，r2 六例及 `conversations-final` 三个实际用户回合在可见正文与相应契约范围内通过；所有执行均早于本次复评，不是本次新测试。旧版 word-count PARTIAL 保留。13 个分发文件与 r2 安装快照逐字一致，不因文档改动要求重跑同一组行为。

## 文件与阅读方式

- [SKILL.md](SKILL.md)：运行入口。
- `references/`：运行所需的规则、评分锚点与模式说明。
- `assets/`：空白模板；不是候选人记录。
- [REVIEW.md](REVIEW.md)：已知缺陷、审查问题与证据限制。
- [SECURITY.md](SECURITY.md)：敏感材料与安全报告边界。

运行内容仅为指令与模板文本；随仓工作流仅作静态格式检查，不执行技能行为。本轮核对了归档、安装快照、历史输入输出和本地文档补丁；没有新启动模型或执行真实宿主安装。记录中的模型名与读取文件清单不能独立认证后台身份或工具访问。不要把下载或静态检查成功当作有效加载或行为通过。

一个不需要真实简历的审查提示：

```text
请只读审查这些规则：如果问题是 HR 面的职业规划或反问，rubric 的非 STAR 规则与正式评分模板是否一致？请引用仓内文件位置，不编造候选人经历或给出修复已通过的结论。
```

## Job Kit 双仓协作

可与 `loop-resume-writer` 通过账本衔接，但不作为本仓发布依赖。本仓内置 `references/career-facts-ledger.md`，可独立使用；本次证据包没有另一仓文件，不能据此认证双仓账本逐字一致或另一仓的发布状态。

协作方式是由使用者保存并显式导入同一份账本；没有自动同步服务。两仓使用时应另核对 schema 与文件哈希；本仓的单独验收不等于联合工作流验收，不以另一仓待验收无限阻塞本仓。

薪资临场 holding 可在本仓独立准备；offer 议价超出范围。相关 [loop-negotiation 固定公开候选](https://github.com/steven-pku/loop-negotiation/tree/383096ca0b0c201315814ded67ca22224be8c1f9) 是历史参考，不声明其当前状态，也不要求安装后才能使用本仓。

## 证据与使用边界

本仓不存储候选人的真实简历或经历账本。独立复评使用单独提供的公开候选与合成输入输出；证据包含历史运行记录。宿主只读／无网络限制参与了防护，原生事件日志和线程 ID 已剔除；可见正文通过不证明宽权限环境下 Skill 单独防护、招聘公平性、跨模型稳定性或真实面试效果。

仅用合成或充分脱敏材料做评审。不要上传身份、联系方式、精确薪资或可识别他人的履历。模型宿主和服务商可能保留输入或生成文件。来源标签不能验证用户提供事实的真伪；评分不能代替录用判断，也不预测面试或求职结果。指令要求和静态检查均不是对模型行为的保证。

## License

[MIT License](LICENSE)，保留源仓许可证原文。

## 安装预备

以下项目级目录沿用随包安装约定，未在本轮另做跨宿主兼容性认证。仅在维护者创建 `v0.2.3` 标签并公布最终提交与归档 SHA-256 后执行；标签不存在、目标目录已存在或哈希不符时停止，不改用移动分支、不覆盖已有目录。标签不是内容哈希，须同时核对发布回执。在目标项目目录执行。

Codex:

```bash
test ! -e .agents/skills/loop-interview-writer || exit 1
mkdir -p .agents/skills
git clone --branch v0.2.3 --depth 1 \
  https://github.com/steven-pku/loop-interview-writer.git \
  .agents/skills/loop-interview-writer
```

Claude Code:

```bash
test ! -e .claude/skills/loop-interview-writer || exit 1
mkdir -p .claude/skills
git clone --branch v0.2.3 --depth 1 \
  https://github.com/steven-pku/loop-interview-writer.git \
  .claude/skills/loop-interview-writer
```

安装后，在相应目录运行 `git rev-parse HEAD`，与发布回执的最终提交比较；核对 `SKILL.md`、`references/`、`assets/` 和 `LICENSE` 的哈希清单。按宿主方式重新加载技能；首次调用可用上面的合成只读审查提示，但不要把该提示当行为回归。宿主未发现技能时仅排查目录和加载方式，不报告安装成功，也不因此抹去已有历史行为证据。
