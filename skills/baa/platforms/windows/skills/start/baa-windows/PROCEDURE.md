---
name: baa-windows-router
description: Build any Windows app. Start here to pick the next skill for a native Windows app.
---

## BAA execution context

Read [BAA execution rules](../../../../../EXECUTION.md) before this platform procedure. This skill belongs to the windows pack. Preserve the selected platform, task type, ownership and verification environment. Resolve all follow-up skills through BAA, never an external BAMA/BAWA installation. Existing project settings and dev-install rules override template examples.


# Build any Windows app

Keep the assigned platform, entrypoint scope and current task. Find the needed step below,
resolve its packaged PROCEDURE.md through BAA and read it. Do not invoke the Skill tool.
Existing apps enter the requested step; do not restart planning or scaffolding.
Use `python3 <runtime root>/scripts/resolve.py --entrypoint <inherited entrypoint> --platform windows --step <role>`; preserve the entrypoint on name lookups too. If the request contradicts the assigned platform, report the conflict to the coordinator before changing files; do not reroute yourself.

```text
idea -> research -> clone (optional) -> app-brief -> user-stories -> new-windows-app
     -> windows-design + design-system + app-icon -> improve-loop (ux, code, design, verify, commit) -> repeat
     -> distribute
```

For a new app only, pick the app's name first (app-brief, step 1) and create
`<parent>\<AppName>\docs\` before research, so every skill writes into the
same folder. Design comes right after the scaffold: tokens from the first
page, and the real icon in every snapshot.

## Plan

| The user has | Skill |
| --- | --- |
| A vague idea, or asks "what should I build" | `baa-research`, then `baa-app-brief` |
| An app they want to replace or rebuild | `baa-windows-clone` |
| A brief or a screen index, no backlog | `baa-user-stories` |
| A spec from BAWA's `specs/` folder | `baa-app-brief` (it copies the spec) |
| Several specs to build as one app (a suite) | `baa-windows-new-windows-app`, then its suite.md |

## Build

| The user wants to | Skill |
| --- | --- |
| Start a new project | `baa-windows-new-windows-app` |
| Write or fix C#, XAML, and WinUI code | `baa-windows-csharp-winui` |
| Hook into Windows: hotkeys, tray, windows, clipboard, screen capture, startup | `baa-windows-os-integrations` |
| Make it fast: slow start, hangs, stutter, GPU, video, memory | `baa-windows-performance` |
| Let Claude Code, Codex, or scripts drive the app: a CLI, an MCP server | `baa-windows-agent-cli` |
| Refactor, clean up, or check the code as it grows | `baa-improve-architecture` |

## Design

| The user wants to | Skill |
| --- | --- |
| Decide how a feature works and what it says: names, flow, dialogs, accessibility | `baa-ux-design` |
| Make it look and feel like a Windows 11 app | `baa-windows-windows-design` |
| An accent or brand color, a color picker, tokens | `baa-windows-design-system` |
| Their own parts and feel, not Fluent's: buttons, rows, navigation, icons | `baa-windows-design-kit` |
| The look of an app they name, or screenshots of one | `baa-windows-design-from-app` |
| One set of colors, radii, motion, and controls for the whole app | `baa-windows-design-system` |
| Fix spacing and alignment, or check the layout on the grid | `baa-windows-layout-grid` |
| An app icon | `baa-windows-app-icon` |

## Ship

| The user wants to | Skill |
| --- | --- |
| Build it and look at every page | `baa-windows-build-and-verify` |
| Tests, a self-test, or an agent that drives the running app | `baa-windows-test-windows-app` |
| Work through the backlog on its own | `baa-improve-loop` |
| Share it: a release, signing, an installer, WinGet, the Store | `baa-windows-distribute` |

## Done when

You read and followed the packaged procedure for the requested step, preserving the assigned scope and reporting verification evidence.
