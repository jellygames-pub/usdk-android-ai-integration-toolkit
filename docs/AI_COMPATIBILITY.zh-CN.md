# AI 兼容性说明

这份文档说明当前 USDK Android AI 接入工具包适合哪些 AI 工具，以及适配成本大致如何。

## 支持层级

### 原生目标环境

- `Codex` 或其他具备 Skill 风格工作流的环境

要求：

- 能读取本地文件
- 能执行本地命令
- 能做多文件修改

这套 toolkit 目前就是按这种模式设计的。

### 高优先级适配环境

- `Cline`
- `GitHub Copilot CLI`

这些工具与当前 toolkit 的结构最接近，迁移成本较低。

### 次优先级适配环境

- `Cursor`
- `Claude Code`

这些工具可以复用 Spec、模板和脚本，但不能直接原样消费当前的 `SKILL.md`，需要额外适配层。

可选适配形式：

- rule 文件
- agent 指令
- slash command 包装
- MCP 包装

### 不推荐直接使用

- 仅浏览器聊天型 AI
- 不具备工程访问能力的通用聊天模型
- 无法运行本地脚本的 AI 环境

这些环境可以阅读文档，但不能稳定完成工程级闭环接入。

## 一个可用的 AI 环境至少要具备什么

- 能读取项目文件
- 能运行 `scripts/usdk_doctor.py`
- 能按需运行 `scripts/usdk_repair_runner.py`
- 能修改 Android 工程文件
- 能在修改时保留项目原有逻辑

## 当前推荐顺序

1. `Codex`
2. `Cline`
3. `GitHub Copilot CLI`
4. `Cursor`
5. `Claude Code`

## 迁移说明

- `Codex`
  - 可以直接使用当前仓库

- `Cline`
  - 将 Skill 改写成 Cline 的 rules / workflows
  - Python 脚本可以保持不变

- `GitHub Copilot CLI`
  - 将 Skill 改写成 custom instructions / hooks / agent 包装
  - Python 脚本可以保持不变

- `Cursor`
  - 将 Skill 改写成 Cursor rules 或 `AGENTS.md`
  - Spec 与脚本仍可继续复用

- `Claude Code`
  - 将 Skill 改写成 slash commands、本地指令或子代理流程
  - Spec 与脚本仍可继续复用
