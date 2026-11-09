# Developer toolkit

## Brief

Transform text or open an approved local project from a compact workspace. Implement only the agreed first milestone for Windows using Tauri 2 and the existing frontend.

## Implementation

Tauri frontend for local text tools; Rust validated file/process operations. Keep typed IPC contracts, narrow capabilities, dev/release separation and cleanup ownership explicit. Native APIs belong in Rust, not an unrestricted webview shell command.

## Stories and acceptance

- Keep text transforms deterministic with unit tests and no network side effects.
- Validate paths and structured arguments before any OS process action.
- Preserve originals and report malformed input without crashing the UI.

## Verification

Use Rust tests for deterministic logic and frontend tests for presentation. Exercise native integration on Windows with isolated data; browser mocks do not prove native behavior. Read [verification](../verification.md).

## Done when

The agreed user flow and relevant failure/cancel behavior have actual evidence, and blocked environment/device checks are recorded separately. Additional features remain outside the current milestone.
