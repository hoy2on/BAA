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

[Quick start](#quick-start) · [How it works](#how-it-works) · [Commands](#commands) · [Install](#install) · [Development and verification](#development-and-verification)

</div>

BAA builds on the macOS workflow from [BAMA](https://github.com/daveebbelaar/bama) and the Windows workflow from [BAWA](https://github.com/daveebbelaar/bawa), adding specialist procedures for iOS, iPadOS, and Android and a central platform router. Install BAA once; separate BAMA and BAWA installations are not required.

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

Central BAA router → platform specialist → procedures needed for the current task → verification and integration.

If your request names a target platform, BAA uses it. Otherwise, it checks the scope already agreed for the task, the actual targets of the files or modules you selected, and the platforms supported by the project. When the target is clear, BAA states it and proceeds. When multiple candidates remain, it asks which platforms to work on. The host OS or a language name such as Swift or Kotlin is not enough to choose a platform.

For a new app, the workflow is research → reference app analysis (optional) → brief → user stories → scaffold → design → implementation and verification. For an existing app, BAA starts at the stage your request needs. A design-only request does not restart planning or create a new app.

Independent platform work can run in parallel through available subagents. Shared files have one owner. Verification that uses the same device, build output, or installation runs sequentially. Without parallel agent tools, BAA works sequentially.

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

## Specialist skills

| Area | Procedures |
| --- | --- |
| Shared | Research, app briefs, user stories, UX, architecture review, and improvement loops |
| macOS | BAMA-based Swift, SwiftUI, and AppKit; macOS design, OS integration, performance, builds, and tests |
| iOS and iPadOS | Shared Swift, SwiftUI, and UIKit implementation; device-specific native design, OS integration, performance, builds, tests, and distribution preparation |
| Android | Kotlin, Compose, and Views; Android design, OS integration, performance, Gradle and adb verification, and distribution preparation |
| Windows | BAWA-based C# and WinUI; Windows design, OS integration, performance, builds, tests, and distribution |

Stages may share names without sharing platform implementations. Existing UIKit, WPF, Views, or cross-platform apps are not converted to match a template. Where the original macOS pack has no distribution procedure, BAA inspects the project's actual release workflow.

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

Building apps requires the tools used by the actual project, such as Xcode and Apple SDKs, Android SDK, JDK and Gradle, or Windows SDK and .NET. BAA does not require every tool to be installed or raise the project's minimum OS version. UI interaction needs available test, device, or computer-use tools.

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
      apple/           macOS, iOS, iPadOS, and shared mobile resources
      android/
      windows/
    scripts/resolve.py
    LICENSES/          Original BAMA and BAWA licenses
    UPSTREAM.json      Imported upstream commits
  baa-apple/           Apple-only entry point
  baa-android/         Android-only entry point
  baa-windows/         Windows-only entry point
scripts/link-skills.sh  Manual local links
tests/                 Routing, installation, and dev-app protection checks
```

The central skill folder contains its procedures, references, tools, templates, and attribution. Plugin installations and skills CLI folder copies therefore use the same resources.

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

[MIT](LICENSE). BAA is based on [BAMA](https://github.com/daveebbelaar/bama) and [BAWA](https://github.com/daveebbelaar/bawa) by [Dave Ebbelaar](https://github.com/daveebbelaar). It preserves upstream specialist procedures, references, and templates while integrating a central router, shared procedures, and mobile specialist procedures.

Imported commits are recorded in [UPSTREAM.json](skills/baa/UPSTREAM.json). Original terms are preserved in the [macOS license](skills/baa/LICENSES/macos-upstream.txt) and [Windows license](skills/baa/LICENSES/windows-upstream.txt). See the upstream projects for REA and their other references.
