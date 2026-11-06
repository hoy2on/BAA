---
name: baa-apple-distribute
description: Apple mobile distribute procedure for the assigned platform and current app workflow.
---

# Apple mobile Distribute

Read the [BAA execution rules](../../../../../../EXECUTION.md). Inherit platform, purpose, owned files and acceptance. This internal procedure does not restart platform selection or team creation; preserve other workers' changes.

## Execution

Apply only to explicit distribution/archive/TestFlight/App Store requests; a dev build is not publication authorization.
Inspect actual release scheme, bundle ID, marketing/build policy, team/provisioning/entitlements, privacy/usage descriptions and extension IDs. Don't merge dev/release data or keychains automatically.
Prefer existing archive/export scripts/CI and installed Xcode export options. Archive the real generic iOS destination/release configuration; don't disguise distribution-signing failure with ad-hoc signing. Run existing tests/release checks and review changed metadata/privacy/device-support requirements. Declared iPad support needs separate iPad screens/assets verification.
Distinguish local archive/package, upload, TestFlight rollout and store submission; perform only authorized stages. Keep credentials/signing secrets out of documents. Never overwrite/install Release merely because an archive was created.
Done when actual stages/artifacts/logs/external submissions and remaining user work are explicit.

## Follow-up and handoff

Resolve subsequent roles from the runtime root with `python3 scripts/resolve.py --entrypoint <entrypoint> --platform <assigned-platform> --step <role>`. Read the returned PROCEDURE.md; do not use internal names as Skill-tool/slash commands. Do not recurse into the current stage or add unrequested distribution, installation or commits.
Return changed files, source state/target/environment, check/screen/log paths, unverified items and shared-change proposals to the coordinator.

Official references: [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/), [SwiftUI](https://developer.apple.com/documentation/swiftui), [UIKit](https://developer.apple.com/documentation/uikit), [XCTest](https://developer.apple.com/documentation/xctest). Confirm API availability/signatures against the installed SDK and project minimum OS.
