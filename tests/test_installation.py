"""Check portable skill copies and safe manual links with an isolated home."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

REPO = Path(__file__).resolve().parents[1]
NAMES = ('baa', 'baa-apple', 'baa-android', 'baa-windows')


class InstallationTests(unittest.TestCase):
    def test_skill_copy_includes_the_complete_runtime(self):
        with tempfile.TemporaryDirectory(prefix='baa-copy-') as folder:
            installed = (Path(folder) / '.agents/skills').resolve()
            for name in NAMES:
                shutil.copytree(REPO / 'skills' / name, installed / name)
            runtime = installed / 'baa'
            catalog = json.loads((runtime / 'routing.json').read_text())
            for entrypoint, platforms in catalog['entrypoints'].items():
                for platform in platforms:
                    result = subprocess.run([sys.executable, str(runtime / 'scripts/resolve.py'),
                                             '--entrypoint', entrypoint, '--platform', platform,
                                             '--step', 'router'], capture_output=True, text=True)
                    self.assertEqual(result.returncode, 0, result.stderr)
                    route = json.loads(result.stdout)
                    self.assertTrue(Path(route['path']).is_relative_to(runtime))
                    self.assertTrue(Path(route['path']).is_file())
            self.assertTrue((runtime / 'LICENSES/macos-upstream.txt').is_file())
            self.assertTrue((runtime / 'LICENSES/windows-upstream.txt').is_file())
            self.assertTrue((runtime / 'platforms/apple/macos/skills/start/new-mac-app/template/build.sh').is_file())
            self.assertTrue((runtime / 'platforms/windows/skills/start/new-windows-app/template/build.ps1').is_file())

    def test_manual_links_are_idempotent_and_do_not_expose_internal_procedures(self):
        with tempfile.TemporaryDirectory(prefix='baa-link-') as folder:
            env = dict(os.environ, HOME=folder)
            for _ in range(2):
                result = subprocess.run(['bash', str(REPO / 'scripts/link-skills.sh')],
                                        env=env, capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, result.stderr)
            for target in ('.claude/skills', '.agents/skills'):
                entries = sorted((Path(folder) / target).iterdir())
                self.assertEqual([p.name for p in entries], sorted(NAMES))
                for link in entries:
                    self.assertTrue(link.is_symlink())
                    self.assertEqual(link.resolve(), REPO / 'skills' / link.name)

    def test_manual_links_preserve_existing_files_directories_and_wrong_links(self):
        for kind in ('file', 'directory', 'symlink'):
            with self.subTest(kind=kind), tempfile.TemporaryDirectory(prefix='baa-conflict-') as folder:
                home = Path(folder)
                target = home / '.agents/skills/baa-windows'
                target.parent.mkdir(parents=True)
                if kind == 'file':
                    target.write_text('existing skill')
                elif kind == 'directory':
                    target.mkdir()
                    (target / 'keep.txt').write_text('existing skill')
                else:
                    target.symlink_to(home / 'missing-original')
                result = subprocess.run(['bash', str(REPO / 'scripts/link-skills.sh')],
                                        env=dict(os.environ, HOME=folder), capture_output=True, text=True)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn('Refusing to replace existing path:', result.stderr)
                self.assertFalse((home / '.claude/skills').exists())
                if kind == 'file':
                    self.assertEqual(target.read_text(), 'existing skill')
                elif kind == 'directory':
                    self.assertEqual((target / 'keep.txt').read_text(), 'existing skill')
                else:
                    self.assertEqual(target.readlink(), home / 'missing-original')
