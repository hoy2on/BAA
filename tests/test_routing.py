"""BAA routing, namespace isolation, complete packaged graphs and relocatability."""
import importlib.util
import json
import re
import shutil
import tempfile
from pathlib import Path
import unittest

REPO = Path(__file__).resolve().parents[1]
ROOT = REPO / 'skills/baa'
spec = importlib.util.spec_from_file_location('baa_resolve', ROOT / 'scripts/resolve.py')
resolver = importlib.util.module_from_spec(spec)
spec.loader.exec_module(resolver)


class RoutingTests(unittest.TestCase):
    def setUp(self):
        self.catalog = json.loads((ROOT / 'routing.json').read_text())
        self.manifest = json.loads((REPO / '.claude-plugin/plugin.json').read_text())

    def test_platform_and_common_dispatch(self):
        expected = {'macos': 'baa-macos-swift-swiftui', 'windows': 'baa-windows-csharp-winui'}
        for platform in self.catalog['platforms']:
            for step in self.catalog['platforms'][platform].keys() | self.catalog['common'].keys():
                result = resolver.resolve(platform, step)
                self.assertTrue(Path(result['path']).is_file())
            if platform in expected:
                self.assertEqual(resolver.resolve(platform, 'code')['name'], expected[platform])
        for platform in self.catalog['platforms']:
            self.assertEqual(resolver.resolve(platform, 'user-stories')['name'], 'baa-user-stories')
        self.assertEqual(resolver.resolve('ios', 'code')['path'], resolver.resolve('ipados', 'code')['path'])
        self.assertNotEqual(resolver.resolve('ios', 'native-design')['path'], resolver.resolve('ipados', 'native-design')['path'])
        self.assertNotEqual(resolver.resolve('macos', 'build-and-verify')['path'], resolver.resolve('windows', 'build-and-verify')['path'])

    def test_unknown_platform_or_missing_role_never_falls_back(self):
        for platform, step in (('linux', 'code'), ('', 'code'), ('macos', 'csharp-winui'), ('macos', 'distribute')):
            with self.assertRaises(ValueError):
                resolver.resolve(platform, step)

    def test_relocation_and_removed_upstream_plugins(self):
        with tempfile.TemporaryDirectory(prefix='baa-standalone-') as folder:
            relocated = (Path(folder) / 'only-baa').resolve()
            shutil.copytree(ROOT, relocated, ignore=shutil.ignore_patterns('__pycache__'))
            for platform in self.catalog['platforms']:
                for step in self.catalog['platforms'][platform]:
                    result = resolver.resolve(platform, step, relocated)
                    self.assertTrue(Path(result['path']).is_relative_to(relocated))
                    for reference in result['references']:
                        self.assertTrue(Path(reference).is_relative_to(relocated))

    def test_reject_outside_or_unknown_internal_skill(self):
        with tempfile.TemporaryDirectory(prefix='baa-route-') as folder:
            fake = Path(folder)
            (fake / 'routing.json').write_text(json.dumps({'platforms': {'windows': {'code': '../outside'}}, 'common': {}}))
            with self.assertRaisesRegex(ValueError, 'inside'):
                resolver.resolve('windows', 'code', fake)
            (fake / 'routing.json').write_text(json.dumps({'platforms': {'windows': {'code': 'internal'}}, 'common': {}}))
            (fake / 'internal').mkdir()
            (fake / 'internal/PROCEDURE.md').write_text('---\nname: baa-fake\ndescription: fake\n---\n')
            self.assertEqual(resolver.resolve('windows', 'code', fake)['name'], 'baa-fake')
            with self.assertRaisesRegex(ValueError, 'unknown'):
                resolver.resolve_name('baa-not-declared', fake)

    def test_registered_names_graph_edges_and_packaged_links(self):
        public = ['./skills/baa', './skills/baa-apple', './skills/baa-android', './skills/baa-windows']
        self.assertEqual(self.manifest['skills'], public)
        entries = set(self.catalog['common'].values())
        for roles in self.catalog['platforms'].values():
            entries.update(roles.values())
        documents = [ROOT / entry / 'PROCEDURE.md' for entry in entries]
        documents.extend(REPO / path.removeprefix('./') / 'SKILL.md' for path in public)
        names = [re.search(r'^name: (.+)$', doc.read_text(), re.M).group(1) for doc in documents]
        self.assertEqual(len(names), len(set(names)))
        self.assertNotIn('version', self.manifest)
        names = set(names)
        for doc in REPO.rglob('*.md'):
            text = doc.read_text()
            visible = re.sub(r'(?ms)^```[^\n]*\n.*?^```\s*$', '', text)
            visible = re.sub(r'`[^`\n]+`', '', visible)
            for target in re.findall(r'\]\(([^)]+)\)', visible):
                if '://' in target or target.startswith('#'):
                    continue
                self.assertTrue((doc.parent / target.split('#')[0]).exists(), (doc, target))
            if doc.name in ('SKILL.md', 'PROCEDURE.md'):
                for called in re.findall(r'Read and follow the packaged procedure for `([^`]+)`', text):
                    self.assertIn(called, names, (doc, called))
                    if '/platforms/windows/' in str(doc):
                        self.assertFalse(called.startswith('baa-macos-'), (doc, called))
                    if '/platforms/apple/macos/' in str(doc):
                        self.assertFalse(called.startswith('baa-windows-'), (doc, called))


    def test_internal_names_resolve_without_public_registration(self):
        self.assertEqual(self.manifest['skills'], ['./skills/baa', './skills/baa-apple', './skills/baa-android', './skills/baa-windows'])
        paths = set(self.catalog['common'].values())
        for roles in self.catalog['platforms'].values():
            paths.update(roles.values())
        for path in paths:
            name = re.search(r'^name: (.+)$', (ROOT / path / 'PROCEDURE.md').read_text(), re.M).group(1)
            result = resolver.resolve_name(name)
            self.assertEqual(Path(result['path']), (ROOT / path / 'PROCEDURE.md').resolve())
        with self.assertRaises(ValueError):
            resolver.resolve_name('baa')


    def test_direct_entrypoints_restrict_platform_routes(self):
        expected = {'baa': {'macos', 'ios', 'ipados', 'android', 'windows'},
                    'baa-apple': {'macos', 'ios', 'ipados'},
                    'baa-android': {'android'}, 'baa-windows': {'windows'}}
        self.assertEqual({key: set(value) for key, value in self.catalog['entrypoints'].items()}, expected)
        for entrypoint, allowed in expected.items():
            for platform in self.catalog['platforms']:
                if platform in allowed:
                    self.assertEqual(resolver.resolve(platform, 'code', entrypoint=entrypoint)['platform'], platform)
                    self.assertEqual(resolver.resolve(platform, 'research', entrypoint=entrypoint)['name'], 'baa-research')
                else:
                    with self.assertRaisesRegex(ValueError, 'outside'):
                        resolver.resolve(platform, 'code', entrypoint=entrypoint)
        with self.assertRaisesRegex(ValueError, 'entrypoint'):
            resolver.resolve('android', 'code', entrypoint='baa-unknown')

    def test_named_routes_preserve_direct_scope(self):
        self.assertEqual(resolver.resolve_name('baa-research', entrypoint='baa-android')['name'], 'baa-research')
        self.assertEqual(resolver.resolve_name('baa-macos-mac-design', entrypoint='baa-apple')['name'], 'baa-macos-mac-design')
        for entrypoint, name in [('baa-android', 'baa-macos-mac-design'), ('baa-apple', 'baa-windows-csharp-winui')]:
            with self.assertRaises(ValueError):
                resolver.resolve_name(name, entrypoint=entrypoint)
        for entrypoint in self.catalog['entrypoints']:
            with self.assertRaises(ValueError):
                resolver.resolve_name(entrypoint)

    def test_cli_rejects_cross_platform_and_unknown_entrypoints(self):
        import subprocess
        import sys
        base = [sys.executable, str(ROOT / 'scripts/resolve.py')]
        result = subprocess.run(base + ['--entrypoint', 'baa-android', '--platform', 'windows', '--step', 'code'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)
        self.assertIn('outside', result.stderr)
        result = subprocess.run(base + ['--entrypoint', 'baa-apple', '--platform', 'ios', '--step', 'native-design'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)['name'], 'baa-ios-design')

    def test_recursive_discovery_exposes_only_four_entrypoints(self):
        files = sorted(p.relative_to(REPO).as_posix() for p in REPO.rglob('SKILL.md'))
        self.assertEqual(files, sorted(path.removeprefix('./') + '/SKILL.md' for path in self.manifest['skills']))
        self.assertEqual(len(files), 4)


if __name__ == '__main__':
    unittest.main()
