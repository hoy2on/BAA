---
name: baa-android
description: BAA Android-only entrypoint. Route /baa-android app work to specialist procedures within Android scope.
---

# BAA Android

Keep the invocation entrypoint as `baa-android` and allowed targets as Android.
Read the [central BAA procedure](../baa/SKILL.md) and follow the same target selection, stage routing, assignment and verification workflow.
Reading that document must not reset scope to all of baa. If the request names an outside platform, resolve the conflict before editing; do not switch automatically.
Pass `--entrypoint baa-android` for platform-role lookups. Limit common procedures and shared-file changes to the selected targets' needs.
Respond in the user's language and follow project documentation/localization conventions; English internal instructions do not change product copy.
