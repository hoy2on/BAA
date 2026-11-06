#!/bin/sh
# Build or test only; select a concrete simulator/device for tests.
set -eu
cd "$(dirname "$0")"
action=${1:-build}
case "$action" in build|build-for-testing|test) ;; *) echo "Usage: ./build.sh [build|build-for-testing|test] [destination]" >&2; exit 2 ;; esac
destination=${2:-generic/platform=iOS Simulator}
if [ "$action" = test ] && [ "$destination" = 'generic/platform=iOS Simulator' ]; then
    echo 'Tests require an explicit destination, such as id=<simulator-UDID>.' >&2
    exit 2
fi
exec xcodebuild -project __APP_NAME__.xcodeproj -scheme __APP_NAME__ \
    -configuration Debug -destination "$destination" -derivedDataPath .build/DerivedData "$action"
