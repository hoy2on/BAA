# BAA shared execution rules

Use BAA's packaged BAMA macOS, BAWA Windows, common and mobile procedures. Do not resolve same-named procedures from external BAMA/BAWA installations. User requests, project instructions and these rules take precedence over upstream fixed paths, personal-app assumptions and new-project examples.

## Language

Internal instructions use English. Respond in the user's language unless the user requests another language. Follow project conventions for documents, source comments and localization. Preserve existing app strings and translations; translating internal instructions does not authorize translating product UI or user data. Keep code identifiers, paths, CLI flags and error originals intact where they matter. Provide English and Korean usage guides through README.md and README.ko.md.

## Procedure connections

Pass entrypoint, allowed platforms, selected target/evidence, purpose/current stage, project path/stack/supported OS, story/screen, owned files/shared contracts, acceptance and environment to follow-up procedures. Do not re-ask the target.
The runtime root is the directory containing this document. Never hard-code a user's home or cache name. Resolve the exact role, for example:
`python3 <runtime-root>/scripts/resolve.py --entrypoint <entrypoint> --platform <target> --step build-and-verify`.
Read the returned `path`'s PROCEDURE.md. Public entrypoints are baa, baa-apple, baa-android and baa-windows. Preserve routing.json entrypoint restrictions. Internal procedures are documents, not Skill-tool/slash commands.
For a packaged unique name, use `python3 <runtime-root>/scripts/resolve.py --entrypoint <entrypoint> --name <unique-name>`. Never substitute another platform's procedure by guessing. Preserve the direct entrypoint downstream; do not change it to baa to bypass an error. Name lookups are scoped too.
Check the host's actual Python executable. If Python is absent, inspect routing.json entrypoint permissions and select the same platform/role document directly. Do not install a runtime automatically or substitute another platform.
Unique names identify packaged internal documents. Resolve relative tools/templates from that procedure's folder. The host CLAUDE_SKILL_DIR may still identify the public entrypoint: before each internal command set BAA_SKILL_DIR to the parent of the resolver-returned PROCEDURE.md, not the public skill directory.

Folders categorize tasks: start (router/scaffold), plan (clone), code (implementation/OS integration/performance/agent CLI), design (native UI/tokens/assets), ship (build/test/distribution). They are not a required sequence.
iOS/iPadOS each have start/plan/code/design/ship specialists and specs. The role path points to its OS procedure, with apple/shared base procedures in references. Preserve device-specific requirements; shared guidance is not permission to add other platforms and does not route through macOS. Keep desktop tools/templates and platform-independent common procedures in their existing locations.
Common roles: research, app-brief, user-stories, ux-design, improve-architecture, improve-loop. Platform roles: router, clone, scaffold, code, native-design, design-system, design-kit, design-from-app, layout-grid, app-icon, os-integrations, performance, build-and-verify, test, agent-cli, distribute. Missing combinations return an error.
For macOS distribute, inspect the real channel/workflow. Distinguish direct distribution from App Store workflows and authorize build/package creation, notarization, upload, store submission and installation as separate stages.

## Scope

Preserve the project's technology, components, data and API compatibility. A SwiftUI/WinUI starter does not authorize converting UIKit/WPF/Views/cross-platform code. Choose a suitable starter only for a new app.
Do not remove requested accounts, sync, payment or sharing because an upstream example assumes a personal app. Design-only work starts in the design branch, not a new brief/scaffold. Review-only work returns observations/proposals without edits, installation or commits.
Upstream OS/SDK defaults describe starter baselines, not permission to raise existing deployment targets or dependencies. Confirm required APIs with installed versions/current official documentation; inspect existing capabilities before adding a package.

## UI design evidence and review

For UI changes apply [design intelligence](common/baa-ux-design/design-intelligence.md), then [UI review](common/baa-ux-design/ui-review.md) for the target and changed scope. Use installed ui-ux-pro-max local searches where relevant; SDK/platform requirements prevail over generic results. Without that skill use packaged guidance. Do not force searches for backend or nonvisual scripts.
The coordinator alone edits shared visual decisions, canonical design documents, MASTER and page overrides. Platform owners inherit verified decisions and propose deltas rather than regenerating the same system concurrently. Do not copy the search database/scripts into BAA or add public commands.

## Parallel work

The coordinator decides shared requirements and file ownership, then hands each selected target's router/role paths to its owner. Preserve entrypoint restrictions, evidence and current stage; owners do not repeat platform selection. Explicitly tell owners others are working and they must not revert their changes.
Assign one owner for shared models/APIs/translations/project files/lockfiles/task documents. Platform owners propose shared-document updates to the coordinator.
Apple platform names alone do not imply independent files. Group overlapping sources under one owner or integrate predecessor work before follow-up. Parallelize only independent work. Platform owners must not create nested teams; upstream research/suite team creation must not duplicate coordinator assignments. Queue within slot limits and state when tools require sequential execution.
Do not concurrently mutate the same build output, simulator, device or designated dev install; serialize only conflicting checks. Do not create extra installed app copies for parallelism. Create a needed worktree from the current branch HEAD; upstream BAWA suite instructions to merge main do not grant user authorization.

## Installation and user data

Before installing, verify actual product name, ID, signing, build variant and every termination/deletion target. Release and development apps must coexist.
macOS uses one `/Applications/[actual-product-name]-dev.app` and an ID distinct from Release. iOS/iPadOS/Android/Windows also use one existing designated dev variant; establish separation first if absent.
Host and target differ: editing Windows sources on Mac does not supply a Windows runtime. Do not delete or automatically migrate Release apps, user documents/history/recordings/settings/keychain/shared storage. Inspect upstream scripts against these rules before running; prefer the project's existing workflow. Keep CLI/MCP/deep-link/IPC channels from mixing dev and release data.

## Verification, handoff and commits

Inspect the real build/test/UI workflow. Do not assume upstream-only APP_SEED, SidebarItem or capture tools exist. Verify a representative executable flow first, then expand as needed.
UI changes require actual runtime screens/interactions. Separate build success from runtime success and name simulator/emulator/hardware/remote environments. Report unavailable checks as unverified/pending. Use remote devices or CI only when actually available and authorized.
Return changed files, acceptance, source state/target/environment, commands/results, screen/log paths, shared proposals, blockers and resumption conditions. Recheck evidence validity after shared-source integration. Do not repeat failures without a new hypothesis/change; separate product defects from build/detection/permission issues.
Upstream automatic commits, git add -A and distribution steps do not expand permissions. Commit only owned relevant files under current user authorization and the project's commit workflow, without Co-Authored-By. Signing/package creation is separate from external publication.
