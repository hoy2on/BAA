---
name: baa-apple-performance
description: Apple mobile performance procedure for the assigned platform and current app workflow.
---

# Apple mobile Performance

Read the [BAA execution rules](../../../../../../EXECUTION.md). Inherit platform, purpose, owned files and acceptance. This internal procedure does not restart platform selection or team creation; preserve other workers' changes.

## Execution

Fix the slow scenario, device/OS, configuration, data and metrics before editing. Don't add speculative caches/async layers without symptoms.
Choose symptom-appropriate Instruments Time Profiler, SwiftUI/animation/hitch, Allocations/Leaks and existing signposts/metrics. Confirm installed CLI help for automation.
Trace UI-thread parsing/image decoding/files/DB work; narrow SwiftUI invalidation/identity/excess state publishing and UIKit reuse/constraint cost with evidence. Use display-sized decoding/downsampling, existing lazy/reuse patterns and lifetime-aware cancellation. Don't add NSCache, Task.detached or storage layers without measurements.
Check affected memory warnings, foreground/background transitions and cancellation. Preserve data, accessibility and correctness. Compare before/after on relevant physical iOS/iPadOS devices under identical scenarios; Simulator metrics are not hardware results.
Done when cause/fix/comparable metrics/regression evidence exist, or actual measurement limitations are explicit.

## Follow-up and handoff

Resolve subsequent roles from the runtime root with `python3 scripts/resolve.py --entrypoint <entrypoint> --platform <assigned-platform> --step <role>`. Read the returned PROCEDURE.md; do not use internal names as Skill-tool/slash commands. Do not recurse into the current stage or add unrequested distribution, installation or commits.
Return changed files, source state/target/environment, check/screen/log paths, unverified items and shared-change proposals to the coordinator.

Official references: [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/), [SwiftUI](https://developer.apple.com/documentation/swiftui), [UIKit](https://developer.apple.com/documentation/uikit), [XCTest](https://developer.apple.com/documentation/xctest). Confirm API availability/signatures against the installed SDK and project minimum OS.
## Supporting reference

Read [recipes.md](recipes.md) when performing this role; keep the assigned platform and scope.
