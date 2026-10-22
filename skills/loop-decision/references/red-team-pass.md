# Red Team Pass

Adversarial review of the leading option. Method lineage: red-teaming as structured challenge to plans and assessments (Hoffman 2017; Zenko 2015; UK MoD Red Teaming Handbook 3rd ed. 2021; CIA Tradecraft Primer 2009 — exact citations in `anchors-and-sources.md`).

## Protocol

1. **Steelman first（必做，先立后破）**：用最强形式陈述支持该选项的理由——比 brief 里写的更强。攻击一个弱化版对手不产生信息（稻草人红队在 rubric 对立面强度维度记 0）。

2. **Four attack lines**（每条至少认真试一次）：
   - **攻证据**：哪些载重 F2 从未核实？什么证据一旦出现就直接推翻关键主张（falsification test）？
   - **攻框架**：这是不是正确的问题？（「选 A 还是 B」可能真问题是「为什么必须二选一」「为什么是现在」）
   - **攻激励**：谁从这个选择中获益？信息输入是否被获益方塑形（中介、销售、急于结案的自己）？
   - **攻时机**：等待的真实成本是多少？「机不可失」有多少是卖方叙事？

3. **Survivor selection**：保留修订后仍然成立的最强反对意见，通常至多 3 条，没有最低条数。每条附一句：「如果 ___ 为真，这条反对就足以否决整个决策。」零条存活也可以，但四条攻击线均须记录检验过什么、依据是什么、如何排除，以及残留未知；无依据的口头解释不算排除。

4. **Into the memo**：幸存反对意见连同否决条件原样写进决策备忘录；若为零，写入带依据的无新增发现记录及残留未知。不得为了达到数量而编造反对意见，也不得通过改措辞把存活问题打磨掉。

## Output format

```markdown
## Red Team（选项 X）
**Steelman**：（该选项的最强论证，2-4 句）
| # | 攻击线 | 反对意见 | 修订后是否仍成立 | 否决条件（如果___为真则足以否决） |
|---|---|---|---|---|
```

## Anti-patterns

- 用无依据的解释消掉红队意见；或者因为 brief 没有改动就断定红队无效。改变与否不决定质量：按四条攻击线的覆盖、所查证据、排除理由和残留未知判断。
- 用红队表演审慎（列 10 条弱反对刷数量）。3 条能否决的 > 10 条挠痒的。
- 红队之后偷偷加固 steelman——幸存反对意见带否决条件入备忘录，不做二次辩护。
