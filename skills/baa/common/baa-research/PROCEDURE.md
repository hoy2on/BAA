---
name: baa-research
description: Organize sources, comparisons and decision evidence for cross-platform app research, feature/API comparisons and BAA research stages.
---

# Research

Read the [shared execution rules](../../EXECUTION.md). Inherit BAA's selected platform, purpose, current stage, file ownership and acceptance; do not repeat target selection or restart planning. Respond in the user's language and follow project documentation/localization conventions.

Resolve follow-up roles with `python3 scripts/resolve.py --entrypoint <entrypoint> --platform <target> --step <role>` from the runtime root. Use the returned name/path, not upstream short names or external installations. Read the returned PROCEDURE.md, not a Skill-tool/slash command. Read relevant returned references when present.

The coordinator is the sole editor of shared BRIEF/STORIES/GLOSSARY/research/review documents. Platform owners return proposals and evidence, not concurrent edits. In solo execution, the current worker holds that role.

Investigate user tasks, competing apps and implementation constraints on selected platforms. Preserve the BAMA/BAWA research → merge → planning handoff.

## 1. Frame

State the research question and the resulting decision in one sentence each. Read existing BRIEF, research and screen indexes first. For a local issue in an existing app, research only relevant API/behavior questions; do not add market research or a new plan.

## 2. Tracks

Select only needed tracks. Product direction includes Market and Reviews; API selection emphasizes Platform and relevant Features.

- Market: competitors with verified platforms, pricing and core features.
- Reviews: what people like/dislike; distinguish store/forum opinions from verified product facts.
- Features: documented behavior/limits from official manuals, help and changelogs.
- Design: screens, navigation, input and accessibility; record platform differences separately.
- Platform: official APIs, permissions, supported OS, distribution/identity constraints and existing project implementations.

The coordinator may assign independent research to existing workers. Work sequentially when tools/scope do not permit parallel work; platform owners do not create nested research teams. Researchers return sources/proposals without editing files.
Handoffs specify question, decision, platform, scope, preference for official sources and output format. Label claims `[V]` source-verified, `[K]` knowledge-based or `[U]` unverified, with URL and check date. Verify prices/current APIs/supported versions live. Do not claim to have read inaccessible material.

## 3. Merge

For each question, update one existing research document or `docs/research/<topic>.md` with question/targets/date/scope, competitors' strengths/friction/sources and recurring user needs, a feature/comparison-app/platform/in-scope matrix, decisions/reasons/evidence/verification, and consequential `[U]` questions with the smallest confirming experiment.
Pass included matrix features to user-stories; retain meaningful user benefits as decisions or accepted differences. Evaluate storage/sync fit without treating research as permission to adopt services or connect accounts. Check Windows package identity/OS availability, Apple entitlements/OS support, and Android SDK/permission/execution restrictions. Do not recommend an active database in a sync folder without investigating operational risks.

## 4. Hand off

Resolve the selected platform's clone role if observing a reference app is necessary. Without app/browser access, use public help and sourced screenshots, recording limitations. Use app-brief for a new app outline; local research requests end with findings.
Done when selected tracks are merged, included features/decisions have sources or explicit verification plans, and unknowns remain distinct from verified facts.
