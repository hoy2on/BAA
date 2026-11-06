---
name: baa-apple-code
description: Apple mobile code procedure for the assigned platform and current app workflow.
---

# Apple mobile Code

Read the [BAA execution rules](../../../../../../EXECUTION.md). Inherit platform, purpose, owned files and acceptance. This internal procedure does not restart platform selection or team creation; preserve other workers' changes.

## Execution

Inspect callers, models, storage, screens/tests and actual Swift language/SDK/minimum OS. Do not impose new syntax or observation systems across an existing app.
Preserve SwiftUI state ownership, distinguishing owned state from incoming values/Binding. Use stable model IDs; do not start I/O/data mutations in body. Update UI under the existing main-actor rules, move heavy computation/files off the UI path and reuse actors/async APIs. Check Task cancellation, view lifetime and error delivery; don't add unchecked Sendable just to suppress warnings.
For UIKit preserve controller/view lifecycles, reuse and delegates. For bridges check UIViewRepresentable/UIViewControllerRepresentable update/teardown and Coordinator ownership. Do not import AppKit types into iOS code.
Use existing persistence migrations and preserve files/data. Don't bind selection to array indexes that change after deletion/sorting. Preserve iOS push/pop, sheet dismissal, keyboard/safe-area behavior and iPadOS selection/editing across columns, scenes and resizing.
Implement the smallest working change and check affected unit/UI edge cases. Resolve build-and-verify/test for proof, native-design for appearance and os-integrations for OS APIs.
Done when requested behavior/compatibility is implemented with linked evidence and failures/unverified scope.

## Follow-up and handoff

Resolve subsequent roles from the runtime root with `python3 scripts/resolve.py --entrypoint <entrypoint> --platform <assigned-platform> --step <role>`. Read the returned PROCEDURE.md; do not use internal names as Skill-tool/slash commands. Do not recurse into the current stage or add unrequested distribution, installation or commits.
Return changed files, source state/target/environment, check/screen/log paths, unverified items and shared-change proposals to the coordinator.

Official references: [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/), [SwiftUI](https://developer.apple.com/documentation/swiftui), [UIKit](https://developer.apple.com/documentation/uikit), [XCTest](https://developer.apple.com/documentation/xctest). Confirm API availability/signatures against the installed SDK and project minimum OS.
