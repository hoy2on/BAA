# Workspace Notes

An optional iPadOS example. Adapt the scope before building; this document is not evidence that an app has been built or tested.

## Brief

```markdown
# Workspace Notes
Local plain-text notes for a person who needs a small offline workspace.
## Replaces
A temporary scratchpad workflow.
## Main jobs
Select and edit a local plain-text note beside the list; resize or rotate without losing the current note; use a keyboard to save.
## Data
Note: stable ID, title, body, last-edited date. Persist in the app sandbox using the project's existing storage. Preserve existing user data.
## Platforms and shape
iPadOS. An iPad list/detail workspace. A narrow window collapses navigation without losing selection or draft text. Extra windows and cloud sync are outside this example.
Use the existing SwiftUI/UIKit approach; confirm minimum OS and SDK in the actual project. Do not raise deployment targets for this example.
## System hooks
Standard app navigation, local persistence, and accessibility. No global keyboard hooks or Mac Accessibility permission.
## Reference and look
System controls, semantic colors, scalable text, and the project's existing tokens.
## Operating constraints
Offline. No account or network service in this example. Use a distinct dev bundle ID and the designated dev installation.
## Not in this scope
Cloud sync, sharing, rich text, extra platform targets, and store submission.
```

## How it works

Resolve `scaffold` for a new app only; existing projects keep their targets and storage.
Use `code` for stable-ID selection, editor state, and persistence; `native-design` for the iPadOS layout.
Use the existing persistence implementation and its migrations. A failed save retains the draft and exposes an actionable error.
Resolve `build-and-verify` and `test` with the inherited entrypoint and `--platform ipados`.
Do not use macOS template build scripts, AppKit panels, or menu-bar utilities for this app.

## Stories

```markdown
# Stories

## M1 Local notes

### S-001 Select and save a note
As a user, I select a note in the list and edit its detail beside it.
Acceptance:
- [unit] Notes use stable IDs, and saving and loading preserves content.
- [manual] On the selected iPad, create two notes, edit one, relaunch the dev app, and verify both contents.
- [snap] A wide window shows list and detail with a clear selection.
Status: todo

### S-002 Preserve work while resizing
As a user, I keep my selected note and draft when the window becomes narrow or rotates.
Depends: S-001
Acceptance:
- [manual] Edit a draft, narrow the iPad window, restore its width, and rotate; selection and draft stay intact.
- [manual] In the collapsed layout, return to the list and reopen the selected note without losing the draft.
- [snap] At a large Dynamic Type size, the list and editor remain usable in the narrow layout.
Status: todo

### S-003 Save with supported input
As a user, I can save using touch and a hardware keyboard.
Depends: S-001
Acceptance:
- [manual] Touch Save and the existing save shortcut produce the same persisted content.
- [manual] With a connected keyboard and pointer, focus and selection remain distinguishable; the shortcut targets the visible note.
- [manual] VoiceOver announces the selected row and named Save action.
Status: todo
```

## Gotchas

Use the current window width, not the physical display width. Do not create separate stores for list and detail. A pointer or physical-keyboard check remains unverified when that input is unavailable. Do not add multi-scene support or remove existing iPhone support as a side effect.
Cancel and save are distinct actions. Deleting a note does not reset the entire store. No check may read or clear release-app data.

## Done when

The listed acceptance checks have results from the actual iPadOS dev target, with source state,
scheme, device/OS, commands, logs or xcresult, and relevant screenshots recorded.
Unavailable hardware or input checks remain explicitly unverified; a build alone does not complete the example.
