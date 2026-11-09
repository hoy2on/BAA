---
name: baa-windows-layout-grid
description: Verify desktop web layout across supported Windows window and display sizes.
---

# Tauri layout review

Use the [BAA execution rules](../../../../../EXECUTION.md) already established for this task. Preserve the assigned Windows target, current stage, file ownership and acceptance; do not create a nested team.

Use the existing CSS spacing scale and layout components. Inspect computed layout and actual screenshots for clipping, alignment, hit areas, scroll ownership, focus visibility and minimum supported widths. Check text zoom/long labels and relevant Windows DPI scales; do not equate screenshot pixels with CSS pixels.

Keep content resizable without excessive empty bands or nested scrolling. Verify overlays, menus and dialogs against their viewport/window bounds and ensure title-bar drag regions exclude controls. Reuse existing frontend tests and Windows captures; do not add layout probes to every screen for a local adjustment.
