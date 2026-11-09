---
name: baa-windows-new-windows-app
description: Generate a new Rust and TypeScript Tauri project with a separate dev identity.
---

# New Windows Tauri app

Use the [BAA execution rules](../../../../../EXECUTION.md) already established for this task. Preserve the assigned Windows target, current stage, file ownership and acceptance; do not create a nested team.

For a new app only, use the packaged generator from the runtime root:

```sh
python3 scripts/new-app.py windows MyApp com.example.myapp <parent-directory>
```

The starter contains a Tauri 2 Rust host, TypeScript/Vite frontend, a validated IPC command, Rust unit tests and a .dev configuration. It preserves planning documents and refuses existing projects or output conflicts. No dependency installation, app installation or Git commands run during generation.

Inspect Node/npm, stable Rust and the Windows prerequisites before installing dependencies. Use the existing frontend framework for an existing Tauri app; the starter's vanilla TypeScript is not a migration target. For a fresh starter run `npm install`, retain package-lock.json and Cargo.lock, then follow [verification](../../../verification.md). The default `app:dev` and `app:build` scripts use the dev config; the base config describes the future release identity. Verify merged identifiers, process path and storage before launching or installing. Add product icons and the requested Windows installer only during the relevant app-icon/distribute stage.

Prerequisites: [official guide](https://v2.tauri.app/start/prerequisites/).
