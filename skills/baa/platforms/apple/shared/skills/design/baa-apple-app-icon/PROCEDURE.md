---
name: baa-apple-app-icon
description: Apple mobile app icon procedure for the assigned platform and current app workflow.
---

# Apple mobile App Icon

Read the [BAA execution rules](../../../../../../EXECUTION.md). Inherit platform, purpose, owned files and acceptance. This internal procedure does not restart platform selection or team creation; preserve other workers' changes.

## Execution

Inspect asset catalogs, AppIcon settings, Info.plist, build target and supported OS. Use icon formats actually supported by current Xcode.
Preserve product meaning/brand and requested scope. Reuse raster/vector originals and generation scripts with their licenses. Verify sizes, appearances and transparency requirements through current docs/Xcode validation; do not register .icns/.ico as mobile assets.
Use Icon Composer only when the project/OS uses it; don't convert an old catalog unrequested. Connect icons to the actual iOS/iPadOS dev targets and inspect build warnings and launcher/settings light/dark/tinted states where supported.
Never remove Release to replace an icon. Return generated assets/captures and distinguish verified appearances from unverified ones.
Done when the correct dev target references verified assets and remaining appearances are explicit.

## Follow-up and handoff

Resolve subsequent roles from the runtime root with `python3 scripts/resolve.py --entrypoint <entrypoint> --platform <assigned-platform> --step <role>`. Read the returned PROCEDURE.md; do not use internal names as Skill-tool/slash commands. Do not recurse into the current stage or add unrequested distribution, installation or commits.
Return changed files, source state/target/environment, check/screen/log paths, unverified items and shared-change proposals to the coordinator.

Official references: [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/), [SwiftUI](https://developer.apple.com/documentation/swiftui), [UIKit](https://developer.apple.com/documentation/uikit), [XCTest](https://developer.apple.com/documentation/xctest). Confirm API availability/signatures against the installed SDK and project minimum OS.
