---
name: baa-apple-agent-cli
description: Apple mobile agent cli procedure for the assigned platform and current app workflow.
---

# Apple mobile Agent Cli

Read the [BAA execution rules](../../../../../../EXECUTION.md). Inherit platform, purpose, owned files and acceptance. This internal procedure does not restart platform selection or team creation; preserve other workers' changes.

## Execution

Apply only to requested app automation/agent control. Inspect existing App Intents, URL routes, UI-test bridges and test entrypoints.
Do not assume iOS/iPadOS can host an always-running desktop CLI/MCP/socket daemon. Prefer App Intents/Shortcuts for OS automation and existing XCUITest for tests.
Define input schema, permissions, read/write effects and completion/error responses; reuse services instead of duplicating UI/data writers. Validate external URL/payload authentication, format, size and allowed commands. Do not expose arbitrary paths/code execution; verify a dev-only bridge is disabled in Release.
If a host CLI/MCP is needed, distinguish authorized host device/Xcode/test tools from the mobile app. Do not claim connectivity without a control channel. Verify foreground/background/locked/terminated limits, single-writer data and scene updates.
Done when supported commands/limits and real valid/invalid/permission/error responses are verified.

## Follow-up and handoff

Resolve subsequent roles from the runtime root with `python3 scripts/resolve.py --entrypoint <entrypoint> --platform <assigned-platform> --step <role>`. Read the returned PROCEDURE.md; do not use internal names as Skill-tool/slash commands. Do not recurse into the current stage or add unrequested distribution, installation or commits.
Return changed files, source state/target/environment, check/screen/log paths, unverified items and shared-change proposals to the coordinator.

Official references: [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/), [SwiftUI](https://developer.apple.com/documentation/swiftui), [UIKit](https://developer.apple.com/documentation/uikit), [XCTest](https://developer.apple.com/documentation/xctest). Confirm API availability/signatures against the installed SDK and project minimum OS.
