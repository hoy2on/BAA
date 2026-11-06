---
name: baa-apple-design-from-app
description: Apple mobile design from app procedure for the assigned platform and current app workflow.
---

# Apple mobile Design From App

Read the [BAA execution rules](../../../../../../EXECUTION.md). Inherit platform, purpose, owned files and acceptance. This internal procedure does not restart platform selection or team creation; preserve other workers' changes.

## Execution

Identify reference device, resolution, pixel scale, OS, text/theme/state. Don't simply resize desktop-window captures into iPhone/iPad designs.
Use clone to confirm flows and map information order, navigation and shared components. Separate requested reproduction from authorization to use branding/logos/proprietary assets.
Measure using actual image metadata/device scale; don't assume pixels/2, and distinguish pixel/point coordinates. Express intent through native-design system controls first, using design-kit only for needed custom components and existing tokens for spacing/type/color.
Capture identical data/viewport/scale/theme and compare structure, typography, space, then color. Don't misclassify another OS's rendering/state as a pixel defect. Use available diff tools only as supporting evidence and verify visible differences/interactions directly. Record unresolved differences; don't retry without changed input/evidence.
Done when reproduction scope, changed tokens/components, comparable before/after screens and remaining differences are recorded.

## Follow-up and handoff

Resolve subsequent roles from the runtime root with `python3 scripts/resolve.py --entrypoint <entrypoint> --platform <assigned-platform> --step <role>`. Read the returned PROCEDURE.md; do not use internal names as Skill-tool/slash commands. Do not recurse into the current stage or add unrequested distribution, installation or commits.
Return changed files, source state/target/environment, check/screen/log paths, unverified items and shared-change proposals to the coordinator.

Official references: [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/), [SwiftUI](https://developer.apple.com/documentation/swiftui), [UIKit](https://developer.apple.com/documentation/uikit), [XCTest](https://developer.apple.com/documentation/xctest). Confirm API availability/signatures against the installed SDK and project minimum OS.
## Supporting reference

Read [measuring.md](measuring.md) when performing this role; keep the assigned platform and scope.
