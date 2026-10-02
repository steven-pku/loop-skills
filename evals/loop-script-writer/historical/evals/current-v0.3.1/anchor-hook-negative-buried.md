# anchor-hook-negative-buried

Anchor pair A（负例）。配对：`anchor-hook-positive-named`。按各自锚点评价，不强求固定分差。

## Input

```text
用 loop-script-writer 的 QA Only 模式看这条 60 秒抖音口播的开头(先只看钩子):
「大家好,我是老王,做剪辑八年了。今天想跟大家聊一个话题,就是很多新手朋友经常会问我的:
剪辑软件到底应该怎么选。这个问题其实挺复杂的,我们先从头说起。市面上的剪辑软件大概分三类……」
```

## Expected behavior

- Hook Gate 失败：前 3 句是自我介绍 + 话题预告 + 「从头说起」——教科书级背景铺垫开场
- 钩子类型无法命名（七类均不命中）,按 hook-types.md 判定「砍到冲突处」
- 只指出可选钩子类型和改动方向，不写替换句，更不能编造第一人称经历
- Hook 强度维度 0-7 分档；fatal「开头 3 句无钩子」触发

## Pass criteria

- fatal 判定明确，指认三句原文
- 改动方向能命名钩子类型；QA Only 没有实际改稿
