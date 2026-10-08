"""Refresh numbered GitHub/Obsidian contents pages from publication configs."""
import json, os
from pathlib import Path
from collections import defaultdict
from urllib.parse import quote

ROOT=Path(__file__).resolve().parents[2]
BOOKS={'hardware':('硬件','Hardware'),'software':('软件','Software'),'first-machining':('首次加工','First Machining')}
LABEL={'zh':('中文','共用章节','选配件'),'en':('English','Shared Content','Accessories')}
CATEGORIES={'zh':('硬件','软件','首次加工','工艺库','FAQ','维保'),'en':('Hardware','Software','First Machining','Process Library','FAQ','Maintenance')}
def write(path,lines):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text('\n'.join(lines)+'\n',encoding='utf-8',newline='\n')
def entries(cfg):
    children=defaultdict(list)
    for i,n in enumerate(cfg['nodes']):children[n.get('parentId')].append((n.get('order',0),i,n))
    result=[]
    def visit(pid,prefix):
        siblings=sorted(children[pid])
        start=0 if pid is None and siblings and siblings[0][2]['title'].strip().lower() in ('前言','preface') else 1
        for number,(_,_,node) in enumerate(siblings,start):
            label=f'{number:02}' if pid is None else str(number)
            numbers=prefix+[label];result.append((node,'.'.join(numbers)));visit(node['id'],numbers)
    visit(None,[])
    if len(result)!=len(cfg['nodes']):raise ValueError('Invalid chapter hierarchy')
    return result
def toc(lang,key,cfg,path):
    heading=cfg['projectName'] if key=='full' else BOOKS[key][0 if lang=='zh' else 1]
    lines=['# '+heading,'','Wiki 与用户手册共用下列源文档。点击章节名查看和编辑。' if lang=='zh' else 'Wiki and user manuals share the source documents below. Open a chapter to read or edit it.','']
    if key=='hardware':
        shared,access=LABEL[lang][1:]
        draft='待审核资料' if lang=='zh' else 'Review Drafts'
        for folder in (shared,access,draft):
            lines.append('- ['+folder+']('+quote(folder+'/README.md',safe='/.-')+')')
        lines+=['','## 用户手册章节' if lang=='zh' else '## User manual chapters','']
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
    for path in sorted((ROOT/'.maintenance'/'publications'/lang).glob('*.json')):
        key=path.stem;cfg=json.loads(path.read_text(encoding='utf-8'))
        output=ROOT/base/'完整目录.md' if key=='full' else ROOT/base/BOOKS[key][0 if lang=='zh' else 1]/'README.md'
        toc(lang,key,cfg,output)
    for folder in (shared,access):
        directory=ROOT/base/BOOKS['hardware'][0 if lang=='zh' else 1]/folder;lines=['# '+folder,'']
        for path in sorted(directory.rglob('*.md')):
            if path==directory/'README.md':continue
            url=quote(os.path.relpath(path,directory).replace('\\','/'),safe='/.-')
            label=path.parent.name if path.name=='README.md' else path.stem
            lines.append('- ['+label+']('+url+')')
        write(directory/'README.md',lines)
    draft=ROOT/base/BOOKS['hardware'][0 if lang=='zh' else 1]/('待审核资料' if lang=='zh' else 'Review Drafts')
    lines=['# '+draft.name,'','以下为迁移保留的补充稿和练习稿，未接入正式发布。审核后请合并到对应章节，避免重复维护。' if lang=='zh' else 'Supplementary and practice drafts retained during migration. These are excluded from publication; review and merge into the relevant chapter.','']
    for path in sorted(draft.rglob('*.md')):
        if path==draft/'README.md':continue
        lines.append('- ['+path.relative_to(draft).as_posix().replace('[','(').replace(']',')')+']('+quote(path.relative_to(draft).as_posix(),safe='/.-')+')')
    write(draft/'README.md',lines)
    lines=['# '+('中文资料' if lang=='zh' else 'English Documents'),'','Wiki 与用户手册共用一套正文。' if lang=='zh' else 'One set of source documents for the Wiki and user manuals.','']
    for name in CATEGORIES[lang]:
        target=name+'/README.md' if (ROOT/base/name/'README.md').is_file() else name+'/'
        lines.append('- ['+name+']('+quote(target,safe='/.-')+')')
    lines+=['','[完整目录](完整目录.md)' if lang=='zh' else '[Complete contents](完整目录.md)','', '[返回首页](../README.md)' if lang=='zh' else '[Library home](../README.md)']
    write(ROOT/base/'README.md',lines)
print('Updated bilingual category pages and publication contents; six categories per language.')
