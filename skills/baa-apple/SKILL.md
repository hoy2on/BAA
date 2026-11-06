---
name: baa-apple
description: BAA Apple-only entrypoint. Route /baa-apple app work to specialist procedures within macOS, iOS and iPadOS scope.
---

# BAA Apple

Keep the invocation entrypoint as `baa-apple` and allowed targets as macOS, iOS and iPadOS.
Read the [central BAA procedure](../baa/SKILL.md) and follow the same target selection, stage routing, assignment and verification workflow.
Reading that document must not reset scope to all of baa. If the request names an outside platform, resolve the conflict before editing; do not switch automatically.
Pass `--entrypoint baa-apple` for platform-role lookups. Limit common procedures and shared-file changes to the selected targets' needs.
Respond in the user's language and follow project documentation/localization conventions; English internal instructions do not change product copy.
