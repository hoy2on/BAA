---
name: baa-apple-scaffold
description: Apple mobile scaffold procedure for the assigned platform and current app workflow.
---

# Apple mobile Scaffold

Read the [BAA execution rules](../../../../../../EXECUTION.md). Inherit platform, purpose, owned files and acceptance. This internal procedure does not restart platform selection or team creation; preserve other workers' changes.

## Execution

Read [runtime verification](../../../verification.md) for project-specific commands and evidence.

Inspect existing xcodeproj/xcworkspace, generators, packages and targets. Never create a new skeleton over an existing project.
For a new app confirm product name, iOS/iPadOS scope, supported OS, SwiftUI/UIKit and actual tools. Prefer installed Xcode templates or existing repository generators. A Swift package alone is not an executable iOS app.
Create only agreed app/test targets, a minimal screen and persistent/relaunchable core state. Don't add iPad support to iPhone-only scope; confirm device families for Universal targets. Configure Debug/dev name, distinct bundle ID, signing/provisioning; don't share production App Group/keychain storage or migrate user data automatically.
Check existing dependencies/Xcode capabilities before packages/generators, using the installed generator's schema/docs. Build with actual scheme/destination and verify the first dev screen. Resolve native-design/design-system/app-icon or the current story's code next.
Done when targets/dev identity/minimal app and build/launch results or environment limits are documented.

## Follow-up and handoff

Resolve subsequent roles from the runtime root with `python3 scripts/resolve.py --entrypoint <entrypoint> --platform <assigned-platform> --step <role>`. Read the returned PROCEDURE.md; do not use internal names as Skill-tool/slash commands. Do not recurse into the current stage or add unrequested distribution, installation or commits.
Return changed files, source state/target/environment, check/screen/log paths, unverified items and shared-change proposals to the coordinator.

Official references: [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/), [SwiftUI](https://developer.apple.com/documentation/swiftui), [UIKit](https://developer.apple.com/documentation/uikit), [XCTest](https://developer.apple.com/documentation/xctest). Confirm API availability/signatures against the installed SDK and project minimum OS.
## Packaged base template

The shared [template](template) contains real Xcode app/test targets, a shared scheme, app entrypoint, title model/tests and build script.
Generate it together with ContentView from the iOS/iPadOS new-app procedure. The base alone is not a complete executable app.
The runtime scripts/new-app.py combines OS files and refuses to overwrite existing projects/files.
