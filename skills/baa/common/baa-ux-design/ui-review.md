# UI review before handoff

BAA's shared review adapts ui-ux-pro-max priorities to the requested platform and changed screens. Read the installed skill's relevant quick-reference categories when available; use pro-rules for its native/mobile scope. This reference remains usable without that skill. Review only applicable states and input methods; an unavailable check is unverified, not a pass.

## Review in priority order

First verify accessibility and interaction: meaningful control names/roles/state; decorative versus meaningful icon semantics; visible keyboard focus; focus not hidden behind overlays/IME; usable hit areas in platform units; touch alternatives to hover/drag/swipe-only actions; clear enabled, pressed, selected, loading and error states. Preserve system Back/Cancel and prevent repeated submissions without hiding failures.

Then check layout and perceived performance: current window/viewport constraints, navigation/selection preservation, keyboard and system chrome clearance, text scaling, long translations/RTL where relevant, bounded readable content width, stable layout while loading, and responsive feedback. Don't infer physical-device speed from a screenshot or impose web bundle/CLS metrics on native rendering.

Finally check visual consistency: reuse semantic light/dark tokens and native type scaling, distinguish text and non-text contrast requirements, consistent icon family/weight/alignment, required form labels and nearby errors, meaningful motion with reduced-motion behavior. Measure composed colors where transparency is involved; don't claim numerical contrast from visual inspection. Charts need labels/legend and a non-color way to convey data only when charts are actually present.

## Platform checks

For macOS, verify the changed window at relevant sizes, keyboard/menu shortcuts, focus and pointer behavior, light/dark/high-contrast appearance and relevant accessibility settings. Preserve native AppKit/SwiftUI conventions. Do not force phone-sized touch density or mobile layout into a desktop window.

For iOS, verify the actual iPhone viewport, text size, touch area, keyboard/safe area, back/sheet cancellation, VoiceOver semantics and supported orientation. For iPadOS, also verify relevant window widths, column collapse/selection restoration and supported keyboard/pointer or scene behavior. An iPhone capture is not iPad evidence.

For Android, verify the actual variant/serial, dp/sp/font-scale behavior, IME/system insets, Back, Activity recreation/restoration, TalkBack semantics and the requested window classes. Use current Material/Views conventions rather than Apple's pt values.

For Windows, verify the actual Tauri window and WebView2 content, DOM semantics, window/display scaling, keyboard/focus/access keys, pointer states, theme/high-contrast and relevant automation semantics. Don't infer Windows runtime correctness from a frontend preview on macOS.

## Evidence and handoff

Use build-and-verify/test for the actual runtime and preserve the source state, target, UI states, screenshots, interaction results and remaining checks. A static source review, search result, successful build, screenshot and screen-reader walkthrough prove different things.
Record resolved issues, remaining issues and environmental limitations in existing task/story notes. Reuse current evidence and rerun only affected checks. Do not introduce a second approval gate or mandatory global report for a small UI change. Review-only requests end with observations/proposals; they do not authorize edits, installs or publishing.
