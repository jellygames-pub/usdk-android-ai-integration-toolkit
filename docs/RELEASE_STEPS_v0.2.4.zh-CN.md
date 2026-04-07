# v0.2.4 Tag / Release 发布步骤

这份文档用于指导 Provider 将当前仓库发布为 `v0.2.4`。

适用仓库：

- `https://github.com/jellygames-pub/usdk-android-ai-integration-toolkit`

当前目标版本：

- `v0.2.4`

## 一、发布前确认

在创建 tag 和 release 之前，先确认以下内容已经完成：

- `VERSION` 为 `0.2.4`
- `toolkit-manifest.json` 为 `0.2.4`
- `CHANGELOG.md` 已包含 `0.2.4`
- `main` 分支最新提交已经推送到 GitHub

当前可用于发布的提交版本：

- 版本：`0.2.4`
- 当前最新提交请以 GitHub `main` 分支页面为准

## 二、本地创建 tag

在仓库根目录执行：

```bash
git tag -a v0.2.4 -m "Release v0.2.4"
```

检查 tag：

```bash
git tag
```

推送 tag：

```bash
git push origin v0.2.4
```

## 三、GitHub 上创建 Release

进入仓库页面：

- `https://github.com/jellygames-pub/usdk-android-ai-integration-toolkit`

然后按下面步骤操作：

1. 点击 `Releases`
2. 点击 `Draft a new release`
3. 在 `Choose a tag` 中选择：
   - `v0.2.4`
4. Release title 填写：
   - `v0.2.4`
5. Release description 中粘贴：
   - `docs/GITHUB_RELEASE_v0.2.1.zh-CN.md` 的内容

## 四、建议的 Release 标题

```text
v0.2.4
```

## 五、建议的 Release 正文来源

直接使用这份文档中的现成草稿：

- [docs/GITHUB_RELEASE_v0.2.1.zh-CN.md](GITHUB_RELEASE_v0.2.1.zh-CN.md)

如果你希望更精确，也可以在正文最前面加一行：

```text
本次发布基于 v0.2.4，包含中文交付文档、接入支持 FAQ 与 GitHub Issue 模板。
```

## 六、发布后建议检查

发布完成后，建议快速检查：

- Release 页面是否能正常打开
- Tag `v0.2.4` 是否存在
- 仓库首页是否仍然指向正确的中英文文档入口
- Issue 模板是否正常生效
- 中文 FAQ、接入模板、Codex 快速说明链接是否可访问

## 七、可选补充动作

如果后续想让接入方下载更方便，可以额外做：

- 上传一个 release zip
- 在 release 正文中附上推荐阅读顺序：
  - `README.zh-CN.md`
  - `docs/CODEX_INTEGRATOR_QUICKSTART.zh-CN.md`
  - `docs/INTEGRATOR_FAQ.zh-CN.md`

## 八、当前建议

当前最稳的发布方式是：

1. 先打 `v0.2.4` tag
2. 再在 GitHub 上创建 release
3. release 正文直接使用仓库内现成中文草稿

这样最省事，也最不容易出现发布内容和仓库内容不一致的问题。
