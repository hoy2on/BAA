---
name: baa-apple-clone
description: Apple mobile clone procedure for the assigned platform and current app workflow.
---

# Apple mobile Clone

Read the [BAA execution rules](../../../../../../EXECUTION.md). Inherit platform, purpose, owned files and acceptance. This internal procedure does not restart platform selection or team creation; preserve other workers' changes.

## Execution

Define the reference app, screens and flow; record assigned iOS/iPadOS device/OS/app version. Verify Simulator/hardware and app access without reading other apps' private containers/data.
Use existing UI tests or available interaction tools to inspect default/edit/sheet/popover/settings/error/empty states. Capture only the target app. `xcrun simctl io <udid> screenshot <file>` captures but does not tap/scroll; use a UI tool for interaction.
Record iOS Back/tabs/keyboard and supported iPad column/narrow-window/pointer interactions. Include image paths, device/size/scale, entry/exit, observed/unverified states in the screen index.
Return the assigned platform section rather than concurrently editing a shared index. Resolve user-stories next.
Done when requested flows have images/observations or explicit access limitations.

## Follow-up and handoff

Resolve subsequent roles from the runtime root with `python3 scripts/resolve.py --entrypoint <entrypoint> --platform <assigned-platform> --step <role>`. Read the returned PROCEDURE.md; do not use internal names as Skill-tool/slash commands. Do not recurse into the current stage or add unrequested distribution, installation or commits.
Return changed files, source state/target/environment, check/screen/log paths, unverified items and shared-change proposals to the coordinator.

Official references: [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/), [SwiftUI](https://developer.apple.com/documentation/swiftui), [UIKit](https://developer.apple.com/documentation/uikit), [XCTest](https://developer.apple.com/documentation/xctest). Confirm API availability/signatures against the installed SDK and project minimum OS.
