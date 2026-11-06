---
name: baa-improve-architecture
description: Inspect difficult-to-change app structure and propose minimal behavior-preserving refactors during architecture reviews or milestone check-ins.
---

# Improve architecture

Read the [shared execution rules](../../EXECUTION.md). Inherit BAA's selected platform, purpose, current stage, file ownership and acceptance; do not repeat target selection or restart planning. Respond in the user's language and follow project documentation/localization conventions.

Resolve follow-up roles with `python3 scripts/resolve.py --entrypoint <entrypoint> --platform <target> --step <role>` from the runtime root. Use the returned name/path, not upstream short names or external installations. Read the returned PROCEDURE.md, not a Skill-tool/slash command. Read relevant returned references when present.

The coordinator is the sole editor of shared BRIEF/STORIES/GLOSSARY/research/review documents. Platform owners return proposals and evidence, not concurrent edits. In solo execution, the current worker holds that role.

Preserve BAMA/BAWA's survey → propose → refactor → record workflow. Reduce current change cost, not unify platform technology or add layers.

## 1. Survey

Begin read-only. Read project instructions, ARCHITECTURE, ADR, FIXLOG and relevant sources. Use history, large files, recurring bugs, numerous callers, broad UI updates, slow UI-thread work and testing friction to find real hotspots. File size is a signal, not sufficient reason to split.
Map targets/modules/dependency direction, domain versus UI/I/O boundaries and thread/lifecycle ownership. Resolve code/performance/test for actual language/framework constraints. Inspect state objects owning many screens; pass-through wrappers/speculative single-implementation interfaces; pure logic/slow work/synchronous waits tied to UI; private cross-module coupling and divergent copies; test access exposed to production data; distant related views/settings/tests; and shared ownership conflicts.
Use the deletion test: if removing a module concentrates complexity, it may be simplifiable; if complexity spreads to every caller, the boundary may be justified. Don't assume template-specific types/APIs exist everywhere.

## 2. Propose

In the existing review document or docs/architecture-review-<date>.md, record files, observed signals, an example currently difficult change, minimal proposal, caller impact, equivalence proof and sequence. Grade Strong / Worth exploring / Speculative. Identify the preferred proposal and considered alternatives not recommended. No justified change is a valid result.
Review-only work ends with proposals. Proceed within already-authorized refactoring scope without repeated approval, but do not add unapproved features/data changes. During improve-loop milestone review, apply only current-feature Strong proposals within existing authority; leave others as proposals.

## 3. Refactor and prove

Before editing, capture relevant unit/integration/self-tests, screens/interactions, golden outputs, existing data/settings loading and necessary performance evidence. Use test/build-and-verify; unavailable checks remain pending.
Change one structural concern at a time without mixing features. Prefer existing boundaries/types; introduce abstraction only for demonstrated caller/testing benefit. Preserve validation/error handling/compatibility when moving callers and safely remove obsolete paths. Don't routinely add temporary flags or dual compatibility paths.
One owner changes shared API/data/project contracts and checks affected platform regressions. Preserve other workers' edits. Compare affected checks against prior evidence and fix behavioral differences. Follow current commit authorization/project procedure; do not stage unrelated files.

## 4. Record

Update existing ARCHITECTURE boundaries/dependencies when structure changes. Add ADR only for consequential difficult-to-reverse decisions and real tradeoffs. Record a discovered/fixed bug's symptom/cause/fix/prevention Rule in FIXLOG. Small changes don't require a new document suite.
Done when evidence/choice are clear, authorized callers/compatibility/checks are verified, and reviewed-only versus implemented/verified scope is explicit.
