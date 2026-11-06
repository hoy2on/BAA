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
        self.assertNotEqual(resolver.resolve('ios', 'code')['path'], resolver.resolve('ipados', 'code')['path'])
        self.assertEqual(resolver.resolve('ios', 'code')['references'], resolver.resolve('ipados', 'code')['references'])
        self.assertNotEqual(resolver.resolve('ios', 'native-design')['path'], resolver.resolve('ipados', 'native-design')['path'])
        self.assertNotEqual(resolver.resolve('macos', 'build-and-verify')['path'], resolver.resolve('windows', 'build-and-verify')['path'])

    def test_every_platform_role_uses_the_matching_workflow_stage(self):
        stages = {
            'start': {'router', 'scaffold'},
            'plan': {'clone'},
            'code': {'code', 'os-integrations', 'performance', 'agent-cli'},
            'design': {'native-design', 'design-system', 'layout-grid', 'design-kit',
                       'design-from-app', 'app-icon'},
            'ship': {'build-and-verify', 'test', 'distribute'},
        }
        for platform, roles in self.catalog['platforms'].items():
            for stage, steps in stages.items():
                for step in steps & roles.keys():
                    with self.subTest(platform=platform, step=step):
                        route = Path(resolver.resolve(platform, step)['path'])
                        self.assertEqual(route.parent.parent.name, stage)
                        self.assertEqual(route.parent.parent.parent.name, 'skills')

    def test_mobile_apple_specialists_have_local_roles_and_shared_bases(self):
        for platform in ('ios', 'ipados'):
            pack = ROOT / 'platforms/apple' / platform
            self.assertEqual({p.name for p in (pack / 'skills').iterdir() if p.is_dir()},
                             {'start', 'plan', 'code', 'design', 'ship'})
            self.assertTrue((pack / 'specs/README.md').is_file())
            self.assertTrue(any(p.name != 'README.md' for p in (pack / 'specs').glob('*.md')))
            for step in self.catalog['platforms'][platform]:
                result = resolver.resolve(platform, step, entrypoint='baa-apple')
                with self.subTest(platform=platform, step=step):
                    path = Path(result['path'])
                    self.assertTrue(path.is_relative_to(pack / 'skills'))
                    if step not in ('router', 'native-design'):
                        shared_procedures = [Path(item) for item in result['references'] if Path(item).name == 'PROCEDURE.md']
                        self.assertEqual(len(shared_procedures), 1)
                        shared = shared_procedures[0]
                        self.assertTrue(shared.is_relative_to(ROOT / 'platforms/apple/shared/skills'))
                        self.assertTrue(shared.is_file())
                        self.assertEqual(shared.parent.parent.name, path.parent.parent.name)
                        # Name dispatch must still find shared bases within Apple scope.
                        name = re.search(r'^name: (.+)$', shared.read_text(), re.M).group(1)
                        self.assertEqual(Path(resolver.resolve_name(name, entrypoint='baa-apple')['path']), shared)
                        with self.assertRaises(ValueError):
                            resolver.resolve_name(name, entrypoint='baa-android')
                        other = 'ipados' if platform == 'ios' else 'ios'
                        self.assertIn(str(shared), resolver.resolve(other, step)['references'])

    def test_all_platforms_have_specs_shipping_and_task_specific_references(self):
        for platform in self.catalog['platforms']:
            with self.subTest(platform=platform):
                ship = resolver.resolve(platform, 'distribute')
                self.assertTrue(Path(ship['path']).is_file())
                pack = ROOT / ('platforms/apple/' + platform if platform in ('macos', 'ios', 'ipados') else 'platforms/' + platform)
                self.assertTrue((pack / 'specs/README.md').is_file())
                self.assertGreater(len(list((pack / 'specs').glob('*.md'))), 1)
                for step in ('ux-design', 'improve-architecture'):
                    result = resolver.resolve(platform, step)
                    self.assertTrue(result['references'], (platform, step))
                    for reference in result['references']:
                        self.assertTrue(Path(reference).is_file())

    def test_design_intelligence_is_shared_scoped_and_portable_without_external_skill(self):
        workflow = 'common/baa-ux-design/design-intelligence.md'
        review = 'common/baa-ux-design/ui-review.md'
        with tempfile.TemporaryDirectory(prefix='baa-design-') as folder:
            relocated = (Path(folder) / 'baa').resolve()
            shutil.copytree(ROOT, relocated, ignore=shutil.ignore_patterns('__pycache__'))
            for entrypoint, platforms in self.catalog['entrypoints'].items():
                for platform in platforms:
                    for role in ('ux-design', 'native-design', 'design-system', 'design-kit',
                                 'design-from-app', 'layout-grid', 'app-icon'):
                        result = resolver.resolve(platform, role, relocated, entrypoint)
                        self.assertIn(str((relocated / workflow).resolve()), result['references'])
                        self.assertTrue(all(Path(p).is_file() and Path(p).is_relative_to(relocated)
                                            for p in result['references']))
                    for role in ('build-and-verify', 'test'):
                        result = resolver.resolve(platform, role, relocated, entrypoint)
                        self.assertIn(str((relocated / review).resolve()), result['references'])
                    for role in ('code', 'os-integrations', 'distribute', 'research'):
                        result = resolver.resolve(platform, role, relocated, entrypoint)
                        self.assertNotIn(str((relocated / workflow).resolve()), result['references'])

    def test_unknown_platform_or_missing_role_never_falls_back(self):
        for platform, step in (('linux', 'code'), ('', 'code'), ('macos', 'csharp-winui'), ('macos', 'not-a-role')):
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
        shared = {ROOT / item for roles in self.catalog['references'].values() for items in roles.values() for item in items if Path(item).name == 'PROCEDURE.md'}
        documents.extend(sorted(shared))
        self.assertEqual(set(documents), set(ROOT.rglob('PROCEDURE.md')))
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
