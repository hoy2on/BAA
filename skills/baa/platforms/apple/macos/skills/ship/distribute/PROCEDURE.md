---
name: baa-macos-distribute
description: Prepare a macOS release using the existing project's Mac App Store or Developer ID distribution workflow. Use for explicitly requested packaging, signing, notarization or submission.
---

# macOS distribution

Read [BAA execution rules](../../../../../../EXECUTION.md). Preserve the inherited entrypoint, macOS target, project and requested external-action scope. A build request alone doesn't authorize uploading or installing a release.

## Inspect before building

Read the actual release script/CI and choose the existing channel: Mac App Store/TestFlight or direct Developer ID. Confirm product and bundle IDs, version/build values, architectures, minimum OS, nested helpers/extensions, entitlements, signing identities and provisioning where required. Keep secrets in the existing secret store, not docs or logs.
Keep dev/release app data, keychain groups and app-group boundaries distinct. Don't use packaging as a reason to replace the installed Release app.

## Build and verify artifacts

Use the existing release configuration and packaging output. Verify required tests and supported architectures. Inspect signing of every nested executable/bundle; a top-level signature check alone doesn't establish that nested code uses the correct distribution identity/timestamp.
For direct distribution, use the project's Developer ID and notarization flow. Record the accepted notary result, staple supported artifacts, and assess both the final DMG/package and the inner app with the platform's actual verification tools. A local ad-hoc signature isn't a distribution signature.
For App Store/TestFlight, use the app's archive/export and App Store Connect workflow. Check sandbox entitlements, privacy declarations and required metadata for the changed release. Don't apply direct-distribution notarization steps as a substitute for App Store submission.

## External actions and evidence

Separate local archive/package creation, notarization submission, hosting upload, TestFlight distribution and store review submission. Perform only the requested stages; report any account, certificate or portal work that the user must complete.
Return source revision, channel, commands and exit codes, signing/verification results, artifact paths and checksums, external submissions performed, and remaining acceptance on another machine. Never delete user data or uninstall Release to prove a package installs.

Reference: [Notarizing macOS software](https://developer.apple.com/documentation/security/notarizing-macos-software-before-distribution). Confirm exact commands and options using the installed Xcode/security tools and current project documentation.
