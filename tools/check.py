#!/usr/bin/env python3
"""Validate the catalog, runtime identity and self-contained product resources."""
from pathlib import Path
import hashlib
import json
import re
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]


def check(root=ROOT):
    errors = []
    catalog = json.loads((root / 'catalog/products.json').read_text())['products']
    runtime = json.loads((root / 'catalog/runtime-files.json').read_text())['files']
    products = {p['name']: p for p in catalog}
    if len(products) != len(catalog):
        errors.append('Duplicate catalog name')
    discovered = {str(p.parent.relative_to(root)) for group in ('skills', 'labs')
                  for p in (root / group).glob('*/SKILL.md')}
    if discovered != {p['path'] for p in catalog}:
        errors.append('Discovered products differ from catalog')
    recorded = set()
    for item in runtime:
        product = products.get(item['product'])
        path = root / item['path']
        if not product or not path.resolve().is_relative_to((root / product['path']).resolve()):
            errors.append('Invalid runtime path: ' + item['path'])
            continue
        if item['path'] in recorded:
            errors.append('Duplicate runtime entry: ' + item['path'])
        recorded.add(item['path'])
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != item['sha256']:
            errors.append('Runtime content differs: ' + item['path'])
    for product in catalog:
        base = root / product['path']
        for required in ('SKILL.md', 'README.md', 'LICENSE', 'REVIEW.md', 'SECURITY.md'):
            if not (base / required).is_file():
                errors.append(product['name'] + ': missing ' + required)
        skill = (base / 'SKILL.md').read_text()
        name = re.search(r'^name:\s*[\"\']?([^\n\"\']+)', skill, re.M)
        if not name or name.group(1).strip() != product['name']:
            errors.append('Skill name mismatch: ' + product['name'])
        if product['version']:
            version = re.search(r'^\s+version:\s*[\"\']?([0-9.]+)', skill, re.M)
            if not version or version.group(1) != product['version']:
                errors.append('Product version mismatch: ' + product['name'])
        for path in base.rglob('*'):
            if path.is_symlink():
                errors.append('Product symlink not supported: ' + str(path.relative_to(root)))
            if path.name == '__pycache__' or path.suffix == '.pyc':
                errors.append('Generated cache in source: ' + str(path.relative_to(root)))
            if not path.is_file() or path.suffix != '.md':
                continue
            text = path.read_text()
            targets = re.findall(r'\[[^\]]*\]\(([^\s)]+)', text)
            for target in targets:
                if re.match(r'^[a-z]+:', target, re.I) or target.startswith('#'):
                    continue
                dest = (path.parent / unquote(target.split('#')[0])).resolve()
                if not dest.is_relative_to(base.resolve()) or not dest.exists():
                    errors.append('Nonportable product link: ' + str(path.relative_to(root)) + ' -> ' + target)
            if str(path.relative_to(root)) in recorded:
                for target in re.findall(r'`((?:references|assets|templates|scripts|examples|evals|agents)/[^`\s]+)`', text):
                    if any(c in target for c in '*<|'):
                        continue
                    target = target.rstrip('.,;:')
                    if not (base / target).exists():
                        errors.append('Missing runtime resource: ' + product['name'] + ' -> ' + target)
    return errors, len(products), len(runtime)


if __name__ == '__main__':
    failures, products, files = check()
    print(json.dumps({'status': 'FAIL' if failures else 'PASS', 'products': products,
                      'runtime_files': files, 'errors': failures}, ensure_ascii=False, indent=2))
    sys.exit(bool(failures))
