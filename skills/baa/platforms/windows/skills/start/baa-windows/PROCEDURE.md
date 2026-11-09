---
name: baa-windows-router
description: Select the current Windows Tauri stage without restarting planning.
---

# Windows Tauri routing

Use the [BAA execution rules](../../../../../EXECUTION.md) already established for this task. Preserve the assigned Windows target, current stage, file ownership and acceptance; do not create a nested team.

Windows work uses Tauri 2: Rust host commands, the project's existing web frontend and WebView2. Inspect package.json, src-tauri/Cargo.toml, Tauri configuration, capabilities and callers. If the assigned project uses another desktop framework, report the mismatch and obtain a migration scope before changing its architecture.

Use the inherited entrypoint with `python3 <runtime-root>/scripts/resolve.py --entrypoint <entrypoint> --platform windows --step <role>`. New apps use scaffold; existing behavior uses code; interaction/layout uses native-design and only the relevant design roles; OS services use os-integrations; diagnosis uses performance; execution uses build-and-verify/test; publishing uses distribute only when requested. Shared planning/UX roles remain common.

Read [example plans](../../../specs/README.md) only for new-app examples. Keep shared sources under one owner; a Windows assignment does not authorize changing another platform. Return implementation, actual Windows runtime evidence and environment waits separately.
