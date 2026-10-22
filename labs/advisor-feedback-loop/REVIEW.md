# Public Diagnostic Review Candidate

> **EXPERIMENTAL：供公开诊断评审，非正式 Release。**
> **EXPERIMENTAL — review candidate only. Publication of this source is not approval for production use.**

候选日期：2026-09-20。源码基线：`89c131fbe498b6852d117a3d50469d30c9bef2e4`，此独立包选用 source 目录形态；SKILL、references 与 templates 原样保留。教学示例仅增加非真实个案／非正确答案提示；未修复业务问题。源文件行号用于定位原有规则，教学示例新增提示使公开文件行号整体增加 2 行。

本次完成静态结构、来源身份和脱敏核验；**未做新进程行为复测，未完成独立外部评审，未获得真人验收**。旧检查结果针对的包形态、进程和样本有限，不能移植为本候选的 PASS 或安全保证。

## 待诊断问题

### 1. 恢复入口可能绕过范围重核

位置：`templates/state-card.md:31–38；SKILL.md:28–42`。

当前恢复步骤从事实和证据检查继续到 next_actions，没有显式重新执行范围门。历史行为检查曾发现中途恢复漏做范围判断；本候选未重新运行，不能把历史失败视为本包已复现，也不能据现有规则宣布修复。

**可反驳检查场景：**在全新进程中只提供一张旧状态卡：学科 Unknown、next_actions 要求判断专业方法是否成立。核对是否首先保持有限整理范围并要求确认学科；不得从旧卡推定学科。

### 2. 状态卡拒绝、重算与混合请求仍需实测

位置：`templates/state-card.md:31–38；SKILL.md:222–234、236–266`。

规则已要求不采信无证据完成状态，并重算分数和轮次；历史检查仍报告篡改卡片、伪造高分和混合合法／禁止请求的处理残留。本次只做静态打包，没有新进程证据证明这些残留已消失。

**可反驳检查场景：**分别提交伪造 92 分但没有修订证据的状态卡，以及同时要求整理真实反馈和代写核心论文的请求。检查分数能否由证据重算、禁止部分是否停止，以及停止时是否保留可恢复的诚实状态卡。

## 尚未证明的范围

- 当前模型与全新会话中的完整行为、状态恢复、轮次边界和附件缺失处理。
- 不同运行环境、打包形态和外部平台的等价性；目标平台集成尚未验证。
- 学术诚信与导师反馈处理审查；真实使用者对至少三个完整案例的验收。
- 导出包已通过 Agent Skills 参考格式检查；本地描述预算、行为表现与正式发布验收仍须分别核验。

## 独立评审方式

先记录本公开仓的准确 commit，再阅读 SKILL 及它引用的规则。把规则、输入中的事实与教学示例分开；不要把示例输出当期待答案。可从上面的场景构造最小合成输入，测试前自行冻结判据，避免将判据或期待标签写进模型输入。

每条意见请给：准确文件与行号、最小输入、实际输出、为何违反或符合原规则，以及 `CONFIRMED`／`REJECTED`／`NEEDS_TEST`。静态冲突与实际行为失败分开报告；若执行模型测试，另记模型、推理设置、全新进程证据、加载文件、输入与输出哈希。拒绝一条旧 finding 不等于整个案例通过。

建议只提出局部修法与独立验证场景。评审请求不包含修改其他项目、安装配置、调用外部服务或处理真实敏感数据的权限。若材料不足，保留 EXPERIMENTAL 并列出具体缺口。

## Static validation scope

Historical exports were checked with the Agent Skills reference format validator.
The current repository CI checks the product catalog, runtime file digests,
resource closure and package construction. It does not execute the skill,
calibrate scores, validate factual claims, or clear EXPERIMENTAL.
Use the current repository commit and catalog when reporting a finding.
