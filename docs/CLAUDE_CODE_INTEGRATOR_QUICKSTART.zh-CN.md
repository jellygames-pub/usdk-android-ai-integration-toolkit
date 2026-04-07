# Claude Code 接入方快速开始

本文说明如何把 USDK Android AI Integration Toolkit 用在 Claude Code 中。

## 本适配使用到的 Claude Code 官方能力

Claude Code 官方支持：

- 项目级 `CLAUDE.md`
- 项目级 `.claude/commands/` 自定义命令

这套 toolkit 把接入工作流拆成了共享上下文加可复用命令两层。

## 推荐目录结构

先把 toolkit 以目录方式放进目标 Android 工程，推荐路径：

```text
<game-project>/
  tools/usdk-android-ai-integration-toolkit/
```

然后把下面这些适配文件复制到目标工程：

- `adapters/claude/CLAUDE.md` -> `CLAUDE.md`
- `adapters/claude/.claude/commands/usdk-diagnose.md` -> `.claude/commands/usdk-diagnose.md`
- `adapters/claude/.claude/commands/usdk-plan.md` -> `.claude/commands/usdk-plan.md`
- `adapters/claude/.claude/commands/usdk-integrate.md` -> `.claude/commands/usdk-integrate.md`

如果 toolkit 不放在 `tools/usdk-android-ai-integration-toolkit`，复制后必须把文件里的路径一起改掉。

## 首次使用流程

1. 在目标 Android 工程根目录打开终端。
2. 确认工程内已经包含 vendored toolkit 目录。
3. 在该目录启动 Claude Code。
4. 运行 `/usdk-diagnose`
5. 如有必要，运行 `/usdk-plan`
6. 编辑前人工确认协议模式和其他必须人工确认的项目。
7. 运行 `/usdk-integrate`
8. 检查最终 doctor 结果和剩余 manual inputs

## 推荐命令

- `/usdk-diagnose`
- `/usdk-plan`
- `/usdk-integrate`

如果需要缩小范围，可以在命令后追加自然语言说明。

## Claude 不允许自行猜测的内容

- 协议模式
- exit 相关产品逻辑
- Provider 后台参数
- 后端回调参数
- 真实的角色字段映射
- 真实的支付字段映射

## 说明

- `CLAUDE.md` 是这条接入工作流的项目共享记忆入口。
- `.claude/commands/` 中的命令只是项目命令模板，团队可以继续按需修改。
- 当前版本的 `doctor` 和 `repair runner` 仍然要求本机具备 `Python 3.x`。
