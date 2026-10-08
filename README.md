# C500 文档库

Wiki 和用户手册共用一套源文档。按语言和分类查找，内容只维护一次。

| 中文 | English |
| --- | --- |
| [硬件](中文/硬件/README.md) | [Hardware](English/Hardware/README.md) |
| [软件](中文/软件/README.md) | [Software](English/Software/README.md) |
| [首次加工](中文/首次加工/README.md) | [First Machining](English/First%20Machining/README.md) |
| [工艺库](中文/工艺库/) | [Process Library](English/Process%20Library/) |
| [FAQ](中文/FAQ/) | [FAQ](English/FAQ/) |
| [维保](中文/维保/) | [Maintenance](English/Maintenance/) |

维保包含故障排除、维护指南和零件更换。工艺库、FAQ 和维保目前只建立目录，暂不填正文。

## 修改资料

进入对应章节修改，在 GitHub Desktop 或网页端提交修改分支，再创建 Pull Request 审核。审核通过后合并，由发布人员更新 Wiki 和生成用户手册。

图片统一保存在 [assets](assets/) 中。硬件下的“待审核资料 / Review Drafts”保留补充稿和练习稿，审核后合入对应正式章节。

## 发布维护

发布配置和工具统一收在 `.maintenance` 中：`publications` 保存手册章节配置，`tools` 保存生成和检查脚本，`wiki` 保存发布映射。它们不存放另一套正式正文。

调整章节后运行：

```powershell
python .maintenance/tools/update_contents.py
python .maintenance/tools/validate_library.py
python .maintenance/tools/prepare_publications.py
```

生成的 `_build` 是本机工作副本，不要在其中修改正文。PDF 继续使用 `_build/zh` 或 `_build/en` 下对应的手册目录及现有模板。

Wiki 发布助手选择 `.maintenance/wiki` 文件夹；工作书库指向 `_build/zh/full` 和 `_build/en/full`。先检查预览再发布，不要切回旧书库。空白页面暂存于 `.maintenance/wiki/pending-pages.json`，补充真实正文后再接入发布配置。

现有 Wiki 页面地址保持不变，本次整理不直接发布或调整线上导航。
