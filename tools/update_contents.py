"""Refresh numbered GitHub/Obsidian contents pages from publication configs."""
import json, os
from pathlib import Path
from collections import defaultdict
from urllib.parse import quote

ROOT=Path(__file__).resolve().parents[1]
BOOKS={'hardware':('硬件操作手册','Hardware Manual'),'software':('软件操作手册','Software Manual'),'first-machining':('首次加工指南','First Machining Guide')}
LABEL={'zh':('中文','通用内容','选配件'),'en':('English','Shared Content','Accessories')}
def write(path,lines):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text('\n'.join(lines)+'\n',encoding='utf-8',newline='\n')
def entries(cfg):
    children=defaultdict(list)
    for i,n in enumerate(cfg['nodes']):children[n.get('parentId')].append((n.get('order',0),i,n))
    result=[]
    def visit(pid,prefix):
        for number,(_,_,node) in enumerate(sorted(children[pid]),1):
            numbers=prefix+[str(number)];result.append((node,'.'.join(numbers)));visit(node['id'],numbers)
    visit(None,[])
    if len(result)!=len(cfg['nodes']):raise ValueError('Invalid chapter hierarchy')
    return result
def toc(lang,key,cfg,path):
    lines=['# '+cfg['projectName'],'','点击章节名打开文档。章节编号和顺序来自手册目录配置；共用章节链接到同一份源文件。' if lang=='zh' else 'Open a chapter below. Order and numbering follow the publication configuration; shared chapters link to one source file.','']
    for node,number in entries(cfg):
        if not node.get('file'):continue
        source=(ROOT/node['file']).resolve()
        if not source.is_file() or not source.is_relative_to(ROOT):raise ValueError('Invalid chapter '+str(source))
        url=quote(os.path.relpath(source,path.parent).replace('\\','/'),safe='/.-')
        mark='（草稿）' if node.get('draft') and lang=='zh' else ' (Draft)' if node.get('draft') else ''
        title=node['title'].replace('[','(').replace(']',')')
        lines.append('  '*number.count('.')+'- ['+number+' '+title+mark+']('+url+')')
    home=quote(os.path.relpath(ROOT/'README.md',path.parent).replace('\\','/'),safe='/.-')
    lines+=['','[返回书库首页]('+home+')' if lang=='zh' else '[Library home]('+home+')']
    write(path,lines)
for lang in ('zh','en'):
    base,shared,access=LABEL[lang]
    for path in sorted((ROOT/'publications'/lang).glob('*.json')):
        key=path.stem;cfg=json.loads(path.read_text(encoding='utf-8'))
        output=ROOT/base/'完整目录.md' if key=='full' else ROOT/base/BOOKS[key][0 if lang=='zh' else 1]/'README.md'
        toc(lang,key,cfg,output)
    for folder in (shared,access):
        directory=ROOT/base/folder;lines=['# '+folder,'']
        for path in sorted(directory.rglob('*.md')):
            if path==directory/'README.md':continue
            url=quote(os.path.relpath(path,directory).replace('\\','/'),safe='/.-')
            label=path.parent.name if path.name=='README.md' else path.stem
            lines.append('- ['+label+']('+url+')')
        write(directory/'README.md',lines)
print('Updated six manual contents pages, two full-library contents pages and shared/accessory indexes.')
