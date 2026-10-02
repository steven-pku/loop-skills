#!/usr/bin/env python3
"""Reject runtime changes that keep a product version, against a Git base."""
import argparse,json,subprocess,re,sys
from pathlib import Path
from validate import ROOT
p=argparse.ArgumentParser();p.add_argument('--base',required=True);p.add_argument('--repo',type=Path,default=ROOT);a=p.parse_args();ROOT=a.repo.resolve()
def git(*args):return subprocess.run(['git',*args],cwd=ROOT,text=True,capture_output=True)
def semver(v):
 assert re.fullmatch(r'\d+\.\d+\.\d+',v),v
 return tuple(map(int,v.split('.')))
assert git('cat-file','-e',a.base+'^{commit}').returncode==0,'base must resolve to a commit'
old=git('show',a.base+':catalog/skills.json')
if old.returncode:
 assert not git('ls-tree','--name-only',a.base,'skills').stdout.strip(),'missing catalog in an existing skills tree'
 print('Initial catalog import: validate provenance and fixed source; no prior monorepo version to compare.');sys.exit(0)
previous={x['name']:x for x in json.loads(old.stdout)['skills']};current=json.loads((ROOT/'catalog/skills.json').read_text())['skills'];errors=[]
for x in current:
 if x['name'] not in previous:continue
 prior=previous[x['name']];diff=sorted(set(git('diff','--name-only',a.base,'--',x['path']).stdout.splitlines()+git('ls-files','--others','--exclude-standard','--',x['path']).stdout.splitlines()))
 runtime=[]
 for f in diff:
  rel=f[len(x['path'])+1:];top=rel.split('/')[0]
  if rel=='SKILL.md' or top in ['references','assets','scripts','agents','examples'] or (x['name']=='loop-article-writer' and rel.startswith('evals/cases/')):runtime.append(f)
 if runtime and semver(x['version'])<=semver(prior['version']):errors.append(x['name']+': runtime change requires version increase')
 if diff and not runtime and x['packaging_revision']<=prior['packaging_revision']:errors.append(x['name']+': changed bundle documentation/license requires packaging revision increase')
print(json.dumps({'status':'FAIL' if errors else 'PASS','errors':errors},indent=2));sys.exit(bool(errors))
