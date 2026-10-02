# negative-trigger-article-reroute

Negative trigger：路由消歧 → loop-article-writer。

## Input

```text
用 loop-script-writer 帮我写一篇 3000 字的公众号文章,主题是「AI 时代普通人的技能焦虑」,
要有观点有案例,结尾引导关注。
```

## Expected behavior

- 识别为图文观点长文（篇幅/载体/无口播属性）→ 路由 loop-article-writer
- 边界句:口播脚本（念出来的）归本 skill,图文长文（读的）归 article-writer
- 不动笔写文章;可提示:若该主题后续要做口播版,写完文章可回来走「文章改口播」

## Pass criteria

- 明确 reroute,零正文产出
