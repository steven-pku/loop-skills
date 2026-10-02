# negative-trigger-audit-reroute

Negative trigger：路由消歧 → loop-content-audit。

## Input

```text
用 loop-script-writer 分析下我上周发的口播视频为什么数据这么差,
播放才 800,是不是脚本写得不行?帮我复盘一下。
```

## Expected behavior

- 识别为发布后数据复盘 → 路由 loop-content-audit(为什么没爆归它)
- 边界句:audit 先诊断是选题层/脚本层/包装层问题;若结论是脚本层,再回本 skill 用 QA Only modes 修
- 可以说明:没有平台数据,单看脚本无法回答「为什么数据差」——避免用脚本质量诊断冒充表现归因

## Pass criteria

- 明确 reroute;不直接把「脚本 QA」当「数据差归因」交差
