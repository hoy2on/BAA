---
name: baa-windows
description: BAA Windows-only entrypoint. Route /baa-windows app work to specialist procedures within Windows scope.
---

# BAA Windows

Keep the invocation entrypoint as `baa-windows` and allowed targets as Windows.
Read the [central BAA procedure](../baa/SKILL.md) and follow the same target selection, stage routing, assignment and verification workflow.
Reading that document must not reset scope to all of baa. If the request names an outside platform, resolve the conflict before editing; do not switch automatically.
Pass `--entrypoint baa-windows` for platform-role lookups. Limit common procedures and shared-file changes to the selected targets' needs.
Respond in the user's language and follow project documentation/localization conventions; English internal instructions do not change product copy.
