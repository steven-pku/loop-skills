# Prompt Examples

Use these examples to test whether the skill triggers and behaves correctly.

## WeChat Full Loop

```text
Use loop-article-writer to write a 公众号 opinion essay.
Topic: 为什么 AI 写作越来越像正确废话
Reader: 用 AI 辅助写作但觉得文章越来越空的中文写作者
Goal: 让读者看完知道先定核心立场，再设计 QA Loop
Core stance: AI 写作最容易失败的地方不是生成正文，而是没有检查观点是否成立
Required sections: 开头钩子、一个模拟失败案例、反驳段、结尾判断
Tone: 像一个人在分享经验，不要写成百科解释
Exclusions: 空泛概念、连续排比、AI 腔、过度客气、SEO 套路
Output: Full Loop
```

## Xiaohongshu Rewrite QA

```text
Use loop-article-writer QA Only mode for 小红书.
下面是一篇我写的小红书笔记。不要重写，先做 QA，指出 AI 腔、节奏和事实风险。
[paste draft]
```

Expected behavior:

- Identify article type.
- Quote original sentences for deductions.
- Flag Chinese AI-tone patterns before fact-risk issues.
- Mark hard facts as `〔待核验〕` if sources are missing.

## Fast Loop

```text
Use loop-article-writer fast loop.
写一篇公众号文章，主题是“写作 prompt 为什么解决不了观点空的问题”。
读者是会用 AI 但文章没有判断感的内容创业者。
要有一个可反驳的主张、一个案例、一个结尾判断。
```

## Rewrite Only

```text
Use loop-article-writer to rewrite this draft for 公众号.
Keep my main idea, but remove Chinese AI tone, sharpen the stance, and mark unverifiable hard facts.
[paste draft]
```

## Secondary X Example

```text
Use loop-article-writer to convert this long article into an X thread.
Each post should move the argument forward. Do not just split paragraphs.
[paste article]
```

## Research Gap Handling

```text
Use loop-article-writer to write an article about the most important ETF trends in 2026.
It must include data and examples.
```

Expected behavior:

- Do not invent data.
- Ask for sources or mark claims as `〔待核验〕` if retrieval is unavailable.
- Build the article around verified or user-provided materials.
