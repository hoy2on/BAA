# Tauri architecture review

Trace frontend action -> invoke/event -> Rust command -> domain/storage -> rendered result. Keep validation and OS access on the host side; keep rendering in the existing frontend. Inspect lock lifetimes, cancellation, event-listener disposal and serialization/error contracts. Preserve stored data and migration compatibility. Review capability scopes, custom command input checks and dev/release identifiers. Refactor only an observed source of change cost; do not add a general IPC abstraction or switch frontend frameworks.
