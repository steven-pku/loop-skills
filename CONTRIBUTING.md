# 贡献与发行身份

九款各自维护在 `skills/<name>`；不创建第二份可发现的 SKILL.md。新功能、指令或运行资源变化至少升级产品补丁版本，并更新本款证据。目录位置或纯包装变化可保持运行版本，但必须增加 packaging_revision，已发布资产不得覆盖。

metadata.version 是版本唯一输入；运行 `python3 tools/catalog.py` 生成导航，`python3 tools/catalog.py --check` 检查漂移。来源清单包含明确的运行文件集合及摘要。共同根文档变更不重新给九款打产品标签。

产品标签形如 loop-topic-picker-v0.4.1，指向不可变整仓 commit，声明只覆盖对应产品目录。合集标签形如 series-2026.10.1，记录各款版本与摘要，不表示全量重测。包名还携带 p1 等分发修订。

验证命令：

```sh
python3 -m pip install -r tools/requirements.txt
python3 tools/catalog.py --check
python3 tools/validate.py
python3 tools/check_controls.py
python3 tools/package.py --output /tmp/loop-packages
```

构建输出在仓外，正式构建必须来自干净固定提交；未提交的准备构建需显式加 --allow-dirty，并记录为 preparation。对运行变更检查版本、资源闭合和相关行为；对根导航做链接检查。原历史评测不编辑或重判。反馈使用脱敏材料；Issue 与 PR 不含私有路径或账号凭证。版本和发行不得自动发布。
