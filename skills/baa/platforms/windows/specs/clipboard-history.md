# Clipboard history

## Brief

Search locally retained clipboard items and restore a chosen item. Implement only the agreed first milestone for Windows using Tauri 2 and the existing frontend.

## Implementation

Rust clipboard integration with a bounded dev-only store; Tauri search/list UI. Keep typed IPC contracts, narrow capabilities, dev/release separation and cleanup ownership explicit. Native APIs belong in Rust, not an unrestricted webview shell command.

## Stories and acceptance

- Observe only clipboard access authorized by the feature.
- Preserve supported formats and avoid logging sensitive copied content.
- Verify selection/paste, retention limits and restart against isolated fixtures.

## Verification

Use Rust tests for deterministic logic and frontend tests for presentation. Exercise native integration on Windows with isolated data; browser mocks do not prove native behavior. Read [verification](../verification.md).

## Done when

The agreed user flow and relevant failure/cancel behavior have actual evidence, and blocked environment/device checks are recorded separately. Additional features remain outside the current milestone.
