# 安装一款

本分支提供候选布局，正式发行切换门尚未完成。请先看[兼容表](compatibility.md)；未通过的路线不要视为支持承诺。旧版固定发行包继续有效。

## 项目级目录

[Codex 官方技能文档](https://learn.chatgpt.com/docs/build-skills)描述项目中的 `.agents/skills`；[Claude Code 官方技能文档](https://code.claude.com/docs/en/skills)描述 `.claude/skills`。此处测试的精确版本和限制见兼容表。

从固定候选 commit 取得源码或核对摘要后的单款 ZIP。在目标项目中建立相应目录，把完整的 `loop-<name>/` 放进去。结构必须是：

```text
project/
  .agents/skills/loop-article-writer/SKILL.md   # Codex
  .claude/skills/loop-article-writer/SKILL.md   # Claude Code
```

资源目录跟随 SKILL.md 完整复制；不要只复制一个文件。开启新会话，显式选择该款并运行最小示例，再核对实际资源读取和输出。两种目录是两条独立路线，不要求同装。

## 源码候选演练

以下项目内复制形式已用于本轮文件布局演练；宿主调用状态单列，不把复制成功当作行为通过。从已检出的固定候选仓根执行：

```sh
mkdir -p /path/to/project/.agents/skills
cp -R skills/loop-article-writer /path/to/project/.agents/skills/
```

Claude Code 把目的目录换成 `.claude/skills`。目标同名目录已存在时，先走[迁移与回滚](migration.md)，不得直接覆盖或把两版叠加。

本轮没有改任何个人全局安装。第三方安装器、插件商店及来源锁自动迁移尚未测试，当前不提供这些路线的已验证命令。
