# mode-duration-compression-complete-v0.3.0

Tests duration compression with a complete synthetic source rather than a placeholder.

## Input

```text
用 loop-script-writer 的时长压缩模式，把下面这条 60 秒标准语速的完整口播，压成 30 秒标准语速版。

「很多人写口播，第一步就打开文档，结果盯着空白页半天写不出第一句。我今天给你四个办法，让你先有话可说，再把话写好。第一，先别写完整句，只列三个你最想讲的关键词。第二，对着手机把这三个词随口讲一遍，把录音里最顺的那句抄下来。第三，找一个真实场景，比如你是在通勤路上、会议结束后，还是做完一次失败尝试后想讲这件事。第四，把开头里的背景句删掉，直接从冲突或结果开始。四步都做完，你才开始润色。现在就拿你最想讲的主题，先写下三个关键词。」
```

## Expected behavior

- Treat the supplied text as complete and synthetic; do not ask for a missing source.
- Re-select rather than proportionally trim: keep the opening problem and the strongest executable path, dropping weaker or repetitive steps as needed.
- Rewrite the four-method promise so the compressed version promises only what it actually delivers.
- Produce a 30-second two-column script, declare the 130-character target for standard pace, report actual count and deviation, and keep the result within ±15% or revise once.
- Run a light fatal scan after compression and preserve a single concrete CTA.

## Pass criteria

- No source facts or first-person experience are invented.
- The compressed promise matches the retained content.
- Read-aloud count and greater-than-30% fatal boundary are applied correctly.
- Output is a complete compressed script, not a list of editing suggestions.
