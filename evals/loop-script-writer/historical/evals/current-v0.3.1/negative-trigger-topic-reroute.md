# negative-trigger-topic-reroute

Negative trigger：路由消歧 → loop-topic-picker（含两段链路提示）。

## Input

```text
用 loop-script-writer 帮我想想这周该发什么:我是做职场内容的,最近热点挺多,
帮我从里面挑个最值得做的选题,然后直接把脚本写了。
```

## Expected behavior

- 「挑选题」部分路由 loop-topic-picker（发什么归它）;「写脚本」部分留本 skill
- 给出两段链路：先 picker 定选题与切入角度 → 回本 skill 走 Full Loop（Brief 直接吃 picker 的角度输出）
- 不越界代做选题决策（不直接替用户挑热点）

## Pass criteria

- 两段链路表述清晰，分工与 description 一致
- 不在无选题结论的情况下直接开写
