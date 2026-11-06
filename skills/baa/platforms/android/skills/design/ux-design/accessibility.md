# Android accessibility verification

Use semantic Material components or existing accessible Views. State the expected TalkBack label, role, value and action for changed controls; avoid a clickable Box replacing a semantic Button without equivalent behavior.
Inspect large font scale, long translations, focus order, contrast, dark theme, supported keyboard input and the IME-visible layout. Essential actions must be reachable without hover or a particular swipe gesture.
Compose semantics/Espresso assertions, source inspection and an actual TalkBack walkthrough are separate evidence. Name the device/API/input methods used and leave unavailable hardware checks unverified.
