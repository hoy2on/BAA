---
name: baa-android-native-design
description: Android native design procedure for the assigned platform and current app workflow.
---

# Android Native Design

Read the [BAA execution rules](../../../../../EXECUTION.md). Inherit platform, purpose, owned files and acceptance. This internal procedure does not restart platform selection or team creation; preserve other workers' changes.

## Execution

Inspect screen purpose, existing navigation, Material version/theme and supported windows. Prefer current app/system components. Distinguish primary destinations from subnavigation; preserve bar/rail/drawer/app-bar conventions.
Follow installed SDK/navigation rules for system/predictive Back; don't hide essential actions in hover. Verify actual targetSdk/window edge-to-edge, system bars, cutouts and IME insets, not fixed physical pixels with padding patches.
Use existing sp/dp/type/semantic colors and dynamic-color policy; don't add a theme engine/color setting for a screen change. Check font scale, TalkBack reading order/semantics, hit areas, contrast and relevant reduced-motion/animation settings. Color alone must not convey selected/error states.
For supported phone/tablet/foldable/desktop use actual window bounds for navigation/list-detail, not device names alone. Run changed screens with light/dark, long copy, large text and required windows; resolve layout-grid/build-and-verify/test.
Done when native Android/project conventions and real screen/input evidence match the task.

## Follow-up and handoff

Resolve subsequent roles from the runtime root with `python3 scripts/resolve.py --entrypoint <entrypoint> --platform <assigned-platform> --step <role>`. Read the returned PROCEDURE.md; do not use internal names as Skill-tool/slash commands. Do not recurse into the current stage or add unrequested distribution, installation or commits.
Return changed files, source state/target/environment, check/screen/log paths, unverified items and shared-change proposals to the coordinator.

Official references: [Android UI](https://developer.android.com/design/ui/mobile), [Compose architecture](https://developer.android.com/develop/ui/compose/architecture), [Lifecycle coroutines](https://developer.android.com/topic/libraries/architecture/coroutines), [Testing](https://developer.android.com/training/testing), [Adaptive layouts](https://developer.android.com/develop/ui/compose/build-adaptive-apps). Verify APIs against actual Compose/Views and installed dependency versions.
