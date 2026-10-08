# 发布维护

日常正文在根目录的中文和 English 中修改，图片在 assets 中维护。

- publications：中英文手册和完整书库的章节配置。
- tools：目录生成、链接检查和工作书库生成脚本。
- wiki：Wiki 页面映射及待接入的空白页面。

从仓库根目录运行：

```powershell
python .maintenance/tools/update_contents.py
python .maintenance/tools/validate_library.py
python .maintenance/tools/prepare_publications.py
```

Wiki 发布助手选择本目录下的 wiki 文件夹。以上命令只生成本机工作副本，不执行线上发布。
