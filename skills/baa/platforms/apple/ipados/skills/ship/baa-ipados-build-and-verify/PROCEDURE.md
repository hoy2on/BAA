---
name: baa-ipados-build-and-verify
description: BAA iPadOS build and verification specialist. Perform the assigned iPadOS build-and-verify stage.
---

# iPadOS Build and verification

Read and apply the [BAA execution rules](../../../../../../EXECUTION.md) and [shared build and verification procedure](../../../../shared/skills/ship/baa-apple-build-and-verify/PROCEDURE.md) together.
Apply only the iPadOS branch of shared iOS/iPadOS guidance, preserving the entrypoint, owned files, purpose and acceptance. Reading shared guidance does not add other platform targets or create another team.

Use an actual iPad destination. Verify wide/narrow windows, rotation, column transitions and supported multiple windows. Mark keyboard/pointer checks unverified when input tools are unavailable.

Return changed files, environment, check results and unverified items against both shared acceptance and these iPadOS conditions. Resolve follow-up roles with the inherited entrypoint and `--platform ipados`; reading a base procedure must not recursively re-enter this role.
