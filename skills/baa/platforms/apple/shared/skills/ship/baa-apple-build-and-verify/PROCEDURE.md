---
name: baa-apple-build-and-verify
description: Apple mobile build and verify procedure for the assigned platform and current app workflow.
---

# Apple mobile Build And Verify

Read the [BAA execution rules](../../../../../../EXECUTION.md). Inherit platform, purpose, owned files and acceptance. This internal procedure does not restart platform selection or team creation; preserve other workers' changes.

## Execution

Read [runtime verification](../../../verification.md) for project-specific commands and evidence.

Inspect project instructions and xcodebuild -list/Xcode tools for the actual workspace/project, scheme, dev configuration and destinations. Use actual xcodebuild -showdestinations results; choose iPhone for iOS and iPad for iPadOS without invented schemes.
Reuse build/test scripts. Direct commands specify workspace or project, scheme, dev configuration and concrete destination, preserving original errors/result bundles. Before installation inspect actual .app ID, signing/entitlements and dev settings. Use simctl install/launch with the verified UDID for Simulator; check installed Xcode/devicectl help for hardware. Never remove Release.
Exercise changed and adjacent runtime flows; screenshots alone do not prove buttons/undo/save. Use existing XCUITest/UI flows as needed. Verify iPhone keyboard/safe area/Back and iPad window/column/orientation/pointer/keyboard conditions separately. One device result does not pass both platforms.
Serialize only runs sharing a device, DerivedData or dev installation.
Done when source/target/device/build-test/screens are linked and unverified items are separately reported.

## Follow-up and handoff

Resolve subsequent roles from the runtime root with `python3 scripts/resolve.py --entrypoint <entrypoint> --platform <assigned-platform> --step <role>`. Read the returned PROCEDURE.md; do not use internal names as Skill-tool/slash commands. Do not recurse into the current stage or add unrequested distribution, installation or commits.
Return changed files, source state/target/environment, check/screen/log paths, unverified items and shared-change proposals to the coordinator.

Official references: [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/), [SwiftUI](https://developer.apple.com/documentation/swiftui), [UIKit](https://developer.apple.com/documentation/uikit), [XCTest](https://developer.apple.com/documentation/xctest). Confirm API availability/signatures against the installed SDK and project minimum OS.
## Supporting reference

Read [existing-app.md](existing-app.md) when performing this role; keep the assigned platform and scope.
