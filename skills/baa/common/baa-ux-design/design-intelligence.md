# Design intelligence in BAA

Adapted from the user's installed ui-ux-pro-max workflow. This is a shared reference, not a new public command or a replacement for platform specialist procedures. It applies when a task changes UI structure, visual direction, interaction, components, tokens or UI quality. Skip design searches for backend logic, infrastructure and performance work without a visible/interactive change.

## 1. Establish the real task

Keep BAA's selected platform, entrypoint restriction, purpose and file ownership. Read existing design decisions, assets, tokens, components and the changed flow first. Identify the product, audience/context, dominant interaction and actual implementation stack from the relevant target, not the host OS or a language extension.
For new UI or a deliberately new product-wide direction, evaluate a coherent design-system candidate. For a small existing-screen issue, keep the current system and search only the affected outcome. Creating a new screen in an established product is not permission to rebrand it.

## 2. Use the installed skill when available

Find ui-ux-pro-max in the host's available skills and read its actual SKILL.md. Resolve symlinks and derive its directory from that file; use the search.py inside its scripts directory. Never assume a personal home path, CLAUDE_PLUGIN_ROOT layout or the current project directory. Use the Python executable available on the current host.

```sh
python3 "<actual-ui-ux-pro-max-directory>/scripts/search.py" "<one product/context intent>" --design-system --json
python3 "<actual-ui-ux-pro-max-directory>/scripts/search.py" "<one observable UX outcome>" --domain ux -n 3
python3 "<actual-ui-ux-pro-max-directory>/scripts/search.py" "<one implementation concern>" --stack <verified-stack> -n 3
```

Choose one dominant intent, usually 2–5 meaningful terms and a relevant platform/interaction constraint. Search a semantic UX outcome before stack implementation when diagnosing accessibility, wrapping or compact-component behavior. Use an explicit domain for color, typography, icons or charts only when that is the actual concern; do not run every domain.
Use swiftui or jetpack-compose only for those actual stacks. Windows uses Tauri: select the existing frontend stack (React, Vue, Svelte or plain HTML/CSS/TypeScript) when the search tool supports it; do not invent a tauri stack selector. UIKit, AppKit, Views or other unmatched stacks do not silently become SwiftUI, Compose or html-tailwind. Generic findings may inform intent; use the actual platform procedure and current SDK for implementation.
If the skill or local search data is absent, continue with BAA's packaged platform guidance and the review reference. Say that no database search was performed. Do not install a dependency, download a database, or fabricate a search result merely to continue BAA.

## 3. Validate before applying

Check the returned domain, source/category, top result identity, status/applicable versions and fit for the selected platform. A nonempty result is not proof of relevance. If empty or off-topic, retry once with a narrower or explicitly scoped query. If the second attempt still lacks a verified match, report that and distinguish general guidance from database evidence. Don't persist rejected or unverified results.
A web focus result can suggest keeping focus visible, but CSS scroll-padding and WCAG AA/AAA labels do not become native API implementations or a native compliance certification. A design-system result may include website hero/CTA sections, Google Fonts/CSS imports, GSAP snippets or unsupported components: discard website marketing sections for an app UI. CSS/DOM guidance can apply to Tauri web content, but not to native mobile or Apple views.
Platform conventions, existing components and the repository's tokens take precedence over generic style suggestions. Preserve system fonts, existing assets and platform icon families unless the task explicitly needs a change. Raster product art or store-required PNGs are not banned by a generic vector-icon preference. Don't add packages, fonts, charts, deep links, haptics or animations merely because a recommendation mentions them.
Keep px, CSS px, pt, dp and sp distinct. Review mobile hit areas in native units (the installed skill's quality goals include 44pt on iOS/iPadOS and 48dp on Android); retain desktop control density, pointer/keyboard behavior and display scaling. Do not turn mobile safe areas, 375px test widths, 16px web typography or CSS/GSAP timings into universal Mac/Windows rules. Existing accessibility and reduced-motion settings remain authoritative.

## 4. Record one accepted design decision

The BAA coordinator owns shared design decisions; platform agents return proposed deltas instead of rewriting the same file. Shared meaning/brand intent may be decided once, while native controls, density, typography scaling and input behavior remain platform-specific.
Read the existing canonical design document first, including design/DESIGN-SYSTEM.md or design-system/<project-slug>/MASTER.md where present, then any applicable page override. Preserve that source of truth; don't create competing masters. A platform/page exception must remain within the selected scope, not silently change all platforms.
Search without persistence first. Merge only validated decisions into the existing document. If the installed skill's --persist is appropriate after the full output is verified, always pass --output-dir with the actual project root and preserve existing MASTER/page files. Never pass --force without explicit user authorization. A component fix doesn't require a new global document or persisted search output.

Record only the useful decision in the existing design/story notes:

```text
Context: target platform, real stack, screen/task, existing token source
Evidence: query/mode, result identity and applicable scope, or no verified match
Decision: accepted behavior/tokens, rationale and rejected cross-platform assumptions
Platform delta: native control/input/layout differences and affected files
Verification: expected visible/interactive states, evidence and unverified conditions
```

Pass the accepted decision and canonical document path to native-design, design-system, design-kit, layout-grid or app-icon as needed, preserving BAA's inherited scope. Don't restart research or run a second global design-system search in every platform agent. Finish changed UI with [UI review](ui-review.md).
