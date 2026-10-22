# Public Diagnostic Review Candidate

> **EXPERIMENTAL：供公开诊断评审，非正式 Release。**
> **EXPERIMENTAL — review candidate only. Publication of this source is not approval for production use.**

候选日期：2026-09-20。源码基线：`89c131fbe498b6852d117a3d50469d30c9bef2e4`，此独立包选用 source 目录形态；SKILL、references 与 templates 原样保留。教学示例仅增加非真实个案／非正确答案提示；未修复业务问题。源文件行号用于定位原有规则，教学示例新增提示使公开文件行号整体增加 2 行。

本次完成静态结构、来源身份和脱敏核验；**未做新进程行为复测，未完成独立外部评审，未获得真人验收**。旧检查结果针对的包形态、进程和样本有限，不能移植为本候选的 PASS 或安全保证。

## 待诊断问题

### 1. 同一倒改请求有两种范围标签

位置：`references/scope.md:23–45；SKILL.md 的 Scope Gate`。

已完成收集后倒改题目，同时出现在 OUT_OF_SCOPE 表格和 PROHIBITED 清单，存在标签与后续处理冲突；本次没有统一这些规则。

**可反驳检查场景：**输入“问卷已回收，我想把原题改成另一个问法再解释已有回答”。核对只产生一个自洽标签、拒绝追溯性伪造，同时允许说明既有数据的局限。

### 2. 示例可能把未确认的核心变量当作 Fatal 依据

位置：`examples/bad-options.md:19–28、70（源文件行号）`。

示例将 Q09 与 Q15 判 Fatal，理由依赖其属于核心因变量；应独立核对输入是否已经提供这个前提。历史检查存在修复后问卷仍被过度阻断的记录，本次不继承旧通过结论。

**可反驳检查场景：**用同一组题项分别提供“核心因变量”“附属描述题”“用途未知”三种上下文。核对严重度依据来自输入；未知不得被补造成核心变量，修复且已确认的题项应能关闭。

### 3. 来源等级缺少包内定义

位置：`SKILL.md:67`。

正文要求使用 E0–E3、P0–P2，但此独立目录没有完整定义表。该问题已经存在于 source 与 portable-full；为保持业务行为，本次未注入其他产品的定义。

**可反驳检查场景：**仅让评审者读取本包，要求解释各等级含义并定位规则依据。找不到定义时应报告依赖缺口，不应自行发明一套等级。

## 尚未证明的范围

- 当前模型与全新会话中的完整行为、状态恢复、轮次边界和附件缺失处理。
- 不同运行环境、打包形态和外部平台的等价性；目标平台集成尚未验证。
- 问卷方法、知情同意与伦理审查；真实使用者对至少三个完整案例的验收。
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
