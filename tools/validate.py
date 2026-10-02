#!/usr/bin/env python3
"""Validate the fixed content identity and self-contained runtime bundles."""
from pathlib import Path
import hashlib,json,re,sys
import yaml
ROOT=Path(__file__).resolve().parents[1]
def digest(b):return hashlib.sha256(b).hexdigest()
def validate(root=ROOT):
 catalog=json.loads((root/'catalog/skills.json').read_text());products=catalog['skills'];errors=[];checked=0
 expected={p['name'] for p in products};actual={str(p.parent.relative_to(root/'skills')) for p in (root/'skills').rglob('SKILL.md')}
 if actual!=expected:errors.append(f'discovery mismatch: {actual ^ expected}')
 for p in products:
  d=root/p['path'];m=json.loads((root/'provenance'/f'{p["name"]}.json').read_text());f=yaml.safe_load((d/'SKILL.md').read_text().split('---',2)[1])
  if f['name']!=d.name or str(f['metadata']['version'])!=p['version'] or f['description']!=p['description'] or len(f['description'])>300:errors.append(p['name']+': metadata mismatch')
  if not (d/'LICENSE').is_file():errors.append(p['name']+': missing license')
  if digest(json.dumps(m['runtime_files'],sort_keys=True,separators=(',',':')).encode())!=p['runtime_manifest_sha256']:errors.append(p['name']+': invalid runtime manifest')
  actual_runtime=[]
  for file in sorted(d.rglob('*')):
   rel=file.relative_to(d);top=rel.parts[0]
   if file.is_symlink():errors.append(str(file.relative_to(root))+': unexpected symlink')
   if file.is_file() and (str(rel)=='SKILL.md' or top in ['references','assets','scripts','agents','examples'] or (p['name']=='loop-article-writer' and str(rel).startswith('evals/cases/'))):
    actual_runtime.append({'path':str(rel),'sha256':digest(file.read_bytes()),'mode':oct(0o755 if file.stat().st_mode&0o111 else 0o644)})
  if actual_runtime!=m['runtime_files']:errors.append(p['name']+': changed or additional runtime file')
  for x in m['imported_files']:
   path=root/x['target_path'];checked+=1
   if not path.is_file():errors.append(str(path.relative_to(root))+': missing imported file');continue
   mode=0o755 if path.stat().st_mode&0o111 else 0o644
   if path.is_symlink() or digest(path.read_bytes())!=x['sha256'] or oct(mode)!=x['mode']:errors.append(str(path.relative_to(root))+': byte/type/mode drift')
  for x in m['runtime_files']:
   file=d/x['path']
   if file.suffix!='.md':continue
   text=file.read_text()
   links=re.findall(r'\[[^\]]*\]\(([^\s)]+)',text)
   inline=re.findall(r'`((?:\.\./)?(?:references|assets|scripts|examples|evals|agents)/[^`\s]+)`',text)
   for link in links+inline:
    if re.match(r'^[a-z]+:',link,re.I) or link.startswith('#') or '*' in link or '<' in link:continue
    target=link.split('#',1)[0].rstrip('.,;:')
    if not target:continue
    base=file.parent if target.startswith('../') or link in links else d
    resolved=(base/target).resolve()
    if not resolved.is_relative_to(d.resolve()) or not resolved.exists():errors.append(f'{p["name"]}/{x["path"]}: missing/escaping {link}')
  for file in d.rglob('*.md'):
   for link in re.findall(r'\[[^\]]*\]\(([^\s)]+)',file.read_text()):
    if re.match(r'^[a-z]+:',link,re.I) or link.startswith('#'):continue
    target=link.split('#',1)[0]
    if not target:continue
    resolved=(file.parent/target).resolve()
    if not resolved.is_relative_to(d.resolve()) or not resolved.exists():errors.append(f'{p["name"]}/{file.relative_to(d)}: bundled documentation link missing/escaping {link}')
  for x in m['asset_comparison']:
   if x.get('runtime_mismatches'):errors.append(p['name']+': source/asset mismatch')
 collections=json.loads((root/'catalog/collections.json').read_text())['collections']
 for name,members in collections.items():
  if len(members)!=len(set(members)) or set(members)-expected:errors.append(name+': invalid collection')
 for f in root.rglob('*'):
  if not f.is_file() or '.git' in f.parts:continue
  if f.suffix in ['.md','.txt','.json','.py','.yml','.yaml']:
   txt=f.read_text(errors='replace')
   # Fixtures may contain synthetic attacks; concrete credentials and home paths are forbidden.
   if re.search(r'/' + r'Users/[^/\s]+|(?:ghp_|github_pat_|sk-proj-)[A-Za-z0-9_\-]{20,}|-----BEGIN (?:RSA |OPENSSH )?PRIVATE KEY-----',txt):errors.append(str(f.relative_to(root))+': private path/credential pattern')
 result={'status':'PASS' if not errors else 'FAIL','products':len(products),'imported_files_checked':checked,'errors':sorted(set(errors)),'scope':'static content identity, name discovery, referenced runtime resource closure, license presence and bounded publication scan; no model behavior claim'}
 return result
if __name__=='__main__':
 result=validate();print(json.dumps(result,ensure_ascii=False,indent=2));sys.exit(bool(result['errors']))
