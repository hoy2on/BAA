---
name: baa-windows-app-icon
description: Prepare the requested Windows app and installer icon assets.
---

# Windows Tauri icons

Use the [BAA execution rules](../../../../../EXECUTION.md) already established for this task. Preserve the assigned Windows target, current stage, file ownership and acceptance; do not create a nested team.

Preserve existing icon source and licensing; distinguish product icon, tray image and in-content symbols. Use the project's installed Tauri CLI `icon` command for a suitable high-resolution source and inspect the generated ICO/PNG outputs at taskbar, small tray and installer sizes.

Update actual bundle icon paths, test transparency/light and dark backgrounds and retain recognizable dev branding. Do not invent a separate icon-conversion utility or regenerate the whole icon family for a content-icon fix. Generating assets is separate from rebuilding installers and from publishing.
