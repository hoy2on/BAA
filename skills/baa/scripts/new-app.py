#!/usr/bin/env python3
"""Create a new native mobile app from BAA templates without overwriting files."""
import argparse
import json
import os
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def create_app(platform, name, identifier, parent, min_os="17.0", root=ROOT):
    if platform not in ("ios", "ipados", "android"):
        raise ValueError("platform must be ios, ipados, or android")
    if not re.fullmatch(r"[A-Z][A-Za-z0-9]*", name):
        raise ValueError("AppName must be UpperCamelCase letters and digits, like DailyNotes")
    if not re.fullmatch(r"[A-Za-z][A-Za-z0-9-]*(?:\.[A-Za-z][A-Za-z0-9-]*)+", identifier):
        raise ValueError("identifier must be a reverse-domain ID containing letters, digits, dots and hyphens")
    release_id = identifier[:-4] if identifier.endswith(".dev") else identifier
    if "." not in release_id:
        raise ValueError("release identifier must contain a reverse-domain prefix")
    if platform == "android":
        reserved = set("abstract as assert boolean break byte case catch char class const continue default do double else enum extends false final finally float for fun goto if implements import in instanceof int interface is long native new null object package private protected public return short static strictfp super switch synchronized this throw throws transient true try val var void volatile when while".split())
        if not re.fullmatch(r"[a-z][a-z0-9_]*(?:\.[a-z][a-z0-9_]*)+", release_id) or any(part in reserved for part in release_id.split(".")):
            raise ValueError("Android identifier must use lowercase non-keyword package segments")
    if not re.fullmatch(r"[0-9]+\.[0-9]+", min_os) or tuple(map(int, min_os.split("."))) < (17, 0):
        raise ValueError("Apple template requires --min-os 17.0 or later; keep existing apps on their existing workflow")
    root = Path(root).resolve()
    catalog = json.loads((root / "routing.json").read_text())
    procedure = root / catalog["platforms"][platform]["scaffold"]
    templates = []
    if platform in ("ios", "ipados"):
        bases = catalog["references"][platform]["scaffold"]
        templates.append((root / bases[0]).parent / "template")
    templates.append(procedure / "template")
    values = {
        "__APP_NAME__": name,
        "__PLATFORM__": platform,
        "__RELEASE_ID__": release_id,
        "__BUNDLE_ID__": release_id + ".dev",
        "__APPLICATION_ID__": release_id,
        "__PACKAGE_PATH__": release_id.replace(".", "/"),
        "__DEVICE_FAMILY__": "1" if platform == "ios" else "2",
        "__MIN_OS__": min_os,
    }
    def render(text):
        for key, value in values.items():
            text = text.replace(key, value)
        return text
    destination = Path(parent).expanduser().resolve() / name
    if destination.is_symlink() or (destination.exists() and not destination.is_dir()):
        raise ValueError(f"Refusing non-directory or symlink destination: {destination}")
    if destination.exists():
        markers = ("*.xcodeproj", "*.xcworkspace", "Package.swift", "settings.gradle*", "build.gradle*", "*.sln", "*.slnx")
        if any(any(destination.rglob(pattern)) for pattern in markers):
            raise ValueError(f"Refusing to scaffold an existing project: {destination}")
    files = {}
    for template in templates:
        if not template.is_dir():
            raise ValueError(f"Missing packaged template: {template}")
        for source in sorted(template.rglob("*")):
            if source.is_symlink():
                raise ValueError(f"Refusing template symlink: {source}")
            if not source.is_file():
                continue
            relative = Path(render(source.relative_to(template).as_posix()))
            if relative in files:
                raise ValueError(f"Duplicate template output: {relative}")
            files[relative] = source
    if not files:
        raise ValueError("No template files found")
    # Check every output before writing: docs may exist, but generated paths must be new.
    for relative in files:
        target = destination / relative
        if os.path.lexists(target):
            raise ValueError(f"Refusing to replace existing path: {target}")
        for ancestor in target.parents:
            if ancestor == destination.parent:
                break
            if ancestor.is_symlink() or (ancestor.exists() and not ancestor.is_dir()):
                raise ValueError(f"Refusing conflicting parent path: {ancestor}")
    for relative, source in files.items():
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        if source.suffix == ".jar":
            with target.open("xb") as output:
                output.write(source.read_bytes())
        else:
            # Exclusive creation also guards a file appearing after the preflight.
            with target.open("x", encoding="utf-8", newline="\r\n" if source.suffix == ".bat" else "") as output:
                output.write(render(source.read_text()))
        if source.name in ("gradlew", "build.sh"):
            target.chmod(0o755)
    return destination


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("platform", choices=("ios", "ipados", "android"))
    parser.add_argument("name")
    parser.add_argument("identifier", help="Release/base ID; development uses a separate .dev ID")
    parser.add_argument("parent", nargs="?", default=str(Path.cwd()))
    parser.add_argument("--min-os", default="17.0", help="Minimum iOS/iPadOS version for a new app (default: 17.0)")
    args = parser.parse_args()
    try:
        result = create_app(args.platform, args.name, args.identifier, args.parent, args.min_os)
    except (ValueError, OSError, KeyError) as error:
        parser.exit(2, str(error) + "\n")
    print(f"Created {result}")
    print("Review the generated files and signing settings. Nothing was installed, staged, committed or pushed.")


if __name__ == "__main__":
    main()
