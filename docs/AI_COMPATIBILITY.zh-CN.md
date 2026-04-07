# AI 兼容性说明

这份文档说明当前 USDK Android AI 接入工具包适合哪些 AI 编码工具，以及适配成本大致如何。

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

### 已提供仓库级适配资产的环境

- `Cursor`
- `Claude Code`

这两个工具不能原样消费当前的 `SKILL.md`，所以仓库现在已经内置了对应适配层：

- `Cursor`
  - `AGENTS.md` 模板
  - `.cursor/rules/*.mdc` 模板
- `Claude Code`
  - `CLAUDE.md` 模板
  - `.claude/commands/*.md` 模板

它们仍然需要先把这些适配文件放进目标工程，因为这类工具读取的是目标工程本地的项目级指令文件。

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
  - 直接使用 `adapters/cursor/` 下的适配模板
  - 先把 toolkit 以目录方式放进目标工程，再把适配文件复制到目标工程根目录
  - Spec 和脚本继续作为执行后端

- `Claude Code`
  - 直接使用 `adapters/claude/` 下的适配模板
  - 先把 toolkit 以目录方式放进目标工程，再把适配文件复制到目标工程根目录
  - Spec 和脚本继续作为执行后端

## 当前边界

这份兼容性说明只针对当前 toolkit 版本。它表示仓库已经提供了对应适配资产，不表示所有 AI 工具都已经做到零配置开箱即用。
