---
name: baa-windows-performance
description: Diagnose Windows UI, IPC and Rust bottlenecks before changing implementation.
---

# Tauri performance

Use the [BAA execution rules](../../../../../EXECUTION.md) already established for this task. Preserve the assigned Windows target, current stage, file ownership and acceptance; do not create a nested team.

Reproduce the changed flow on Windows and separate frontend rendering, WebView2, IPC serialization, Rust work, storage and OS service time. Capture a bounded trace or measurements with the current build/config/data size. Browser performance alone is not native-process performance.

Fix the measured cause: batch chatty IPC, bound payloads and event rates, virtualize long lists, move blocking work off interactive paths and cancel obsolete jobs. Inspect detached tasks, listeners, timers, native handles and WebView/process memory when repeated use grows resource use. Do not add caching or concurrency without evidence and invalidation rules.

Recheck the same scenario and data after the fix, including correctness and cancellation. Record observed timings/resource trends; a short smoke run does not prove absence of leaks.
