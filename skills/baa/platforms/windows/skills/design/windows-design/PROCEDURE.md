---
name: baa-windows-windows-design
description: Design Windows desktop interactions in Tauri web content and native windows.
---

# Windows Tauri UX

Use the [BAA execution rules](../../../../../EXECUTION.md) already established for this task. Preserve the assigned Windows target, current stage, file ownership and acceptance; do not create a nested team.

Use the current frontend components and semantic HTML for content, with Tauri native window/menu/dialog APIs where appropriate. Tauri content is web UI: CSS, DOM, focus order and browser accessibility semantics apply, while window chrome and system integrations follow Windows conventions.

Keep native decorations unless custom chrome serves an explicit requirement. Custom title bars must retain drag/resize/maximize, system menu, keyboard behavior and correctly excluded interactive regions. Use readable desktop density, resizable layouts, visible focus, keyboard traversal/access keys and discoverable pointer actions; touch is an additional supported input, not a reason to make every desktop control phone-sized.

Check WebView2 zoom versus Windows display scaling, forced-colors/high-contrast, reduced motion, theme and long localized content. Use CSS pixels for web layout, physical pixels for capture and the appropriate logical/physical units for native window APIs. Native window appearance does not establish web-content contrast.

Use shared ux-design for behavior/copy and the relevant design-system/layout-grid role for visuals. Proposal/review-only work ends with inspectable proposals; implemented UI uses actual Windows runtime evidence for changed screens.
