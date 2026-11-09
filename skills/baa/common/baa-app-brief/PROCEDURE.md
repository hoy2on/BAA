---
name: baa-app-brief
description: Define app purpose, minimum jobs, data and target platforms in a one-page brief when turning ideas/research into implementation scope.
---

# App brief

Read the [shared execution rules](../../EXECUTION.md). Inherit BAA's selected platform, purpose, current stage, file ownership and acceptance; do not repeat target selection or restart planning. Respond in the user's language and follow project documentation/localization conventions.

Resolve follow-up roles with `python3 scripts/resolve.py --entrypoint <entrypoint> --platform <target> --step <role>` from the runtime root. Use the returned name/path, not upstream short names or external installations. Read the returned PROCEDURE.md, not a Skill-tool/slash command. Read relevant returned references when present.

The coordinator is the sole editor of shared BRIEF/STORIES/GLOSSARY/research/review documents. Platform owners return proposals and evidence, not concurrent edits. In solo execution, the current worker holds that role.

Preserve BAA's one-page BRIEF → user-stories/scaffold connection. Local existing-screen design work does not require a new BRIEF.

## 1. Name and read

Confirm existing project path, product name and supported platforms. For a new project use the user's name/location; resolve missing consequential details from context or ask only what is needed. Do not silently create a folder and treat it as agreed.
Read existing docs/BRIEF.md, docs/research/, docs/screens/INDEX.md and supplied specs. Integrate spec Brief/Stories into existing docs without changing their meaning/scope; link detailed behavior/gotchas through docs/SPEC.md. Preserve originals and do not repeat answered questions.

## 2. Resolve the scope

Preserve settled choices. Clarify only consequential unknowns; if autonomous decisions were requested, record your evidence and choices.
Determine the user/job and replacement habit/app; common actions/data; selected platforms/devices/OS/actual technology; screen/navigation/entrypoints; OS hooks/permissions; offline/server/account/sync/payment/privacy needs; reference/look/shared vocabulary/brand/native differences; and the minimum completion flow and explicit exclusions.
Do not remove requested services/accounts/sharing/onboarding under a personal-app assumption. Keep the smallest useful flow while explaining scope changes. Do not promise screen counts or development time without evidence.

## 3. Write BRIEF

The coordinator writes about one page without duplicating existing documentation.

```markdown
# <AppName>
One-sentence purpose and audience.
## Replaces
The app/habit replaced, or the existing product behavior improved.
## Main jobs
Primary user actions.
## Data
Data and preservation/compatibility requirements.
## Platforms and shape
Selected platforms, actual technology/supported OS, screens and navigation.
## System hooks
OS capabilities, permissions and platform differences.
## Reference and look
References, shared visual intent and native platform expression.
## Operating constraints
Verified offline/service/account/sync/privacy requirements.
## Not in this scope
Agreed exclusions and remaining verification.
```

## 4. Hand off

Resolve user-stories for features/acceptance. If requirements are sufficient and a new runnable skeleton is requested, resolve the target's scaffold. Write a multi-platform brief once, assigning implementation per platform. New-app instructions do not authorize regenerating an existing app.
Done when purpose, data, targets/screen shape, operational limits and scope are clear enough for stories/scaffold.
