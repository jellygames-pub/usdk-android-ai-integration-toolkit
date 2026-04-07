# 接入支持 FAQ

这份 FAQ 汇总了当前 toolkit 在真实试点和样例工程中已经确认过的典型问题。

## 1. 为什么导入 `HeroUSDK.aar` 之后，Gradle 报 `prefer settings repositories over project repositories`？

这是 Gradle 7+ 的仓库管理策略问题，不是 USDK 二进制本身有问题。

如果项目在 `settings.gradle` 中启用了类似：

- `RepositoriesMode.FAIL_ON_PROJECT_REPOS`
- `RepositoriesMode.PREFER_SETTINGS`

那么 `flatDir` 不能再写在 `app/build.gradle` 里，必须写到 `settings.gradle` 的 `dependencyResolutionManagement.repositories` 中。

## 2. 协议弹窗到底该怎么选？

只有两种模式，不允许混用：

- `USDK protocol popup`
  - 走 `setProtocolListener`
- `Game-owned protocol popup`
  - 游戏自己出协议弹窗
  - 用户同意后走 `setAgreeProtocol`

接入前必须先选模式，AI 不应替接入方猜。

## 3. 为什么协议和初始化不能放在 `SplashActivity`？

因为 `SplashActivity` 结束后会 `finish()`。

如果把协议判断、初始化、后续运行链路都放在这里，容易导致后续 SDK 逻辑和 Activity 生命周期脱节。当前推荐做法是：

- `SplashActivity` 只负责闪屏和跳转
- 协议判断、回调注册、`onCreate` 转发、`init` 等逻辑放在真正运行中的主 Activity 或接入包装层

## 4. 为什么回调必须先注册，再调接口？

因为某些接口在调用过程中就可能触发回调。

当前已确认：

- 相关回调必须先注册
- `HeroSdk.getInstance().onCreate(this)` 也应该放在回调注册之后

否则可能出现事件触发了，但监听器还没挂上的情况。

## 5. `exit` 接口为什么不能直接写死在退出按钮里？

因为退出逻辑取决于渠道是否提供自己的退出弹窗。

必须先检查：

- `HeroSdk.getInstance().isChannelHasExitDialog()`

处理方式：

- 如果渠道提供退出弹窗：
  - 游戏禁止再弹本地退出确认框
  - 直接调用 `exit(activity)`
- 如果渠道不提供退出弹窗：
  - 游戏必须先走自己的退出确认逻辑
  - 用户确认后再调用 `exit(activity)`

同时要确认：

- 退出按钮
- 返回键
- 其他离开游戏入口

是否复用同一条退出链路。

## 6. 为什么退出按钮里不能同时调 `logout()` 和 `exit()`？

因为这两个语义不同：

- `logout()` 是账号登出
- `exit()` 是退出游戏

它们不能强行绑定成同一个动作。

退出按钮应走 `exit()`。  
`logout()` 应该绑定到账号中心、切换账号或其他真实账号管理入口。

## 7. 为什么 `setKickListener` 必须接？

因为这是强制下线、被顶号、防沉迷踢下线等场景的关键回调入口。

如果不接：

- 游戏无法正确处理被踢下线后的跳转逻辑
- AI 也无法把接入链路视为完整

当前 toolkit 已把 `setKickListener` 视为必需工程项。

## 8. 为什么只接了 `enterGame` 还不够？

因为角色上报不只一个接口。

当前核心角色上报接口包括：

- `enterGame(Activity activity, RoleInfo roleInfo)`
- `createNewRole(Activity activity, RoleInfo roleInfo)`
- `roleLevelUp(Activity activity, RoleInfo roleInfo)`

它们必须分别绑定到真实业务事件：

- 进入游戏
- 创建角色
- 角色升级

禁止把这些接口硬塞到启动流程里。

## 9. `RoleInfo` 为什么不能只填几个最小字段？

因为真实联运和渠道侧经常依赖更完整的角色信息。

除了基础字段，还应回到真实项目确认：

- 帮派信息
- 职业信息
- 角色战力
- 创建时间
- 好友列表
- 累计付费
- 扩展字段

当前样例已经提供了更完整的字段骨架，但真实值必须由接入方替换。

## 10. `OrderInfo` 为什么不能只填 `goodsId` 和 `cpOrderId`？

因为支付链路真实依赖的远不止这两个字段。

需要确认的字段包括：

- 商品名
- 商品描述
- 金额
- 数量
- 单价
- 回调地址
- 服务端透传信息
- 货币类型
- 扩展参数

当前样例已经补了完整骨架，但真实值必须回到业务支付数据中映射。

## 11. 这个 toolkit 为什么要求本地装 Python？

因为当前版本的核心诊断和修复计划工具是：

- `scripts/usdk_doctor.py`
- `scripts/usdk_repair_runner.py`

如果没有 Python 3.x：

- 仍然可以阅读文档和 Skill
- 但无法运行本地诊断链路

当前版本适合内部 Beta，不适合无 Python 的公开自助交付。

## 12. 接入方使用 Codex 时，是直接给 Git 地址就能用吗？

不是。

当前正确方式是：

1. 将仓库 clone 到本地
2. 准备本地 Android 工程
3. 在本地运行 `doctor` / `repair_runner`
4. 在 Codex 中使用本地 Skill、Spec、脚本和目标工程

当前不应按“远程 Git URL 直接引用 skill 自动生效”的模式设计。
