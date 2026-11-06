---
name: baa-ipados-design
description: BAA iPadOS native design specialist for the assigned screen, existing architecture and actual tools.
---

# iPadOS native design

Read the [BAA execution rules](../../../../../../EXECUTION.md). Inherit target, purpose, ownership and acceptance without restarting platform selection/team creation. Preserve others' changes.

## Execution

Inspect real iPad targets/device families/scenes/navigation and boundaries between shared iPhone code and iPad screens. An iPad is not simply a larger phone.
Use established split/list-detail/sidebar patterns where space permits, preserving selection/editing when columns collapse. Use traits/current container width, not device models, to decide columns. Check columns/toolbars/inspectors/main actions through rotation/resizing/multitasking using APIs available on the existing minimum OS.
Anchor popovers to actual sources; verify compact adaptations/cancellation/input preservation without applying phone full-screen behavior everywhere. Add touch/Pencil-specific features only when required. Preserve supported pointer/hardware-keyboard focus/shortcuts, drag/drop and context menus, while keeping essential functions reachable by touch.
Verify Dynamic Type, VoiceOver, contrast, Reduce Motion and long copy. For existing multiple scenes distinguish selection/document state/restoration without duplicating shared storage. Use actual iPad narrow/wide/orientation/input/sheet/popover results, not iPhone snapshots.
Resolve design-system/design-kit/layout-grid, then code/build-and-verify/test.
Done when state/navigation/accessibility remain correct under actual iPad size changes/input with evidence.

## Follow-up and handoff

Resolve exact role paths from the runtime root with `python3 scripts/resolve.py --entrypoint <entrypoint> --platform ipados --step <role>`. Read the returned PROCEDURE.md, not internal Skill-tool/slash commands. Do not recurse into the current stage or add unrequested distribution/installation/commits. Return files/source/target/environment/checks/screens/logs/unverified scope and shared proposals.

Official references: [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/), [SwiftUI](https://developer.apple.com/documentation/swiftui), [UIKit](https://developer.apple.com/documentation/uikit), [XCTest](https://developer.apple.com/documentation/xctest). Confirm API availability/signatures against the installed SDK and project minimum OS.
