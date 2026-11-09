"""Exercise native mobile template generation, dev IDs, portability and data guards."""
import importlib.util
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1] / "skills/baa"
spec = importlib.util.spec_from_file_location("baa_new_app", ROOT / "scripts/new-app.py")
generator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(generator)


class MobileTemplateTests(unittest.TestCase):
    def test_all_platforms_generate_native_projects_and_keep_existing_brief(self):
        with tempfile.TemporaryDirectory(prefix="baa-mobile-") as folder:
            for platform in ("ios", "ipados", "android"):
                name = "Starter" + platform.title()
                dest = Path(folder) / name
                (dest / "docs").mkdir(parents=True)
                brief = dest / "docs/BRIEF.md"
                brief.write_text("User requirements")
                generator.create_app(platform, name, "com.example.notes", folder)
                self.assertEqual(brief.read_text(), "User requirements")
                self.assertFalse((dest / ".git").exists())
                self.assertEqual((dest / "CLAUDE.md").read_text(), "@AGENTS.md\n")
                for document in dest.rglob("*"):
                    if document.is_file() and document.suffix != ".jar":
                        self.assertNotRegex(document.read_text(), r"__[A-Z_]+__", str(document))
                if platform == "android":
                    self.assertTrue((dest / "gradle/wrapper/gradle-wrapper.jar").is_file())
                    batch = (dest / "gradlew.bat").read_bytes()
                    self.assertIn(b"\r\n", batch)
                    self.assertNotIn(b"\n", batch.replace(b"\r\n", b""))
                    self.assertTrue((dest / "app/src/main/java/com/example/notes/MainActivity.kt").is_file())
                    manifest = ET.parse(dest / "app/src/main/AndroidManifest.xml").getroot()
                    ns = "{http://schemas.android.com/apk/res/android}"
                    self.assertEqual(manifest.find("application").get(ns + "icon"), "@mipmap/ic_launcher")
                    icon = ET.parse(dest / "app/src/main/res/mipmap-anydpi/ic_launcher.xml").getroot()
                    self.assertEqual(icon.tag, "adaptive-icon")
                    for layer in ("foreground", "background", "monochrome"):
                        self.assertIsNotNone(icon.find(layer))
                    rules = ET.parse(dest / "app/src/main/res/xml/data_extraction_rules.xml").getroot()
                    for channel in ("cloud-backup", "device-transfer"):
                        exclusions = rules.findall(channel + "/exclude")
                        self.assertIn({"domain": "sharedpref", "path": "."}, [node.attrib for node in exclusions])
                    build = (dest / "app/build.gradle.kts").read_text()
                    self.assertIn('applicationId = "com.example.notes"', build)
                    self.assertIn('applicationIdSuffix = ".dev"', build)
                else:
                    project = dest / (name + ".xcodeproj/project.pbxproj")
                    text = project.read_text()
                    self.assertIn("PRODUCT_BUNDLE_IDENTIFIER = com.example.notes.dev;", text)
                    self.assertIn("PRODUCT_BUNDLE_IDENTIFIER = com.example.notes;", text)
                    self.assertIn('TARGETED_DEVICE_FAMILY = "' + ("1" if platform == "ios" else "2") + '";', text)
                    scheme = ET.parse(dest / (name + ".xcodeproj/xcshareddata/xcschemes/" + name + ".xcscheme")).getroot()
                    test_targets = [node.get("BlueprintName") for node in scheme.findall("./TestAction/Testables/TestableReference/BuildableReference")]
                    self.assertEqual(set(test_targets), {name + "Tests", name + "UITests"})
                    self.assertTrue((dest / ("UITests/" + name + "UITests/NoteEditorUITests.swift")).is_file())
                    if sys.platform == "darwin":
                        result = subprocess.run(["plutil", "-lint", str(project)], capture_output=True, text=True)
                        self.assertEqual(result.returncode, 0, result.stderr)
                with self.assertRaises(ValueError):
                    generator.create_app(platform, name, "com.example.notes", folder)
                self.assertEqual(brief.read_text(), "User requirements")

    def test_conflicts_fail_before_any_template_file_is_written(self):
        for conflict in ("file", "directory", "parent-file", "parent-symlink", "destination-symlink", "existing-project"):
            with self.subTest(conflict=conflict), tempfile.TemporaryDirectory(prefix="baa-guard-") as folder:
                parent = Path(folder)
                dest = parent / "Notes"
                dest.mkdir()
                if conflict in ("file", "directory"):
                    target = dest / "build.sh"
                    target.write_text("keep") if conflict == "file" else target.mkdir()
                elif conflict == "parent-file":
                    (dest / "Sources").write_text("keep")
                elif conflict == "parent-symlink":
                    (parent / "outside").mkdir()
                    (dest / "Sources").symlink_to(parent / "outside", target_is_directory=True)
                elif conflict == "destination-symlink":
                    dest.rmdir()
                    dest.symlink_to(parent / "outside", target_is_directory=True)
                else:
                    (dest / "Existing.xcodeproj").mkdir()
                before = sorted(p.relative_to(parent).as_posix() for p in parent.rglob("*"))
                with self.assertRaises(ValueError):
                    generator.create_app("ios", "Notes", "com.example.notes", parent)
                self.assertEqual(before, sorted(p.relative_to(parent).as_posix() for p in parent.rglob("*")))
                if conflict == "file":
                    self.assertEqual(target.read_text(), "keep")

    def test_nested_projects_are_rejected_before_writing(self):
        markers = (("apple/Existing.xcodeproj", True), ("apple/Existing.xcworkspace", True),
                   ("packages/Core/Package.swift", False), ("android/settings.gradle.kts", False),
                   ("android/build.gradle", False), ("windows/Existing.sln", False),
                   ("windows/Existing.slnx", False))
        for platform in ("ios", "ipados", "android"):
            for marker, directory in markers:
                with self.subTest(platform=platform, marker=marker), tempfile.TemporaryDirectory(prefix="baa-existing-") as folder:
                    destination = Path(folder) / "Notes"
                    target = destination / marker
                    target.parent.mkdir(parents=True)
                    if directory:
                        target.mkdir()
                        (target / "keep.txt").write_text("Existing project data")
                    else:
                        target.write_text("Existing project data")
                    before = {p.relative_to(destination): p.read_bytes() if p.is_file() else None
                              for p in destination.rglob("*")}
                    with self.assertRaisesRegex(ValueError, "existing project"):
                        generator.create_app(platform, "Notes", "com.example.notes", folder)
                    self.assertEqual(before, {p.relative_to(destination): p.read_bytes() if p.is_file() else None
                                              for p in destination.rglob("*")})

    def test_invalid_inputs_never_create_a_destination(self):
        cases = [("ios", "../Notes", "com.example.notes", "17.0"),
                 ("android", "Notes", "com.example.class", "17.0"),
                 ("android", "Notes", "com.example.bad-id", "17.0"),
                 ("ios", "Notes", "com.example/notes", "17.0"),
                 ("ios", "Notes", "com.example.notes", "16.0"),
                 ("linux", "Notes", "com.example.notes", "17.0")]
        with tempfile.TemporaryDirectory(prefix="baa-invalid-") as folder:
            for platform, name, identifier, minimum in cases:
                with self.subTest(platform=platform, name=name, identifier=identifier, minimum=minimum):
                    with self.assertRaises(ValueError):
                        generator.create_app(platform, name, identifier, folder, minimum)
            self.assertEqual(list(Path(folder).iterdir()), [])

    def test_dev_identifier_is_not_duplicated_and_minimum_os_is_explicit(self):
        with tempfile.TemporaryDirectory(prefix="baa-dev-id-") as folder:
            dest = generator.create_app("ipados", "Notes", "com.example.notes.dev", folder, "18.0")
            project = (dest / "Notes.xcodeproj/project.pbxproj").read_text()
            self.assertNotIn(".dev.dev", project)
            self.assertIn("IPHONEOS_DEPLOYMENT_TARGET = 18.0;", project)

    def test_copied_runtime_contains_every_mobile_starter(self):
        with tempfile.TemporaryDirectory(prefix="baa-portable-") as folder:
            runtime = Path(folder) / "runtime"
            shutil.copytree(ROOT, runtime, ignore=shutil.ignore_patterns("__pycache__"))
            for platform in ("ios", "ipados", "android"):
                result = subprocess.run([sys.executable, str(runtime / "scripts/new-app.py"), platform,
                                         "Portable" + platform.title(), "com.example.portable", folder],
                                        capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue((Path(folder) / "PortableAndroid/gradle/wrapper/gradle-wrapper.jar").is_file())
