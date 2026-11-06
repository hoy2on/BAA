---
name: baa-android-app-icon
description: Android app icon procedure for the assigned platform and current app workflow.
---

# Android App Icon

Read the [BAA execution rules](../../../../../EXECUTION.md). Inherit platform, purpose, owned files and acceptance. This internal procedure does not restart platform selection or team creation; preserve other workers' changes.

## Execution

Inspect launcher resources, manifest icon/roundIcon, adaptive foreground/background/monochrome assets. Preserve product meaning/brand and reuse authorized originals/generators with Android Studio or existing supported tools.
Prepare adaptive/fallback/themed icons for actual minSdk/target/launcher requirements. Verify safe zone/mask/density on current docs/devices; don't register iOS/Mac formats. Check dev manifest/resource overlays actually reference the icon in the build and installed launcher; don't remove production apps or clear launcher data.
Verify requested light/dark/themed/mask appearances; unsupported/unperformed checks remain unverified.
Done when correct dev resources and required actual appearances are evidenced.

## Follow-up and handoff

Resolve subsequent roles from the runtime root with `python3 scripts/resolve.py --entrypoint <entrypoint> --platform <assigned-platform> --step <role>`. Read the returned PROCEDURE.md; do not use internal names as Skill-tool/slash commands. Do not recurse into the current stage or add unrequested distribution, installation or commits.
Return changed files, source state/target/environment, check/screen/log paths, unverified items and shared-change proposals to the coordinator.

Official references: [Android UI](https://developer.android.com/design/ui/mobile), [Compose architecture](https://developer.android.com/develop/ui/compose/architecture), [Lifecycle coroutines](https://developer.android.com/topic/libraries/architecture/coroutines), [Testing](https://developer.android.com/training/testing), [Adaptive layouts](https://developer.android.com/develop/ui/compose/build-adaptive-apps). Verify APIs against actual Compose/Views and installed dependency versions.
## Starter resources

The new [Android template](../../start/new-android-app/template/app/src/main/res) includes adaptive/monochrome icons for all supported API levels (minSdk 26+). Existing lower-minSdk apps retain required fallbacks. Replace with product assets and verify actual launcher appearances against [official adaptive-icon guidance](https://developer.android.com/develop/ui/compose/system/icon_design_adaptive).
