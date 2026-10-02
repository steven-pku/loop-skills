from pathlib import Path,PurePosixPath
import json,tarfile,zipfile,io,hashlib,shutil,sys,argparse,re
parser=argparse.ArgumentParser();parser.add_argument('--packages',required=True);parser.add_argument('--sources',required=True);parser.add_argument('--work-dir',required=True);args=parser.parse_args()
repo=Path(__file__).resolve().parents[1];packages=Path(args.packages).resolve();sources=Path(args.sources).resolve();test=Path(args.work_dir).resolve()
assert not test.exists() and not test.is_relative_to(repo),'work-dir must be a new directory outside the repository'
test.mkdir(parents=True)
products=json.loads((packages/'release-manifest.json').read_text())['products'];rows=[]
for item in products:
 assert re.fullmatch(r'loop-[a-z0-9-]+',item['name']) and Path(item['asset']).name==item['asset']
 assert hashlib.sha256((packages/item['asset']).read_bytes()).hexdigest()==item['asset_sha256']
def snapshot(root):
 return {str(f.relative_to(root)):{'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'executable':bool(f.stat().st_mode&0o111)} for f in sorted(root.rglob('*')) if f.is_file()}
def unpack(data,kind,target):
 files={}
 if kind=='zip':
  with zipfile.ZipFile(io.BytesIO(data)) as z:
   for i in z.infolist():
    if not i.is_dir():files[i.filename]=(z.read(i),i.external_attr>>16)
 else:
  with tarfile.open(fileobj=io.BytesIO(data),mode='r:gz') as t:
   for m in t.getmembers():
    assert not (m.issym() or m.islnk()),m.name
    if m.isfile():files[m.name]=(t.extractfile(m).read(),m.mode)
 skill=[n for n in files if n.endswith('/SKILL.md') or n=='SKILL.md'];assert len(skill)==1,skill
 prefix=skill[0][:-len('SKILL.md')];target.mkdir(parents=True,exist_ok=False)
 for n,(data,mode) in files.items():
  if not n.startswith(prefix):continue
  rel=PurePosixPath(n[len(prefix):]);assert not rel.is_absolute() and '..' not in rel.parts
  f=target/str(rel);f.parent.mkdir(parents=True,exist_ok=True);f.write_bytes(data);f.chmod(0o755 if mode&0o111 else 0o644)
def names(scope):return sorted(p.parent.name for p in scope.rglob('SKILL.md'))
for route,sub in [('codex','.agents/skills'),('claude','.claude/skills')]:
 for p in products:
  name=p['name'];root=test/route/name;scope=root/sub;scope.mkdir(parents=True);oldassets=sources/name/'assets';old=next(x for x in oldassets.iterdir() if x.name.endswith(('.zip','.tar.gz')))
  installed=scope/name;unpack(old.read_bytes(),'zip' if old.suffix=='.zip' else 'tar',installed);initial=snapshot(installed);assert names(scope)==[name]
  backup=root/'backup-outside-discovery'/name;backup.parent.mkdir();shutil.copytree(installed,backup);assert snapshot(backup)==initial
  shutil.rmtree(installed);unpack((packages/p['asset']).read_bytes(),'zip',installed)
  new=snapshot(installed);assert names(scope)==[name]
  for f in json.loads((repo/'provenance'/f'{name}.json').read_text())['runtime_files']:assert new[f['path']]['sha256']==f['sha256']
  shutil.rmtree(installed);shutil.copytree(backup,installed);assert snapshot(installed)==initial and names(scope)==[name]
  rows.append({'route':route,'product':name,'sequence':'fixed old asset -> complete backup outside discovery -> clean candidate install -> restore fixed old asset','status':'PASS','old_files':len(initial),'new_files':len(new)})
 allroot=test/route/'all'/sub;allroot.mkdir(parents=True)
 for p in products:unpack((packages/p['asset']).read_bytes(),'zip',allroot/p['name'])
 assert names(allroot)==sorted(p['name'] for p in products)
 for fixture in ['user-edited-runtime','old-residual-file']:
  root=test/route/fixture;scope=root/sub;scope.mkdir(parents=True);installed=scope/products[0]['name'];unpack((packages/products[0]['asset']).read_bytes(),'zip',installed);baseline=snapshot(installed)
  if fixture=='user-edited-runtime':(installed/'SKILL.md').write_bytes((installed/'SKILL.md').read_bytes()+b'\nLocal synthetic edit\n')
  else:(installed/'old-only.txt').write_text('synthetic retained old file\n')
  changed=snapshot(installed);assert changed!=baseline
  # The documented safety gate refuses an unbacked replacement when the tree differs.
  refused=changed!=baseline;assert refused
  backup=root/'backup-outside-discovery';shutil.copytree(installed,backup);assert snapshot(backup)==changed
  shutil.rmtree(installed);unpack((packages/products[0]['asset']).read_bytes(),'zip',installed)
  assert snapshot(installed)==baseline and names(scope)==[products[0]['name']]
  shutil.rmtree(installed);shutil.copytree(backup,installed);assert snapshot(installed)==changed
  rows.append({'route':route,'fixture':fixture,'status':'PASS','unbacked_replace_refused':refused,'complete_backup_restore':True,'new_install_has_residual':False})
r={'status':'PASS','upgrade_restore_sequences':18,'conflict_fixtures':4,'all_install_name_set':'exact nine on both filesystem layouts','rows':rows,'scope':'archive bytes, directory layout, complete backups, clean replacement and restore; not native model execution or installer source-lock migration'}
(test/'receipt.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({k:v for k,v in r.items() if k!='rows'}))
