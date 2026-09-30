# C500 团队文档书库

这里保存用户手册和现有 Wiki 的源文档。团队修改正文后通过修改申请审核，审核通过的同一版本用于生成 PDF 和发布 Wiki。

## 在哪里编辑

- `library/zh`：中文总书库，包括未被三本手册选中的选配件等章节。
- `library/en`：英文总书库。
- `library/zh/book-specific`、`library/en/book-specific`：硬件、软件、首次加工指南各自的手册说明。
- `supplemental`：从独立配件与 Wiki 文档目录收集的补充稿，尚未接入总库的发布配置；有同主题内容时应先评审，避免把草稿当成已发布版本。
- `publications`：三本手册的中英文章节配置。这里选择章节，不再存放六份重复正文。
- `wiki/wiki-map.json`：现有 Wiki 页面的映射，保留原页面 ID 和路径。
- `assets`：正文图片。保留原文件名称并添加内容标识，避免重名覆盖。
- `docs`：最初练习 GitHub 流程的测试章节，仅供练习，不是正式书库。

推荐在 Obsidian 打开整个仓库目录，编辑 `library` 下的源文件。不要编辑生成目录 `_build`，其中的工作书库会被重新生成。

## 修改和审核

1. 同步最新 main，创建本次修改分支。
2. 修改正文或图片，检查预览，提交并上传。
3. 创建 Pull Request，注明改动及是否影响 PDF、Wiki。
4. 审核通过后合并；发布人员同步该确认版本。

## 准备 PDF 和 Wiki

电脑需要 Python 3。在仓库目录运行：

```powershell
python tools/prepare_publications.py
```

脚本检查图片和章节引用，然后生成八个工作书库：中英文总库，以及硬件、软件、首次加工指南各自的中英文版。

PDF：在现有出版工作台中打开 `_build/zh/hardware`、`_build/zh/software` 或 `_build/zh/first-machining`；英文选择 `_build/en` 中对应目录。使用现有模板和封面封底工具输出成品。章节结构来自原有三本手册配置。

Wiki：在现有发布助手中选择本仓库的 `wiki` 项目目录。脚本已生成本机 `workbench-link.json`，指向 `_build/zh/full` 和 `_build/en/full`。先检查生成预览，再发布勾选页面。不要点击“从出版工作台联动”把它换回其他旧书库。

生成脚本不会发布 Wiki，也不会生成 PDF。正式发布前检查正文、表格、图片和目录；记录源版本、Wiki 更新页面和 PDF 成品。

## 一致性

共用章节只在总库维护一份，所有手册生成时读取同一源文件。每本专属的“关于本手册”分别保存，图号和章节层级沿用迁移后的配置与源文档。此次迁移使用三本手册当前稿统一总库；旧稿已在本地备份。

现有程序的本机配置、浏览器登录数据、缓存、PDF 成品和 Obsidian 设置不进入源仓库。最终 PDF 可作为 GitHub Release 附件保存。
