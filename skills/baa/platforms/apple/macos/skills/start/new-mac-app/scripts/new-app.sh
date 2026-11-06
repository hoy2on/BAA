#!/bin/zsh
# Creates a new macOS app from the template next to this script.
# Usage: new-app.sh <AppName> <bundle-id> [parent-folder]
#   new-app.sh Tasks com.yourname.tasks ~/Developer
# Creates <parent-folder>/<AppName>. If that folder exists, it must not have a
# Package.swift yet; existing files (like docs/BRIEF.md) are kept.
# AppName must be one word in UpperCamelCase (letters and digits only).
set -euo pipefail
name=${1:?usage: new-app.sh <AppName> <bundle-id> [parent-folder]}
bundle=${2:?usage: new-app.sh <AppName> <bundle-id> [parent-folder]}
parent=${3:-$PWD}
[[ "$bundle" =~ ^[A-Za-z0-9]+([.-][A-Za-z0-9]+)+$ ]] || { echo "bundle-id must contain only letters, digits, dots and hyphens"; exit 1; }
[[ "$bundle" == *.dev ]] || bundle="$bundle.dev"
[[ "$name" =~ ^[A-Z][A-Za-z0-9]*$ ]] || { echo "AppName must be UpperCamelCase letters and digits, like Tasks or DailyLog"; exit 1; }
template=${0:A:h:h}/template
dest="$parent/$name"
# An existing folder is fine if it has no project yet (for example only docs/BRIEF.md).
[[ ! -e "$dest/Package.swift" ]] || { echo "$dest already has a Package.swift"; exit 1; }

mkdir -p "$dest"
# Keep files that are already there. Not `cp -n`: on macOS it exits 1 when it
# skips a file, and set -e then stops the script halfway.
rsync -a --ignore-existing "$template/" "$dest/"
# A kept .gitignore gets the template lines it lacks.
if ! cmp -s "$template/.gitignore" "$dest/.gitignore"; then
  [[ -z $(tail -c1 "$dest/.gitignore") ]] || echo >> "$dest/.gitignore"
  grep -vxF -f "$dest/.gitignore" "$template/.gitignore" >> "$dest/.gitignore" || true
fi
mv "$dest/Sources/__APP_NAME__" "$dest/Sources/$name"
mv "$dest/Sources/__APP_NAME__Kit" "$dest/Sources/${name}Kit"
mv "$dest/Tests/__APP_NAME__KitTests" "$dest/Tests/${name}KitTests"
# Replace the placeholders in every text file.
grep -rlI "__APP_NAME__\|__BUNDLE_ID__" "$dest" | while read -r f; do
  sed -i '' -e "s/__APP_NAME__/$name/g" -e "s/__BUNDLE_ID__/$bundle/g" "$f"
done
chmod +x "$dest/build.sh" "$dest/tools/make_icon.sh" "$dest/tools/icon_review.sh" "$dest/tools/grid-lint.sh" "$dest/tools/check-layout.swift" "$dest/tools/snap.sh" "$dest/tools/selftest.sh"

cd "$dest"
[[ -d .git ]] || git init -q
# Commit through the project workflow so existing user files are not staged.
echo "review the generated files before committing"
echo "created $dest"
echo "next: cd \"$dest\" && ./build.sh --open"
