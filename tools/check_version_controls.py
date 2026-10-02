from pathlib import Path
import subprocess,tempfile,json
script=Path(__file__).resolve().with_name('check_versions.py')
with tempfile.TemporaryDirectory(prefix='loop-version-controls-') as temp:
 root=Path(temp);(root/'catalog').mkdir();(root/'skills/loop-topic-picker').mkdir(parents=True)
 c={'skills':[{'name':'loop-topic-picker','path':'skills/loop-topic-picker','version':'0.4.1','packaging_revision':1}]};cat=root/'catalog/skills.json';cat.write_text(json.dumps(c));skill=root/'skills/loop-topic-picker/SKILL.md';skill.write_text('Original runtime.\n');(root/'README.md').write_text('Docs.\n')
 def git(*args):return subprocess.run(['git',*args],cwd=root,capture_output=True,text=True,check=True).stdout.strip()
 git('init','-q');git('add','.');git('-c','user.name=Fixture','-c','user.email=fixture@example.invalid','commit','-qm','fixture baseline');base=git('rev-parse','HEAD')
 def check(expected):
  r=subprocess.run(['python3',str(script),'--repo',str(root),'--base',base],capture_output=True,text=True);assert (r.returncode==0)==expected,r.stdout+r.stderr
 check(True);(root/'README.md').write_text('Changed root documentation.\n');check(True)
 skill.write_text('Changed runtime.\n');check(False);c['skills'][0]['version']='0.4.2';cat.write_text(json.dumps(c));check(True)
 skill.write_text('Original runtime.\n');c['skills'][0]['version']='0.4.1';cat.write_text(json.dumps(c));(root/'skills/loop-topic-picker/README.md').write_text('Package documentation.\n');check(False);c['skills'][0]['packaging_revision']=2;cat.write_text(json.dumps(c));check(True)
print('version controls PASS: root docs, runtime version and packaging revision')
