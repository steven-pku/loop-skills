#!/usr/bin/env python3
"""Exercise migration validation with meaningful mutation controls in a temp copy."""
from pathlib import Path
import tempfile,shutil,json
from validate import ROOT,validate
with tempfile.TemporaryDirectory(prefix='loop-controls-') as temp:
 root=Path(temp)/'repo';shutil.copytree(ROOT,root,ignore=shutil.ignore_patterns('.git','__pycache__'));assert not validate(root)['errors']
 f=root/'README.md';f.write_text(f.read_text()+'\nDocumentation-only control.\n');assert not validate(root)['errors']
 f=root/'skills/loop-article-writer/SKILL.md';original=f.read_bytes();f.write_bytes(original+b'\nRuntime tamper control.\n');assert validate(root)['errors'];f.write_bytes(original)
 f=root/'skills/loop-article-writer/references/unexpected.md';f.write_text('Unexpected runtime resource.\n');assert validate(root)['errors'];f.unlink()
 f=root/'skills/loop-article-writer/LICENSE';original=f.read_bytes();f.unlink();assert validate(root)['errors'];f.write_bytes(original)
 f=root/'skills/loop-negotiation/REVIEW.md';original=f.read_bytes();f.write_bytes(original+b'\n[missing](evals/missing-evidence.md)\n');assert validate(root)['errors'];f.write_bytes(original)
 assert not validate(root)['errors']
print(json.dumps({'status':'PASS','controls':['root README change does not change runtime identity','changed runtime blocked','additional runtime blocked','missing license blocked','indirect historical document link blocked']}))
