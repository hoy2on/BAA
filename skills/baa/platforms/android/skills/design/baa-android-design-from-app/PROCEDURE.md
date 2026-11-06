---
name: baa-android-design-from-app
description: Android design from app procedure for the assigned platform and current app workflow.
---

# Android Design From App

Read the [BAA execution rules](../../../../../EXECUTION.md). Inherit platform, purpose, owned files and acceptance. This internal procedure does not restart platform selection or team creation; preserve other workers' changes.

## Execution

Identify reference app/OS/device/pixels/density/font scale/theme/state and map the current user flow. Pixels are not dp. Match viewport/density/IME/system bars and compare information order/navigation/components first.
Keep Android native-design conventions and existing Material/app controls and design-system tokens; don't import another platform's title bars/popovers/hover assumptions. Use design-kit for needed custom components and finish one relevant screen first. Separate logo/proprietary-asset authorization from reproduction scope.
Capture identical data/theme/size and compare structure, typography, spacing/alignment, then color. Pixel diffs are supporting evidence only with matched rendering/scale/state. Record resolved/remaining differences and verify behavior through test.
Done when scope, changed components/tokens, before/after and unresolved differences are connected.

## Follow-up and handoff

Resolve subsequent roles from the runtime root with `python3 scripts/resolve.py --entrypoint <entrypoint> --platform <assigned-platform> --step <role>`. Read the returned PROCEDURE.md; do not use internal names as Skill-tool/slash commands. Do not recurse into the current stage or add unrequested distribution, installation or commits.
Return changed files, source state/target/environment, check/screen/log paths, unverified items and shared-change proposals to the coordinator.

Official references: [Android UI](https://developer.android.com/design/ui/mobile), [Compose architecture](https://developer.android.com/develop/ui/compose/architecture), [Lifecycle coroutines](https://developer.android.com/topic/libraries/architecture/coroutines), [Testing](https://developer.android.com/training/testing), [Adaptive layouts](https://developer.android.com/develop/ui/compose/build-adaptive-apps). Verify APIs against actual Compose/Views and installed dependency versions.
## Supporting reference

Read [measuring.md](measuring.md) when performing this role; keep the assigned platform and scope.
