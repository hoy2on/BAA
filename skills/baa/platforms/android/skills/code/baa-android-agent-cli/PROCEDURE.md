---
name: baa-android-agent-cli
description: Android agent cli procedure for the assigned platform and current app workflow.
---

# Android Agent Cli

Read the [BAA execution rules](../../../../../EXECUTION.md). Inherit platform, purpose, owned files and acceptance. This internal procedure does not restart platform selection or team creation; preserve other workers' changes.

## Execution

Apply only to requested agent/CLI/MCP automation. Inspect existing instrumentation/UI Automator/App Link/Intent/test bridges before adding a channel. Do not turn the app into an unrestricted shell service/public endpoint; distinguish host CLI/MCP from app/instrumentation roles.
Define input schema, read/write effects, results/errors and reuse existing services/UI state. Fix adb serial and dev package; don't accept arbitrary shell commands/file paths. Verify exports, permissions and callers. Dev bridges must be absent/disabled in Release and must not bypass real authentication.
Document background/lock/termination/process limits. Preserve one data writer and existing UI updates. Verify valid/invalid/permission/cancel responses over a real connection; an absent endpoint is not an implemented integration.
Done when supported commands, trust boundaries, runtime limits and actual connection evidence exist.

## Follow-up and handoff

Resolve subsequent roles from the runtime root with `python3 scripts/resolve.py --entrypoint <entrypoint> --platform <assigned-platform> --step <role>`. Read the returned PROCEDURE.md; do not use internal names as Skill-tool/slash commands. Do not recurse into the current stage or add unrequested distribution, installation or commits.
Return changed files, source state/target/environment, check/screen/log paths, unverified items and shared-change proposals to the coordinator.

Official references: [Android UI](https://developer.android.com/design/ui/mobile), [Compose architecture](https://developer.android.com/develop/ui/compose/architecture), [Lifecycle coroutines](https://developer.android.com/topic/libraries/architecture/coroutines), [Testing](https://developer.android.com/training/testing), [Adaptive layouts](https://developer.android.com/develop/ui/compose/build-adaptive-apps). Verify APIs against actual Compose/Views and installed dependency versions.
