"""Validate source chapters, local links, shared assets and Wiki bindings."""
import json
import re
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[2]
LINK = re.compile(r'!?\[[^\]\n]*\]\(([^\n]*?)\)')
HTML = re.compile(r'<img\b[^>]*src=["\x27]([^"\x27]+)["\x27]', re.I)
errors = []
chapters = 0
links = 0

for language in ('中文', 'English'):
    expected = {'硬件', '软件', '首次加工', '工艺库', 'FAQ', '维保'} if language == '中文' else {'Hardware', 'Software', 'First Machining', 'Process Library', 'FAQ', 'Maintenance'}
    actual = {p.name for p in (ROOT/language).iterdir() if p.is_dir()}
    if actual != expected:
        errors.append(f'{language}: unexpected categories {actual ^ expected}')

for path in ROOT.rglob('*.md'):
    rel = path.relative_to(ROOT)
    if any(x in rel.parts for x in ('.git', '_build', '.obsidian', '__pycache__')):
        continue
    text = path.read_text(encoding='utf-8-sig')
    for ref in LINK.findall(text) + HTML.findall(text):
        ref = ref.strip().strip('<>')
        if re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:|#|//', ref):
            continue
        target = (path.parent/unquote(ref.partition('#')[0])).resolve()
        links += 1
        if not target.is_relative_to(ROOT) or not target.exists():
            errors.append(f'{rel}: missing or external local link {ref}')

for lang in ('zh', 'en'):
    for path in (ROOT/'.maintenance'/'publications'/lang).glob('*.json'):
        cfg = json.loads(path.read_text(encoding='utf-8'))
        ids = [n['id'] for n in cfg['nodes']]
        if len(ids) != len(set(ids)):
            errors.append(f'{path.name}: duplicate node IDs')
        for node in cfg['nodes']:
            if node.get('parentId') and node['parentId'] not in ids:
                errors.append(f'{path.name}: unknown parent {node["parentId"]}')
            if node.get('file'):
                chapters += 1
                source = (ROOT/node['file']).resolve()
                if not source.is_relative_to(ROOT) or not source.is_file():
                    errors.append(f'{path}: missing source {node["file"]}')

wiki = json.loads((ROOT/'.maintenance/wiki/wiki-map.json').read_text(encoding='utf-8'))
for page in wiki['pages']:
    for lang in ('zh', 'en'):
        item = page.get(lang, {})
        if item.get('file'):
            source = (ROOT/'.maintenance'/'wiki'/item['file']).resolve()
            if not source.is_relative_to(ROOT) or not source.is_file():
                errors.append(f'Wiki {page["id"]}: missing or external source')
        if item.get('workbenchNodeId'):
            cfg = json.loads((ROOT/'.maintenance'/'publications'/lang/'full.json').read_text(encoding='utf-8'))
            if item['workbenchNodeId'] not in {n['id'] for n in cfg['nodes']}:
                errors.append(f'Wiki {page["id"]}: unknown node')

for path in ROOT.rglob('*'):
    if path.is_file() and path.suffix.lower() in {'.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp'}:
        rel = path.relative_to(ROOT)
        if not any(x in rel.parts for x in ('.git', '_build', '.obsidian')) and rel.parts[0] != 'assets':
            errors.append(f'Image outside assets: {rel}')

if errors:
    print('\n'.join(errors))
    raise SystemExit(1)
print(f'PASS: six categories per language, {chapters} chapter references, {links} local links, images and Wiki bindings.')
