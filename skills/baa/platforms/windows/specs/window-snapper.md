# Window snapper

## Brief

Move the foreground window to agreed screen regions using keyboard shortcuts. Implement only the agreed first milestone for Windows using Tauri 2 and the existing frontend.

## Implementation

Rust Windows APIs for window handles, work areas and DPI-aware coordinates; Tauri settings and shortcut registration. Keep typed IPC contracts, narrow capabilities, dev/release separation and cleanup ownership explicit. Native APIs belong in Rust, not an unrestricted webview shell command.

## Stories and acceptance

- Register/unregister the shortcut without duplicates.
- Move an owned test window to a selected region; preserve unrelated windows.
- Exercise multiple monitors and Windows display scaling.

## Verification

Use Rust tests for deterministic logic and frontend tests for presentation. Exercise native integration on Windows with isolated data; browser mocks do not prove native behavior. Read [verification](../verification.md).

## Done when

The agreed user flow and relevant failure/cancel behavior have actual evidence, and blocked environment/device checks are recorded separately. Additional features remain outside the current milestone.
