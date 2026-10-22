#!/usr/bin/env python3
"""Build deterministic, independent product ZIPs after integrity validation."""
import argparse
import hashlib
import json
from pathlib import Path
import zipfile
from check import ROOT, check


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    output = args.output.resolve()
    if output.is_relative_to(ROOT):
        parser.error('Choose an output directory outside the source checkout')
    failures, _, _ = check()
    if failures:
        raise SystemExit('\n'.join(failures))
    output.mkdir(parents=True, exist_ok=True)
    catalog = json.loads((ROOT / 'catalog/products.json').read_text())
    packages = []
    for product in catalog['products']:
        base = ROOT / product['path']
        label = product['version'] or 'experimental'
        name = f"{product['name']}-{label}-p{catalog['packaging_revision']}.zip"
        target = output / name
        with zipfile.ZipFile(target, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
            for path in sorted(base.rglob('*')):
                if not path.is_file():
                    continue
                entry = zipfile.ZipInfo(str(Path(product['name']) / path.relative_to(base)), (2026, 10, 22, 0, 0, 0))
                entry.compress_type = zipfile.ZIP_DEFLATED
                entry.create_system = 3
                entry.external_attr = (0o100755 if path.stat().st_mode & 0o111 else 0o100644) << 16
                archive.writestr(entry, path.read_bytes())
        packages.append({'product': product['name'], 'product_version': product['version'],
                         'status': product['status'], 'file': name,
                         'sha256': hashlib.sha256(target.read_bytes()).hexdigest()})
    manifest = {'packaging_revision': catalog['packaging_revision'],
                'publication_state': catalog['publication_state'], 'packages': packages}
    (output / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    (output / 'SHA256SUMS.txt').write_text(''.join(f"{p['sha256']}  {p['file']}\n" for p in packages))
    print(f'Built {len(packages)} independent packages in {output}')


if __name__ == '__main__':
    main()
