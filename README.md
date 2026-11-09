[English](README.md) | [한국어](README.ko.md)

<div align="center">

# BAA — Build Any App

### One command. Platform-specific skills.

Apple · Android · Windows<br>
Agent skills that connect planning, coding, design improvements, builds, and verification.

[![Claude Code](https://img.shields.io/badge/Claude_Code-plugin-D97757)](#install)
[![Codex](https://img.shields.io/badge/Codex-plugin-10A37F)](#install)
[![Agent Skills](https://img.shields.io/badge/Agent_Skills-compatible-5E5CE6)](#install)
[![MIT](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

[Quick start](#quick-start) · [How it works](#how-it-works) · [Commands](#commands) · [Skills](#skills) · [Install](#install) · [Development and verification](#development-and-verification)

</div>


## Quick start

Install from inside Claude Code:

```text
/plugin marketplace add https://github.com/hoy2on/BAA.git
/plugin install baa@baa
```

Start a new session and describe your task:

```text
/baa Improve the Settings screen design on macOS and Windows.
Keep the existing behavior and navigation. Change only spacing, alignment, and type sizes.
```

See [Install](#install) for Codex and other agents.

## How it works

Describe the app or the change once. BAA identifies the target, selects the procedures needed for this task, and carries their results through verification.

| Step | What BAA does | Result |
| --- | --- | --- |
| 1. Select the target | Use your requested platforms and actual project targets; ask when several candidates remain. | Selected platforms, task scope and current stage. |
| 2. Plan | For a new app, research the idea, optionally inspect a reference app, and define a brief, stories and acceptance. For an existing app, reuse the agreed plan. | A scoped plan and checkable user flows. |
| 3. Design | Define navigation, states, copy and accessibility, then apply the selected platform's layout, input and visual conventions. | UX decisions and the requested design proposals or implementation direction. |
| 4. Implement | Create a starter only for a new app, then implement the agreed behavior with the relevant platform code, OS integration and design procedures. | Source changes within the assigned scope. |
| 5. Verify and integrate | Build, test and exercise affected behavior in the available target environment; fix observed defects and integrate shared changes. | Evidence for completed checks, plus any pending checks and their resumption conditions. |

These steps describe the new-app path, not a mandatory restart for every request. BAA uses the platform named in your request or confirmed by the project; a host OS or a language name alone is not enough. Existing-app work enters at the relevant stage and keeps its current technology and documents.

### Start where your task needs it

| Request | Workflow |
| --- | --- |
| “Build an app that…” | Select the platform, plan the agreed scope, design, scaffold, implement and verify. |
| “Create five design proposals” or “Suggest better UX” | Inspect the current screens and platform conventions, then return the requested alternatives and rationale. A proposal-only request does not authorize changing the app. |
| “Implement this feature” or “Apply this design” | Reuse the existing plan or selected design, implement the affected behavior, and verify it without restarting research or scaffolding. |

Independent platform work can run through available subagents. Shared behavior and design decisions are agreed once, and shared files have one owner. Checks using the same device, build output or dev installation run sequentially; without parallel tools, work proceeds sequentially.

Build success, actual UI interaction and physical-device verification are reported separately. Missing devices or permissions leave the affected checks pending, not passed. Commits, app installation and external publication remain within your actual authorization; a request to build an app does not automatically publish it to a store.

## Commands

| Command | Scope |
| --- | --- |
| `/baa` | Determines the target macOS, iOS, iPadOS, Android, or Windows platforms from your request and project. |
| `/baa-apple` | Restricts work to macOS, iOS, and iPadOS. |
| `/baa-android` | Restricts work to Android. |
| `/baa-windows` | Restricts work to Windows. |

Plugin installations may show namespaced commands such as `/baa:baa` or `/baa:baa-apple`. Select the matching entry in your agent's command list. Only these four entry points are public; internal specialist procedures stay out of the command list.

`/baa-apple` does not automatically select all three Apple platforms. BAA uses your request and actual targets to distinguish macOS, iOS, and iPadOS, and asks when the scope is unclear. If a direct command conflicts with the request body, BAA clarifies before editing.

```text
/baa-apple Review the open-and-save flow on iPhone and iPad.
/baa-apple Improve only the spacing and alignment of the macOS Settings screen.
/baa-android Fix the loss of unsaved edits after screen rotation.
/baa-windows Fix file opening, then build and test the change.
```

For an existing project, “all” means the supported targets within the command's scope. For a new app, it means all platforms allowed by that command. BAA does not add unsupported platforms without a request to do so.

## Skills

Stages help select the work; they are not a mandatory execution sequence. Existing-app requests start at the relevant feature, design, or verification step. Only the four commands above are public. The names below are internal roles selected by BAA; platform roles resolve to their actual documents through [routing.json](skills/baa/routing.json).

| Stage | Skill / role | What it does |
| --- | --- | --- |
| Start | [`baa`](skills/baa/SKILL.md) | Select the target platforms and current task; ask only when the target is ambiguous. |
| Start | `router` | Connect the selected platform to the procedure needed now. |
| Start | [`app-brief`](skills/baa/common/baa-app-brief/PROCEDURE.md) | Turn a new app idea into a scoped brief; reuse an existing brief. |
| Start | `scaffold` | Create a new project from the selected platform starter, with a separate dev identity. |
| Plan | [`research`](skills/baa/common/baa-research/PROCEDURE.md) | Investigate the users, reference products, UX and technical constraints relevant to the request. |
| Plan | `clone` | Inspect a supplied reference app and record screens, behaviors and evidence. |
| Plan | [`user-stories`](skills/baa/common/baa-user-stories/PROCEDURE.md) | Define user actions, dependencies, milestones and checkable acceptance criteria. |
| Code | `code` | Implement the agreed behavior using the selected platform and existing architecture. |
| Code | `os-integrations` | Connect only the OS services the feature needs, with permissions and lifecycle handling. |
| Code | `performance` | Measure a reproducible bottleneck, fix its cause, and compare the result. |
| Code | [`improve-architecture`](skills/baa/common/baa-improve-architecture/PROCEDURE.md) | Review actual structural problems and make only justified, behavior-preserving changes. |
| Code | `agent-cli` | When requested, add a scoped automation or CLI integration using the platform's available mechanisms. |
| Design | [`ux-design`](skills/baa/common/baa-ux-design/PROCEDURE.md) | Decide action names, navigation, presentation, states, copy and accessibility before implementation. |
| Design | `native-design` | Apply platform-specific window, screen, input and interaction conventions, including Tauri web content on Windows. |
| Design | `design-system` | Reuse or define the required semantic colors, typography, spacing, themes and motion tokens. |
| Design | `layout-grid` | Check the changed layout for spacing, alignment, clipping and relevant size or scale behavior. |
| Design | `design-kit` | Reuse or extend the app's components and their interaction states. |
| Design | `design-from-app` | Adapt a supplied visual reference and compare matching screens and states. |
| Design | `app-icon` | Prepare the platform's app and related icon assets, preserving existing sources. |
| Ship | `build-and-verify` | Build and exercise the affected app behavior; distinguish compilation from actual runtime evidence. |
| Ship | `test` | Run the relevant logic, integration and UI checks using existing project tools where suitable. |
| Ship | [`improve-loop`](skills/baa/common/baa-improve-loop/PROCEDURE.md) | Work through the agreed stories: plan, implement, verify, fix and record; commit only when authorized. |
| Ship | `distribute` | Prepare the requested packaging, signing or distribution stage without assuming permission to publish or install. |

### Platform specialists

Research, planning, UX, architecture review and iteration share the common procedures above. These links show the actual platform-specific starters, code, design and test procedures. OS integration, performance, design tokens and distribution likewise resolve to the selected platform. iOS and iPadOS combine device-specific specialists with shared Apple bases.

| Platform | New app | Code | Platform UX / design | Tests |
| --- | --- | --- | --- | --- |
| macOS | [new-mac-app](skills/baa/platforms/apple/macos/skills/start/new-mac-app/PROCEDURE.md) | [Swift / SwiftUI / AppKit](skills/baa/platforms/apple/macos/skills/code/swift-swiftui/PROCEDURE.md) | [mac-design](skills/baa/platforms/apple/macos/skills/design/mac-design/PROCEDURE.md) | [test-mac-app](skills/baa/platforms/apple/macos/skills/ship/test-mac-app/PROCEDURE.md) |
| iOS | [new-ios-app](skills/baa/platforms/apple/ios/skills/start/new-ios-app/PROCEDURE.md) | [Swift / SwiftUI / UIKit](skills/baa/platforms/apple/ios/skills/code/baa-ios-code/PROCEDURE.md) | [iOS design](skills/baa/platforms/apple/ios/skills/design/baa-ios-design/PROCEDURE.md) | [iOS tests](skills/baa/platforms/apple/ios/skills/ship/baa-ios-test/PROCEDURE.md) |
| iPadOS | [new-ipados-app](skills/baa/platforms/apple/ipados/skills/start/new-ipados-app/PROCEDURE.md) | [Swift / SwiftUI / UIKit](skills/baa/platforms/apple/ipados/skills/code/baa-ipados-code/PROCEDURE.md) | [iPadOS design](skills/baa/platforms/apple/ipados/skills/design/baa-ipados-design/PROCEDURE.md) | [iPadOS tests](skills/baa/platforms/apple/ipados/skills/ship/baa-ipados-test/PROCEDURE.md) |
| Android | [new-android-app](skills/baa/platforms/android/skills/start/new-android-app/PROCEDURE.md) | [Kotlin / Compose / Views](skills/baa/platforms/android/skills/code/baa-android-code/PROCEDURE.md) | [Android design](skills/baa/platforms/android/skills/design/baa-android-native-design/PROCEDURE.md) | [Android tests](skills/baa/platforms/android/skills/ship/baa-android-test/PROCEDURE.md) |
| Windows | [new-windows-app](skills/baa/platforms/windows/skills/start/new-windows-app/PROCEDURE.md) | [Tauri / Rust / web frontend](skills/baa/platforms/windows/skills/code/tauri/PROCEDURE.md) | [Windows Tauri design](skills/baa/platforms/windows/skills/design/windows-design/PROCEDURE.md) | [Tauri tests](skills/baa/platforms/windows/skills/ship/test-windows-app/PROCEDURE.md) |

New Android starters use Compose; existing Views apps are not migrated without a request. Windows work uses Tauri only and retains the existing web frontend; other Windows technologies require an explicitly agreed migration scope. macOS distribution follows the actual project's direct-distribution or App Store workflow.

## Install

Choose one installation method per agent. Combining a plugin installation, the skills CLI, and manual links can expose duplicate commands.

<details open>
<summary><b>Claude Code</b></summary>

Run inside Claude Code:

```text
/plugin marketplace add https://github.com/hoy2on/BAA.git
/plugin install baa@baa
```

Or use your terminal:

```sh
claude plugin marketplace add https://github.com/hoy2on/BAA.git
claude plugin install baa@baa --scope user
```

To update, run the following and start a new session:

```sh
claude plugin marketplace update baa
claude plugin update baa@baa
```

</details>

<details>
<summary><b>Codex</b></summary>

Run with a Codex CLI that supports plugin commands:

```sh
codex plugin marketplace add https://github.com/hoy2on/BAA.git
codex plugin add baa@baa
```

To update, run the following and restart your running Codex instance:

```sh
codex plugin marketplace upgrade baa
codex plugin add baa@baa
```

</details>

<details>
<summary><b>Other agents or the skills CLI</b></summary>

Use the [skills CLI](https://github.com/vercel-labs/skills). Node.js 22.20 or later is required.

```sh
npx skills@latest add hoy2on/BAA --skill "*"
```

Choose the agents to install to. Installation is project-local by default; add `-g` to use BAA across projects.

```sh
npx skills@latest add hoy2on/BAA --skill "*" -a codex -g
npx skills@latest add hoy2on/BAA --skill "*" -a claude-code -g
```

If you only need `/baa`, install the central skill alone. It includes the internal specialist procedures for all supported platforms.

```sh
npx skills@latest add hoy2on/BAA --skill baa -a codex
```

`baa-apple`, `baa-android`, and `baa-windows` depend on the central `baa` skill. Install all four or just `baa`; do not install a platform entry point on its own. Update with `npx skills@latest update`.

</details>

<details>
<summary><b>Manual links / local development</b></summary>

Clone the repository and run the script in Bash on macOS or Linux:

```sh
git clone https://github.com/hoy2on/BAA.git
cd BAA
./scripts/link-skills.sh
```

This links only the four public skills into `~/.claude/skills` and `~/.agents/skills`. Existing files and unrelated links are preserved. Changes in the checkout are shared by both agents. Update with `git pull`, then start a new session.

On Windows, use the plugin or skills CLI installation above.

</details>

## Requirements and verification limits

BAA needs an agent that supports skills. Its resolver uses Python 3.9 or later and the standard library. If Python is unavailable, the agent reads the same `routing.json` to check scope and locate procedures. BAA does not automatically install runtimes or packages just to use a skill.

Building apps requires the tools used by the actual project, such as Xcode and Apple SDKs, Android SDK, JDK and Gradle, or Rust MSVC, Microsoft C++ build tools, and WebView2. BAA does not require every tool to be installed or raise the project's minimum OS version. UI interaction needs available test, device, or computer-use tools.

Source changes, successful builds, UI execution, and physical-device verification are separate results. Editing Windows code on macOS does not verify Windows execution. iOS and iPadOS need their own target-device evidence. Verification stays pending when the required execution environment is unavailable.

Release apps and user data are preserved. Development apps use distinct identifiers and one designated dev installation. Signing, distribution, and store submission stay within the scope of your request.

## Structure

```text
.claude-plugin/         Claude and Codex marketplace and plugin metadata
skills/
  baa/                 Self-contained central skill and runtime package
    SKILL.md
    EXECUTION.md
    routing.json
    common/            Shared procedures
    platforms/
      apple/
        shared/skills/  Reusable iOS/iPadOS base procedures by workflow stage
        macos/skills/   macOS procedures, grouped by workflow stage
        ios/
          skills/      iOS specialists: start, plan, code, design, ship
          specs/       iPhone example build plans
        ipados/
          skills/      iPadOS specialists: start, plan, code, design, ship
          specs/       iPad example build plans
      android/skills/   Android procedures, grouped by workflow stage
      windows/skills/   Windows procedures, grouped by workflow stage
    scripts/resolve.py
    LICENSES/          Original licenses and provenance
  baa-apple/           Apple-only entry point
  baa-android/         Android-only entry point
  baa-windows/         Windows-only entry point
scripts/link-skills.sh  Manual local links
tests/                 Routing, installation, and dev-app protection checks
```

The central skill folder contains its procedures, references, tools, templates, and attribution. Plugin installations and skills CLI folder copies therefore use the same resources.

Procedures use `start` (entry point and scaffolding), `plan` (reference-app analysis), `code` (implementation, OS integration, performance, and agent CLI), `design` (native UI and design assets), and `ship` (build, test, and distribution). These are task categories, not a required sequence: existing-app work starts at the relevant stage. Platform-independent planning and UX stay in `common/`.

Each Apple OS has its own specialist procedures. iOS and iPadOS each provide all five stages and their own specs; their procedures combine device-specific requirements with reusable bases in `apple/shared/skills/<stage>/`. The resolver returns the OS procedure as `path` and its shared base as `references`. macOS retains its AppKit tools, templates, and desktop specs; those are not interchangeable with UIKit/mobile procedures. `routing.json` is the source of truth for each role's location.

Optional example plans: [iOS specs](skills/baa/platforms/apple/ios/specs/README.md), [iPadOS specs](skills/baa/platforms/apple/ipados/specs/README.md), and [macOS specs](skills/baa/platforms/apple/macos/specs/README.md). Existing-app work does not require these examples.

The mobile `scaffold` role resolves to `start/new-ios-app`, `start/new-ipados-app`, or `start/new-android-app`, matching the desktop new-app folder naming. Apple shares an Xcode project, app entry point, title model, XCTest/XCUITest targets, and build script in `apple/shared/skills/start/new-apple-app/template`; each OS supplies its own SwiftUI screen. Android supplies a native Kotlin/Compose app, Gradle Wrapper, manifest/resources, and unit/instrumentation tests. These starters apply to new projects only.

```sh
python3 skills/baa/scripts/new-app.py ios MyPhoneApp com.example.myphoneapp ~/Developer
python3 skills/baa/scripts/new-app.py ipados MyPadApp com.example.mypadapp ~/Developer
python3 skills/baa/scripts/new-app.py android MyAndroidApp com.example.myandroidapp ~/Developer
python3 skills/baa/scripts/new-app.py windows MyWindowsApp com.example.mywindowsapp ~/Developer
```

The generator preserves existing briefs, refuses conflicting files and existing projects, and does not install apps or run Git commands. Apple starters use Swift 6, Xcode 16+, and iOS/iPadOS 17.0+ (`--min-os` can select a higher minimum). The Android starter pins Gradle 8.14.3, AGP 8.11.2, Kotlin 2.3.20, Compose BOM 2025.09.00, compile/target SDK 36, and minSdk 26; confirm the installed toolchain before using it. Existing projects keep their versions. Android's first build may download dependencies; Gradle wrapper licensing is preserved in the template. Product icons and physical-device signing remain follow-up work.

The [platform coverage review](docs/platform-coverage.md) records the filled gaps and intentional differences. Mobile UX/architecture, integration/performance recipes, existing-app verification and screenshot comparison references are connected through the router. Android example plans are in [Android specs](skills/baa/platforms/android/specs/README.md).

For UI work, BAA uses the [design-intelligence workflow](skills/baa/common/baa-ux-design/design-intelligence.md). When ui-ux-pro-max is installed, it uses the actual local skill's relevant searches, validates their platform/stack fit, and passes accepted decisions to platform specialists. New visual direction uses a coherent design-system candidate; existing-screen fixes keep the current system and use a targeted query. The coordinator preserves existing master/page decisions and writes shared changes once. Native-aware [UI review](skills/baa/common/baa-ux-design/ui-review.md) connects to verification. BAA's packaged criteria remain available without the external skill; its search database is not bundled or auto-installed.

Windows starters use a TypeScript/Vite frontend, a Rust host, and a separate `.dev` configuration. Existing Tauri apps retain their frontend. Actual Windows builds and runtime checks require a Windows environment; browser previews establish only frontend behavior.

## Development and verification

```sh
python3 -m unittest discover -s tests -v
bash -n scripts/link-skills.sh
claude plugin validate .
python3 skills/baa/scripts/resolve.py --entrypoint baa-apple --platform macos --step native-design
python3 skills/baa/scripts/resolve.py --entrypoint baa-android --platform android --step code
```

Checks cover the four public entry points, platform scope restrictions, internal routing and relative links, standalone copies of the central skill, installation conflicts, and protection in the adapted dev templates. They do not prove app runtime behavior or every natural-language routing decision. macOS-only template tests run on macOS and are skipped on other operating systems.

BAA uses Git commits for updates and does not declare a numeric version. Some validation tools may recommend adding a version field.

## Credits and license

[MIT](LICENSE). BAA draws on [BAMA](https://github.com/daveebbelaar/bama) and [BAWA](https://github.com/daveebbelaar/bawa) by [Dave Ebbelaar](https://github.com/daveebbelaar). Original license terms and imported commit records are preserved in [LICENSES](skills/baa/LICENSES).
