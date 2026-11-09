---
name: baa-windows-design-system
description: Maintain the existing Windows frontend tokens and appearance modes.
---

# Tauri design tokens

Use the [BAA execution rules](../../../../../EXECUTION.md) already established for this task. Preserve the assigned Windows target, current stage, file ownership and acceptance; do not create a nested team.

Read existing CSS variables, component themes and design documents. Reuse one semantic token source for text, surfaces, borders, focus, selection, spacing and motion; make only scoped changes. Shared brand meaning does not force another platform's control sizes or typography onto Windows.

Respect prefers-color-scheme, forced-colors and prefers-reduced-motion where relevant, plus any explicit app preference. Use system fonts or existing approved assets, and measure contrast using composed colors. Keep native title-bar/theme changes aligned with content without adding a new UI library for a small change. Return changed tokens and light/dark/high-contrast evidence, or clearly label proposal-only work.
