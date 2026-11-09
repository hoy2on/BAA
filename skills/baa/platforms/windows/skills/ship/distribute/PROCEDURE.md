---
name: baa-windows-distribute
description: Prepare the requested Tauri Windows release without implicit publication or installation.
---

# Windows Tauri distribution

Use the [BAA execution rules](../../../../../EXECUTION.md) already established for this task. Preserve the assigned Windows target, current stage, file ownership and acceptance; do not create a nested team.

Inspect the existing release workflow, release identifier, architecture, version, icons, signing and WebView2 requirements. Use the project's locked frontend/Rust dependencies and actual Tauri configuration; keep the dev overlay out of release artifacts. Do not replace the user's installed release during development.

Tauri supports NSIS setup executables and MSI installers. Choose the existing/requested channel; build on the appropriate Windows runner with its required toolchain. Inspect merged config and updater endpoints/keys if already used. Do not add an updater, signing provider or installer channel without a requirement.

Report compilation, package creation, signing, install/upgrade verification and public upload separately. Package creation does not authorize executing the installer, publishing binaries, or submitting to a store. Check upgrade/data preservation only in an explicitly approved isolated environment. Never put signing or updater private keys in the repository.

Reference: [Windows installer guide](https://v2.tauri.app/distribute/windows-installer/).
