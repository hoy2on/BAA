---
name: baa-ios
description: BAA iOS platform owner entrypoint. Connect assigned iOS work to shared planning and platform-specific code, design and verification.
---

# BAA iOS owner

Read the [execution contract](../../../../../../EXECUTION.md). A direct platform assignment selects iOS. Inherit the coordinator's entrypoint/allowed scope, target, project, purpose/current stage, owned files and acceptance; do not reselect the target or restart planning. Explain conflicting requests before editing, without switching platforms based on host OS.

## Target and ownership

Inspect actual modules/targets/stack/supported OS/dev ID/build-test commands and callers for the assigned behavior. Only assigned owners edit shared sources/models/translations/project configuration. Preserve others' changes; propose additional shared edits with impact and continue independent work first. Do not create a nested team. Serialize only runs sharing a device/output/designated dev install.

## Stage routing

Resolve exact names and PROCEDURE.md paths from the runtime root with `python3 scripts/resolve.py --entrypoint <entrypoint> --platform ios --step <role>`. Read one needed role at a time; follow-up roles retain this target. Never select another platform's same-named procedure. Planning/general UX/improvement are shared; code/native UI/OS APIs/build/tests use platform mappings.

- Research/planning: research → optional clone → app-brief → user-stories → ux-design.
- New app: scaffold → native-design plus needed design-system/app-icon → current story code.
- Existing feature: code plus needed os-integrations/performance → build-and-verify/test.
- Design-only: ux-design for flow/copy issues, native-design → relevant design-system/design-kit/design-from-app/layout-grid/app-icon → build-and-verify/test.
- Architecture: improve-architecture; agreed backlog iteration: improve-loop.
- Agent control/distribution: agent-cli/distribute only when explicitly part of the task.

Reuse existing briefs/stories/design docs and start at the current required stage. Don't fork/overwrite common documents being written by the coordinator. If a follow-up points back here, execute the current role rather than recursively entering the router.

## Platform conditions and handoff

Use iOS specialists plus their shared bases while preserving device family/purpose. Shared iPhone/iPad targets still need separate destinations/screens/input proof. Check iPhone navigation, touch, keyboard, safe area and Dynamic Type; don't add iPad support when it wasn't requested.
Separate implementation/static checks from pending runtime when permissions/environments are absent. Other-OS tools or empty results are not execution success. Return per-acceptance changed files, source/target/environment, checks/screens/logs, unverified items and shared-change proposals.
Done when roles route to the correct platform and implementation, actual verification and environmental waits are distinct.

## Example plans

Read [platform specs](../../../specs/README.md) when a new-app example is needed. Existing app tasks do not require example plans.
