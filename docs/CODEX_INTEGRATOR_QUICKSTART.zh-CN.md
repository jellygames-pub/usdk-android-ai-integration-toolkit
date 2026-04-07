# Codex 接入方快速说明

这份说明专门面向使用 Codex 的接入方。

## 使用方式

当前这套 toolkit 不是“给一个远程 Git 地址就自动生效”的模式。
正确用法是：

1. 将本仓库拉到本地
2. 将目标 Android 工程放在本地
3. 在 Codex 中使用本地 Skill、Spec、脚本和目标工程

## 推荐操作步骤

1. 克隆工具包仓库：

   ```bash
   git clone https://github.com/jellygames-pub/usdk-android-ai-integration-toolkit.git
   ```

2. 准备目标 Android 工程路径。

3. 在本地运行：

   ```bash
   python scripts/usdk_doctor.py --project-root <android_project_root> --pretty
   ```

4. 如有需要，再运行：

   ```bash
   python scripts/usdk_repair_runner.py --project-root <android_project_root> --format markdown
   ```

5. 在 Codex 中让 AI 读取这些文件：
   - `skill/usdk-android-integration/SKILL.md`
   - `spec/USDK_INTEGRATION_SPEC.yaml`
   - `spec/USDK_REPAIR_PLAYBOOK.yaml`
   - `doctor` 输出结果
   - `repair runner` 输出结果

6. 让 Codex 对目标工程执行修改。

7. 每次修改后重新运行 `doctor`，直到静态工程状态收敛。

## 需要明确告诉接入方的点

- 协议模式必须明确选择：
  - `USDK protocol popup`
  - `Game-owned protocol popup`
- `exit` 接口不是纯粹复制粘贴：
  - 必须结合渠道是否提供退出弹窗来处理
- `RoleInfo` 和 `OrderInfo` 必须替换成真实业务字段
- 支付结果必须继续结合服务端回调判断

## 当前交付边界

Codex 当前使用这套 toolkit 的前提是：

- 能访问本地文件
- 能执行本地命令
- 能修改目标工程文件
- 本地具备 `Python 3.x`

如果接入方不能满足这些条件，这套工具包当前不适合直接使用。
