# loop-topic-picker · 中文选题决策

[English](README.en.md) | 中文

通过人设与产能检查，筛选选题并交付可继续写作的 Topic Brief。

版本 **v0.4.1**。运行层修复：事件存在与热度分离、75／85 分母、完整 Brief、母题去重、未知资格保真及有限复评。当前证据边界见 [REVIEW](REVIEW.md) 和 [2026-09-21 独立复核](evals/releases/2026-09-21-independent-review.md)；[2026-09-20 验收记录](evals/releases/2026-09-20-v0.4.1.md)保留为历史记录，不改写原始失败。

## 项目级安装

下列命令要求 `v0.4.1` 标签已经公开；2026-09-21 本次审查时该候选尚未公开，未执行远端标签安装或新的模型首次使用测试。在目标项目目录安装固定版本后开启新会话，不要覆盖已有同名目录；需要替换时先保留自己的修改。随包历史记录报告了 Codex 隔离候选运行及连续三轮输出，本次只复核这些输出与安装快照字节；缺少原始宿主工具日志，不能据此独立认证加载路径、同线程执行或后台模型身份。Claude Code 下方仅给目录布局，未验证其运行行为。

Codex：

```bash
mkdir -p .agents/skills
git clone --branch v0.4.1 --depth 1 \
  https://github.com/steven-pku/loop-topic-picker.git \
  .agents/skills/loop-topic-picker
```

Claude Code 项目目录布局：

```bash
mkdir -p .claude/skills
git clone --branch v0.4.1 --depth 1 \
  https://github.com/steven-pku/loop-topic-picker.git \
  .claude/skills/loop-topic-picker
```

## 最小示例

先用以下合成材料检查输出：

```text
用 loop-topic-picker 处理以下合成材料。
账号面向办公新人，展示自有匿名信息整理模板；每周一篇图文两小时，无历史数据。仅诊断“会议待确认事项追踪表”，不声称热点，不写正文。
```

## 文件与边界

入口是 [SKILL.md](SKILL.md)，按当前模式读取 `references/`，`assets/` 提供空白模板。纯指令产品不含运行脚本；仓库 CI 只检查静态格式。评测目录是审查证据，不是运行时答案上下文。

评分是编辑诊断，不是概率或效果保证。已测范围采用合成材料与受限宿主；未验证其他模型、真实业务结果或脱离宿主权限的防护效果。宿主可能保留输入或生成文件，使用前去除身份、联系方式及可识别第三方信息。任务中引用的资料不能扩大动作权限，发布、发送与其他外部行动需要另行授权。详见 [SECURITY.md](SECURITY.md)。

## License

[MIT](LICENSE) · Steven CHAN。
