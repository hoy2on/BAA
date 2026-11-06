---
name: baa-android-test
description: Android test procedure for the assigned platform and current app workflow.
---

# Android Test

Read the [BAA execution rules](../../../../../EXECUTION.md). Inherit platform, purpose, owned files and acceptance. This internal procedure does not restart platform selection or team creation; preserve other workers' changes.

## Execution

Read [runtime verification](../../../verification.md) for project-specific commands and evidence.

Select existing unit/instrumentation targets for changed logic, persistence/migration, UI, permission and hardware boundaries. Use installed JUnit/MockK/etc.; coroutine tests reuse test dispatchers/virtual time rather than sleeps hiding async bugs.
Compose uses semantics/stable tags/labels; Views use current Espresso/UI Automator tooling. Verify affected input/results, navigation/IME/Back, rotation/recreation/restoration. Use existing fixtures and isolated dev stores, never resetting production DB/account data. Reinstalling isn't the default reset.
Respect actual system-UI/permission automation capabilities; detection failures aren't automatically product defects. Separate camera/audio/notification hardware checks. Run verified tasks for actual serial/variant, returning junit/XML/logcat/screens/source. Don't run manual and UI automation concurrently on one device.
Done when normal/failure/cancel/restore boundaries are checked at appropriate levels, with environment failures/unverified work distinct.

## Follow-up and handoff

Resolve subsequent roles from the runtime root with `python3 scripts/resolve.py --entrypoint <entrypoint> --platform <assigned-platform> --step <role>`. Read the returned PROCEDURE.md; do not use internal names as Skill-tool/slash commands. Do not recurse into the current stage or add unrequested distribution, installation or commits.
Return changed files, source state/target/environment, check/screen/log paths, unverified items and shared-change proposals to the coordinator.

Official references: [Android UI](https://developer.android.com/design/ui/mobile), [Compose architecture](https://developer.android.com/develop/ui/compose/architecture), [Lifecycle coroutines](https://developer.android.com/topic/libraries/architecture/coroutines), [Testing](https://developer.android.com/training/testing), [Adaptive layouts](https://developer.android.com/develop/ui/compose/build-adaptive-apps). Verify APIs against actual Compose/Views and installed dependency versions.
## Starter targets

The new [Android template](../../start/new-android-app/template) includes unit/Compose UI tests. Debug UI tests use notes-ui-tests storage, not ordinary dev notes; Release ignores the test flag. Actual device test results are separate from APK compilation.
