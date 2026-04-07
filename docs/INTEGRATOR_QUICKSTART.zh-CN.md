# 接入方快速开始

这份说明面向接入方研发或使用 AI 工具执行接入的操作者。

## 你需要准备的内容

- 目标 Android 工程根目录
- 官方 USDK 二进制包
- 运行脚本的机器具备 `Python 3.x`
- 提供方给出的真实参数：
  - `product_id`
  - `product_key`
  - `sdk_variant`
  - `protocol_popup_mode`
  - `payment_callback_url`
  - `payment_callback_key`

## AI 不会自动猜的内容

- 协议模式：
  - `USDK protocol popup`
  - `Game-owned protocol popup`
- 退出逻辑：
  - AI 会强提醒，但不会替你决定最终产品逻辑
- `RoleInfo` 字段映射：
  - AI 只能生成骨架，不能替你确认真实字段来源
- `OrderInfo` 字段映射：
  - AI 只能生成骨架，不能替你确认真实支付字段

## 推荐使用流程

1. 获取本工具包仓库的本地副本。
2. 运行诊断脚本：

   ```bash
   python scripts/usdk_doctor.py --project-root <android_project_root> --pretty
   ```

3. 如果缺项较多，再生成修复计划：

   ```bash
   python scripts/usdk_repair_runner.py --project-root <android_project_root> --format markdown
   ```

4. 在 AI 工具中加载这些内容：
   - `skill/usdk-android-integration/SKILL.md`
   - `spec/USDK_INTEGRATION_SPEC.yaml`
   - `spec/USDK_REPAIR_PLAYBOOK.yaml`

5. 让 AI 按阶段修改工程。
6. 每次修改后重新运行 `doctor`。
7. 当结果达到 `blocked_on_manual_inputs` 或更好时，停止静态改动并进入联调阶段。

## Gradle 仓库说明

- 对于 Gradle 7+ 且使用 `settings.gradle` 管理仓库的项目：
  - `flatDir` 必须配置在 `settings.gradle`
- 对于允许 module 级仓库的旧项目：
  - `flatDir` 仍可配置在 `app/build.gradle`

## 目标状态

目标工程应达到：

- 没有失败的必需静态检查项
- 剩余项明确收敛到参数、后台配置和运行时联调

## 结果状态解释

- `blocked_on_project_shape`
  - 工具包指向了错误目录，或项目结构不受支持

- `integration_partially_detected`
  - 已开始接入，但关键工程项仍缺失

- `blocked_on_manual_inputs`
  - 静态工程接入基本完成，剩余是参数、后台和联调工作

- `integration_verified_static`
  - 所有可静态检测项均通过，且没有额外声明的人工阻塞项
