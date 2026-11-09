---
name: baa-windows-design-kit
description: Reuse or extend the existing desktop frontend components.
---

# Tauri component kit

Use the [BAA execution rules](../../../../../EXECUTION.md) already established for this task. Preserve the assigned Windows target, current stage, file ownership and acceptance; do not create a nested team.

Inventory current buttons, fields, lists, tabs, menus, dialogs and navigation before adding a component. Prefer semantic elements and established framework primitives; define names, focus order, disabled/selected/loading/error states and keyboard dismissal. Preserve existing event and data contracts.

Create custom components only for a requested gap. Native file dialogs and OS menus use Tauri APIs rather than imitation web controls where the product requires them. Verify forced-colors, text sizing and keyboard/pointer behavior in WebView2. Document only reusable decisions in the existing design source.
