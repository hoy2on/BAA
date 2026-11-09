# Color picker

## Brief

Pick a screen color and keep a small editable palette. Implement only the agreed first milestone for Windows using Tauri 2 and the existing frontend.

## Implementation

Rust screen sampling and coordinate conversion; Tauri palette UI. Keep typed IPC contracts, narrow capabilities, dev/release separation and cleanup ownership explicit. Native APIs belong in Rust, not an unrestricted webview shell command.

## Stories and acceptance

- Verify physical versus logical coordinates across monitors.
- Provide keyboard cancel and do not persist screen captures by default.
- Verify displayed/copied color values and palette persistence using fixture data.

## Verification

Use Rust tests for deterministic logic and frontend tests for presentation. Exercise native integration on Windows with isolated data; browser mocks do not prove native behavior. Read [verification](../verification.md).

## Done when

The agreed user flow and relevant failure/cancel behavior have actual evidence, and blocked environment/device checks are recorded separately. Additional features remain outside the current milestone.
