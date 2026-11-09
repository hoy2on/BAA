"""Exercise the adapted BAA scaffold and install guards without building or installing an app."""
import os
import sys
from pathlib import Path
import plistlib
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1] / 'skills/baa'
SCAFFOLD = ROOT / 'platforms/apple/macos/skills/start/new-mac-app'


@unittest.skipUnless(sys.platform == 'darwin', 'macOS scaffold tools required')
class DevTemplateTests(unittest.TestCase):
    def test_scaffold_and_install_guards(self):
        with tempfile.TemporaryDirectory(prefix='baa-template-') as folder:
            work = Path(folder)
            project = work / 'BaaTemplateCheck'
            (project / 'docs').mkdir(parents=True)
            brief = project / 'docs/BRIEF.md'
            brief.write_text('Existing user brief\n')
            result = subprocess.run(['zsh', str(SCAFFOLD / 'scripts/new-app.sh'),
                                     project.name, 'com.example.baatest', str(work)],
                                    capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(brief.read_text(), 'Existing user brief\n')
            info = project / 'Info.plist.in'
            data = plistlib.loads(info.read_bytes())
            self.assertEqual(data['CFBundleIdentifier'], 'com.example.baatest.dev')
            staged = subprocess.check_output(['git', '-C', str(project), 'diff', '--cached', '--name-only'])
            self.assertEqual(staged, b'')
            bad = subprocess.run(['zsh', str(SCAFFOLD / 'scripts/new-app.sh'),
                                  'Invalid', 'bad/id', str(work)], capture_output=True)
            self.assertNotEqual(bad.returncode, 0)
            self.assertFalse((work / 'Invalid').exists())

            # Redirect only test fixture paths; use the real production guard logic.
            script = project / 'build.sh'
            text = script.read_text()
            self.assertIn('app="/Applications/$name-dev.app"', text)
            scratch = work / 'scratch'
            app = work / 'Applications/BaaTemplateCheck-dev.app'
            text = text.replace('scratch="$HOME/Library/Developer/$name/build"', f'scratch="{scratch}"')
            text = text.replace('app="/Applications/$name-dev.app"', f'app="{app}"')
            script.write_text(text)
            shutil.rmtree(project / 'Icon')
            binary = scratch / 'release/BaaTemplateCheck'
            binary.parent.mkdir(parents=True)
            binary.write_text('#!/bin/sh\nexit 0\n')
            binary.chmod(0o755)
            tools = work / 'tools'
            tools.mkdir()
            for name in ('swift', 'codesign', 'xattr', 'open'):
                executable = tools / name
                executable.write_text('#!/bin/sh\nexit 0\n')
                executable.chmod(0o755)
            env = dict(os.environ, PATH=str(tools) + os.pathsep + os.environ['PATH'], SIGN_IDENTITY='-')

            def build():
                return subprocess.run(['zsh', str(script)], env=env, capture_output=True, text=True)

            existing_info = app / 'Contents/Info.plist'
            existing_info.parent.mkdir(parents=True)
            existing_info.write_bytes(plistlib.dumps({'CFBundleIdentifier': 'com.example.release'}))
            sentinel = app / 'keep.txt'
            sentinel.write_text('Keep the existing installation')
            result = build()
            self.assertNotEqual(result.returncode, 0)
            self.assertIn('different bundle identifier', result.stdout)
            self.assertTrue(sentinel.exists())

            existing_info.write_bytes(plistlib.dumps({'CFBundleIdentifier': data['CFBundleIdentifier']}))
            (tools / 'swift').write_text('#!/bin/sh\nexit 42\n')
            result = build()
            self.assertEqual(result.returncode, 42)
            self.assertTrue(sentinel.exists())
            (tools / 'swift').write_text('#!/bin/sh\nexit 0\n')
            data['CFBundleIdentifier'] = 'com.example.release'
            info.write_bytes(plistlib.dumps(data))
            result = build()
            self.assertNotEqual(result.returncode, 0)
            self.assertIn('expected a .dev bundle identifier', result.stdout)
            self.assertTrue(sentinel.exists())

            data['CFBundleIdentifier'] = 'com.example.baatest.dev'
            info.write_bytes(plistlib.dumps(data))
            result = build()
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertTrue((app / 'Contents/MacOS/BaaTemplateCheck').is_file())
            self.assertEqual(plistlib.loads(existing_info.read_bytes())['CFBundleIdentifier'], data['CFBundleIdentifier'])


    def test_optional_cli_uses_dev_alias_and_preserves_other_programs(self):
        with tempfile.TemporaryDirectory(prefix='baa-cli-') as folder:
            work = Path(folder)
            subprocess.run(['zsh', str(SCAFFOLD / 'scripts/new-app.sh'),
                            'BaaCliCheck', 'com.example.baacli', str(work)], check=True,
                           capture_output=True)
            project = work / 'BaaCliCheck'
            helper = ROOT / 'platforms/apple/macos/skills/code/agent-cli/scripts/add-agent-cli.sh'
            result = subprocess.run(['zsh', str(helper), str(project), 'baacheck'], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            build = (project / 'build.sh').read_text()
            self.assertIn('local/bin/baacheck-dev', build)
            socket = (project / 'Sources/BaaCliCheck/Agent/AgentSocket.swift').read_text()
            self.assertIn('appending(path: "BaaCliCheck-dev"', socket)
            alias_dir = work / 'bin'
            alias_dir.mkdir()
            alias = alias_dir / 'baacheck-dev'
            alias.write_text('existing unrelated program')
            block = build.split('# The dev CLI alias.', 1)[1].replace('$HOME/.local/bin', str(alias_dir))
            env = dict(os.environ, app=str(work / 'BaaCliCheck-dev.app'), name='BaaCliCheck')
            result = subprocess.run(['zsh', '-c', block], env=env, capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(alias.read_text(), 'existing unrelated program')
            alias.unlink()
            result = subprocess.run(['zsh', '-c', block], env=env, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(os.readlink(alias), str(work / 'BaaCliCheck-dev.app/Contents/MacOS/BaaCliCheck'))

    def test_quit_script_passes_dev_path_as_argument(self):
        template = (SCAFFOLD / 'template/build.sh').read_text()
        command = next(line.strip() for line in template.splitlines() if 'osascript -e' in line)
        with tempfile.TemporaryDirectory(prefix='baa-quit-') as folder:
            work = Path(folder)
            capture = work / 'args.json'
            fake = work / 'osascript'
            fake.write_text('#!/usr/bin/env python3\nimport json,os,sys\nopen(os.environ["BAA_CAPTURE"],"w").write(json.dumps(sys.argv[1:]))\n')
            fake.chmod(0o755)
            env = dict(os.environ, PATH=str(work) + os.pathsep + os.environ['PATH'],
                       app='/Applications/BaaQuit-dev.app', BAA_CAPTURE=str(capture))
            subprocess.run(['zsh', '-c', command], env=env, check=True)
            import json
            args = json.loads(capture.read_text())
            self.assertEqual(args[-1], '/Applications/BaaQuit-dev.app')
            self.assertEqual(args[1], 'on run argv')
            self.assertEqual(args[3], 'tell application (item 1 of argv) to quit')
            self.assertNotIn('\\', args[3])
            compiled = work / 'quit.scpt'
            subprocess.run(['/usr/bin/osacompile', '-o', str(compiled)] + args[:-1], check=True, capture_output=True)


if __name__ == '__main__':
    unittest.main()
