# Public Diagnostic Review Candidate

> **EXPERIMENTAL：供公开诊断评审，非正式 Release。**
> **EXPERIMENTAL — review candidate only. Publication of this source is not approval for production use.**

候选日期：2026-09-20。源码基线：`89c131fbe498b6852d117a3d50469d30c9bef2e4`，此独立包选用 source 目录形态；SKILL、references 与 templates 原样保留。教学示例仅增加非真实个案／非正确答案提示；少数示例中的人数已泛化，没有修复业务问题。源文件行号用于定位原有规则，教学示例新增提示使公开文件行号整体增加 2 行。

本次完成静态结构、来源身份和脱敏核验；**未做新进程行为复测，未完成独立外部评审，未获得真人验收**。旧检查结果针对的包形态、进程和样本有限，不能移植为本候选的 PASS 或安全保证。

## 待诊断问题

### 1. 用户自述在规则与示例中被分到不同等级

位置：`references/evidence-model.md:5–18；examples/weak-evidence.md:11–17（源文件行号）`。

来源规则将用户自述列为 E1，弱证据示例却把三条自述全部列 E0。缺基准、缺归因和缺书面材料应作为不同缺口核对，不能未经说明改变来源等级。

**可反驳检查场景：**只提供“我协助运营公众号、粉丝涨了一些、领导说不错”，不附证明。核对来源等级、证据强度与归因缺口是否分别说明；再补真实可查看记录，检查升级依据。

### 2. 采用记录可能被错误升级成效果或个人归因证据

位置：`references/evidence-model.md:7–10、21–35；references/attribution-rules.md:14–27`。

规则允许采用记录和第三方确认升级为 E3，并称 E3 可支持影响类结论，但采用、产生效果与个人贡献并不等价。当前表格的区分不够明确；本次未补新判据。

**可反驳检查场景：**提供一份被团队采用的模板与署名，但没有前后指标，也未证明独立设计或主导。核对只陈述可核验的采用与角色，不推导效率提升、因果效果或个人领导贡献。

### 3. 状态卡没有独立业务判决字段

位置：`templates/state-card.md:3–34；SKILL.md 的硬性收尾契约`。

状态卡明确记录范围标签，但没有独立业务判决字段；当前分数不能替代业务处置。该结构需在恢复和下游读取前验证。

**可反驳检查场景：**用相同范围标签、不同未解决归因问题的状态卡恢复；检查正文判决与恢复后的处置能否一致，不能凭分数自动进入最终简历包装。

## 尚未证明的范围

- 当前模型与全新会话中的完整行为、状态恢复、轮次边界和附件缺失处理。
- 不同运行环境、打包形态和外部平台的等价性；目标平台集成尚未验证。
- 个人贡献归因与简历表述审查；真实使用者对至少三个完整案例的验收。
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
