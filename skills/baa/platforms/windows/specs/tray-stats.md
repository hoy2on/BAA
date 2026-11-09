# Tray stats

## Brief

Show a bounded set of system resource readings in a tray utility. Implement only the agreed first milestone for Windows using Tauri 2 and the existing frontend.

## Implementation

Rust system sampling and Tauri tray/menu integration. Keep typed IPC contracts, narrow capabilities, dev/release separation and cleanup ownership explicit. Native APIs belong in Rust, not an unrestricted webview shell command.

## Stories and acceptance

- Poll at a bounded interval and release resources at quit.
- Close-to-tray and explicit Quit follow the agreed behavior.
- Exercise repeated open/close and observe actual Windows resource trends.

## Verification

Use Rust tests for deterministic logic and frontend tests for presentation. Exercise native integration on Windows with isolated data; browser mocks do not prove native behavior. Read [verification](../verification.md).

## Done when

The agreed user flow and relevant failure/cancel behavior have actual evidence, and blocked environment/device checks are recorded separately. Additional features remain outside the current milestone.
