# Cursor 接入方快速开始

本文说明如何把 USDK Android AI Integration Toolkit 用在 Cursor 中。

## 本适配使用到的 Cursor 官方能力

Cursor 官方支持：

- 项目根目录的 `AGENTS.md`
- `.cursor/rules/*.mdc` Project Rules

这套 toolkit 同时提供了这两种形态，方便接入方按项目习惯选择。

## 推荐目录结构

先把 toolkit 以目录方式放进目标 Android 工程，推荐路径：

```text
<game-project>/
  tools/usdk-android-ai-integration-toolkit/
```

然后把下面两个适配文件复制到目标工程根目录：

- `adapters/cursor/AGENTS.md` -> `AGENTS.md`
- `adapters/cursor/.cursor/rules/usdk-android-integration.mdc` -> `.cursor/rules/usdk-android-integration.mdc`

如果 toolkit 不放在 `tools/usdk-android-ai-integration-toolkit`，复制后必须把文件里的路径一起改掉。

## 首次使用流程

1. 用 Cursor 打开目标 Android 工程。
2. 确认工程内已经包含 vendored toolkit 目录。
3. 先让 Cursor 跑 doctor，不要直接改代码。
4. 如果诊断结果涉及多项修复，再让 Cursor 生成 phased repair plan。
5. 在编辑前人工确认协议模式和其他必须人工确认的项目。
6. 让 Cursor 执行接入修改。
7. 修改完成后，再让 Cursor 重新跑 doctor，并输出剩余 manual inputs。

## 推荐提示词

诊断：

```text
先读取 AGENTS.md 和 Cursor rule，再运行这个工程的 USDK doctor，并总结结果。
```

生成修复计划：

```text
使用工程内 vendored 的 USDK toolkit，为这个 Android 工程生成分阶段修复计划。
```

执行接入：

```text
使用工程内 vendored 的 USDK toolkit 完成 USDK 接入。编辑前先确认协议模式，并提醒我 exit 逻辑，再执行需要的修改，最后重新运行 doctor。
```

## Cursor 不允许自行猜测的内容

- 协议模式
- exit 相关产品逻辑
- Provider 后台参数
- 后端回调参数
- 真实的角色字段映射
- 真实的支付字段映射

## 说明

- Cursor 可以只用 `AGENTS.md`，也可以同时使用 `.cursor/rules`。
- 当前版本的 `doctor` 和 `repair runner` 仍然要求本机具备 `Python 3.x`。
