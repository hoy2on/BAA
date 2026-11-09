# Screen recorder

## Brief

Record an approved screen source with explicitly requested audio inputs. Implement only the agreed first milestone for Windows using Tauri 2 and the existing frontend.

## Implementation

Rust capture/encoding pipeline and device lifecycle; Tauri recording controls. Keep typed IPC contracts, narrow capabilities, dev/release separation and cleanup ownership explicit. Native APIs belong in Rust, not an unrestricted webview shell command.

## Stories and acceptance

- Verify device permissions and selected source on actual hardware.
- Keep start/pause/stop/cancel responsive and finalize output safely.
- Test input loss, disk/export errors and shutdown without corrupting prior recordings.

## Verification

Use Rust tests for deterministic logic and frontend tests for presentation. Exercise native integration on Windows with isolated data; browser mocks do not prove native behavior. Read [verification](../verification.md).

## Done when

The agreed user flow and relevant failure/cancel behavior have actual evidence, and blocked environment/device checks are recorded separately. Additional features remain outside the current milestone.
