---
name: baa-android-os-integrations
description: Android os integrations procedure for the assigned platform and current app workflow.
---

# Android Os Integrations

Read the [BAA execution rules](../../../../../EXECUTION.md). Inherit platform, purpose, owned files and acceptance. This internal procedure does not restart platform selection or team creation; preserve other workers' changes.

## Execution

Inspect manifest, runtime permissions, exported components/intent filters, targetSdk and OS differences for the requested feature. Use existing Activity Result/Storage Access Framework/MediaStore and URI-permission lifetimes; a content URI is not a permanent filesystem path.
Route sharing/deep links/App Links/notifications/foreground services/background work through existing routes/storage services. Validate extras, URI, MIME, path and size; external input must not open arbitrary components/files.
Request permissions when needed; handle denial, don't-ask-again, Settings return and relaunch. Don't grant everything, pm clear or uninstall Release for testing convenience. Use existing WorkManager/service/Activity lifecycles and OS limits, not desktop-daemon or iOS background assumptions.
On the selected device verify affected normal/cancel/denied/external/background paths; preserve hardware evidence for hardware APIs.
Done when permission/lifecycle/trust/failure boundaries are implemented and verification scope is stated.

## Follow-up and handoff

Resolve subsequent roles from the runtime root with `python3 scripts/resolve.py --entrypoint <entrypoint> --platform <assigned-platform> --step <role>`. Read the returned PROCEDURE.md; do not use internal names as Skill-tool/slash commands. Do not recurse into the current stage or add unrequested distribution, installation or commits.
Return changed files, source state/target/environment, check/screen/log paths, unverified items and shared-change proposals to the coordinator.

Official references: [Android UI](https://developer.android.com/design/ui/mobile), [Compose architecture](https://developer.android.com/develop/ui/compose/architecture), [Lifecycle coroutines](https://developer.android.com/topic/libraries/architecture/coroutines), [Testing](https://developer.android.com/training/testing), [Adaptive layouts](https://developer.android.com/develop/ui/compose/build-adaptive-apps). Verify APIs against actual Compose/Views and installed dependency versions.
## Supporting reference

Read [recipes.md](recipes.md) when performing this role; keep the assigned platform and scope.
