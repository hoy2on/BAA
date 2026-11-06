---
name: baa-apple-layout-grid
description: Apple mobile layout grid procedure for the assigned platform and current app workflow.
---

# Apple mobile Layout Grid

Read the [BAA execution rules](../../../../../../EXECUTION.md). Inherit platform, purpose, owned files and acceptance. This internal procedure does not restart platform selection or team creation; preserve other workers' changes.

## Execution

Read safe area, container, existing spacing/type and actual screen size. Don't impose Mac 4pt grids or fixed desktop margins on mobile.
Align baselines, leading/trailing, related/group spacing to existing tokens. Inspect SwiftUI priority/alignment and UIKit constraint conflicts before hiding issues with numeric offsets. Preserve intrinsic/system sizing; check wrapping/truncation/hit areas under Dynamic Type and long translations.
For iOS verify keyboard/home-indicator/orientation space changes; for iPadOS check narrow/wide windows, split navigation, popover anchors and column boundaries. Reuse existing snapshots/layout probes; otherwise use runtime captures and hierarchy/constraint logs, not a new global grid system.
Fix alignment/spacing at token usage and check adjacent screens.
Done when before/after and relevant size/text states verify the requested alignment correction.

## Follow-up and handoff

Resolve subsequent roles from the runtime root with `python3 scripts/resolve.py --entrypoint <entrypoint> --platform <assigned-platform> --step <role>`. Read the returned PROCEDURE.md; do not use internal names as Skill-tool/slash commands. Do not recurse into the current stage or add unrequested distribution, installation or commits.
Return changed files, source state/target/environment, check/screen/log paths, unverified items and shared-change proposals to the coordinator.

Official references: [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/), [SwiftUI](https://developer.apple.com/documentation/swiftui), [UIKit](https://developer.apple.com/documentation/uikit), [XCTest](https://developer.apple.com/documentation/xctest). Confirm API availability/signatures against the installed SDK and project minimum OS.
