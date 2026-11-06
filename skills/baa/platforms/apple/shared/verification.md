# iOS and iPadOS runtime verification

Read when constructing scaffold, build-and-verify or test commands. macOS uses its own build procedure.
Prefer existing project scripts. Resolve every value from the project/tools; never run an invented example scheme, configuration or device.

## Inspect the project and destination

```sh
xcodebuild -version
xcodebuild -list -json -workspace "$BAA_WORKSPACE"
xcodebuild -showdestinations -workspace "$BAA_WORKSPACE" -scheme "$BAA_SCHEME"
xcrun simctl list devices available
```

Without a workspace, use the actual .xcodeproj and -project. Available Xcode tools may provide equivalent inspection commands.
Inspect supported platforms, TARGETED_DEVICE_FAMILY, PRODUCT_BUNDLE_IDENTIFIER, signing and dev configuration in the selected scheme build settings.
An iPhone destination proves iOS; an iPad destination proves iPadOS. A Universal target does not make one run evidence for both.

## Building and installation are separate

```sh
xcodebuild -workspace "$BAA_WORKSPACE" -scheme "$BAA_SCHEME" \
  -configuration "$BAA_DEV_CONFIGURATION" -destination "id=$BAA_DEVICE_UDID" build
```

Inspect the built .app Info.plist ID, signing and entitlements. Build success is not runtime success.
Use these installation commands only for a verified designated dev ID on Simulator. For hardware follow installed Xcode/devicectl help and the existing project workflow.

```sh
xcrun simctl install "$BAA_DEVICE_UDID" "$BAA_DEV_APP"
xcrun simctl launch "$BAA_DEVICE_UDID" "$BAA_DEV_BUNDLE_ID"
xcrun simctl io "$BAA_DEVICE_UDID" screenshot "$BAA_SCREENSHOT"
```

Do not reset Simulator or remove Release to fix installation. Confirm the changed state and actual foreground app before capturing.
simctl screenshot captures; it does not verify taps/scrolling. Use XCUITest or available UI interaction tools.

## Tests and evidence

```sh
xcodebuild -workspace "$BAA_WORKSPACE" -scheme "$BAA_SCHEME" \
  -configuration "$BAA_DEV_CONFIGURATION" -destination "id=$BAA_DEVICE_UDID" \
  -resultBundlePath "$BAA_NEW_RESULT_BUNDLE" test
```

Inspect actual test targets/plans and affected scope, narrowing with -only-testing when useful. Use a new result-bundle path rather than overwriting evidence.
Preserve build/test exit codes when piping logs, using the current shell pipefail support or existing project tools.
On failure retain first cause, whether execution occurred, selected destination and xcresult. Zero tests, unavailable destinations and permission blocks are not passes.

Select affected normal/cancel/Back/keyboard/restoration/long-translation/large-text/light-dark flows.
Verify iPad narrow/wide windows, column transitions, rotation and keyboard/pointer; verify iPhone touch, safe area and navigation return in actual flows.
Return selected target, source state, scheme/configuration, device/OS, commands/exit codes, xcresult/logs/screens and remaining hardware checks.

Official reference: [Xcode testing](https://developer.apple.com/documentation/xcode/running-tests-and-interpreting-results).
Confirm command availability using installed xcodebuild -help, xcrun simctl help and xcrun devicectl help.
