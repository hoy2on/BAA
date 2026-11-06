#!/bin/zsh
# Builds __APP_NAME__ and installs it to /Applications/__APP_NAME__-dev.app.
# Build products live in ~/Library/Developer/__APP_NAME__, outside the repo
# (and outside Dropbox or iCloud, which would try to sync them).
#
# Usage: ./build.sh            release build, install
#        ./build.sh --debug    debug build, install
#        ./build.sh --open     install, then quit the running copy and open the new one
set -euo pipefail
here=${0:A:h}
name="__APP_NAME__"
scratch="$HOME/Library/Developer/$name/build"
config=release
[[ " $* " == *" --debug "* ]] && config=debug

# Sign with your Apple Development certificate when you have one (Xcode >
# Settings > Accounts). Otherwise sign ad hoc, which is fine for your own Mac.
identity="${SIGN_IDENTITY:-}"
if [[ -z "$identity" ]]; then
  identity=$(security find-identity -v -p codesigning 2>/dev/null | grep -m1 -o '"Apple Development: [^"]*"' | tr -d '"' || true)
fi
[[ -n "$identity" ]] || identity=-

swift build -c $config --package-path "$here" --scratch-path "$scratch"
bin="$scratch/$config/$name"
[[ -x "$bin" ]] || { echo "build failed"; exit 1; }
# swift build can report success while an edited file failed to compile. Catch that.
stale=$(find "$here/Sources" -name '*.swift' -newer "$bin" | head -1)
if [[ -n "$stale" ]]; then
  echo "build failed: binary is older than $stale"
  swift build -c $config --package-path "$here" --scratch-path "$scratch" 2>&1 | grep -E "error" | head -20
  exit 1
fi

app="/Applications/$name-dev.app"
bundle=$(/usr/libexec/PlistBuddy -c 'Print CFBundleIdentifier' "$here/Info.plist.in")
[[ "$bundle" == *.dev ]] || { echo "refusing to install: expected a .dev bundle identifier"; exit 1; }
if [[ -e "$app" ]]; then
  installed_bundle=$(/usr/libexec/PlistBuddy -c 'Print CFBundleIdentifier' "$app/Contents/Info.plist")
  [[ "$installed_bundle" == "$bundle" ]] || { echo "refusing to replace an app with a different bundle identifier"; exit 1; }
  if pgrep -f "^$app/Contents/MacOS/$name$" >/dev/null; then
    osascript -e 'on run argv' -e 'tell application (item 1 of argv) to quit' -e 'end run' "$app"
    sleep 0.5
    pgrep -f "^$app/Contents/MacOS/$name$" >/dev/null && { echo "dev app is still running; replacement stopped"; exit 1; }
  fi
fi
rm -rf "$app"
mkdir -p "$app/Contents/MacOS" "$app/Contents/Resources"
cp "$bin" "$app/Contents/MacOS/$name"
sed -e "s/__BUILD__/$(date +%Y%m%d%H%M)/" "$here/Info.plist.in" > "$app/Contents/Info.plist"
# The icon: Icon/AppIcon.icon -> Resources/Assets.car + AppIcon.icns, rebuilt when it changed.
if [[ -d "$here/Icon/AppIcon.icon" ]]; then
  car="$here/Resources/Assets.car"
  if [[ ! -f "$car" || -n "$(find "$here/Icon/AppIcon.icon" -newer "$car" | head -1)" ]]; then
    "$here/tools/make_icon.sh"
  fi
  cp -X "$car" "$here/Resources/AppIcon.icns" "$app/Contents/Resources/"
fi
xattr -cr "$app"
codesign --force --sign "$identity" "$app"
codesign --verify --strict "$app"
echo "installed $app (signed: ${identity})"

if [[ " $* " == *" --open "* ]]; then
  open "$app"
fi
