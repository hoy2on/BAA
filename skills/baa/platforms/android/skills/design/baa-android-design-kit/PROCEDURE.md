---
name: baa-android-design-kit
description: Android design kit procedure for the assigned platform and current app workflow.
---

# Android Design Kit

Read the [BAA execution rules](../../../../../EXECUTION.md). Inherit platform, purpose, owned files and acceptance. This internal procedure does not restart platform selection or team creation; preserve other workers' changes.

## Execution

Check existing Material/composable/custom View components before custom work. Define state/events, enabled/selected/pressed/focused/loading/error and semantics. Don't make small components new owners of business state.
Preserve existing Compose modifiers/theme/interaction sources and meaningful Button semantics, rather than clickable Boxes. For Views retain styles/state lists/focus/click patterns. Use design-system semantic colors/type/shapes/spacing with font scaling, touch, keyboard and TalkBack actions.
Add relevant states to existing previews/samples/test hosts and connect the real screen; don't build a separate gallery/framework for one component. Check dark/long text/narrow-wide supported windows and disabled/selected/error states.
Done when the actual component and state/accessibility/interaction evidence are present.

## Follow-up and handoff

Resolve subsequent roles from the runtime root with `python3 scripts/resolve.py --entrypoint <entrypoint> --platform <assigned-platform> --step <role>`. Read the returned PROCEDURE.md; do not use internal names as Skill-tool/slash commands. Do not recurse into the current stage or add unrequested distribution, installation or commits.
Return changed files, source state/target/environment, check/screen/log paths, unverified items and shared-change proposals to the coordinator.

Official references: [Android UI](https://developer.android.com/design/ui/mobile), [Compose architecture](https://developer.android.com/develop/ui/compose/architecture), [Lifecycle coroutines](https://developer.android.com/topic/libraries/architecture/coroutines), [Testing](https://developer.android.com/training/testing), [Adaptive layouts](https://developer.android.com/develop/ui/compose/build-adaptive-apps). Verify APIs against actual Compose/Views and installed dependency versions.
