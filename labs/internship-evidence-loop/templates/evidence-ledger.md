# 证据账本

## Event ID 规范

`W<周次>-<序号>`，例如 `W03-02`。序号在同一周内递增，不复用，不重排。

更正历史时新增一条事件，并在 Corrects 字段写旧 Event ID，不修改旧条目。

## 事件条目

```markdown
### W__-__
- Project：
- Situation：
- Role：
- Action：
- Output：
- Outcome：
- Evidence：
- Attribution：
- Confidentiality：
- Evidence Level：
- Next Evidence Action：
- Corrects：
```

字段缺失写 `Unknown`，不留空，不用推测填充。

Outcome 字段注明所处层级：`Did` / `Delivered` / `Adopted` / `Outcome`。

## 索引表

| Event ID | 周次 | Project | Role | Outcome 层 | Evidence Level | 保密分级 | 状态 |
|---|---|---|---|---|---|---|---|
| W01-01 |  |  |  | Delivered | E2 | 需脱敏 | 待补证 |

状态取值：`待补证`、`证据齐备`、`已更正`、`已作废`。

`已作废` 只能由一条新的更正事件设置，原条目内容保留不动。

## 写盘幂等

文件不存在：按本模板创建完整账本。

文件已存在：在文件末尾追加

```markdown
## 追记 · YYYY-MM-DD HH:MM
```

追记段内只放本次新增或更正的事件。规则：

- 不覆盖旧事件；
- 不重排索引表已有行，只追加新行；
- 同一周重复提交时，先比对已有 Event ID，只写新增部分；
- 更正必须成对出现：新事件写 `Corrects`，旧事件在索引表状态列改为 `已更正`，正文不动。

## 三张清单

```markdown
### 强证据
- W__-__：

### 弱证据
- W__-__：缺（产物／基准／第三方确认／贡献边界）

### 无证据
- W__-__：当前不能支持任何对外表述
```

## 下周补证动作

| Event ID | 缺什么 | 最小动作 | 本人可独立完成 | 截止 |
|---|---|---|---|---|
|  |  |  | 是 | |
