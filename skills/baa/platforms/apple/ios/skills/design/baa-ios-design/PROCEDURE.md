---
name: baa-ios-design
description: BAA iOS native design specialist for the assigned screen, existing architecture and actual tools.
---

# iOS native design

Read the [BAA execution rules](../../../../../../EXECUTION.md). Inherit target, purpose, ownership and acceptance without restarting platform selection/team creation. Preserve others' changes.

## Execution

Inspect existing iPhone navigation/view hierarchy, screen purpose/state and main action. Preserve out-of-scope navigation for an existing screen. Retain the app's tabs for primary destinations, stacks for hierarchy and sheets for independent tasks. Preserve system Back and cancellation, checking unsaved input on dismissal.
Keep fields/actions visible with safe areas/keyboard; use actual containers, not fixed UIScreen dimensions. Reuse system controls/tokens and verify visual bounds versus hit areas and icon-only names. Essential functions must not require desktop hover/menus.
Check affected Dynamic Type, VoiceOver order/actions, contrast, Reduce Motion, long translations and RTL; don't communicate state only by color. Run light/dark, small supported iPhone, large text, visible keyboard and empty/loading/error states. Don't raise minimum OS for a material effect.
Resolve design-system/design-kit/layout-grid/app-icon for more design and code/build-and-verify/test for implementation/proof.
Done when requested structure/copy/input meet purpose/acceptance with actual iPhone evidence and remaining checks.

## Follow-up and handoff

Resolve exact role paths from the runtime root with `python3 scripts/resolve.py --entrypoint <entrypoint> --platform ios --step <role>`. Read the returned PROCEDURE.md, not internal Skill-tool/slash commands. Do not recurse into the current stage or add unrequested distribution/installation/commits. Return files/source/target/environment/checks/screens/logs/unverified scope and shared proposals.

Official references: [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/), [SwiftUI](https://developer.apple.com/documentation/swiftui), [UIKit](https://developer.apple.com/documentation/uikit), [XCTest](https://developer.apple.com/documentation/xctest). Confirm API availability/signatures against the installed SDK and project minimum OS.
