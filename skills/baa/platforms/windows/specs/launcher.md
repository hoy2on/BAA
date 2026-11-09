# Launcher

## Brief

Find and open approved applications or files from one search field. Implement only the agreed first milestone for Windows using Tauri 2 and the existing frontend.

## Implementation

Tauri search frontend; Rust indexing and validated launch targets. Keep typed IPC contracts, narrow capabilities, dev/release separation and cleanup ownership explicit. Native APIs belong in Rust, not an unrestricted webview shell command.

## Stories and acceptance

- Results are keyboard navigable and loading does not block typing.
- Launch only a selected validated target; preserve argument boundaries.
- Cancel/reopen and missing-target errors retain predictable focus.

## Verification

Use Rust tests for deterministic logic and frontend tests for presentation. Exercise native integration on Windows with isolated data; browser mocks do not prove native behavior. Read [verification](../verification.md).

## Done when

The agreed user flow and relevant failure/cancel behavior have actual evidence, and blocked environment/device checks are recorded separately. Additional features remain outside the current milestone.
