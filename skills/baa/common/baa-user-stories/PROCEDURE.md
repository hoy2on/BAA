---
name: baa-user-stories
description: Organize shared user requirements and platform acceptance into stories, backlogs and implementation order for BAA.
---

# User stories

Read the [shared execution rules](../../EXECUTION.md). Inherit BAA's selected platform, purpose, current stage, file ownership and acceptance; do not repeat target selection or restart planning. Respond in the user's language and follow project documentation/localization conventions.

Resolve follow-up roles with `python3 scripts/resolve.py --entrypoint <entrypoint> --platform <target> --step <role>` from the runtime root. Use the returned name/path, not upstream short names or external installations. Read the returned PROCEDURE.md, not a Skill-tool/slash command. Read relevant returned references when present.

The coordinator is the sole editor of shared BRIEF/STORIES/GLOSSARY/research/review documents. Platform owners return proposals and evidence, not concurrent edits. In solo execution, the current worker holds that role.

Turn screens into user actions and verifiable acceptance. Preserve BAMA/BAWA stories, dependencies, milestones, UX blocks and verification tags.

## Read and map

Read BRIEF, research feature matrix, screen index and task records. The coordinator owns one shared story list; do not duplicate the same feature per platform. If the project already has task management conventions, add equivalent information there.

```markdown
### S-012 Complete an item
As the user, I can complete an item and undo a mistake.
Platforms: selected targets among macos, windows, ios, ipados, android
Screens: reference screen or runtime state to verify
Depends: S-004
Acceptance:
- [unit][shared] Completion and undo preserve the data.
- [snap][<platform>] The specified screen shows the completed state.
- [self/manual][<platform>] Complete and undo through the platform's input/navigation.
Status: todo
Platform status: <platform>: todo / doing / done / blocked / not-applicable
```

Each story covers one action and completes a screen with its screen-specific controls. Acceptance names the method ([snap], [unit], [self], [manual]) and applicable platform. Shared unit tests do not establish native UI success. Specify keyboard/menu/Back/permission criteria per platform.
Order dependencies first; distinguish shared data/API contracts from allowed platform differences. Preserve todo/doing/done/dropped states and record environmental waits with reasons/resumption conditions. A story is done only when required selected-platform conditions are met. Platform owners propose status; the coordinator records it.

## Milestones

Each milestone ends with a runnable useful flow. Core loop → Organize → Time → Speed → System → Polish is an example, not a required product shape. Keep necessary actions and attach OS integrations to relevant stories. Reconsider scope/dependencies when the list is large; do not drop requirements to meet an arbitrary count.
Use seed data/state the user can actually create. Do not inject unsupported feature data to simulate implementation. Record excluded requirements as Dropped/Later with reasons; don't routinely exclude requested accounts/sharing/services.

## UX and handoff

Resolve ux-design for stories with new screens/behavior/copy to fill UX and terminology. Improve-loop fills missing UX before later milestones. For an existing-screen design-only task, specify only that screen/state's criteria, not a full backlog.
Done when in-scope actions, features and reference screens map to stories or explicit exclusions, with matching UX/platform verification/dependencies/status.
