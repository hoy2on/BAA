# Window switcher

## Brief

Choose a visible desktop window from a keyboard-driven picker. Implement only the agreed first milestone for Windows using Tauri 2 and the existing frontend.

## Implementation

Rust window enumeration and activation; Tauri picker window with explicit focus behavior. Keep typed IPC contracts, narrow capabilities, dev/release separation and cleanup ownership explicit. Native APIs belong in Rust, not an unrestricted webview shell command.

## Stories and acceptance

- Filter eligible windows without exposing private content in logs.
- Keyboard selection/cancel returns focus correctly.
- Confirm actual Windows activation and stale-window handling.

## Verification

Use Rust tests for deterministic logic and frontend tests for presentation. Exercise native integration on Windows with isolated data; browser mocks do not prove native behavior. Read [verification](../verification.md).

## Done when

The agreed user flow and relevant failure/cancel behavior have actual evidence, and blocked environment/device checks are recorded separately. Additional features remain outside the current milestone.
