---
name: baa-improve-loop
description: Implement an agreed backlog in functional increments with builds, tests and screen comparisons, for milestone completion or continuing in-scope work.
---

# Improve loop

Read the [shared execution rules](../../EXECUTION.md). Inherit BAA's selected platform, purpose, current stage, file ownership and acceptance; do not repeat target selection or restart planning. Respond in the user's language and follow project documentation/localization conventions.

Resolve follow-up roles with `python3 scripts/resolve.py --entrypoint <entrypoint> --platform <target> --step <role>` from the runtime root. Use the returned name/path, not upstream short names or external installations. Read the returned PROCEDURE.md, not a Skill-tool/slash command. Read relevant returned references when present.

The coordinator is the sole editor of shared BRIEF/STORIES/GLOSSARY/research/review documents. Platform owners return proposals and evidence, not concurrent edits. In solo execution, the current worker holds that role.

Preserve the shared BAMA/BAWA iteration:

```text
pick → plan → code → build/test/snapshot → compare → fix → commit(if authorized) → update STORY → repeat
```

Stop at the requested milestone/features. If unspecified, use the agreed current milestone, not the whole product. Do not implicitly add scaffolding or distribution.

## 1. Pick and claim

Choose the next in-scope item with satisfied prerequisites from existing STORIES/tasks. The coordinator assigns per-platform files and shared data/behavior contracts, and alone records todo → doing → done. Platform owners return progress/status proposals rather than editing the shared story file.
Inherit target/current stage, source state, actual stack, owned files, I/O contracts and acceptance. Assign overlapping Apple sources to one owner or complete predecessor changes first.

## 2. Plan

Resolve ux-design if UI/action/copy acceptance is incomplete. Briefly identify affected callers/models/tests/resources, screen states and environment. Review defaults/migrations and the current storage's compatibility path for schema/field changes. Never reset data to bypass the problem.

## 3. Code

Resolve target code/native-design and implement within the UX block, existing design definitions and ownership. Add os-integrations only when needed. Use resolver-returned names/paths, not guesses. Don't replace language/control/state technology with another platform's approach.
Connect new screens to the project's actual navigation/test/snapshot lists; don't assume SidebarItem/SidebarPage enums or seed environment variables exist. Preserve others' edits, validation and error handling.

## 4. Build, test and snapshot

Resolve build-and-verify/test. Add or update appropriate checks for nontrivial logic/bug fixes and verify reproducing conditions. Reuse existing tests/self-tests/UI automation/seed data and user-creatable states.
Verify modified screens and adjacent flows first; expand at milestone end for impact/required checks. Cover supported light/dark, size/scale/input and accessibility states. Isolate test data from user storage and preserve Release. Serialize only shared device/output/designated dev-install conflicts.

## 5. Compare and fix

Compare actual runtime screens/interactions with references/acceptance in this order: missing behavior/wrong data/recovery/preservation; agreed UX naming/flow/state/feedback; structure/order/missing elements/layout failures; then hierarchy/spacing/alignment/type/color/details.
Without a reference use acceptance/native-design. Unless exact pixel reproduction was requested, prefer native controls/input. Match data/viewport/scale/state when comparing captures.
Distinguish product defects, test expectations and automation/permission/device failures. Form a hypothesis from logs/screens/source, make the smallest fix and rerun affected checks. Do not repeat identical commands without new evidence/change/environment. If required runtime/permissions are unavailable, leave that platform pending with attempts/reason/resumption conditions; continue independent items. Never mark an unpassed item done.

## 6. Commit and record

When authorized, commit relevant functional code/tests and coordinator-integrated status. Do not bulk-stage unrelated/user/other-worker files. Without commit permission, hand off the verified diff and status proposals. Owners must not concurrently edit shared STORY/FIXLOG/GLOSSARY or commit another owner's incomplete work.
The coordinator verifies per-platform results and evidence for integrated sources before status updates. Re-evaluate evidence if shared code changed after checks. Record necessary FIXLOG symptom/cause/fix/Rule once.

## 7. Report and milestone check-in

Return completed behavior; per-platform source/target/device/checks; screen/log paths; pending items/resumption; manual user acceptance; and the next item. If running the app was requested, make the designated dev app usable. Don't create Release or extra installs merely for reporting.
At milestone completion use improve-architecture to review current structure. Do not start the next milestone automatically or treat autonomous work as authorization for scope expansion, publication or data deletion.
Done when each in-scope platform is verified or explicitly waiting on an environment, shared contracts/integrated-source required checks are confirmed, and evidence/remaining work are handed off. Required pending checks preclude overall completion claims.
