# Mobile accessibility verification

Name the changed controls and expected VoiceOver label, value, selected/disabled state and action. Keep Button and other semantic controls; make custom gestures available through accessible actions.
Use the existing Dynamic Type styles and test a large accessibility size, long localized text, light/dark appearance, and relevant contrast/reduced-motion settings. Inspect a real iPhone/iPad viewport for clipped controls and an editor hidden by the keyboard.
On iPad, verify keyboard traversal and pointer behavior when supported; a hover state cannot be the only route to an action. Source inspection, XCUITest visibility and VoiceOver interaction are different evidence. Report which were actually performed.
