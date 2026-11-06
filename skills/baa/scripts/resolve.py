#!/usr/bin/env python3
"""Resolve BAA internal procedures; public entrypoints share a scoped internal catalog."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_skill(path, root):
    folder = (root / path).resolve()
    if not folder.is_relative_to(root):
        raise ValueError('skill path must remain inside the BAA package')
    document = folder / 'PROCEDURE.md'
    text = document.read_text()
    if not text.startswith('---\n'):
        raise ValueError(f'invalid skill frontmatter: {document}')
    names = [line.removeprefix('name:').strip() for line in text.split('---', 2)[1].splitlines() if line.startswith('name:')]
    if len(names) != 1 or not names[0].startswith('baa-'):
        raise ValueError(f'invalid internal BAA skill name: {document}')
    return {'name': names[0], 'path': str(document)}


def allowed_platforms(catalog, entrypoint):
    if entrypoint is None:
        return catalog['platforms']
    if entrypoint not in catalog.get('entrypoints', {}):
        raise ValueError(f'unknown entrypoint: {entrypoint}')
    return catalog['entrypoints'][entrypoint]


def resolve(platform, step, root=ROOT, entrypoint=None):
    root = Path(root).resolve()
    catalog = json.loads((root / 'routing.json').read_text())
    if platform not in catalog['platforms']:
        raise ValueError(f'unsupported platform: {platform}')
    if platform not in allowed_platforms(catalog, entrypoint):
        raise ValueError(f'platform {platform} is outside entrypoint {entrypoint}')
    path = catalog['platforms'][platform].get(step, catalog['common'].get(step))
    if path is None:
        raise ValueError(f'no skill for {platform}/{step}; inspect the project workflow instead of substituting another platform')
    result = load_skill(path, root)
    references = []
    for item in catalog.get('references', {}).get(platform, {}).get(step, []):
        reference = (root / item).resolve()
        if not reference.is_relative_to(root) or not reference.is_file():
            raise ValueError(f'invalid packaged reference: {reference}')
        references.append(str(reference))
    return dict(result, platform=platform, step=step, references=references)


def resolve_name(name, root=ROOT, entrypoint=None):
    root = Path(root).resolve()
    catalog = json.loads((root / 'routing.json').read_text())
    paths = set(catalog['common'].values())
    if name in catalog.get('entrypoints', {}):
        raise ValueError(f'public entrypoint is not an internal procedure: {name}')
    for platform in allowed_platforms(catalog, entrypoint):
        paths.update(catalog['platforms'][platform].values())
    matches = [result for path in sorted(paths) if (result := load_skill(path, root))['name'] == name]
    if len(matches) != 1:
        raise ValueError(f'unknown or duplicate internal skill: {name}')
    return matches[0]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--platform')
    parser.add_argument('--entrypoint', help='Preserve the public entrypoint platform restriction')
    selector = parser.add_mutually_exclusive_group(required=True)
    selector.add_argument('--step')
    selector.add_argument('--name')
    args = parser.parse_args()
    if args.name and args.platform:
        parser.error('--name is used without --platform')
    if args.step and not args.platform:
        parser.error('--step requires --platform')
    try:
        result = resolve_name(args.name, entrypoint=args.entrypoint) if args.name else resolve(args.platform, args.step, entrypoint=args.entrypoint)
        print(json.dumps(result, ensure_ascii=False))
    except (ValueError, OSError, KeyError) as exc:
        parser.exit(2, f'BAA route error: {exc}\n')


if __name__ == '__main__':
    main()
