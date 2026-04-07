# Provider 发版检查表

在把 toolkit 交给内部支持团队或试点接入方之前，先过一遍这份检查表。

## 版本管理

- 更新 [VERSION](../VERSION)
- 更新 [CHANGELOG.md](../CHANGELOG.md)
- 更新 [toolkit-manifest.json](../toolkit-manifest.json)

## 文档检查

- 确认 [README.md](../README.md) 与当前交付范围一致
- 确认 [README.zh-CN.md](../README.zh-CN.md) 与当前交付范围一致
- 确认 [INTEGRATOR_QUICKSTART.md](INTEGRATOR_QUICKSTART.md) 与当前操作流程一致
- 确认 [INTEGRATOR_QUICKSTART.zh-CN.md](INTEGRATOR_QUICKSTART.zh-CN.md) 与当前操作流程一致
- 确认 [USDK_PROVIDER_WORKFLOW.md](USDK_PROVIDER_WORKFLOW.md) 与当前版本一致
- 确认 [USDK_PROVIDER_WORKFLOW.zh-CN.md](USDK_PROVIDER_WORKFLOW.zh-CN.md) 与当前版本一致
- 确认 [AI_COMPATIBILITY.md](AI_COMPATIBILITY.md) 与当前支持边界一致
- 确认 [DELIVERY_READINESS.md](DELIVERY_READINESS.md) 与当前交付状态一致

## Skill 与 Spec 检查

- 确认 [skill/usdk-android-integration/SKILL.md](../skill/usdk-android-integration/SKILL.md) 与当前流程一致
- 确认 [spec/USDK_INTEGRATION_SPEC.yaml](../spec/USDK_INTEGRATION_SPEC.yaml) 与当前检查项一致
- 确认 [spec/USDK_REPAIR_PLAYBOOK.yaml](../spec/USDK_REPAIR_PLAYBOOK.yaml) 与 doctor 输出一致

## 脚本检查

- 运行：
  - `python -m py_compile scripts/usdk_doctor.py`
  - `python -m py_compile scripts/usdk_repair_runner.py`
- 确认 `doctor` 在 fixture 上仍能输出预期状态
- 确认 `repair_runner` 仍能生成阶段化计划

## Fixture 检查

- 验证 `fixtures/android-native-minimal`
- 验证 `fixtures/android-partial-integration`
- 确认 [toolkit-manifest.json](../toolkit-manifest.json) 里的预期状态与真实输出一致
- 如果 doctor 检查项有新增，必须同步更新 fixture 或预期状态说明

## 真实样例工程检查

- 确认真实样例工程试点结论仍然有效
- 确认样例工程已达到：
  - `blocked_on_manual_inputs`
  - `required_failed_count = 0`

## 关键能力检查

- 确认协议模式仍然是显式选择项
- 确认 `exit` 仍然是强提醒，而不是新的接入分支
- 确认角色上报仍覆盖：
  - `enterGame`
  - `createNewRole`
  - `roleLevelUp`
- 确认回调覆盖仍包含 `setKickListener`
- 确认 Gradle 7+ 的 `settings.gradle` 仓库说明仍然存在

## 是否允许发版

只有在以下条件同时成立时再发版：

- 文档和脚本一致
- 脚本和 Spec 一致
- Fixture 状态说明正确
- 当前交付边界写清楚
