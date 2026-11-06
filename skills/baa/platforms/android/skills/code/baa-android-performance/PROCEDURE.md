---
name: baa-android-performance
description: Android performance procedure for the assigned platform and current app workflow.
---

# Android Performance

Read the [BAA execution rules](../../../../../EXECUTION.md). Inherit platform, purpose, owned files and acceptance. This internal procedure does not restart platform selection or team creation; preserve other workers' changes.

## Execution

Fix symptoms/scenario, actual device/OS, variant, data and metrics. Emulator timings are not hardware results. Choose existing symptom-relevant profilers, Perfetto/System Trace, CPU/memory, JankStats/Macrobenchmark. Add benchmark dependencies only after inspecting need/current configuration.
Trace UI-thread blocking I/O/decode/DB work, Compose recomposition/state reads/stable keys, RecyclerView binding/reuse/layout costs. Fix the cause with existing dispatchers/lazy/reuse/image sizing/caching; don't add global caches/GlobalScope/architecture without measurements.
Compare startup/frames/memory on identical device/variant/scenario; check correctness, cancellation, memory lifetime and accessibility regressions. Record thermal/debugger/background-load differences and distinguish Release/profileable measurements from Debug execution.
Done when cause/fix/comparable metrics/regression proof exist or actual environment limits are explicit.

## Follow-up and handoff

Resolve subsequent roles from the runtime root with `python3 scripts/resolve.py --entrypoint <entrypoint> --platform <assigned-platform> --step <role>`. Read the returned PROCEDURE.md; do not use internal names as Skill-tool/slash commands. Do not recurse into the current stage or add unrequested distribution, installation or commits.
Return changed files, source state/target/environment, check/screen/log paths, unverified items and shared-change proposals to the coordinator.

Official references: [Android UI](https://developer.android.com/design/ui/mobile), [Compose architecture](https://developer.android.com/develop/ui/compose/architecture), [Lifecycle coroutines](https://developer.android.com/topic/libraries/architecture/coroutines), [Testing](https://developer.android.com/training/testing), [Adaptive layouts](https://developer.android.com/develop/ui/compose/build-adaptive-apps). Verify APIs against actual Compose/Views and installed dependency versions.
## Supporting reference

Read [recipes.md](recipes.md) when performing this role; keep the assigned platform and scope.
