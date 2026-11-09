---
name: baa-windows-os-integrations
description: Connect Tauri windows and Rust services to the requested Windows features.
---

# Windows OS integration

Use the [BAA execution rules](../../../../../EXECUTION.md) already established for this task. Preserve the assigned Windows target, current stage, file ownership and acceptance; do not create a nested team.

Use existing official Tauri APIs/plugins for windows, menus, tray, dialogs, clipboard, shortcuts, notifications and deep links when they meet the task. Check installed versions and available permissions before adding a dependency. Keep frontend registration, Rust plugin initialization and window-scoped capability entries consistent.

Use Rust Windows APIs for missing OS functionality, checking handle ownership, thread affinity and cleanup. Do not substitute browser clipboard, downloads or notification behavior for the actual Windows integration. Keep global shortcut/hook callbacks short and unregister resources on shutdown. Preserve clipboard contents, monitor/display coordinates, keyboard layouts and accessibility.

Close-to-tray, second-instance handling, taskbar visibility and Quit are separate product decisions. File associations, startup tasks and deep links must distinguish dev and release IDs/paths. Reject untrusted external input before opening a file or invoking a command. Test the actual Windows path, including denial/cancellation and callback state; mocks establish only the integration contract.
