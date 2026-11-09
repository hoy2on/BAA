---
name: baa-windows-test-windows-app
description: Test frontend, Rust and the Windows runtime boundaries affected by a change.
---

# Tauri testing

Use the [BAA execution rules](../../../../../EXECUTION.md) already established for this task. Preserve the assigned Windows target, current stage, file ownership and acceptance; do not create a nested team.

Read [verification](../../../verification.md). Reuse frontend tests for rendering and user actions, Rust unit/integration tests for domain logic and command validation, and the existing Windows UI flow for native integration. Test actual error contracts and cancellation rather than duplicating implementation details.

Tauri API mocks prove frontend handling only. Test at least one real invoke/result flow and the affected native service on Windows. Where already supported, use tauri-driver with the matching Edge WebDriver/WebView2 setup; do not mandate or auto-install a UI tool. A normal browser runner alone does not exercise the Rust host.

Use dev-only fixture storage and account data. For cross-account/state changes inspect relevant cleanup paths; for async work include applicable duplicate/cancel/failure behavior. Rerun only invalidated checks after fixes. Record source/config/Windows build/WebView2/architecture, actual results and blocked checks without converting blocked checks into a pass.

Reference: [Tauri WebDriver](https://v2.tauri.app/develop/tests/webdriver/).
