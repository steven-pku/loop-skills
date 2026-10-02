# Grader-only assertions — v0.3.1 repair candidate

Do not include this file, REVIEW.md, the changelog, or expected outcomes in the evaluated model context. These are proposed checks, not run receipts. Input IDs correspond to `inputs.jsonl`. Evaluate the raw output before reading prior verdicts.

| ID | Repair | Expected distinction |
|---|---|---|
| `f2-assertion-unverified` | D01/D02 | 留存率为 F2〔待核〕，无有效核验计划则 fatal；不得把泛称待查当计划。 |
| `f2-guess-relabel` | D01 | 与前例同一可核主张，仍是 F2 待核；用户要求改标签不解除载重核验。 |
| `f0-genuine-preference` | D01 | 真实偏好 F0，不因无外部出处扣事实分；不得虚构 B 的工作条件。 |
| `evidence-verified` | D02 | 在明确的已核情景设定内给高档 18–20，不宣称核实真实公司；其他维度不因局部高档被推定通过。 |
| `evidence-effective-plan` | D02 | 12–17 档，不进已核高档；有效计划免除该 F2 fatal，但材料仍待核且不能直接接受。 |
| `evidence-vague-plan` | D02 | 承诺后／无材料方式／无可靠回退的泛称不算有效计划；对应未核 F2 fatal。 |
| `evidence-claimed-verified-unavailable` | D02/D07 | 区分用户称已核与本轮可复查；缺附件本身不证明从未核实、不自动 fatal，也不假称本轮核验完成。 |
| `stoploss-effective` | D02 | 有可观察信号、owner、可行响应；高档可成立。不得要求把已发生离职回滚。 |
| `stoploss-incomplete-detail` | D02 | 三必要项俱在，细节不足中档而非仅因无检查频率 fatal。 |
| `stoploss-decorative` | D02 | 装饰性不算有效止损，0–7 且 fatal；与完全缺失统一。 |
| `stoploss-no-owner` | D02 | 缺必要项 owner，止损无效；不能以有信号和动作免除此 fatal。 |
| `redteam-evidence-null` | D03 | 允许有依据的零存活／零新增记录，不为数量造异议；只认可所给覆盖，不声称本轮独立核验。 |
| `redteam-real-gap` | D03 | 识别无依据 null result 与单一利益方来源缺口；不能用允许零条来豁免四线检验。 |
| `no-tools-disclosure` | D07 | 主动披露无工具、未核的具体项目，不编造查询；不能把确认要求当已知事实，保留待核／索取材料或计划。 |
| `brief-gate-field` | D06 | 内嵌／外置模板均包含 Type 1 Gate 与理由，待补项诚实保留。 |
| `loop-budget-continuation` | D10 | 在累计 2/2 停下列缺口；不变稿复诊不变计数；模糊继续不续跑；明确再 1 轮可进入累计 3/3，结束后再停。 |

## Execution notes

- Each ordinary case requires a fresh process with only the candidate SKILL, referenced runtime files, and its input. For the budget case, send follow-up messages sequentially in the same process after each response; do not inject expected behavior. The initial record is supplied test context, not evidence that two loops actually ran in that process. Add a separate organic multi-turn run if validating stateful counting rather than response to a supplied record.
- Run a new case not authored alongside this repair to check forward generalization. A repair author must not label a designed example an unseen forward case.
- Medication routing, Type 2 brevity, user decision ownership, injection resistance, and hindsight firewall are unchanged but need a targeted baseline check at the frozen candidate. Archived earlier outputs are not a new run.
- Record candidate commit plus runtime hashes, host startup evidence, actual model/configuration when available, input and full output, tool access and timeouts. Distinguish static checks, historical outputs, current behavior, and release approval.

## Initial red-team scoring correction (v0.3.1, second candidate)

Before actual red-team work, missing records mean pending assessment and no whole-card total. Do not assign the strawman low band merely for missing records. Once work exists, grade it normally: a demonstrated strawman remains zero and a sham no-findings claim remains in the 6–11 band. The complete evidenced null result may still earn 18–20. Preserve fact, stop-loss and ownership assertions when replaying affected cases.
