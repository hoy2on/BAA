# Development

This is a new __PLATFORM__ SwiftUI app. Preserve the selected device family and deployment target.
Use the shared __APP_NAME__ Xcode scheme and a concrete device destination for verification.
Debug uses __BUNDLE_ID__; Release uses __RELEASE_ID__. Never install Release as part of development.
Use build.sh build or build-for-testing for compilation without installation. The test action installs and launches dev test targets on the selected destination through Xcode. The script does not delete apps, stage, or commit files.
Use the existing views and state before introducing architecture or dependencies.

The UI test target launches only Debug with BAA_UI_TEST=1 and uses a separate .ui-tests defaults domain.
This resets only its test note, never the ordinary dev store. Release ignores the test launch flag.
Use ./build.sh build-for-testing to compile all test targets without installing anything.
Run ./build.sh test 'id=<selected-UDID>' only when dev test installation and the device are in scope.
Screenshots attach to the xcresult; inspect results rather than equating a test build with execution.
