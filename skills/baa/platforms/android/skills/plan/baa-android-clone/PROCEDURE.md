---
name: baa-android-clone
description: Android clone procedure for the assigned platform and current app workflow.
---

# Android Clone

Read the [BAA execution rules](../../../../../EXECUTION.md). Inherit platform, purpose, owned files and acceptance. This internal procedure does not restart platform selection or team creation; preserve other workers' changes.

## Execution

Define reference app/version/OS/flow and requested phone/tablet scope. Confirm actual serial/resolution/density through adb devices -l and device inspection.
Use existing UI Automator/Espresso/Compose or available interaction tools for screens/input/Back/sheets/dialogs/denied/error states. Don't read private storage or bypass authentication.
Prepare captures of only the target app: `adb -s <serial> exec-out screencap -p > <file>` captures the display, so verify foreground app and sensitive overlays first. Captures do not replace interaction.
Attach device/orientation/pixels/density/font scale/theme; distinguish dp/pixels and IME/system bars from content. Record entry/exit/Back/state changes and return the assigned platform section. Resolve user-stories next.
Done when required screens/behavior/environment and unknowns are recorded.

## Follow-up and handoff

Resolve subsequent roles from the runtime root with `python3 scripts/resolve.py --entrypoint <entrypoint> --platform <assigned-platform> --step <role>`. Read the returned PROCEDURE.md; do not use internal names as Skill-tool/slash commands. Do not recurse into the current stage or add unrequested distribution, installation or commits.
Return changed files, source state/target/environment, check/screen/log paths, unverified items and shared-change proposals to the coordinator.

Official references: [Android UI](https://developer.android.com/design/ui/mobile), [Compose architecture](https://developer.android.com/develop/ui/compose/architecture), [Lifecycle coroutines](https://developer.android.com/topic/libraries/architecture/coroutines), [Testing](https://developer.android.com/training/testing), [Adaptive layouts](https://developer.android.com/develop/ui/compose/build-adaptive-apps). Verify APIs against actual Compose/Views and installed dependency versions.
