# C500 团队文档书库

按手册目录浏览、编辑源文档。每个章节使用简短文件名；目录页提供章节编号和链接。大章节只显示一个文件夹，章节介绍保存在文件夹首页。

| 中文 | English |
| --- | --- |
| [硬件操作手册](中文/硬件操作手册/README.md) | [Hardware Manual](English/Hardware%20Manual/README.md) |
| [软件操作手册](中文/软件操作手册/README.md) | [Software Manual](English/Software%20Manual/README.md) |
| [首次加工指南](中文/首次加工指南/README.md) | [First Machining Guide](English/First%20Machining%20Guide/README.md) |
| [选配件](中文/选配件/README.md) | [Accessories](English/Accessories/README.md) |
| [通用内容](中文/通用内容/README.md) | [Shared Content](English/Shared%20Content/README.md) |
| [完整总库目录](中文/完整目录.md) | [Complete Library](English/完整目录.md) |

## 编辑与审核

在 Obsidian 打开整个 `c500-docs` 文件夹。通过目录页进入章节，在修改分支编辑、提交、上传，再创建 Pull Request 审核。审核通过后合并到 main。

共用正文由总库和手册配置共同引用。每本手册的前言、修订记录和专属说明放在自己的前言文件夹中，分别维护。选配件和总库其他内容也保留在团队书库。

目录页由章节配置生成。章节文件夹使用两位数字前缀，让左侧文件树按手册顺序排列。每个文件夹的 README 是该章节正文。调整章节顺序、增加章节后，要同步更新 publications 配置，并运行 python tools/update_contents.py 重新生成目录页。

supplemental 是独立配件及 Wiki 文档补充稿，尚未接入发布配置。docs 是最初练习 GitHub 的测试文件，不是正式书库。assets 保存正文图片。

## PDF 与 Wiki

使用同一个审核后的版本，先生成工作书库：

```powershell
python tools/prepare_publications.py
```

脚本检查章节和图片，生成八个工作书库，不执行正式发布。

- 中文 PDF：出版工作台打开 `_build/zh/hardware`、`_build/zh/software` 或 `_build/zh/first-machining`。
- 英文 PDF：选择 `_build/en` 下对应目录。继续使用已有模板及封面封底工具。
- Wiki：发布助手选择仓库中的 wiki 文件夹。脚本生成的本机联动配置已指向 `_build/zh/full`、`_build/en/full`。先检查发布预览，再发布勾选页面。

不要编辑 _build 中的副本；请在上方目录链接对应的源文档中修改。不要在 Wiki 助手点击“从出版工作台联动”将它换回旧书库。

发布人员记录本次源版本、Wiki 页面与最终 PDF。浏览器登录数据、缓存、Obsidian 设置和生成副本不会上传。
