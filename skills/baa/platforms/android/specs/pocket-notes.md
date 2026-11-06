# Pocket Notes for Android

A small offline plain-text notebook. This is an example plan, not an implemented or tested app.

## Brief

```markdown
# Pocket Notes
A local scratchpad for a person who needs to capture and reopen a short note.
## Replaces
Temporary unsaved text.
## Main jobs
Create, edit, reopen, and deliberately delete a plain-text note.
## Data
Note: stable ID, title, body, updated time. Keep data in the existing app-private store and preserve migrations.
## Platforms and shape
Android phone first. List -> editor, with system Back and IME handling. Keep existing tablet/foldable support if the project has it; don't add it speculatively.
Use native Compose or the existing Views app; confirm minimum OS and SDK from actual tooling.
## System hooks
App-private persistence and ordinary Activity/navigation lifecycle. No storage-wide permissions or background service.
## Reference and look
Existing Material components, semantic colors, scalable text and current app tokens.
## Operating constraints
Offline. No account/network service for this example. One distinct dev application ID and selected device.
## Not in this scope
Cloud sync, rich text, sharing, extra form factors and store submission.
```

## How it works

Resolve scaffold only for a new project. Existing apps keep their module, persistence, navigation and SDK versions.
Use stable note IDs for selection; distinguish a draft from its saved record. A failed save preserves the draft and shows a retry action.
Keep lifecycle-owned state through recomposition and Activity recreation. System Back and IME dismissal must have explicit, separate behavior.
Inspect the actual Debug/dev APK ID and signing before any install. Use the Android test and build-and-verify roles with the selected serial.

## Stories

```markdown
# Stories

## M1 Local notes

### S-001 Save and reopen
As a user, I create a note and reopen its content after a process restart.
Acceptance:
- [unit] Saving/loading preserves stable ID and body; an invalid write retains the original record.
- [manual] On the selected Android device, create a note, restart the dev app, and reopen it.
- [manual] Cancel creation; no empty record is added.
Status: todo

### S-002 Keep editing state
As a user, I retain text when the keyboard opens or the Activity is recreated.
Depends: S-001
Acceptance:
- [manual] Edit the last paragraph with the IME visible; controls remain reachable.
- [device] Recreate the Activity using the existing test runner; text and selected note remain intact.
- [manual] System Back dismisses the IME first where applicable; leaving an unsaved draft follows the documented cancel/save behavior.
- [snap] Large font scale and a long title do not hide essential actions.
Status: todo

### S-003 Delete deliberately
As a user, I cancel or confirm deleting one note.
Depends: S-001
Acceptance:
- [manual] Cancel leaves the note unchanged; confirm deletes only that note, including after relaunch.
- [manual] TalkBack exposes a named action without requiring a particular swipe gesture.
Status: todo
```

## Gotchas

Do not store the entire note list in saved-instance state or create a new store on every recomposition.
A content URI is not an arbitrary local file path. Do not clear app data or reinstall Release to reset a test.
Report input/device checks that could not run; APK compilation alone is not a passed UI flow.

## Done when

Acceptance results reference the actual source state, dev module/variant, package ID, selected serial/API,
unit/instrumentation reports and relevant screens. Hardware-dependent or unavailable input checks remain unverified.
