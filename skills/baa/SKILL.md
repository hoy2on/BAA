---
name: baa
description: BAA (Build Any App) central router. Identify app development, design, and review targets from the request and project evidence, then connect Apple, Android, and Windows specialist procedures. Use when the user invokes BAA or requests app work across platforms.
---

# BAA — Build Any App

Read the [execution rules](EXECUTION.md). This plugin includes BAMA/BAWA-based procedures and mobile specialists.
For a direct `/baa` call, the entrypoint is `baa`. When `/baa-apple`, `/baa-android`, or `/baa-windows` delegates here, preserve that entrypoint and its allowed scope.
Respond in the user's language unless requested otherwise. Follow the project's documentation and localization rules; English internal instructions do not change app copy, existing translations, or the required output language.

## 1. Identify the target

The `entrypoints` in the [routing catalog](routing.json) define allowed platforms: `baa` allows macOS, iOS, iPadOS, Android and Windows; `baa-apple` allows macOS/iOS/iPadOS; `baa-android` allows Android; `baa-windows` allows Windows.
An entrypoint limits this invocation. Apply a newly invoked command's scope; do not freeze a previous direct command's restriction for the entire conversation.

Use the following evidence in order:

1. Platforms explicitly requested as work targets. Normalize iPhone to iOS, iPad to iPadOS, and Mac to macOS. Mentioning a reference or comparison app does not add its platform to the work.
2. Targets already agreed for the same task. Re-evaluate when the request changes the target or points to different files/modules.
3. The real targets containing the specified file/module: Xcode supported platforms/device families/schemes, Gradle source sets/modules, Windows project targets and callers.
4. Supported project targets relevant to this request. Select a sole candidate; do not arbitrarily select all when several remain.

Candidates must be within the entrypoint scope. If the command and request conflict (such as `/baa-android` requesting Windows), or the specified file belongs outside the allowed scope, explain and confirm the target before editing. Do not forward automatically to another platform.
Absent a contradiction, a direct Android/Windows command determines its target. If the existing project lacks that target, clarify whether adding support is intended instead of selecting another platform.
If evidence is insufficient, present the candidates and ask once which platform to work on. Until answered, perform read-only investigation only. `/baa-apple` selects an Apple family, not all three Apple platforms automatically.
Do not infer the target solely from Swift/Kotlin, a file extension, or the host OS. A shared Swift file included in macOS/iOS/iPadOS has multiple candidates.
For an existing project, “all” means all verified supported targets within the entrypoint scope; for a new app, it means all allowed platforms. Do not add missing targets without a request. Shared iOS/iPadOS sources still require separate device/runtime verification.
Briefly state the selected platform and evidence, and identify the purpose: new app, feature change, design improvement, research/review, or build/verification. Do not re-ask clear targets or purposes.

## 2. Connect platform owners and stages

The runtime root is the actual directory containing this SKILL.md. Resolve symlinks first (for example, `Path(<SKILL.md path>).resolve().parent`). Plugin installs and skills CLI copies use procedures/tools/templates inside this folder. Derive paths from the current installation, never a fixed source checkout.
Resolve each target's `router` first and read its stage-selection procedure. Do not recursively enter an already-read platform router.

```sh
python3 <runtime-root>/scripts/resolve.py --entrypoint <entrypoint> --platform <target> --step router
python3 <runtime-root>/scripts/resolve.py --entrypoint <entrypoint> --platform <target> --step <role>
```

`routing.json` is the single role-to-document map. start/plan/code/design/ship are task categories, not mandatory execution order. For iOS/iPadOS, `path` identifies the OS specialist and `references` includes reusable apple/shared guidance. Read the returned PROCEDURE.md and relevant references; do not invoke internal names as Skill-tool or slash commands. All four public entrypoints share these rules.
macOS uses the BAMA-based pack, Windows the BAWA-based pack, and iOS/iPadOS/Android their specialists.

- New app: research → optional clone → app-brief → user-stories → ux-design (visual direction/interactions) → scaffold → native-design + design-system + app-icon → improve-loop.
- Existing feature: inspect requirements/current work list → relevant ux-design → code/os-integrations → build-and-verify + test.
- Design only: relevant ux-design → native-design → needed design-system/design-kit/design-from-app/layout-grid → build-and-verify and affected tests.
- Performance: performance → fix the verified cause → affected checks. Use improve-architecture for structure changes.
- Review only: read the role and return observations/proposals. Do not start edits, scaffolding, installation or commits.
- Distribution request: use the platform's distribute procedure or actual project release workflow, within the authorized external-publication scope.

For UI structure, visuals or interaction, apply [design intelligence](common/baa-ux-design/design-intelligence.md). If ui-ux-pro-max is installed, search from its actual location and validate platform fit. Otherwise use packaged guidance and do not claim a search was performed. Distinguish new visual direction from a local existing-screen fix. The coordinator decides shared direction once and passes it to owners. Apply [UI review](common/baa-ux-design/ui-review.md) to changed UI on the selected platform; omit design searches for non-UI work.
Do not redo the entire plan or preload every document for an existing app. Do not convert its technology to match a starter template.

## 3. Shared decisions and platform assignments

Decide common behavior, terminology, data contracts and acceptance once. Inspect sources/tests/resources to assign platform files and one owner for shared files.
Common procedures do not permit adding UI/features outside a direct entrypoint's scope. Make only selected-target changes in shared files and report effects on unselected targets.
Assign independent platform work through available subagent tools. If iOS/iPadOS/macOS edit the same files, use one Apple owner or integrate shared work first. Split only independent sources, respect slot limits, and report sequential execution if agent tools are unavailable. Do not ask owners to create another team.
A handoff includes entrypoint/allowed scope, selected targets/evidence, purpose/current stage, project/actual stack, owned files/exclusions, shared contracts, acceptance, resolved procedure paths and verification environment. Owners must not restart target selection or planning.
Explicitly say: “Other workers are editing concurrently. Do not revert their changes; return proposals for changes outside your ownership.” The coordinator updates shared document status and integrates shared changes.

## 4. Integrate and finish

Check source state, target, verification environment, evidence and unverified items before integration. If another change invalidates evidence, rerun only affected checks.
Report code completion, builds, UI execution and hardware verification separately by platform. Continue independent work when a platform is blocked. Do not claim overall completion while required verification remains; leave evidence and resumption conditions.
