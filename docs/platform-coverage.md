# Platform coverage review

This review checks whether BAA can discover the procedures and resources needed for each supported platform. File-count equality is not the goal: desktop-only tools are not mobile app features.

## Gaps filled

| Area | Resource now provided | Connection |
| --- | --- | --- |
| New app | macOS, Windows, iOS, iPadOS and Android use new-OS-app folders | The scaffold role in routing.json |
| Example plans | Android specs join the existing Mac/Windows/iOS/iPadOS examples | Each platform router links its specs |
| Design intelligence | Scoped optional ui-ux-pro-max search, shared decisions, native-aware review | Design/UX and build/test role references |
| Mobile UX | Writing, presentation, accessibility and AI task states | ux-design references for iOS/iPadOS/Android |
| Architecture | Scene/state/lifecycle, persistence and shared-source review | improve-architecture references |
| Existing apps | Scheme/variant baseline, toolchain and data preservation | build-and-verify supporting reference |
| OS integrations | Mobile document, permission, lifecycle and command boundaries | os-integrations recipes |
| Performance | Real device, comparable trace and environment requirements | performance recipes |
| Design comparison | Viewport, scale/density, input state and evidence boundaries | design-from-app measuring reference |
| Apple tests | Shared scheme includes unit and UI targets; UI run uses an isolated defaults domain | New Apple base template and OS screen overlays |
| Android tests | Unit and Compose UI target; Debug-only isolated UI preferences | New Android template |
| Android icons | Adaptive foreground/background and monochrome resources for all supported API levels | Manifest -> mipmap resource variants |
| Agent guidance | CLAUDE.md imports the same AGENTS.md | Both mobile template bases |
| macOS shipping | Existing-project direct/App Store release procedure | distribute role and Mac router |

The iOS/iPadOS base procedures and references live in apple/shared; each OS's own procedure retains its device-specific requirements. Public entry points remain only baa, baa-apple, baa-android and baa-windows. Internal documents are not registered as extra slash commands.

## Deliberate platform differences

Mac window management, AppKit panels, global input hooks, Windows UI Automation helpers and desktop socket/pipe servers are not copied into mobile. Mobile agent control uses existing platform automation or UI tests; it is not a promise of a background CLI server.

Built-in screenshot commands and existing project tools are used where they already cover the job. A second generic screenshot/profiling wrapper is not required just because the desktop pack has a script.

The mobile starters are deliberately small working apps, not copies of a desktop settings/suite product. UIKit/Views and existing cross-platform projects retain their own components, design tokens and settings. New dependencies, synthetic data/AI features and gallery applications aren't added merely to match a folder count.

Product-specific icons, branding, certificate/team/provisioning, store metadata, actual release scripts, credentials and private service integrations must come from the target project or an explicit task. They cannot be completed generically by the BAA plugin. Android includes a replaceable starter icon; Apple product icon assets remain an app-icon task.

## Verification boundaries

Package tests check all role paths, platform scope, shared references, specs, copied runtime generation, dev identity separation, scheme test targets, icon resource layers and refusal to overwrite existing files/projects.

Native verification is recorded separately from package checks. Compiling XCTest/XCUITest or an Android instrumentation APK does not mean those tests ran. UI, physical input, VoiceOver/TalkBack, device performance, notarization and store uploads require their actual runtime/account environment. The plugin does not install sample apps or publish artifacts during this review.

한국어: 플랫폼별로 필요한 절차·자료와 라우팅 연결을 점검했습니다. 위 표는 보완 항목이며, 데스크톱 전용 기능과 프로젝트별 아이콘·서명·외부 게시 설정은 의도적으로 구분합니다. 빌드와 실제 실행 검증은 별도로 보고합니다.

## Local verification: 2026-11-06

The package suite passed 26 tests, including nested-project rejection and Windows batch line-ending preservation. Fresh iPhone and iPad Simulator-target builds compiled the app, unit-test and UI-test targets with the Debug-only isolated store enabled. The UI tests themselves were not run. A fresh Android project passed Debug and unsigned Release assembly, its unit test, lint and instrumentation-APK compilation. No sample app was installed. The Release APK was checked to exclude the test launch flag. These results do not establish device UI, screen-reader, store or notarization acceptance.
