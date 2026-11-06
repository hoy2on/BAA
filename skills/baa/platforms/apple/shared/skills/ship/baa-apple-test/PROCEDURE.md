---
name: baa-apple-test
description: Apple mobile test procedure for the assigned platform and current app workflow.
---

# Apple mobile Test

Read the [BAA execution rules](../../../../../../EXECUTION.md). Inherit platform, purpose, owned files and acceptance. This internal procedure does not restart platform selection or team creation; preserve other workers' changes.

## Execution

Read [runtime verification](../../../verification.md) for project-specific commands and evidence.

Choose unit/integration/UI/hardware boundaries from requirements/changes. Reuse existing Swift Testing/XCTest/XCUITest, not a new test framework by habit.
Use small fixtures for pure logic/storage/failure/cancellation; verify migrations with prior-store fixtures, never user stores. XCUITest uses accessible identifiers/meaningful labels and actual state waits, not fixed sleeps, to test input/tap/results/relaunch. Separate animation/permission environment failures from defects.
Use existing dev configuration and isolated data/launch arguments. Test-only runtime paths must not expose production APIs or unattended authentication bypasses. Cover affected iOS cancel/Back/keyboard/sizes and iPad narrow/wide/split navigation/input/scene restoration.
Don't run UI automation and manual control on one destination concurrently. Identify camera/microphone/background/permission checks requiring real hardware. Return commands/xcresult/logs/screens/source and reuse valid build-and-verify evidence.
Done when changed failure boundaries/flows have appropriate checks and environment failures/unverified items are distinct.

## Follow-up and handoff

Resolve subsequent roles from the runtime root with `python3 scripts/resolve.py --entrypoint <entrypoint> --platform <assigned-platform> --step <role>`. Read the returned PROCEDURE.md; do not use internal names as Skill-tool/slash commands. Do not recurse into the current stage or add unrequested distribution, installation or commits.
Return changed files, source state/target/environment, check/screen/log paths, unverified items and shared-change proposals to the coordinator.

Official references: [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/), [SwiftUI](https://developer.apple.com/documentation/swiftui), [UIKit](https://developer.apple.com/documentation/uikit), [XCTest](https://developer.apple.com/documentation/xctest). Confirm API availability/signatures against the installed SDK and project minimum OS.
## Starter targets

The shared [Apple template](../../start/new-apple-app/template) includes unit/UI targets and a shared scheme. Debug UI tests use a separate defaults domain, never resetting ordinary dev storage. build-for-testing compiles; test executes. Existing apps reuse existing tests rather than blindly copying targets.
