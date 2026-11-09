---
name: baa-windows-tauri
description: Implement Windows behavior across the Rust host and the existing frontend.
---

# Tauri implementation

Use the [BAA execution rules](../../../../../EXECUTION.md) already established for this task. Preserve the assigned Windows target, current stage, file ownership and acceptance; do not create a nested team.

Trace the user action through the frontend, invoke/event boundary, Rust command and rendered result. Keep UI state in the existing frontend; put filesystem, OS and durable-data operations behind small typed Rust commands. Preserve the project's framework, package manager, storage format and IPC contracts.

Validate command inputs in Rust even if the form already validates them. Return recoverable errors to the invoking screen, preserve unsaved input, guard duplicate submissions and propagate cancellation where supported. Do not hold state locks across slow I/O or block the UI thread; bound background work and remove event listeners on disposal. Use text rendering rather than injecting returned strings into HTML.

Apply the minimum capability/window scope needed by an actual plugin call. Capabilities do not make custom Rust code safe: validate paths, identifiers and arguments in the command itself. Do not grant arbitrary shell execution or broad filesystem access to solve a permission error. Read [architecture](../improve-architecture/architecture.md) for shared-state or persistence changes; use os-integrations for OS services and build-and-verify/test for evidence.

References: [Rust commands](https://v2.tauri.app/develop/calling-rust/), [capabilities](https://v2.tauri.app/security/capabilities/).
