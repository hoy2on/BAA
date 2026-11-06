---
name: baa-android-design-system
description: Android design system procedure for the assigned platform and current app workflow.
---

# Android Design System

Read the [BAA execution rules](../../../../../EXECUTION.md). Inherit platform, purpose, owned files and acceptance. This internal procedure does not restart platform selection or team creation; preserve other workers' changes.

## Execution

Read existing Material/Compose theme, XML resources/styles, type/spacing/shape/motion and app components. Consolidate only identical meaning, not a speculative theme layer.
Use semantic colors/light-dark resources. Follow actual ColorScheme or Views attributes, not Swift Palette/XAML names. Use sp and existing typography; check scale/weight/fallback/long translations/RTL. Reuse dp spacing/shape tokens.
Share brand/status meaning while respecting Android native sizing/dynamic color/system-bar policies. Check text over custom fills and disabled/pressed contrast. Replace only affected usages under shared-resource ownership, recording meaning/exceptions in one existing document rather than rewriting the whole system.
Verify light/dark/font scale/relevant window sizes through build-and-verify.
Done when actual screens use existing tokens with color/type/accessibility evidence.

## Follow-up and handoff

Resolve subsequent roles from the runtime root with `python3 scripts/resolve.py --entrypoint <entrypoint> --platform <assigned-platform> --step <role>`. Read the returned PROCEDURE.md; do not use internal names as Skill-tool/slash commands. Do not recurse into the current stage or add unrequested distribution, installation or commits.
Return changed files, source state/target/environment, check/screen/log paths, unverified items and shared-change proposals to the coordinator.

Official references: [Android UI](https://developer.android.com/design/ui/mobile), [Compose architecture](https://developer.android.com/develop/ui/compose/architecture), [Lifecycle coroutines](https://developer.android.com/topic/libraries/architecture/coroutines), [Testing](https://developer.android.com/training/testing), [Adaptive layouts](https://developer.android.com/develop/ui/compose/build-adaptive-apps). Verify APIs against actual Compose/Views and installed dependency versions.
