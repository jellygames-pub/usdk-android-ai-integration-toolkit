# USDK Android AI 接入工具包

面向提供方的 USDK Android 工程级 AI 接入工具包。

英文文档入口：
- [README.md](README.md)

## 当前版本说明

- 当前版本：`0.3.0`
- 当前状态：提供方内部 Beta
- 当前脚本运行依赖：`Python 3.x`
- 当前不包含：免 Python 的公开交付形态

## 仓库中包含的内容

- 面向 Codex / Skill 类环境的接入 Skill
- 结构化接入规范
- 结构化修复 Playbook
- 静态诊断脚本 `usdk_doctor.py`
- 分阶段修复计划生成脚本 `usdk_repair_runner.py`
- Java / Gradle 模板参考
- Cursor 适配模板
- Claude Code 适配模板
- Fixture 与示例输出

## 推荐阅读顺序

- 提供方流程：[docs/USDK_PROVIDER_WORKFLOW.zh-CN.md](docs/USDK_PROVIDER_WORKFLOW.zh-CN.md)
- 接入方快速开始：[docs/INTEGRATOR_QUICKSTART.zh-CN.md](docs/INTEGRATOR_QUICKSTART.zh-CN.md)
- Codex 接入方快速说明：[docs/CODEX_INTEGRATOR_QUICKSTART.zh-CN.md](docs/CODEX_INTEGRATOR_QUICKSTART.zh-CN.md)
- Cursor 接入方快速说明：[docs/CURSOR_INTEGRATOR_QUICKSTART.zh-CN.md](docs/CURSOR_INTEGRATOR_QUICKSTART.zh-CN.md)
- Claude Code 接入方快速说明：[docs/CLAUDE_CODE_INTEGRATOR_QUICKSTART.zh-CN.md](docs/CLAUDE_CODE_INTEGRATOR_QUICKSTART.zh-CN.md)
- 交付状态说明：[docs/DELIVERY_READINESS.zh-CN.md](docs/DELIVERY_READINESS.zh-CN.md)
- AI 兼容性说明：[docs/AI_COMPATIBILITY.zh-CN.md](docs/AI_COMPATIBILITY.zh-CN.md)
- Provider 发版检查表：[docs/PROVIDER_RELEASE_CHECKLIST.zh-CN.md](docs/PROVIDER_RELEASE_CHECKLIST.zh-CN.md)
- GitHub Release 文案草稿：[docs/GITHUB_RELEASE_v0.2.1.zh-CN.md](docs/GITHUB_RELEASE_v0.2.1.zh-CN.md)
- v0.2.4 发布步骤：[docs/RELEASE_STEPS_v0.2.4.zh-CN.md](docs/RELEASE_STEPS_v0.2.4.zh-CN.md)
- 接入方信息收集模板：[docs/INTEGRATOR_INTAKE_TEMPLATE.zh-CN.md](docs/INTEGRATOR_INTAKE_TEMPLATE.zh-CN.md)
- 接入支持 FAQ：[docs/INTEGRATOR_FAQ.zh-CN.md](docs/INTEGRATOR_FAQ.zh-CN.md)
- GitHub Issue 模板：
  - `.github/ISSUE_TEMPLATE/integration-support-request.yml`
  - `.github/ISSUE_TEMPLATE/bug-report.yml`
- Skill 入口：[skill/usdk-android-integration/SKILL.md](skill/usdk-android-integration/SKILL.md)
- Cursor 适配模板目录：`adapters/cursor/`
- Claude Code 适配模板目录：`adapters/claude/`

## 核心命令

诊断目标工程：

```bash
python scripts/usdk_doctor.py --project-root <android_project_root> --pretty
```

生成分阶段修复计划：

```bash
python scripts/usdk_repair_runner.py --project-root <android_project_root> --format markdown
```

## 当前覆盖范围

当前版本聚焦 Android 静态工程接入：

- SDK 资源与配置文件检查
- Manifest 与 Gradle 接入检查
- `Application` 与 `SplashActivity` 接入
- 协议门禁与初始化流程
- 登录、角色上报、支付、踢下线、登出、退出
- Activity 生命周期转发

## 支持的 AI 环境

- 原生目标环境：
  - Codex / Skill 类环境
- 高优先级适配环境：
  - Cline
  - GitHub Copilot CLI
- 已提供仓库级适配资产的环境：
  - Cursor
  - Claude Code

详见：[docs/AI_COMPATIBILITY.zh-CN.md](docs/AI_COMPATIBILITY.zh-CN.md)

## AI 不会自动猜的内容

以下内容必须由接入人员或提供方明确确认：

- 协议模式：
  - `USDK protocol popup`
  - `Game-owned protocol popup`
- 退出逻辑提醒：
  - 是否渠道自带退出弹窗
  - 渠道不提供时，游戏是否需要本地退出确认框
  - 哪些入口需要走统一退出链路
- `RoleInfo` 的真实字段映射
- `OrderInfo` 的真实字段映射
- 支付回调与服务端关联参数

## 当前交付边界

当前版本适合：

- 提供方内部使用
- 集成支持团队使用
- 少量接入方试点

当前版本不适合：

- 无 Python 环境的自助交付
- 无提供方支持的公开放量交付
- 需要自动操作 Provider 后台的场景
