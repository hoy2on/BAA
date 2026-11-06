# iPadOS specs

These are optional, platform-specific example build plans, not app templates or a required step for existing projects.
Start with [Workspace Notes](workspace-notes.md). It contains a Brief, implementation boundaries, testable Stories, Gotchas, and Done when.
The desktop examples in `macos/specs` use Mac APIs and are not substitutes for these plans.

Use BAA in an empty project folder:

```text
/baa-apple Build the iPadOS app described in workspace-notes.md.
```

Provide this spec file or its full path with the request. BAA keeps the explicit iPadOS target,
uses the common app-brief and user-stories procedures, then resolves scaffold, code, design,
and ship roles from `ipados/skills`. Those procedures read reusable guidance from `shared/`.
Copy the Brief and Stories into project docs without overwriting existing requirements.
Confirm missing product name, location, minimum OS, and development signing from the actual project and tools.
A spec does not authorize commits, uploads, store submission, or replacement of a release app.

This optional iPadOS example uses shared base guidance and OS-specific procedures; it is not imposed on existing projects.
