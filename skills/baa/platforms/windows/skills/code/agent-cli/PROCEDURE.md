---
name: baa-windows-agent-cli
description: Expose only the explicitly requested automation surface for the Windows dev app.
---

# Tauri agent integration

Use the [BAA execution rules](../../../../../EXECUTION.md) already established for this task. Preserve the assigned Windows target, current stage, file ownership and acceptance; do not create a nested team.

Reuse an existing CLI/test bridge first. If requested, define a small versioned command/result contract and route operations through the same Rust domain functions as the UI. Do not implement a second data store or a general command shell.

Scope local IPC to the current user and the exact dev identifier; enforce access checks and bounded requests. Never expose arbitrary filesystem/shell access, secrets or a public unauthenticated HTTP listener. Keep test fixtures isolated and require explicit startup for debug-only bridges. Exclude development controls from release builds and verify that exclusion.

Return the command schema, target process/identity and actual invocation results. Adding an MCP/CLI server is not required merely to verify ordinary UI.
