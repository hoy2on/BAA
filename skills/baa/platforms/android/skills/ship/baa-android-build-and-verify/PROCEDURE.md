---
name: baa-android-build-and-verify
description: Android build and verify procedure for the assigned platform and current app workflow.
---

# Android Build And Verify

Read the [BAA execution rules](../../../../../EXECUTION.md). Inherit platform, purpose, owned files and acceptance. This internal procedure does not restart platform selection or team creation; preserve other workers' changes.

## Execution

Read [runtime verification](../../../verification.md) for project-specific commands and evidence.

Inspect project instructions, wrapper and actual task list for modules/dev types/flavors/compile-test-lint tasks. Don't assume app/debug. Reuse scripts/repository wrapper; preserve logs and the first failure, without bypassing it through SDK installs/version upgrades.
Confirm serial/OS/emulator versus hardware. Select the requested device when several exist and use -s <serial> per adb command. Inspect actual APK ID/signing/variant, installing only a separate dev ID through the existing flow such as adb install -r. Don't uninstall Release for signature conflicts.
Verify the actual dev launcher, crash/logcat/screens, changed input/Back/IME/save flows and supported size/theme/font scale. Check foreground/private overlays before captures. Don't concurrently replace/terminate the same device/output/dev app.
Use existing test flows; build-only success is not runtime success.
Done when source/variant/package/device/commands/logs/screens and unverified items are recorded.

## Follow-up and handoff

Resolve subsequent roles from the runtime root with `python3 scripts/resolve.py --entrypoint <entrypoint> --platform <assigned-platform> --step <role>`. Read the returned PROCEDURE.md; do not use internal names as Skill-tool/slash commands. Do not recurse into the current stage or add unrequested distribution, installation or commits.
Return changed files, source state/target/environment, check/screen/log paths, unverified items and shared-change proposals to the coordinator.

Official references: [Android UI](https://developer.android.com/design/ui/mobile), [Compose architecture](https://developer.android.com/develop/ui/compose/architecture), [Lifecycle coroutines](https://developer.android.com/topic/libraries/architecture/coroutines), [Testing](https://developer.android.com/training/testing), [Adaptive layouts](https://developer.android.com/develop/ui/compose/build-adaptive-apps). Verify APIs against actual Compose/Views and installed dependency versions.
## Supporting reference

Read [existing-app.md](existing-app.md) when performing this role; keep the assigned platform and scope.
