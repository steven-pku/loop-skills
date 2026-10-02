# Expected Diagnosis: WeChat Datapack — No Judgment

- Article type: requested as opinion essay, but it behaves as a 资料包 / 科普综述 — complete coverage, zero stance. This is the 完整≠判断密度 failure (cf. positive anchor `anchor-positive-wechat-depth`, which names this exact problem; here it is the live failing draft).
- Stance Gate should FAIL the restatement test: there is no single rebuttable claim — only an organized pile of categories (起源 / 商业模式 / 平台 / 品类 / 趋势). Stance Sharpness ~0/30 (a pile of materials).
- FATAL issues (multiple):
  - "Reader cannot act or repeat the core stance after reading" — reader finishes knowing more facts but has no judgment to carry away and nothing to do.
  - "Ending has no judgment" — 综上所述 + 列举式结尾 (起源清晰、模式多元、平台丰富、品类齐全) restates categories instead of taking a position (AI-tone 2.15 + 3.6).
  - "Opinion essay has no rebuttable stance."
- AI-tone: flag the homogeneous 每段总分总 / equal-length section template (`X 方面，……` repeated across §2-§6) — pattern「全文 6 段以『X 方面』起手、总分总等长」+ paragraph range §2-§6, deduct under Structural Variation / Rhythm; flag 综上所述列举式结尾 under Chinese AI-Tone Cleanup. (Do not double-charge.)
- Fact discipline: 「二〇〇四年前后」起源时间 and the iPod+broadcast etymology are F2 checkable — should be marked `〔待核验〕` rather than asserted, but these are NOT the load-bearing problem; the load-bearing problem is the absence of judgment, not a single wrong fact. Do not let fact-marking distract from the fatal stance failure.
- Decision: Revise (fatal present). Revision direction = the article must pick ONE judgment about播客 (e.g. 「国内播客的瓶颈不是内容，是它至今没找到不靠爱发电的变现」) and reorganize the material to serve and defend that stance; a完整 survey is not publishable as an opinion essay. NOT a polish — a stance has to be added before re-scoring.
