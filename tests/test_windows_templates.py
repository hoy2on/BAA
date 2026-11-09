"""Check the Windows starter's portable runtime and data-preserving generation."""
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1] / 'skills/baa'
spec = importlib.util.spec_from_file_location('baa_windows_generator', ROOT / 'scripts/new-app.py')
generator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(generator)


class WindowsTemplateTests(unittest.TestCase):
    def test_copy_install_generates_separate_dev_config_and_working_script_paths(self):
        with tempfile.TemporaryDirectory(prefix='baa-tauri-copy-') as folder:
            parent = Path(folder)
            runtime = parent / 'runtime'
            shutil.copytree(ROOT, runtime, ignore=shutil.ignore_patterns('__pycache__'))
            app = parent / 'Notes'
            (app / 'docs').mkdir(parents=True)
            brief = app / 'docs/BRIEF.md'
            brief.write_text('Keep the agreed scope')
            generator.create_app('windows', 'Notes', 'com.example.notes.dev', parent, root=runtime)
            self.assertEqual(brief.read_text(), 'Keep the agreed scope')
            self.assertFalse((app / '.git').exists())
            release = json.loads((app / 'src-tauri/tauri.conf.json').read_text())
            dev = json.loads((app / 'src-tauri/tauri.dev.conf.json').read_text())
            self.assertEqual(release['identifier'], 'com.example.notes')
            self.assertEqual(dev['identifier'], 'com.example.notes.dev')
            self.assertEqual(dev['productName'], 'Notes-dev')
            self.assertEqual(dev['app']['windows'][0]['label'], release['app']['windows'][0]['label'])
            self.assertFalse(dev['bundle']['active'])
            for path in release['bundle']['icon']:
                self.assertTrue((app / 'src-tauri' / path).is_file())
            capability = json.loads((app / 'src-tauri/capabilities/main.json').read_text())
            self.assertEqual(capability['windows'], ['main'])
            self.assertNotIn('remote', capability)
            package = json.loads((app / 'package.json').read_text())
            for action in ['app:dev', 'app:build']:
                self.assertIn('--config src-tauri/tauri.dev.conf.json', package['scripts'][action])
            self.assertIn('--no-bundle', package['scripts']['app:build'])
            self.assertTrue((app / 'src-tauri/src/title.rs').is_file())
            for file in app.rglob('*'):
                if file.is_file() and file.suffix not in ('.png', '.ico'):
                    self.assertNotRegex(file.read_text(), r'__[A-Z_]+__', str(file))

    def test_windows_device_names_are_rejected_before_writing(self):
        with tempfile.TemporaryDirectory(prefix='baa-tauri-names-') as folder:
            for name in ['Con', 'PRN', 'Aux', 'Nul', 'COM1', 'LPT9']:
                with self.subTest(name=name), self.assertRaises(ValueError):
                    generator.create_app('windows', name, 'com.example.notes', folder)
            self.assertEqual(list(Path(folder).iterdir()), [])

    def test_conflicts_and_nested_projects_preserve_every_byte(self):
        for kind in ['package', 'cargo', 'tauri', 'output', 'symlink']:
            with self.subTest(kind=kind), tempfile.TemporaryDirectory(prefix='baa-tauri-guard-') as folder:
                parent = Path(folder)
                app = parent / 'Notes'
                app.mkdir()
                if kind == 'symlink':
                    (parent / 'outside').mkdir()
                    (app / 'src-tauri').symlink_to(parent / 'outside', target_is_directory=True)
                else:
                    relative = {'package':'existing/package.json', 'cargo':'existing/Cargo.toml',
                                'tauri':'existing/src-tauri/tauri.conf.json', 'output':'package.json'}[kind]
                    path = app / relative
                    path.parent.mkdir(parents=True, exist_ok=True)
                    path.write_text('Keep user data')
                def snapshot():
                    return {str(p.relative_to(parent)): ('link', str(p.readlink())) if p.is_symlink()
                            else ('file', p.read_bytes()) if p.is_file() else ('dir', None)
                            for p in parent.rglob('*')}
                before = snapshot()
                with self.assertRaises(ValueError):
                    generator.create_app('windows', 'Notes', 'com.example.notes', parent)
                self.assertEqual(snapshot(), before)
