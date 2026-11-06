# Android runtime verification

Read when constructing scaffold, build-and-verify or test commands. Prefer the project wrapper and existing scripts.
Inspect actual modules, dev flavors/build types and serials; do not automatically select app, debug or the first connected device.

## Inspect actual tasks and devices

```sh
./gradlew projects
./gradlew tasks --all
adb devices -l
```

On Windows use the actual repository gradlew.bat. Select assemble/test/lint tasks from the inspected module/variant.
For example, use :app:assembleDevDebug only when that task exists and the dev ID is distinct.
Diagnose SDK/AGP/Kotlin compatibility from wrapper/catalog/installed tools; do not upgrade everything for execution convenience.

## Separate build/checks from installation

```sh
./gradlew "$BAA_ASSEMBLE_TASK" "$BAA_UNIT_TEST_TASK" "$BAA_LINT_TASK"
```

Identify actual tasks, APK output, applicationId, signing and variant.
Use apkanalyzer manifest application-id or existing APK inspection tools; Gradle strings alone do not prove the install target.
Install only on the selected device after verifying the designated ID differs from Release. Use existing split-install workflows for split APKs.

```sh
adb -s "$BAA_SERIAL" install -r "$BAA_DEV_APK"
adb -s "$BAA_SERIAL" shell am start -W -n "$BAA_DEV_COMPONENT"
adb -s "$BAA_SERIAL" exec-out screencap -p > "$BAA_SCREENSHOT"
```

BAA_DEV_COMPONENT is the actual dev APK launcher. Never resolve signing conflicts through Release uninstall, pm clear or user-data deletion.
Confirm the foreground app and absence of private overlays before captures. A screenshot command does not prove input/Back/save behavior.

## Device tests and evidence

```sh
ANDROID_SERIAL="$BAA_SERIAL" ./gradlew "$BAA_CONNECTED_TEST_TASK"
```

Check logs that the installed AGP/runner respects the selected serial. Name actual project conventions/devices for multiple-device or Gradle Managed Device execution.
Find actual module unit XML/HTML, instrumentation and lint output paths. UP-TO-DATE, NO-SOURCE and zero tests are not new runtime verification.
Keep the first failing task/exception and target-app crash/logcat. Do not bulk-collect unrelated apps or clear global log buffers.

Select affected system Back, IME, recreation/rotation/restoration, font scale and light/dark flows.
For supported large-screen/foldable layouts verify current window/pane changes. Distinguish emulator results from hardware sensor/performance/permission evidence.
Return source state, module/variant, dev package, serial/OS, commands/exit codes, tests/logs/screens and remaining device checks.

Official references: [Command-line builds](https://developer.android.com/build/building-cmdline), [Command-line testing](https://developer.android.com/studio/test/command-line), [adb](https://developer.android.com/tools/adb).
