---
name: baa-apple-os-integrations
description: Apple mobile os integrations procedure for the assigned platform and current app workflow.
---

# Apple mobile Os Integrations

Read the [BAA execution rules](../../../../../../EXECUTION.md). Inherit platform, purpose, owned files and acceptance. This internal procedure does not restart platform selection or team creation; preserve other workers' changes.

## Execution

Confirm required APIs, entitlements, usage descriptions, extensions/targets and minimum OS from the actual project/current official docs. Do not use AppKit/Carbon/Windows APIs.
Use existing document picker/FileDocument/UIDocument and security-scoped URL lifetimes for import/export. Don't assume permanent access outside the sandbox. Route sharing, URLs/deep links, App Intents and notifications through existing navigation/storage; validate format, permissions and paths, handling duplicate events and events before UI readiness.
Request camera/microphone/photos/location permissions when needed; handle denied/restricted and Settings return. Don't grant everything or reset production permissions for testing. Handle cancellation/restoration/errors within allowed background-task/audio-session lifetimes; don't assume a resident desktop process.
For iPadOS distinguish document scenes and drag/drop/pointer/keyboard targets. One assigned owner edits shared storage. Hardware APIs need actual-device evidence, not substituted Simulator success. Record deep-link/share payload and denial reproductions/logs, then resolve test.
Done when normal/denied/cancel paths exist and actual target verification is separated from unverified items.

## Follow-up and handoff

Resolve subsequent roles from the runtime root with `python3 scripts/resolve.py --entrypoint <entrypoint> --platform <assigned-platform> --step <role>`. Read the returned PROCEDURE.md; do not use internal names as Skill-tool/slash commands. Do not recurse into the current stage or add unrequested distribution, installation or commits.
Return changed files, source state/target/environment, check/screen/log paths, unverified items and shared-change proposals to the coordinator.

Official references: [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/), [SwiftUI](https://developer.apple.com/documentation/swiftui), [UIKit](https://developer.apple.com/documentation/uikit), [XCTest](https://developer.apple.com/documentation/xctest). Confirm API availability/signatures against the installed SDK and project minimum OS.
## Supporting reference

Read [recipes.md](recipes.md) when performing this role; keep the assigned platform and scope.
