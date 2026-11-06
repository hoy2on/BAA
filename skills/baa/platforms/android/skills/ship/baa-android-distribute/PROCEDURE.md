---
name: baa-android-distribute
description: Android distribute procedure for the assigned platform and current app workflow.
---

# Android Distribute

Read the [BAA execution rules](../../../../../EXECUTION.md). Inherit platform, purpose, owned files and acceptance. This internal procedure does not restart platform selection or team creation; preserve other workers' changes.

## Execution

Apply only to explicit release/packaging/store requests, distinguishing dev install from artifact creation/publication. Inspect variant/flavor, applicationId, versionCode/versionName policy, signing, min/target SDK, manifest/permissions/privacy and ProGuard/R8. Never print keys/passwords in code/docs/logs.
Use verified existing wrapper/CI bundle/assemble release tasks, preserving shrink/obfuscation mappings/native symbols and project outputs. Inspect actual package/signature/permissions and use only already-authorized test paths. Don't remove/overwrite Release or migrate user data.
Distinguish AAB/APK generation, internal distribution, Play Console upload and track rollout. Perform only authorized stages; artifact creation is not store publication.
Done when artifacts/signing/checks, actual submissions and remaining stages are explicit.

## Follow-up and handoff

Resolve subsequent roles from the runtime root with `python3 scripts/resolve.py --entrypoint <entrypoint> --platform <assigned-platform> --step <role>`. Read the returned PROCEDURE.md; do not use internal names as Skill-tool/slash commands. Do not recurse into the current stage or add unrequested distribution, installation or commits.
Return changed files, source state/target/environment, check/screen/log paths, unverified items and shared-change proposals to the coordinator.

Official references: [Android UI](https://developer.android.com/design/ui/mobile), [Compose architecture](https://developer.android.com/develop/ui/compose/architecture), [Lifecycle coroutines](https://developer.android.com/topic/libraries/architecture/coroutines), [Testing](https://developer.android.com/training/testing), [Adaptive layouts](https://developer.android.com/develop/ui/compose/build-adaptive-apps). Verify APIs against actual Compose/Views and installed dependency versions.
