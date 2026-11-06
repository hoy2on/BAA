#!/bin/zsh
# Runs the in-app self-test against a fresh store in /tmp. Exit code 0 when every check passed.
set -eu
# Keep cleanup confined to the dev app and the dedicated test store.
[[ "__BUNDLE_ID__" == *.dev ]] || { echo "expected a dev bundle identifier"; exit 1; }
store=/tmp/__APP_NAME__-self.store
rm -f $store $store-shm $store-wal
APP_STORE=$store /Applications/__APP_NAME__-dev.app/Contents/MacOS/__APP_NAME__ --selftest
