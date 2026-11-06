---
name: baa-android-layout-grid
description: Android layout grid procedure for the assigned platform and current app workflow.
---

# Android Layout Grid

Read the [BAA execution rules](../../../../../EXECUTION.md). Inherit platform, purpose, owned files and acceptance. This internal procedure does not restart platform selection or team creation; preserve other workers' changes.

## Execution

Inspect existing dp spacing/sp type, parent constraints and actual window/insets. Do not copy Mac points or Windows epx values. Align leading/trailing/baselines/group spacing through existing tokens.
Check Compose constraints/weight/intrinsics and Views constraint conflicts before compensating with repeated padding. Verify SDK-specific IME/system bars/cutouts/edge-to-edge, clipped targets and conflicting nested scrolling.
Check wrapping/layout with font scale, long translations, RTL and light/dark. For supported large-screen/foldable layouts verify resizing/panes/hinge effects. Reuse screenshot/layout tools and UI hierarchy/logs; don't invent a global probe system merely because no JSON layout probe exists.
Fix affected tokens/constraints and adjacent regressions.
Done when comparable runtime evidence covers the correction and relevant window/text states.

## Follow-up and handoff

Resolve subsequent roles from the runtime root with `python3 scripts/resolve.py --entrypoint <entrypoint> --platform <assigned-platform> --step <role>`. Read the returned PROCEDURE.md; do not use internal names as Skill-tool/slash commands. Do not recurse into the current stage or add unrequested distribution, installation or commits.
Return changed files, source state/target/environment, check/screen/log paths, unverified items and shared-change proposals to the coordinator.

Official references: [Android UI](https://developer.android.com/design/ui/mobile), [Compose architecture](https://developer.android.com/develop/ui/compose/architecture), [Lifecycle coroutines](https://developer.android.com/topic/libraries/architecture/coroutines), [Testing](https://developer.android.com/training/testing), [Adaptive layouts](https://developer.android.com/develop/ui/compose/build-adaptive-apps). Verify APIs against actual Compose/Views and installed dependency versions.
