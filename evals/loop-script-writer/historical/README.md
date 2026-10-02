# Loop Script Writer

> **v0.3.1** · [评测记录](evals/releases/2026-09-20-v0.3.1.md) · [审查与验证范围](REVIEW.md)

![Loop skill cover](assets/cover.jpg)

![version](https://img.shields.io/badge/version-0.3.1-blue)
![license](https://img.shields.io/badge/license-MIT-green)
![type](https://img.shields.io/badge/skill-instruction--only-orange)
![scope](https://img.shields.io/badge/Chinese--first-口播短视频-red)

**中文（当前）** · [English overview →](README.en.md)

把中文口播短视频脚本从「一次性生成」变成打分闭环：Hook Gate（前 3 句钩子判定）→ 双列草稿（口播 × 画面提示）→ 读稿模拟（语速估时长 + 呼吸点）→ rubric 打分 → 迭代改写到能开口念。

专治 AI 脚本三大病：**前 3 秒留不住人、念起来像文章、时长失控。**

## 挑一个模式（不必每次都跑完整闭环）

| 模式 | 什么时候用 | 跑什么 |
|---|---|---|
| **Full Loop** | 从零写一条脚本 | 全流程 + 打分迭代 |
| **Fast Loop** | 快速出稿 | Hook Gate + 单轮打分 |
| **QA Only** | 手里已有脚本 | 诊断不改写：钩子判定 + 读稿报告 + 评分卡 + top-3 修法 |
| **时长压缩** | 3 分钟改 60 秒 | 重选高密度点重写，不是等比例删减 |

## 适合

- 抖音 / 视频号 / B站 / 小红书的口播类脚本（知识、测评、观点、经验分享）
- 给现有脚本做「念出来会不会死」的诊断
- 文章改口播稿（自动防「逐词替换假口语」）
- 时长档改编：30s / 60s / 3min / 10min 四档，字数按语速档换算

## 不适合

- 图文 / 公众号观点长文 → [loop-article-writer](https://github.com/steven-pku/loop-article-writer)
- 选题决策与切入角度 → [loop-topic-picker](https://github.com/steven-pku/loop-topic-picker)（「发什么」归它，「怎么写」归本 skill）
- 发布后数据复盘「为什么没爆」 → [loop-content-audit](https://github.com/steven-pku/loop-content-audit)
- 直播带货话术、分镜表与拍摄执行

## 核心特性

- **Hook Gate 前置**：前 3 句不过关不写正文——失败只循环「钩子+承诺+首转折」，省 token 也省耐心。七类钩子分类学（悬念/冲突/利益/痛点/反常识/权威/结果前置），出处与证据层级全标注
- **读稿时长模拟**：240-350 字/分是可覆盖的计划档，不是官方标准或对所有人的断言；优先用你的实测语速，偏离目标超过 30% 才触发时长 fatal
- **呼吸单元纪律**：一行口播 = 一口气；书面语替换表 + 「书面语成段」fatal 判定
- **双列输出**：口播行 × 画面提示行，拿到手能直接开拍
- **AI 腔口语子集**：自包含的听感检查表，只保留「念出来才暴露」的模式（排比三连、递进套话、列举式结尾……），运行时不依赖其他仓库
- **事实纪律 F0-F3**：口播念出去收不回——载重数字无源 = fatal；平台机制玄学（「XX 才能上热门」）禁入脚本
- **诚实的数据边界**：当前未核到四平台的官方「及格线」出处，本 skill 不编造阈值装权威——查无出处的流行数字在 references 里有明确禁引清单

## 为什么是纯指令

没有脚本、没有 runner——每一条行为都是你能读的纯文本：

- **可审计**——读完指令就知道它会怎么处理你的稿子，没有黑盒
- **可移植**——使用同一组运行文件；各宿主的兼容性以实测为准
- **供应链安全**——运行时零依赖，不自动执行任何东西；安装与 CI 校验继承 npm / Git / GitHub 的信任链，CI 已按 commit SHA 与固定版本 pin

## 安装

**Codex 项目级安装**（在目标项目根目录执行，目标目录应不存在）：

```bash
mkdir -p .agents/skills
git clone --branch v0.3.1 --depth 1 \
  https://github.com/steven-pku/loop-script-writer.git \
  .agents/skills/loop-script-writer
```

在该项目开启新会话，使用下面的最小请求。发布验证使用 Codex CLI 0.155.1、配置模型 `gpt-6-astra`／`xhigh`；实际读取了项目内完整 Skill 与所需引用文件。测试结果与限制见 [评测记录](evals/releases/2026-09-20-v0.3.1.md)。

```text
用 loop-script-writer 的 QA Only 模式，只诊断以下开头，不改稿：
“整理照片前，先挑一小批试试。看看复制到新位置后能不能正常打开，再处理剩下的。”
```

**Claude Code 项目级目录示例**：使用同一 tag，把上面目标目录改为 `.claude/skills/loop-script-writer`。本版未执行 Claude Code 行为验证；其他兼容宿主也需自行验证。

运行时入口是 `SKILL.md`，只在需要时加载 `references/`。根目录文档是发布和贡献材料，运行时不加载。不要覆盖已有安装；升级前保留自己的修改。

## 用法示例

```text
用 loop-script-writer 写一条抖音口播。
主题：新手做视频号最容易踩的一个坑
时长档：60 秒，快节奏
观众：刚开始做视频号的兼职创作者
核心信息：不要一开始就买设备
```

```text
用 loop-script-writer 的 QA Only 模式。
下面是我写的口播稿，60 秒档。不要重写，先诊断：钩子、念感、时长。
[贴稿]
```

完整示例：[60 秒 Full Loop](examples/60s-douyin-full-loop.md) · [QA Only 压线敏感性](examples/qa-only-diagnosis.md)

## 边界声明

- 只负责脚本撰写、诊断、改写与压缩；不管理账号，不上传、发布、发消息或投放广告。
- 未发布脚本默认离线处理。需联网核事实时，只查最小必要断言，不把整篇未发稿送入查询。
- 交付前需人工审核；不保证流量、完播、互动、涨粉、审核通过或事实正确。
- 本 skill 面向真人听众提升口播质量、去 AI 腔，**不针对、不优化、不保证规避任何 AI 检测器**。Not an AI-detector-evasion tool: it improves spoken-script quality for human listeners and does not target, optimize for, or guarantee bypassing any AI detector.

## License

MIT © Steven CHAN
