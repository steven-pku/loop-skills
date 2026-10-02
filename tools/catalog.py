#!/usr/bin/env python3
"""Regenerate public metadata from SKILL.md; provenance provides fixed identities."""
from pathlib import Path
import argparse,json,yaml
ROOT=Path(__file__).resolve().parents[1]
def render():
 products=[]
 for folder in sorted((ROOT/'skills').iterdir()):
  front=yaml.safe_load((folder/'SKILL.md').read_text().split('---',2)[1]);m=json.loads((ROOT/'provenance'/f'{folder.name}.json').read_text())
  products.append({'name':front['name'],'version':str(front['metadata']['version']),'description':front['description'],'path':'skills/'+folder.name,'packaging_revision':m['packaging_revision'],'runtime_manifest_sha256':m['runtime_manifest_sha256'],'source_repository':m['repository'],'source_commit':m['commit'],'source_tag':m['tag']})
 return json.dumps({'schema_version':1,'version_source':'SKILL.md metadata.version','skills':products},ensure_ascii=False,indent=2)+'\n'
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');args=p.parse_args();target=ROOT/'catalog/skills.json';text=render()
 if args.check:
  assert target.read_text()==text,'catalog drift; run tools/catalog.py';print('catalog PASS')
 else:target.write_text(text)
