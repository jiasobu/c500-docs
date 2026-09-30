"""Generate local workspaces from the single versioned library. Python 3 standard library only."""
import json, re, os, hashlib
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
image=re.compile(r'(!\[[^\]]*\]\()([^\n]+?)(\))')
html=re.compile(r'(<img\b[^>]*src=["\x27])([^"\x27]+)(["\x27])',re.I)

def text(p): return p.read_text(encoding='utf-8-sig')
def write(p,t):
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(t,encoding='utf-8',newline='\n')
def convert(source,target):
    def repl(m):
        ref=m.group(2).strip().strip('<>')
        if re.match(r'https?://|data:|#',ref): return m.group(0)
        p=(source.parent/ref).resolve()
        if not p.is_file(): raise ValueError('Missing image: '+str(p))
        if not p.is_relative_to(ROOT): raise ValueError('Image outside library: '+str(p))
        return m.group(1)+os.path.relpath(p,target.parent).replace('\\','/')+m.group(3)
    return html.sub(repl,image.sub(repl,text(source)))

count=0; records=[]; folders={}
for lang in ('zh','en'):
    sources=[(p.stem,p) for p in sorted((ROOT/'publications'/lang).glob('*.json'))]
    for name,config_path in sources:
        cfg=json.loads(text(config_path)); target=ROOT/'_build'/lang/name
        folders[(lang,name)]=str(target)
        for node in cfg['nodes']:
            if not node.get('file'): continue
            source=(ROOT/node['file']).resolve()
            if not source.is_file(): raise ValueError('Missing chapter: '+str(source))
            if not source.is_relative_to(ROOT): raise ValueError('Chapter outside library')
            source_file=node['file']
            generated_file='content/'+node['id']+'.md'
            dest=target/generated_file
            write(dest,convert(source,dest))
            records.append({'workspace':lang+'/'+name,'node':node['id'],'file':source_file,'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest()})
            node['file']=generated_file
            count+=1
        cfg['sourceFile']=str(ROOT)
        write(target/'.publication-order.json',json.dumps(cfg,ensure_ascii=False,indent=2)+'\n')
wiki=json.loads(text(ROOT/'wiki'/'wiki-map.json'))
for page in wiki['pages']:
    for lang in ('zh','en'):
        item=page.get(lang,{})
        if item.get('workbenchNodeId'):
            cfg=json.loads(text(ROOT/'publications'/lang/'full.json'))
            if item['workbenchNodeId'] not in {n['id'] for n in cfg['nodes']}:
                raise ValueError('Unknown Wiki node: '+item['workbenchNodeId'])
write(ROOT/'wiki'/'workbench-link.json',json.dumps({lang:folders[(lang,'full')] for lang in ('zh','en')},ensure_ascii=False,indent=2))
write(ROOT/'_build'/'verification.json',json.dumps({'resolved_chapters':count,'workspaces':len(folders),'records':records},ensure_ascii=False,indent=2))
print('PASS: '+str(count)+' chapter references, '+str(len(folders))+' workspaces; images and Wiki node bindings verified.')
for (lang,name),folder in folders.items(): print(lang+'/'+name+': '+folder)
