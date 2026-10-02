# Expected Diagnosis: Mixed AI/Human Carrier

- Article type should be opinion essay. Stance passes both Stance Gate tests; Stance Sharpness around 24/30 (sharp target + boundary + reframing).
- Meta-article exemption does NOT apply: topic is OKR / small-team management, not AI writing. Every carrier sentence is in scope.
- This case tests DISCRIMINATION, not blanket deduction. The QA must flag AI-tone only on the genuinely AI-tone carrier sentences and must NOT penalize the clean human ones.
  - FLAG (deduct under Chinese AI-Tone Cleanup): 原文「OKR 改变了我们的工作方式，改变了我们的协作模式，也改变了我们的思维方式」(§2) — 排比三连 (2.1), equal-weight slipper-slide.
  - DO NOT FLAG as AI-tone: 「真正的问题不是有没有目标，而是有没有人盯」(§3) is a 不是A而是B (2.2) shape but it is concrete, load-bearing, and earns its contrast — this is the human-side correct use the patterns file warns not to over-penalize. Treat as clean, or a soft note at most, not a stacked deduction.
  - DO NOT FLAG: 「给自行车装飞机仪表盘」/ 「喊一嗓子全听见」/ 「每周肯追你一句的人」 — concrete, specific, human voice; reward under Material Density / rhythm.
- Note that the author themselves frames the 排比三连 line as a mistake they later disown (`现在看就是套话`); a sharp reading recognizes the second occurrence is partly self-critique, but the verbatim 排比 still reads as AI-tone and is the right single deduction target.
- Material Density high (real 7-person team, 周一一句话 / 周五对一次 mechanism, concrete analogy).
- Pass condition for this case: deduction is precise (the 排比三连 line is caught; the legitimate 不是A而是B and concrete lines are spared). A blanket "全文 AI 味重" verdict, or charging the §3 contrast the same as the §2 排比, is a fail — it shows the pattern check cannot discriminate.
- Likely lands Pass (>= 85) after the one AI-tone deduction; the AI-tone line is easy to rewrite and is not fatal.
