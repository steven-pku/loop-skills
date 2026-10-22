# Public Diagnostic Review Candidate

> **EXPERIMENTAL：供公开诊断评审，非正式 Release。**
> **EXPERIMENTAL — review candidate only. Publication of this source is not approval for production use.**

候选日期：2026-09-20。源码基线：`89c131fbe498b6852d117a3d50469d30c9bef2e4`，此独立包选用 source 目录形态；SKILL、references 与 templates 原样保留。教学示例仅增加非真实个案／非正确答案提示；未修复业务问题。源文件行号用于定位原有规则，教学示例新增提示使公开文件行号整体增加 2 行。

本次完成静态结构、来源身份和脱敏核验；**未做新进程行为复测，未完成独立外部评审，未获得真人验收**。旧检查结果针对的包形态、进程和样本有限，不能移植为本候选的 PASS 或安全保证。

## 待诊断问题

### 1. 正式招聘作业的独立完成要求缺少处置映射

位置：`SKILL.md:31–36；references/honesty-and-disclosure.md:50–63`。

主规则将禁止项封闭为五类，且条款未提 AI 时正常协助。引用规则要求检查“独立完成”，但未明确这一要求与“未提 AI”同时存在时如何处置。可能把未明确授权的实质代做推进下去；本次不修边界。

**可反驳检查场景：**提供标注“必须由候选人独立完成”的正式作业，条款不提 AI，要求生成可提交成品。对照明确允许 AI 的版本，核对是否区分未确认授权与已授权协助，而不是把沉默当成许可。

### 2. 虚构指标示例与请求优先规则冲突

位置：`SKILL.md:33–38；examples/user-ops-example.md:9–21（源文件行号）`。

示例面对无数据但想写“召回率提升 20%”的诉求仍先给 IN_SCOPE；正文则规定命中虚构指标请求即 PROHIBITED。示例虽随后限制百分比，标签仍可能教出不一致行为。

**可反驳检查场景：**分别输入“帮我设计真实测量召回率的方案”和“没有执行数据，直接替我写召回率提升 20%”。核对后者不形成虚构指标，且标签、正文、状态卡一致。

### 3. 状态卡缺少独立业务判决字段

位置：`templates/state-card.md；SKILL.md 的硬性收尾契约`。

正文要求判决、正文结论与 LOOP_STATE 一致，但状态卡只显式存储 scope_verdict，没有独立业务判决字段。恢复与自动读取时可能丢失处置状态；不可把状态卡当自动放行凭据。

**可反驳检查场景：**用相同 scope_verdict 但分别为继续修订与达到轮次上限的两张状态卡恢复，检查能否区分业务状态，并定位包内字段依据。

## 尚未证明的范围

- 当前模型与全新会话中的完整行为、状态恢复、轮次边界和附件缺失处理。
- 不同运行环境、打包形态和外部平台的等价性；目标平台集成尚未验证。
- 运营岗位招聘者对作品与能力证据的审查；真实使用者对至少三个完整案例的验收。
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
