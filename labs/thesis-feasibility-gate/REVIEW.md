# Public Diagnostic Review Candidate

> **EXPERIMENTAL：供公开诊断评审，非正式 Release。**
> **EXPERIMENTAL — review candidate only. Publication of this source is not approval for production use.**

候选日期：2026-09-20。源码基线：`89c131fbe498b6852d117a3d50469d30c9bef2e4`，此独立包选用 source 目录形态；SKILL、references 与 templates 原样保留。教学示例仅增加非真实个案／非正确答案提示；未修复业务问题。源文件行号用于定位原有规则，教学示例新增提示使公开文件行号整体增加 2 行。

本次完成静态结构、来源身份和脱敏核验；**未做新进程行为复测，未完成独立外部评审，未获得真人验收**。旧检查结果针对的包形态、进程和样本有限，不能移植为本候选的 PASS 或安全保证。

## 待诊断问题

### 1. 信息不足时的范围门与初步评分规则未完全衔接

位置：`SKILL.md:30–43、47–62`。

范围门把材料不足以支持任何判断列为 OUT_OF_SCOPE 并停止实质判断；最低输入规则又要求关键项缺失时先给初步评分。极少信息或全未知输入的边界仍不清晰。

**可反驳检查场景：**分别只给一句研究意图，以及给题目但数据、方法、授权全部未知。核对是否解释适用分支、未知是否保留，以及是否避免把缺信息写成确定的不可行或放行。

### 2. 可修复 Fatal 的退出判据与示例冲突

位置：`references/verdict-rules.md:7–13、33–42、61–65；examples/over-broad-topic.md；examples/successful-scope-reduction.md`。

优先规则要求交付时任何未关闭 Fatal 都判 NO-GO；后面的 GO WITH CONDITIONS 条件仍写“无不可修复 Fatal”，部分示例保留 Fatal 却使用条件通过。当前候选原样保留，不能把示例当正确答案。

**可反驳检查场景：**给出一个数据授权尚未确认、可通过换公开数据解决的题目。尚未换源时核对 Fatal 与判决一致；用户实际确认换源后独立重算，不能只改措辞就清除 Fatal。

### 3. 方法条件需要专家区分

位置：`references/method-fit.md:35–43`。

DID、IV 与 RDD 被放在一组共同条件下，可能把各自识别假设混同。这里只确认文本采用同组条件，未做领域专家验证，也未执行方法推断实测。

**可反驳检查场景：**由研究方法评审者分别给出只适用于 DID、IV 和 RDD 的最小设计，检查所需识别假设是否被正确区分；不接受仅凭方法名称给出可行结论。

## 尚未证明的范围

- 当前模型与全新会话中的完整行为、状态恢复、轮次边界和附件缺失处理。
- 不同运行环境、打包形态和外部平台的等价性；目标平台集成尚未验证。
- 研究方法、数据可得性与伦理审查；真实使用者对至少三个完整案例的验收。
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
