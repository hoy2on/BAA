---
name: baa-apple-design-kit
description: Apple mobile design kit procedure for the assigned platform and current app workflow.
---

# Apple mobile Design Kit

Read the [BAA execution rules](../../../../../../EXECUTION.md). Inherit platform, purpose, owned files and acceptance. This internal procedure does not restart platform selection or team creation; preserve other workers' changes.

## Execution

Check existing Button/List/Form/Menu/Picker and app components before custom work. Implement only genuinely needed visual components.
Define inputs, owned state, events and normal/pressed/selected/disabled/focused/loading/error states. Don't give a small visual component a new business-model owner. Reuse SwiftUI ButtonStyle/ToggleStyle/View or existing UIKit control/subclass patterns; replacing buttons with shapes/tap gestures must not lose native keyboard/accessibility semantics.
Use design-system tokens and supported tap/pointer/keyboard paths with VoiceOver label/value/action. Check iOS touch/Dynamic Type and iPad pointer/focus/resizing; don't hide essential iPad actions behind hover.
Add relevant states to an existing preview/gallery/test host, not a new standalone gallery/app for one component. Connect to the actual screen and use build-and-verify/test.
Done when requested components/states are in real UI with basic interaction/accessibility preserved.

## Follow-up and handoff

Resolve subsequent roles from the runtime root with `python3 scripts/resolve.py --entrypoint <entrypoint> --platform <assigned-platform> --step <role>`. Read the returned PROCEDURE.md; do not use internal names as Skill-tool/slash commands. Do not recurse into the current stage or add unrequested distribution, installation or commits.
Return changed files, source state/target/environment, check/screen/log paths, unverified items and shared-change proposals to the coordinator.

Official references: [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/), [SwiftUI](https://developer.apple.com/documentation/swiftui), [UIKit](https://developer.apple.com/documentation/uikit), [XCTest](https://developer.apple.com/documentation/xctest). Confirm API availability/signatures against the installed SDK and project minimum OS.
