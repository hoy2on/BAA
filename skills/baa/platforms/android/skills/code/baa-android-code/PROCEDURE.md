---
name: baa-android-code
description: Android code procedure for the assigned platform and current app workflow.
---

# Android Code

Read the [BAA execution rules](../../../../../EXECUTION.md). Inherit platform, purpose, owned files and acceptance. This internal procedure does not restart platform selection or team creation; preserve other workers' changes.

## Execution

Inspect callers, state owners, storage, navigation, Gradle dependencies and SDK support; preserve Compose/Views/other framework choices. Don't convert existing Views to Compose unrequested.
Use state-down/events-up and existing state holders/ViewModels. No DB/network writes in composable bodies; effects need appropriate keys/lifetimes/cancellation. Check installed lifecycle libraries for lifecycle-aware Flow collection; distinguish ViewModel lifetime from screen visibility and stop obsolete work.
Move CPU/blocking I/O off UI with existing dispatchers/suspend APIs. Don't add GlobalScope/unbounded scopes; distinguish cancellation from errors. For Views preserve fragment-view lifecycle, listener/adapter cleanup, RecyclerView IDs/reuse/saved state. Inspect actual AndroidView/ComposeView bridge lifetimes.
Use existing Room/SQLite/file migrations; don't hide failures with destructive migration/data reset. Use stable model IDs for selection/lists. Test affected Back/IME/insets/recreation/rotation and resolve build-and-verify/test.
Done when normal/failure/cancel/restoration behavior is implemented in the existing architecture with evidence.

## Follow-up and handoff

Resolve subsequent roles from the runtime root with `python3 scripts/resolve.py --entrypoint <entrypoint> --platform <assigned-platform> --step <role>`. Read the returned PROCEDURE.md; do not use internal names as Skill-tool/slash commands. Do not recurse into the current stage or add unrequested distribution, installation or commits.
Return changed files, source state/target/environment, check/screen/log paths, unverified items and shared-change proposals to the coordinator.

Official references: [Android UI](https://developer.android.com/design/ui/mobile), [Compose architecture](https://developer.android.com/develop/ui/compose/architecture), [Lifecycle coroutines](https://developer.android.com/topic/libraries/architecture/coroutines), [Testing](https://developer.android.com/training/testing), [Adaptive layouts](https://developer.android.com/develop/ui/compose/build-adaptive-apps). Verify APIs against actual Compose/Views and installed dependency versions.
