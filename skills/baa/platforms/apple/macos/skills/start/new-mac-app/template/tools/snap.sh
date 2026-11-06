#!/bin/zsh
# Snapshots of every page in light and dark, with seed data, on a fresh test store.
# Usage: tools/snap.sh            all pages
#        APP_SNAPSHOT_PAGES=all,settings tools/snap.sh
set -eu
# Keep cleanup confined to the dev app and the dedicated test store.
[[ "__BUNDLE_ID__" == *.dev ]] || { echo "expected a dev bundle identifier"; exit 1; }
app=/Applications/__APP_NAME__-dev.app/Contents/MacOS/__APP_NAME__
store=/tmp/__APP_NAME__-test.store
shots=/tmp/__APP_NAME__-shots
# A crashed run leaves saved window state, and the next launch would wait on a "reopen windows?" alert.
# Seed data only fills an empty store, so start from nothing.
rm -f $store $store-shm $store-wal
rm -rf $shots
APP_STORE=$store APP_SEED=1 APP_SNAPSHOT=$shots $app
