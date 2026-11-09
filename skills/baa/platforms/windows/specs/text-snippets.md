# Text snippets

## Brief

Expand an agreed shortcut into text while preserving user input and clipboard state. Implement only the agreed first milestone for Windows using Tauri 2 and the existing frontend.

## Implementation

Rust Windows keyboard/input integration on a bounded worker; Tauri snippet editor. Keep typed IPC contracts, narrow capabilities, dev/release separation and cleanup ownership explicit. Native APIs belong in Rust, not an unrestricted webview shell command.

## Stories and acceptance

- Validate unique shortcuts and preserve multiline/Unicode content.
- Keep hooks responsive and clean them up on quit; prevent self-trigger loops.
- Verify cancellation, rapid typing, keyboard layouts and clipboard restoration on Windows.

## Verification

Use Rust tests for deterministic logic and frontend tests for presentation. Exercise native integration on Windows with isolated data; browser mocks do not prove native behavior. Read [verification](../verification.md).

## Done when

The agreed user flow and relevant failure/cancel behavior have actual evidence, and blocked environment/device checks are recorded separately. Additional features remain outside the current milestone.
