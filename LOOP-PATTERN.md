# Loop Pattern

[返回目录](README.md)

Loop 的用途是让生成结果可以被检查和修订。一次写完之后，读者常常仍需判断：观点是否成立，材料有没有依据，结构是否回应了目标，以及哪些地方还不能交付。

## 共同构件

1. **前置判断**：确认目标与输入是否足以继续；材料不足时先问清楚。
2. **结构化材料**：区分用户提供的事实、有依据的推算、观点与未知项。
3. **明确的评审标准**：每条批评对应原句、材料或可解释的缺口。
4. **不能被平均分掩盖的问题**：例如编造数字、关键事实冲突或未兑现的承诺。
5. **按问题修订**：优先修正关键缺口，然后重新评审受影响部分。
6. **有界停止**：达到该 Skill 的轮次上限后，交付当前版本和未解决问题，避免无限循环。
7. **轻量入口**：只要诊断或整理素材时，不强制生成完整成稿。

不同任务使用不同标准。Article Writer 检查观点与文章，Report Writer 先建立成果账本；不能把两套分数直接比较。每件的具体规则以对应版本的 `SKILL.md` 为准。

## 证据与限制

数字锚点和判断规则应标明来源或经验性质。输出得分不等于事实已验证；模型可能误读材料、过度扣分或漏掉问题。评测记录应同时写出输入、执行环境、实际观察和未通过部分。

已发布两件的工作流使用文本指令及仓内参考文件。安装工具与模型宿主仍有各自的依赖、权限和数据留存方式；文本可读不等于不存在执行风险。

## English summary

A Loop workflow makes drafts reviewable: check the goal and inputs, organize evidence, apply explicit criteria, repair the identified gaps, and stop at a declared limit. Lightweight modes avoid forcing every request through a full draft-and-revise cycle. Different skills use different criteria; scores are not interchangeable or guarantees of quality. Consult each release for its exact instructions, observations and limitations.
