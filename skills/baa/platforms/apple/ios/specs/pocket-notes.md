# Pocket Notes

An optional iOS example. Adapt the scope before building; this document is not evidence that an app has been built or tested.

## Brief

```markdown
# Pocket Notes
Local plain-text notes for a person who needs a small offline workspace.
## Replaces
A temporary scratchpad workflow.
## Main jobs
Create a plain-text note; edit and find it in a list; delete it after confirmation.
## Data
Note: stable ID, title, body, last-edited date. Persist in the app sandbox using the project's existing storage. Preserve existing user data.
## Platforms and shape
iOS. An iPhone list with push navigation to an editor and a sheet for creating a note. Keep the editor usable while the software keyboard is visible.
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
Use `code` for stable-ID selection, editor state, and persistence; `native-design` for the iOS layout.
Use the existing persistence implementation and its migrations. A failed save retains the draft and exposes an actionable error.
Resolve `build-and-verify` and `test` with the inherited entrypoint and `--platform ios`.
Do not use macOS template build scripts, AppKit panels, or menu-bar utilities for this app.

## Stories

```markdown
# Stories

## M1 Local notes

### S-001 Create and reopen a note
As a user, I create a note and can read it after relaunching the dev app.
Acceptance:
- [unit] A new note has a stable ID; saving and loading preserves its body.
- [manual] On the selected iPhone, create a note, save, return to the list, relaunch, and reopen the same note.
- [manual] Cancel creation; no empty note is added.
Status: todo

### S-002 Edit with the keyboard visible
As a user, I edit a long note without losing access to Save or my text.
Depends: S-001
Acceptance:
- [manual] With the iPhone software keyboard open, edit the last paragraph and save without losing text.
- [manual] Navigate back and reopen; the saved content is unchanged.
- [snap] At a large Dynamic Type size, the editor and actions remain reachable.
Status: todo

### S-003 Delete deliberately
As a user, I can cancel deletion or confirm it for exactly one note.
Depends: S-001
Acceptance:
- [manual] Cancel deletion; the note remains. Confirm deletion; only that note disappears after relaunch.
- [manual] VoiceOver exposes a named deletion action without requiring a swipe gesture.
Status: todo
```

## Gotchas

Keyboard visibility changes available space; avoid fixed screen heights. Preserve draft text through presentation changes. Do not add iPad support or production storage access merely to run the example.
Cancel and save are distinct actions. Deleting a note does not reset the entire store. No check may read or clear release-app data.

## Done when

The listed acceptance checks have results from the actual iOS dev target, with source state,
scheme, device/OS, commands, logs or xcresult, and relevant screenshots recorded.
Unavailable hardware or input checks remain explicitly unverified; a build alone does not complete the example.
