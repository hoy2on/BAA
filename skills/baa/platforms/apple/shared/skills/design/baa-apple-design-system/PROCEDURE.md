---
name: baa-apple-design-system
description: Apple mobile design system procedure for the assigned platform and current app workflow.
---

# Apple mobile Design System

Read the [BAA execution rules](../../../../../../EXECUTION.md). Inherit platform, purpose, owned files and acceptance. This internal procedure does not restart platform selection or team creation; preserve other workers' changes.

## Execution

Inspect existing color assets, fonts, spacing/radius/motion, ButtonStyle and UIKit appearance. A screen change alone doesn't justify a new Theme layer or accent picker.
Consolidate only semantically identical values. Share brand/status meaning, not identical mobile/Mac type/control dimensions. Use semantic Color/UIColor and existing light/dark assets; check text contrast, Increase Contrast and non-color state cues. Don't assume white text reads on every accent.
Prefer system text styles/Dynamic Type. Preserve existing custom fonts with scaled sizing/Bold Text behavior. Check current assets, SF Symbols availability and language direction. Use existing motion duration/Reduce Motion; don't raise minimum OS for an effect.
Record changed token usage/exceptions in one existing document and update affected screens first. Share iPad tokens while handling density/container width in layout. Verify selected iOS/iPadOS screens in light/dark and changed text sizes through build-and-verify.
Done when actual UI uses the existing tokens with theme/accessibility evidence.

## Follow-up and handoff

Resolve subsequent roles from the runtime root with `python3 scripts/resolve.py --entrypoint <entrypoint> --platform <assigned-platform> --step <role>`. Read the returned PROCEDURE.md; do not use internal names as Skill-tool/slash commands. Do not recurse into the current stage or add unrequested distribution, installation or commits.
Return changed files, source state/target/environment, check/screen/log paths, unverified items and shared-change proposals to the coordinator.

Official references: [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/), [SwiftUI](https://developer.apple.com/documentation/swiftui), [UIKit](https://developer.apple.com/documentation/uikit), [XCTest](https://developer.apple.com/documentation/xctest). Confirm API availability/signatures against the installed SDK and project minimum OS.
