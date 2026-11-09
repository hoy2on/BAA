---
name: baa-windows-build-and-verify
description: Build and exercise the changed Windows Tauri behavior with bounded evidence.
---

# Build and verify Tauri

Use the [BAA execution rules](../../../../../EXECUTION.md) already established for this task. Preserve the assigned Windows target, current stage, file ownership and acceptance; do not create a nested team.

Read [verification](../../../verification.md) and inspect actual package scripts, Cargo targets, Tauri configs/capabilities and CI before running commands. Reuse valid artifacts for the same source/config; default to the existing dev variant. A compilation on another host does not prove Windows execution.

Build the affected frontend and Rust targets, then run the actual Windows WebView2 app at the designated dev path with isolated test data. Verify the changed screen, action, result and an applicable failure/cancel path. Capture only relevant windows/states and inspect logs for frontend, IPC and Rust failures; avoid capturing unrelated user windows.

Reuse the project test flow or direct Windows interaction. A frontend browser preview cannot prove native dialogs, tray, shortcuts or IPC. Missing Windows hardware/runner/permissions leave those checks pending while independent checks continue. No automatic commit, installer run or publication is part of this procedure.
