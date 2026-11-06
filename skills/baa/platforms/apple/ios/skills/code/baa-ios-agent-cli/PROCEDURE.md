---
name: baa-ios-agent-cli
description: BAA iOS agent control specialist. Perform the assigned iOS agent-cli stage.
---

# iOS Agent control

Read and apply the [BAA execution rules](../../../../../../EXECUTION.md) and [shared agent control procedure](../../../../shared/skills/code/baa-apple-agent-cli/PROCEDURE.md) together.
Apply only the iOS branch of shared iOS/iPadOS guidance, preserving the entrypoint, owned files, purpose and acceptance. Reading shared guidance does not add other platform targets or create another team.

Use existing UI tests/authorized dev-control paths. Do not port desktop Unix sockets/menu bars/terminal binaries automatically into iPhone apps. Verify the actual connected dev bundle ID.

Return changed files, environment, check results and unverified items against both shared acceptance and these iOS conditions. Resolve follow-up roles with the inherited entrypoint and `--platform ios`; reading a base procedure must not recursively re-enter this role.
