# 交付就绪状态

这份文档说明当前版本已经能做什么、验证到什么程度、以及哪些能力还不在当前版本边界内。

## 当前发布状态

- 版本：`0.2.0`
- 状态：提供方内部 Beta
- 目标用途：内部验证与少量真实 Android 工程试点

## 当前已具备的能力

- Android 工程结构静态诊断
- Manifest / Gradle 接入缺项识别
- 核心 USDK 接口与生命周期检查
- 模板驱动的接入骨架生成
- 分阶段修复计划输出
- 协议模式显式选择提示
- `exit` 逻辑强提醒
- 角色上报骨架覆盖：
  - `enterGame`
  - `createNewRole`
  - `roleLevelUp`
- 核心回调骨架覆盖：
  - init
  - login
  - switch account
  - kick/offline
  - logout
  - exit
  - pay

## 当前已验证的内容

- Fixture 验证：
  - `fixtures/android-native-minimal`
  - `fixtures/android-partial-integration`
- 真实样例工程验证：
  - `D:\AndroidProjects\USDK_AI_Sample`

当前验证结果：

- Fixture：
  - `integration_partially_detected`
  - 新增角色上报与 kick listener 检查已生效
- 真实样例工程：
  - `blocked_on_manual_inputs`
  - 失败的必需项为 `0`

## 当前不在范围内

- 面向外部的免 Python 交付格式
- Provider 后台自动操作
- 支付回调后台自动开通
- 基于真实二进制的自动运行时冒烟验证
- 渠道级行为认证
- 核心接入链路之外的扩展模块自动化

## 当前运行要求

- 运行机器具备 `Python 3.x`
- 能访问目标 Android 工程
- 能获取官方 USDK 二进制包
- 能获取提供方参数：
  - `product_id`
  - `product_key`
  - `payment_callback_url`
  - `payment_callback_key`

## 当前交付建议

当前版本适合：

- 提供方内部交付
- 集成支持团队使用
- 少量试点接入方使用

当前版本不适合：

- 无支持团队参与的公开自助交付
- 无法运行本地脚本的环境
- 强依赖零本地运行时依赖的环境
