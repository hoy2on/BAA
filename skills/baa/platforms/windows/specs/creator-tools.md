# Creator tools

## Brief

Provide an explicitly selected overlay or presentation aid. Implement only the agreed first milestone for Windows using Tauri 2 and the existing frontend.

## Implementation

Tauri overlay windows with Rust input/window integration. Keep typed IPC contracts, narrow capabilities, dev/release separation and cleanup ownership explicit. Native APIs belong in Rust, not an unrestricted webview shell command.

## Stories and acceptance

- Preserve click-through, focus and escape behavior across monitors.
- Do not capture or log sensitive typed content.
- Verify visibility, scaling and resource cleanup in the real Windows desktop.

## Verification

Use Rust tests for deterministic logic and frontend tests for presentation. Exercise native integration on Windows with isolated data; browser mocks do not prove native behavior. Read [verification](../verification.md).

## Done when

The agreed user flow and relevant failure/cancel behavior have actual evidence, and blocked environment/device checks are recorded separately. Additional features remain outside the current milestone.
