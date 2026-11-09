---
name: baa-ux-design
description: Design action names, flows, surfaces, states, copy and accessibility for story UX blocks and existing-screen usability reviews.
---

# UX design

Read the [shared execution rules](../../EXECUTION.md). Inherit BAA's selected platform, purpose, current stage, file ownership and acceptance; do not repeat target selection or restart planning. Respond in the user's language and follow project documentation/localization conventions.

Resolve follow-up roles with `python3 scripts/resolve.py --entrypoint <entrypoint> --platform <target> --step <role>` from the runtime root. Use the returned name/path, not upstream short names or external installations. Read the returned PROCEDURE.md, not a Skill-tool/slash command. Read relevant returned references when present.

The coordinator is the sole editor of shared BRIEF/STORIES/GLOSSARY/research/review documents. Platform owners return proposals and evidence, not concurrent edits. In solo execution, the current worker holds that role.

Use BAA's name → flow → surface → states → copy → supporting explanation → accessibility → UX record. Separate shared meaning from native expression.
Apply [design intelligence](design-intelligence.md) for visual/usability decisions. Evaluate coherent candidates for new direction; target only the relevant outcome for existing-screen problems. Do not regenerate searches/MASTER if the coordinator already supplied verified decisions. Use [UI review](ui-review.md) for changed UI handoff.

## 1. Read and name

Read existing BRIEF, GLOSSARY, relevant story/screens and references. Do not create a new plan for an existing-screen review. Keep product terminology consistent across controls/headings/errors; preserve platform action naming/capitalization and project localization conventions. Copy describes user actions, not internal models/technology.
The coordinator owns common terms; platform owners propose new terms/native differences. Do not edit the same localization file concurrently.

## 2. Map the flow

Write entry → completion → return for every entrypoint. Avoid unnecessary navigation to change an existing value. Define initial values, focus/keyboard, save/cancel, failure recovery and destructive-action confirmation/undo. Touch-only platforms must not require hover/keyboard. Keep essential help and actions discoverable without hover.

## 3. Pick the surface

Prefer inline edits for current values, nearby choices for short selections, platform-appropriate screens/modals for independent tasks, and established navigation for recurring features. Resolve native-design for specific controls/API/layout and adaptive/multi-window requirements. Mac inspectors/sheets, Tauri frontend dialogs/native OS dialogs and mobile navigation/sheets have different implementation and focus requirements.
Do not turn informational status into needless alerts. Modal titles/completion buttons describe the action; define dismissal/return when input can be lost. Confirm actual nested-presentation constraints.

## 4. Cover states and words

Define applicable empty/loading/error/long-content/success/undo content, actions and appearance. Use determinate progress only when known. Errors explain location/cause scope/recovery and preserve input. Do not communicate meaning only through color or brief animation.
Buttons name actions; destructive confirmation names the object and consequence. Don't present guesses as facts. For AI, distinguish generation/progress/failure/cancel/review/apply and preserve originals until reviewed. Copy and accessible names describe the real behavior.
Add supported tooltips/help without making them the only route to necessary information. Icon controls expose names, roles and state through native accessibility APIs.

## 5. Accessibility and proof

Resolve native-design, test and build-and-verify for the current stack. Verify text scaling, contrast/theme, screen-reader naming/order/state, focus and supported inputs. Don't apply fixed Mac font sizes to mobile. Unperformed accessibility interactions remain unverified.

## 6. UX block

```markdown
UX:
- Flow: entry → input/selection → completion feedback → cancel/return
- Surface: platform-specific presentation and rationale
- States: applicable empty/loading/error/long/success states and behavior
- Words: shared terms, action copy and native wording differences
- Access: input/focus/screen-reader/text-scaling requirements
- Proof: screens/states/interactions and runtime environment
```

The coordinator integrates into an existing story/design document. Platform owners return differences and evidence. Review requests end with findings/proposals, not implementation.
Done when action names, surfaces, return behavior, states, copy and accessibility criteria are decided, with actual verification and remaining checks distinguished.
