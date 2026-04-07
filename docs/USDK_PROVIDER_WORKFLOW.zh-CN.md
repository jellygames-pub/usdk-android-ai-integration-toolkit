# USDK Provider 工作流

本仓库是提供方交付给 AI 和接入团队使用的 USDK Android 接入工具包。

## 目标

给接入方和 AI 工具提供一条统一路径：

1. 读取结构化规范
2. 使用 `doctor` 诊断当前工程
3. 按 Skill 工作流实施接入
4. 再次诊断
5. 将代码已完成项和人工项拆开输出

## 版本信息

- 当前版本：`0.2.0`
- 发布状态：提供方内部 Beta
- 顶层入口：[README.zh-CN.md](../README.zh-CN.md)
- 接入方入口：[INTEGRATOR_QUICKSTART.zh-CN.md](INTEGRATOR_QUICKSTART.zh-CN.md)
- 交付状态说明：[DELIVERY_READINESS.zh-CN.md](DELIVERY_READINESS.zh-CN.md)
- 脚本运行依赖：`Python 3.x`

## 角色分工

### 提供方

- 维护 Skill
- 维护结构化接入规范
- 维护诊断脚本与输出格式
- 负责版本管理和规则更新

### 接入方

- 在目标工程中运行 `doctor`
- 使用 Skill 或 AI 工作流做工程改动
- 提供真实参数
- 完成运行时联调与后台配置

### AI 工具

- 读取规范
- 修改前先跑 `doctor`
- 依据结果决定改哪些文件
- 修改后再跑 `doctor`
- 分开汇报“已完成项”和“人工阻塞项”

## 推荐流程

1. 获取本工具包仓库。
2. 指定目标 Android 工程路径。
3. 运行：

   ```bash
   python scripts/usdk_doctor.py --project-root <android_project_root> --pretty
   ```

4. 如有需要，再生成修复计划：

   ```bash
   python scripts/usdk_repair_runner.py --project-root <android_project_root> --format markdown
   ```

5. 将输出结果与 Skill、Spec、Playbook 一并提供给 AI。
6. 让 AI 完成所需改动。
7. 再次运行 `doctor` 对照结果。
8. 补齐剩余提供方和后台相关项。

## 仓库中的首批交付物

- `skill/usdk-android-integration/SKILL.md`
- `spec/USDK_INTEGRATION_SPEC.yaml`
- `spec/USDK_REPAIR_PLAYBOOK.yaml`
- `scripts/usdk_doctor.py`
- `scripts/usdk_repair_runner.py`
- `skill/usdk-android-integration/references/action_template.md`
- `skill/usdk-android-integration/references/template_index.md`
- `skill/usdk-android-integration/references/check_matrix.md`
- `skill/usdk-android-integration/references/manual_inputs.md`
- `docs/AI_COMPATIBILITY.zh-CN.md`
- `docs/DELIVERY_READINESS.zh-CN.md`
- `docs/PROVIDER_RELEASE_CHECKLIST.zh-CN.md`

## Template 层说明

当前仓库已经包含以下模板参考：

- `Application` 接入
- Splash 与协议接入
- 运行时登录、角色上报、支付、踢下线、登出、退出
- 生命周期转发
- AndroidX / legacy 的 Gradle 接入

这些模板不是为了机械粘贴，而是给 AI 做“最小适配”的参考。

## Fixture 验证

可以用内置 fixture 检查 doctor 行为：

```bash
python scripts/usdk_doctor.py --project-root fixtures/android-native-minimal --pretty
python scripts/usdk_doctor.py --project-root fixtures/android-partial-integration --pretty
```

当前预期：

- `android-native-minimal`
  - `summary.status = integration_partially_detected`
  - 缺失项应集中在新增的角色上报和 kick listener 检查上

- `android-partial-integration`
  - `summary.status = integration_partially_detected`
  - `prioritized_repairs` 应包含明确可执行的修复项
