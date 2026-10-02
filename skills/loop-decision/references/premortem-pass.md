# Premortem Pass

Protocol adapted from Gary Klein's project premortem (HBR, Sept 2007 — exact citation in `anchors-and-sources.md`). Klein's insight: instead of asking "what could go wrong?" (which invites polite hedging), assume the failure has already happened and ask "what DID go wrong?" — prospective hindsight legitimizes doubt and frees the imagination.

## Protocol

1. **Set the frame exactly** (wording matters — certainty, not possibility):

   > 现在是〔复盘日期〕。我们选了选项 X，并且已经失败得很难看。写下这场失败的简史。

2. **Generate failure reasons** — for the leading option AND each live alternative, not just the favorite. Aim for volume first (the research basis: imagining an event as certain produces ~30% more reasons than treating it as possible — note this is about the NUMBER of reasons generated, not accuracy; see the misquote correction in `anchors-and-sources.md`). Quality filtering comes next.

3. **Classify each credible failure**:
   - **Process failure**（决策就做错了）：证据没核、选项没找全、激励没看清
   - **Execution failure**（决策没错，执行砸了）：资源不足、时机拖过、关键人离场
   - **External shock**（谁都没错）：政策/市场/平台突变——追问的不是「能否预见」而是「能否活下来」

4. **Convert to brief changes** — every credible failure becomes one of:
   - a new evidence requirement（这条 F2 现在必须核）
   - a revised probability（预期结果的概率下调并写明原因）
   - a concrete stop-loss trigger（可观察信号 + owner + 动作）

5. **Null result rule**: a premortem that changes nothing in the brief is either a ritual run or a genuinely robust decision — say which, and why. Do not pad fake findings to look diligent.

## Output format

```markdown
## Premortem（选项 X · 复盘日期 YYYY-MM-DD）
| # | 失败原因 | 类型（process/execution/shock） | 可信度（高/中/低） | 转化为 |
|---|---|---|---|---|
**Brief 变更清单**：（无变更则写明判断依据）
```

可信度锚定：高＝有输入中的直接证据或明确相关先例支撑；中＝合理外推，必须标明依据与不确定性；低＝纯直觉但不可排除。没有直接证据的假设最高只能记中并标 F2／〔待核〕；「可能漏算成本／回本口径不全」「对方可能怎样」「未来可能怎样」不能因为听起来合理就记高。

Confidence attaches to the stated failure scenario, not to the certainty that a field is missing. An observed information gap may be certain while its proposed future consequence remains unknown. If direct evidence supports only the gap, report the gap separately and leave the future failure at medium or low confidence with its uncertainty explicit.

## Anti-patterns

- 只对心仪选项跑 premortem，替代选项裸奔——比较基准失真。
- 把 premortem 写成风险清单复读机（「可能资金不足」「可能没人用」）——每条必须是**这个决策特有**的失败叙事。
- 用 premortem 吓退用户。它的产出是触发器和证据要求，不是恐慌。
