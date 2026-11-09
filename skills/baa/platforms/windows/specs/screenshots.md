# Screenshots

## Brief

Capture an explicitly selected window or region and export it. Implement only the agreed first milestone for Windows using Tauri 2 and the existing frontend.

## Implementation

Rust Windows capture APIs and safe image export; Tauri selection/annotation UI. Keep typed IPC contracts, narrow capabilities, dev/release separation and cleanup ownership explicit. Native APIs belong in Rust, not an unrestricted webview shell command.

## Stories and acceptance

- Capture only the selected target, with relevant DPI/monitor checks.
- Cancel/export failures preserve original image data.
- Verify exported dimensions, alpha and destination conflict handling.

## Verification

Use Rust tests for deterministic logic and frontend tests for presentation. Exercise native integration on Windows with isolated data; browser mocks do not prove native behavior. Read [verification](../verification.md).

## Done when

The agreed user flow and relevant failure/cancel behavior have actual evidence, and blocked environment/device checks are recorded separately. Additional features remain outside the current milestone.
