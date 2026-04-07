# 接入方信息收集模板

这份模板用于接入方在正式接入前向 Provider 或支持团队提供必要信息。

## 基本信息

- 项目名称：
- 包名：
- 工程类型：
  - 原生 Android
  - Unity 导出 Android 工程
  - 其他
- 当前 Gradle 版本：
- 当前使用的依赖体系：
  - AndroidX
  - Legacy support

## 目标工程信息

- Android 工程根目录：
- `Application` 类名称：
- 启动页 / SplashActivity 名称：
- 主游戏 Activity 名称：
- 当前是否已有自定义登录流程：
  - 是
  - 否

## 协议模式确认

请二选一：

- `USDK protocol popup`
- `Game-owned protocol popup`

如果选择 `Game-owned protocol popup`，请补充：

- 游戏协议弹窗所在页面或逻辑入口：
- 用户同意后准备调用的接入点：

## 退出逻辑确认

请确认以下内容：

- 是否需要根据 `isChannelHasExitDialog()` 做差异化退出逻辑：
  - 是
  - 否
- 如果渠道不提供退出弹窗，游戏是否需要本地退出确认框：
  - 是
  - 否
- 哪些入口需要走统一退出链路：
  - 退出按钮
  - 返回键
  - 其他：

## 角色上报信息

请确认以下真实字段来源：

- `roleId`
- `roleName`
- `serverId`
- `serverName`
- `roleLevel`
- `vipLevel`
- `roleCreateTime`
- `professionId`
- `profession`
- `partyId`
- `partyName`
- `rolePower`
- 其他扩展字段：

并确认以下事件接入点：

- `enterGame` 触发点：
- `createNewRole` 触发点：
- `roleLevelUp` 触发点：

## 支付信息

请确认以下字段来源：

- `goodsId`
- `goodsName`
- `goodsDesc`
- `cpOrderId`
- `amount`
- `count`
- `price`
- `callbackUrl`
- `serverMessage`
- `extraParams`
- `currency`
- 其他扩展字段：

## 回调与账号相关逻辑

请确认以下流程接入位置：

- 登录成功后流程：
- 切换账号后流程：
- 踢下线后流程：
- 登出后流程：
- 退出游戏后流程：

## Provider 参数

由 Provider 补充或确认：

- `product_id`
- `product_key`
- `payment_callback_url`
- `payment_callback_key`
- `sdk_variant`

## 备注

- 是否需要支持团队远程协助：
- 是否已有联调时间安排：
- 其他特殊说明：
