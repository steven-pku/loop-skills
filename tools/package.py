#!/usr/bin/env python3
"""Create deterministic per-product ZIPs; output stays outside the repository."""
from pathlib import Path
import argparse,hashlib,json,zipfile,subprocess
from validate import ROOT,validate
p=argparse.ArgumentParser();p.add_argument('--output',required=True);p.add_argument('--allow-dirty',action='store_true');args=p.parse_args();out=Path(args.output).resolve()
assert not out.is_relative_to(ROOT),'output must be outside discovery tree';out.mkdir(parents=True,exist_ok=True)
r=validate();assert not r['errors'],r
commit=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()
dirty=bool(subprocess.check_output(['git','status','--porcelain'],cwd=ROOT,text=True).strip())
assert not dirty or args.allow_dirty,'freeze a clean commit before packaging, or explicitly use --allow-dirty for preparation only'
records=[]
for item in json.loads((ROOT/'catalog/skills.json').read_text())['skills']:
 name=item['name'];folder=ROOT/item['path'];asset=out/f'{name}-v{item["version"]}-p{item["packaging_revision"]}.zip'
 with zipfile.ZipFile(asset,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
  for f in sorted(folder.rglob('*')):
   if f.is_file():
    info=zipfile.ZipInfo(str(Path(name)/f.relative_to(folder)),(2026,10,2,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;info.create_system=3
    mode=0o755 if f.stat().st_mode&0o111 else 0o644;info.external_attr=(0o100000|mode)<<16;z.writestr(info,f.read_bytes())
 records.append({**item,'asset':asset.name,'asset_sha256':hashlib.sha256(asset.read_bytes()).hexdigest()})
(out/'release-manifest.json').write_text(json.dumps({'schema_version':1,'monorepo_commit':commit,'source_tree_status':'uncommitted preparation' if dirty else 'clean fixed commit','products':records,'packaging':'self-contained per-product; no siblings required'},ensure_ascii=False,indent=2)+'\n')
(out/'SHA256SUMS.txt').write_text(''.join(x['asset_sha256']+'  '+x['asset']+'\n' for x in records))
print(json.dumps({'packages':len(records),'output':str(out)},indent=2))
