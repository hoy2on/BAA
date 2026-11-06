---
name: baa-android-scaffold
description: Android scaffold procedure for the assigned platform and current app workflow.
---

# Android Scaffold

Read the [BAA execution rules](../../../../../EXECUTION.md). Inherit platform, purpose, owned files and acceptance. This internal procedure does not restart platform selection or team creation; preserve other workers' changes.

## Execution

Read [runtime verification](../../../verification.md) for project-specific commands and evidence.

Inspect wrapper, settings/modules, catalog, plugins, min/target SDK, types/flavors and existing app targets. Don't regenerate an existing project.
For a new app use installed Android Studio or verified repository template Gradle configuration. Resolve SDK/AGP/Kotlin/Compose from real tools, compatibility docs and catalogs, not invented versions. Create the minimum appropriate Compose/Views app and unit/instrumentation targets. Use a dev applicationId coexisting with Release; don't automatically share production data/accounts.
Provide a first screen/core state/manifest/launcher and only required permissions. Don't add one-off DI/repository/multi-module/server layers. Confirm actual assemble/test/lint tasks, build minimally and launch the selected emulator/device dev app.
Then resolve native-design/design-system/app-icon or story code. Inspect current capabilities before new dependencies.
Done when actual modules/dev identity/first screen/build-launch results or environment limits are recorded.

## Follow-up and handoff

Resolve subsequent roles from the runtime root with `python3 scripts/resolve.py --entrypoint <entrypoint> --platform <assigned-platform> --step <role>`. Read the returned PROCEDURE.md; do not use internal names as Skill-tool/slash commands. Do not recurse into the current stage or add unrequested distribution, installation or commits.
Return changed files, source state/target/environment, check/screen/log paths, unverified items and shared-change proposals to the coordinator.

Official references: [Android UI](https://developer.android.com/design/ui/mobile), [Compose architecture](https://developer.android.com/develop/ui/compose/architecture), [Lifecycle coroutines](https://developer.android.com/topic/libraries/architecture/coroutines), [Testing](https://developer.android.com/training/testing), [Adaptive layouts](https://developer.android.com/develop/ui/compose/build-adaptive-apps). Verify APIs against actual Compose/Views and installed dependency versions.
## Packaged starter files

Use this [template](template) only for a new app. Existing apps retain their project, technology and minimum OS.
Use the [mobile generator](../../../../../scripts/new-app.py) from the runtime root.

```sh
python3 <runtime-root>/scripts/new-app.py android <AppName> <base-app-id> <parent-folder>
```

Includes a Kotlin/Compose app, Gradle Wrapper, manifest/default icon/strings/theme and unit/UI tests.
New starter baseline: JDK 17+, Gradle 8.14.3, AGP 8.11.2, Kotlin 2.3.20, Compose BOM 2025.09.00, SDK 36/minSdk 26.
Compare installed tooling against official [AGP compatibility](https://developer.android.com/build/releases/agp-8-11-0-release-notes) and [Kotlin compatibility](https://kotlinlang.org/docs/gradle-configure-project.html). Do not impose these versions on existing apps.
Configure SDK paths through local.properties or ANDROID_HOME; never bake personal paths into templates.
Check with `./gradlew :app:assembleDebug :app:testDebugUnitTest :app:lintDebug`. Device tests/installation are separate and require a verified serial.
The wrapper may download Gradle/dependencies on first execution. Preserve the [Gradle license](template/GRADLE-LICENSE.txt).
The generator preserves planning docs and stops before writing on output/project conflicts. It does not install/launch apps or run git init, staging, commits or pushes.
Debug/dev uses a .dev ID and -dev display name, preserving a separate Release identity.
