# USDK Android AI Integration Toolkit v0.2.1

## 版本说明

`v0.2.1` 是在 `v0.2.0` 基础上的交付说明增强版本，重点补齐中文交付文档，方便提供方内部团队和中文接入方直接使用。

## 本版本新增内容

- 新增中文总览说明：
  - `README.zh-CN.md`
- 新增中文接入方快速开始：
  - `docs/INTEGRATOR_QUICKSTART.zh-CN.md`
- 新增中文 Codex 接入说明：
  - `docs/CODEX_INTEGRATOR_QUICKSTART.zh-CN.md`
- 新增中文 Provider 工作流说明：
  - `docs/USDK_PROVIDER_WORKFLOW.zh-CN.md`
- 新增中文交付状态说明：
  - `docs/DELIVERY_READINESS.zh-CN.md`
- 新增中文 AI 兼容性说明：
  - `docs/AI_COMPATIBILITY.zh-CN.md`
- 新增中文 Provider 发版检查表：
  - `docs/PROVIDER_RELEASE_CHECKLIST.zh-CN.md`

## 当前能力范围

当前版本支持：

- Android 工程结构静态诊断
- Manifest / Gradle 接入检查
- Application / SplashActivity 接入骨架
- 协议模式显式选择提示
- 登录、角色上报、支付、踢下线、登出、退出相关骨架
- Activity 生命周期转发检查
- 角色上报接口覆盖：
  - `enterGame`
  - `createNewRole`
  - `roleLevelUp`
- 支付字段骨架与角色字段骨架

## 当前交付状态

当前版本适合：

- 提供方内部使用
- 集成支持团队使用
- 少量试点接入方

当前版本不适合：

- 无 Python 环境的公开自助交付
- 无 Provider 支持的公开放量交付
- 自动操作 Provider 后台或自动完成联调

## 接入方使用方式

对于使用 Codex 的接入方：

1. 克隆本仓库到本地
2. 准备本地 Android 工程
3. 运行：

```bash
python scripts/usdk_doctor.py --project-root <android_project_root> --pretty
```

4. 如有需要，再运行：

```bash
python scripts/usdk_repair_runner.py --project-root <android_project_root> --format markdown
```

5. 在 Codex 中结合以下文件执行接入：
   - `skill/usdk-android-integration/SKILL.md`
   - `spec/USDK_INTEGRATION_SPEC.yaml`
   - `spec/USDK_REPAIR_PLAYBOOK.yaml`

## 特别说明

- 协议模式必须由接入人员明确选择：
  - `USDK protocol popup`
  - `Game-owned protocol popup`
- `exit` 逻辑不是新的接入分支，但 AI 必须明确提醒接入人员：
  - 是否渠道自带退出弹窗
  - 是否需要游戏本地退出确认框
  - 哪些入口要走统一退出链路
- `RoleInfo` 和 `OrderInfo` 只能提供骨架，真实字段必须由接入方映射

## 仓库地址

- https://github.com/jellygames-pub/usdk-android-ai-integration-toolkit
