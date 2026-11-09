# Desktop toolbox

## Brief

Offer a small agreed set of reversible desktop utilities. Implement only the agreed first milestone for Windows using Tauri 2 and the existing frontend.

## Implementation

Rust Windows API services; Tauri controls for user-visible settings. Keep typed IPC contracts, narrow capabilities, dev/release separation and cleanup ownership explicit. Native APIs belong in Rust, not an unrestricted webview shell command.

## Stories and acceptance

- Implement only the selected utilities and record their original states.
- Handle denied operations without requiring blanket administrator privileges.
- Restore temporary changes when the feature requires it and verify cancellation.

## Verification

Use Rust tests for deterministic logic and frontend tests for presentation. Exercise native integration on Windows with isolated data; browser mocks do not prove native behavior. Read [verification](../verification.md).

## Done when

The agreed user flow and relevant failure/cancel behavior have actual evidence, and blocked environment/device checks are recorded separately. Additional features remain outside the current milestone.
