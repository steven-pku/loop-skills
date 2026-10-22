# Public Diagnostic Review Candidate

> **EXPERIMENTAL：供公开诊断评审，非正式 Release。**
> **EXPERIMENTAL — review candidate only. Publication of this source is not approval for production use.**

候选日期：2026-09-20。源码基线：`89c131fbe498b6852d117a3d50469d30c9bef2e4`，此独立包选用 source 目录形态；SKILL、references 与 templates 原样保留。教学示例仅增加非真实个案／非正确答案提示；未修复业务问题。源文件行号用于定位原有规则，教学示例新增提示使公开文件行号整体增加 2 行。

本次完成静态结构、来源身份和脱敏核验；**未做新进程行为复测，未完成独立外部评审，未获得真人验收**。旧检查结果针对的包形态、进程和样本有限，不能移植为本候选的 PASS 或安全保证。

## 待诊断问题

### 1. 示例把“禁止使用”改读成“禁止采用结果”

位置：`examples/complete-record.md:5、28、36–38（源文件行号）；references/policy-parsing.md`。

示例政策明示禁止用于结果分析；EV03 确有询问回归结果解释，却因未采用输出而改判允许但需披露。后文额外加入“并采用其结论”这一限制，超过示例条款原文。

**可反驳检查场景：**提供两份明确不同的政策：一份禁止使用 AI 分析结果，另一份仅禁止采用 AI 分析结论；同一事件为提问后未采用。核对事件与政策逐字对应，不能自行给第一份增加采用条件。

### 2. 状态卡不足以独立承载总体判决

位置：`templates/state-card.md；SKILL.md:192–199、242–247`。

主规则要求总体判决与 LOOP_STATE 一致，但模板没有独立总体判决字段，披露状态或分数也被明确禁止替代总体判决。跨会话恢复或自动消费该卡片前仍需验证。

**可反驳检查场景：**在同一 scope_verdict 下分别给出待确认政策与高风险未整改的记录，恢复后核对总体判决依据；不得由 disclosure_status 或 current_score 推定可披露。

## 尚未证明的范围

- 当前模型与全新会话中的完整行为、状态恢复、轮次边界和附件缺失处理。
- 不同运行环境、打包形态和外部平台的等价性；目标平台集成尚未验证。
- 学校政策、学术诚信与披露准确性审查；真实使用者对至少三个完整案例的验收。
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
