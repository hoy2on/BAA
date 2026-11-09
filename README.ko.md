[English](README.md) | [한국어](README.ko.md)

<div align="center">

# BAA — Build Any App

### 하나의 명령으로, 각 플랫폼에 맞는 앱을 만드세요.

Apple · Android · Windows<br>
기획부터 코딩, 디자인 개선, 빌드와 검증까지 연결하는 에이전트 스킬입니다.

[![Claude Code](https://img.shields.io/badge/Claude_Code-plugin-D97757)](#설치)
[![Codex](https://img.shields.io/badge/Codex-plugin-10A37F)](#설치)
[![Agent Skills](https://img.shields.io/badge/Agent_Skills-compatible-5E5CE6)](#설치)
[![MIT](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

[빠른 시작](#빠른-시작) · [동작 방식](#동작-방식) · [명령](#명령) · [스킬](#스킬) · [설치](#설치) · [개발과 검증](#개발과-검증)

</div>


## 빠른 시작

Claude Code 안에서 설치합니다.

```text
/plugin marketplace add https://github.com/hoy2on/BAA.git
/plugin install baa@baa
```

새 세션에서 작업을 요청합니다.

```text
/baa macOS와 Windows의 설정 화면 디자인을 개선해 주세요.
기존 기능과 화면 흐름을 유지하고 간격, 정렬, 글자 크기만 수정해 주세요.
```

Codex와 다른 에이전트의 설치 방법은 [설치](#설치)를 참고하세요.

## 동작 방식

만들 앱이나 변경할 내용을 한 번 요청하면 BAA가 대상을 확인하고, 현재 작업에 필요한 전문 절차를 선택해 검증까지 이어갑니다.

| 단계 | BAA가 하는 일 | 결과물 |
| --- | --- | --- |
| 1. 대상 선택 | 요청한 플랫폼과 프로젝트의 실제 타깃을 확인하고, 후보가 여러 개 남으면 질문합니다. | 대상 플랫폼·작업 범위·시작 단계 |
| 2. 기획 | 새 앱은 조사·참고 앱 분석(선택)을 거쳐 개요·스토리·완료 기준을 정합니다. 기존 앱은 합의된 계획을 재사용합니다. | 범위가 정해진 계획과 확인 가능한 사용자 흐름 |
| 3. 디자인 | 탐색·상태·문구·접근성을 설계하고, 대상 플랫폼의 배치·입력·시각적 관례를 적용합니다. | UX 결정과 요청한 디자인 시안 또는 구현 방향 |
| 4. 구현 | 새 앱에만 프로젝트를 생성하고, 필요한 플랫폼 코드·OS 연동·디자인 절차로 합의한 기능을 구현합니다. | 담당 범위 안의 소스 변경 |
| 5. 검증·통합 | 사용 가능한 대상 환경에서 빌드·테스트·영향받는 동작을 확인하고, 발견한 결함을 수정한 뒤 공유 변경을 통합합니다. | 수행한 검사의 증거, 남은 검사와 재개 조건 |

위 단계는 새 앱의 전체 흐름이며 매번 처음부터 반복하는 절차가 아닙니다. 요청에서 지정했거나 프로젝트 근거로 확인한 플랫폼을 사용하고, 실행 중인 컴퓨터의 OS나 언어 이름만으로 대상을 고르지 않습니다. 기존 앱은 필요한 단계부터 시작하며 현재 기술과 문서를 유지합니다.

### 요청에 맞는 단계부터 시작합니다

| 요청 | 진행 방식 |
| --- | --- |
| “이런 기능을 하는 앱 만들어줘” | 플랫폼을 정하고 합의한 범위의 기획·디자인·프로젝트 생성·구현·검증을 진행합니다. |
| “디자인 시안 다섯 개 만들어줘” 또는 “더 나은 UX를 제안해줘” | 현재 화면과 플랫폼 관례를 분석한 뒤 요청한 대안과 이유를 제시합니다. 제안만 요청한 경우 앱을 수정하지 않습니다. |
| “이 기능 구현해줘” 또는 “이 디자인으로 적용해줘” | 기존 계획이나 선택한 시안을 이어받아 구현·검증하며 조사나 프로젝트 생성을 다시 시작하지 않습니다. |

독립적인 플랫폼 작업은 사용 가능한 서브에이전트에 나눌 수 있습니다. 공통 동작과 디자인 결정은 한 번 정하고 공유 파일은 한 담당자가 맡습니다. 같은 기기·빌드 출력·dev 설치본을 사용하는 검사는 순서대로 수행하며, 병렬 도구가 없으면 작업도 순차로 진행합니다.

빌드 성공·실제 UI 조작·실기기 검증은 구분해서 보고합니다. 기기나 권한이 없으면 해당 검사를 통과가 아닌 대기로 남깁니다. 커밋·앱 설치·외부 게시는 실제 승인 범위를 따르며, 앱 제작을 요청했다고 스토어에 자동 게시하지 않습니다.

## 명령

| 명령 | 작업 범위 |
| --- | --- |
| `/baa` | 요청과 프로젝트에서 macOS·iOS·iPadOS·Android·Windows 대상을 판단합니다. |
| `/baa-apple` | macOS·iOS·iPadOS 범위로 제한합니다. |
| `/baa-android` | Android 범위로 제한합니다. |
| `/baa-windows` | Windows 범위로 제한합니다. |

플러그인 설치에서는 `/baa:baa`, `/baa:baa-apple`처럼 네임스페이스가 붙을 수 있습니다. 명령 목록에서 해당 항목을 선택하세요. 사용자에게 공개되는 진입점은 네 개이며 내부 전문 절차는 명령 목록에 노출하지 않습니다.

`/baa-apple`은 세 Apple 플랫폼을 모두 수정하라는 뜻이 아닙니다. 요청과 실제 타깃으로 macOS·iOS·iPadOS를 구분하고, 모호하면 그 안에서 질문합니다. 직접 지정한 명령과 본문이 충돌하면 수정 전에 확인합니다.

```text
/baa-apple iPhone과 iPad에서 파일을 열고 저장하는 흐름을 검토해 주세요.
/baa-apple macOS 설정 화면의 간격과 정렬만 개선해 주세요.
/baa-android 화면 회전 후 편집 내용이 사라지는 문제를 수정해 주세요.
/baa-windows 파일 열기 동작을 수정하고 빌드·테스트해 주세요.
```

`전체`는 기존 프로젝트에서는 해당 명령 범위 안의 실제 지원 타깃 전체, 새 앱에서는 해당 명령이 허용하는 플랫폼 전체입니다. 없는 플랫폼을 요청 없이 추가하지 않습니다.

## 스킬

단계는 작업을 찾기 위한 분류이며 강제 실행 순서가 아닙니다. 기존 앱에서는 요청한 기능·디자인·검증 단계부터 시작합니다. 공개 명령어는 위의 네 개뿐이며, 아래 이름은 BAA가 내부에서 선택하는 역할입니다. 플랫폼별 역할은 [routing.json](skills/baa/routing.json)에서 실제 문서로 연결됩니다.

| 단계 | 스킬·역할 | 하는 일 |
| --- | --- | --- |
| 시작 | [`baa`](skills/baa/SKILL.md) | 대상 플랫폼과 현재 작업을 정하고, 모호할 때만 질문합니다. |
| 시작 | `router` | 선택한 플랫폼에서 지금 필요한 전문 절차를 연결합니다. |
| 시작 | [`app-brief`](skills/baa/common/baa-app-brief/PROCEDURE.md) | 새 앱의 목표와 범위를 개요로 정리하고 기존 개요는 재사용합니다. |
| 시작 | `scaffold` | 선택한 플랫폼의 새 프로젝트와 별도 dev 식별자를 구성합니다. |
| 기획 | [`research`](skills/baa/common/baa-research/PROCEDURE.md) | 요청과 관련된 사용자·참고 제품·UX·기술 제약을 조사합니다. |
| 기획 | `clone` | 참고 앱의 화면과 동작을 분석하고 확인 근거를 기록합니다. |
| 기획 | [`user-stories`](skills/baa/common/baa-user-stories/PROCEDURE.md) | 사용자 행동·의존성·단계별 목표와 확인 가능한 완료 기준을 정합니다. |
| 구현 | `code` | 선택한 플랫폼과 기존 구조로 합의한 기능을 구현합니다. |
| 구현 | `os-integrations` | 기능에 필요한 OS 서비스·권한·수명주기 처리를 연결합니다. |
| 구현 | `performance` | 재현 가능한 병목을 측정하고 원인을 수정한 뒤 결과를 비교합니다. |
| 구현 | [`improve-architecture`](skills/baa/common/baa-improve-architecture/PROCEDURE.md) | 실제 구조 문제를 검토하고 동작을 보존하는 근거 있는 변경만 수행합니다. |
| 구현 | `agent-cli` | 요청된 경우 해당 플랫폼에서 가능한 자동화·CLI 연동을 제한된 범위로 구성합니다. |
| 디자인 | [`ux-design`](skills/baa/common/baa-ux-design/PROCEDURE.md) | 구현 전에 행동 이름·탐색·표현 방식·상태·문구·접근성을 설계합니다. |
| 디자인 | `native-design` | 창·화면·입력·상호작용을 플랫폼 관례에 맞춥니다. Windows에서는 Tauri 웹 콘텐츠를 다룹니다. |
| 디자인 | `design-system` | 필요한 의미 기반 색상·서체·간격·테마·모션 토큰을 재사용하거나 정합니다. |
| 디자인 | `layout-grid` | 변경 화면의 간격·정렬·잘림과 필요한 화면 크기·배율 대응을 점검합니다. |
| 디자인 | `design-kit` | 앱의 컴포넌트와 상호작용 상태를 재사용하거나 확장합니다. |
| 디자인 | `design-from-app` | 제공된 시각 자료를 앱에 맞게 적용하고 같은 화면·상태로 비교합니다. |
| 디자인 | `app-icon` | 기존 원본을 보존하며 플랫폼별 앱 아이콘과 관련 자산을 준비합니다. |
| 검증·배포 | `build-and-verify` | 영향받는 앱 동작을 빌드·실행 확인하고 컴파일과 런타임 증거를 구분합니다. |
| 검증·배포 | `test` | 기존 프로젝트 도구를 우선 활용해 관련 로직·통합·UI 검사를 수행합니다. |
| 검증·배포 | [`improve-loop`](skills/baa/common/baa-improve-loop/PROCEDURE.md) | 합의한 스토리의 계획·구현·검증·수정·기록을 반복하고, 승인된 경우에만 커밋합니다. |
| 검증·배포 | `distribute` | 요청한 패키징·서명·배포 단계를 준비하며 게시·설치 권한을 임의로 확대하지 않습니다. |

### 플랫폼별 전문 절차

공통 조사·기획·UX·구조 검토·반복 실행은 위 문서를 함께 사용합니다. 플랫폼에 따라 달라지는 시작·코드·디자인·테스트 절차의 실제 연결은 다음과 같습니다. OS 연동·성능·디자인 토큰·배포도 같은 방식으로 해당 플랫폼 문서에 연결됩니다. iOS·iPadOS는 기기별 전문 절차와 Apple 공통 기반을 함께 읽습니다.

| 플랫폼 | 새 앱 | 구현 | 플랫폼 UX·디자인 | 테스트 |
| --- | --- | --- | --- | --- |
| macOS | [new-mac-app](skills/baa/platforms/apple/macos/skills/start/new-mac-app/PROCEDURE.md) | [Swift / SwiftUI / AppKit](skills/baa/platforms/apple/macos/skills/code/swift-swiftui/PROCEDURE.md) | [mac-design](skills/baa/platforms/apple/macos/skills/design/mac-design/PROCEDURE.md) | [test-mac-app](skills/baa/platforms/apple/macos/skills/ship/test-mac-app/PROCEDURE.md) |
| iOS | [new-ios-app](skills/baa/platforms/apple/ios/skills/start/new-ios-app/PROCEDURE.md) | [Swift / SwiftUI / UIKit](skills/baa/platforms/apple/ios/skills/code/baa-ios-code/PROCEDURE.md) | [iOS design](skills/baa/platforms/apple/ios/skills/design/baa-ios-design/PROCEDURE.md) | [iOS tests](skills/baa/platforms/apple/ios/skills/ship/baa-ios-test/PROCEDURE.md) |
| iPadOS | [new-ipados-app](skills/baa/platforms/apple/ipados/skills/start/new-ipados-app/PROCEDURE.md) | [Swift / SwiftUI / UIKit](skills/baa/platforms/apple/ipados/skills/code/baa-ipados-code/PROCEDURE.md) | [iPadOS design](skills/baa/platforms/apple/ipados/skills/design/baa-ipados-design/PROCEDURE.md) | [iPadOS tests](skills/baa/platforms/apple/ipados/skills/ship/baa-ipados-test/PROCEDURE.md) |
| Android | [new-android-app](skills/baa/platforms/android/skills/start/new-android-app/PROCEDURE.md) | [Kotlin / Compose / Views](skills/baa/platforms/android/skills/code/baa-android-code/PROCEDURE.md) | [Android design](skills/baa/platforms/android/skills/design/baa-android-native-design/PROCEDURE.md) | [Android tests](skills/baa/platforms/android/skills/ship/baa-android-test/PROCEDURE.md) |
| Windows | [new-windows-app](skills/baa/platforms/windows/skills/start/new-windows-app/PROCEDURE.md) | [Tauri / Rust / web frontend](skills/baa/platforms/windows/skills/code/tauri/PROCEDURE.md) | [Windows Tauri design](skills/baa/platforms/windows/skills/design/windows-design/PROCEDURE.md) | [Tauri tests](skills/baa/platforms/windows/skills/ship/test-windows-app/PROCEDURE.md) |

신규 Android 템플릿은 Compose 기반이며 기존 Views 앱은 요청 없이 전환하지 않습니다. Windows는 Tauri만 지원하고 기존 웹 프런트엔드는 유지합니다. 다른 Windows 기술의 프로젝트는 이전 범위를 명시적으로 합의한 후에 변경합니다. macOS 배포는 프로젝트의 실제 직접 배포·App Store 방식을 조사해 진행합니다.

## 설치

에이전트마다 한 가지 방식만 선택하세요. 플러그인·skills CLI·직접 연결을 함께 사용하면 같은 명령이 중복될 수 있습니다.

<details open>
<summary><b>Claude Code</b></summary>

Claude Code 안에서 실행합니다.

```text
/plugin marketplace add https://github.com/hoy2on/BAA.git
/plugin install baa@baa
```

터미널에서는 다음 명령도 사용할 수 있습니다.

```sh
claude plugin marketplace add https://github.com/hoy2on/BAA.git
claude plugin install baa@baa --scope user
```

업데이트한 뒤 새 세션을 시작합니다.

```sh
claude plugin marketplace update baa
claude plugin update baa@baa
```

</details>

<details>
<summary><b>Codex</b></summary>

플러그인 명령을 지원하는 Codex CLI에서 실행합니다.

```sh
codex plugin marketplace add https://github.com/hoy2on/BAA.git
codex plugin add baa@baa
```

업데이트는 다음과 같습니다. 설치 후 실행 중인 Codex를 다시 시작하세요.

```sh
codex plugin marketplace upgrade baa
codex plugin add baa@baa
```

</details>

<details>
<summary><b>다른 에이전트 또는 skills CLI</b></summary>

[skills CLI](https://github.com/vercel-labs/skills)를 사용합니다. Node.js 22.20 이상이 필요합니다.

```sh
npx skills@latest add hoy2on/BAA --skill "*"
```

설치 대상 에이전트를 선택합니다. 기본은 현재 프로젝트 설치이며, 전체 프로젝트에서 사용하려면 `-g`를 추가합니다.

```sh
npx skills@latest add hoy2on/BAA --skill "*" -a codex -g
npx skills@latest add hoy2on/BAA --skill "*" -a claude-code -g
```

`/baa` 하나만 필요하면 중앙 스킬만 설치해도 모든 플랫폼의 내부 전문 절차를 사용할 수 있습니다.

```sh
npx skills@latest add hoy2on/BAA --skill baa -a codex
```

`baa-apple`·`baa-android`·`baa-windows`는 중앙 `baa`를 함께 사용합니다. 플랫폼 진입점만 따로 설치하지 마세요. 네 개를 모두 선택하거나 `baa`만 선택하세요. 업데이트는 `npx skills@latest update`를 사용합니다.

</details>

<details>
<summary><b>직접 연결 / 로컬 수정</b></summary>

macOS·Linux의 Bash에서 저장소를 복제하고 실행합니다.

```sh
git clone https://github.com/hoy2on/BAA.git
cd BAA
./scripts/link-skills.sh
```

공개 스킬 네 개만 `~/.claude/skills`와 `~/.agents/skills`에 연결합니다. 기존 파일이나 다른 링크는 덮어쓰지 않으며, 원본 수정은 두 에이전트에 함께 반영됩니다. 업데이트는 `git pull` 후 새 세션을 시작합니다.

Windows에서는 위 플러그인 또는 skills CLI 설치를 사용하세요.

</details>

## 요구 환경과 검증 범위

BAA는 스킬을 지원하는 에이전트가 필요하며, resolver는 Python 3.9 이상과 표준 라이브러리를 사용합니다. Python이 없으면 에이전트가 같은 `routing.json`에서 허용 범위와 연결 문서를 직접 확인합니다. 스킬 사용을 위해 런타임이나 패키지를 자동 설치하지 않습니다.

앱 빌드에는 실제 프로젝트가 사용하는 Xcode·Apple SDK, Android SDK·JDK·Gradle, Rust MSVC·Microsoft C++ 빌드 도구·WebView2 등의 도구가 별도로 필요합니다. 모든 도구를 설치하거나 최소 OS를 올리도록 강제하지 않습니다. UI 조작에는 실제 사용 가능한 테스트·기기·컴퓨터 조작 도구가 필요합니다.

소스 수정, 빌드 성공, UI 실행, 실기기 검증을 구분합니다. macOS에서 Windows 코드를 수정했다고 Windows 실행을 검증한 것은 아닙니다. iOS와 iPadOS도 대상 기기를 각각 확인합니다. 실행 환경이 없으면 해당 검증을 대기로 남깁니다.

release 앱과 사용자 데이터는 보존하고, 개발 앱은 구분된 식별자와 고정 dev 설치본을 사용합니다. 서명·배포·스토어 제출은 실제 요청한 범위를 따릅니다.

## 구조

```text
.claude-plugin/         Claude·Codex 마켓플레이스와 플러그인 메타데이터
skills/
  baa/                 자체 완결된 중앙 스킬과 실행 패키지
    SKILL.md
    EXECUTION.md
    routing.json
    common/            공통 절차
    platforms/
      apple/
        shared/skills/  단계별 iOS·iPadOS 공통 기반 절차
        macos/skills/   단계별 macOS 절차
        ios/
          skills/      iOS 전문 start·plan·code·design·ship
          specs/       iPhone 예제 기획서
        ipados/
          skills/      iPadOS 전문 start·plan·code·design·ship
          specs/       iPad 예제 기획서
      android/skills/   단계별 Android 절차
      windows/skills/   단계별 Windows 절차
    scripts/resolve.py
    LICENSES/          원본 라이선스·출처 기록
  baa-apple/           Apple 전용 진입점
  baa-android/         Android 전용 진입점
  baa-windows/         Windows 전용 진입점
scripts/link-skills.sh  로컬 직접 연결
tests/                 연결·설치·개발 앱 보호 검사
```

중앙 스킬 폴더에 내부 절차·참고 자료·도구·템플릿·출처를 포함하므로, 플러그인 설치와 skills CLI의 폴더 복사 설치에서 같은 자료를 사용합니다.

절차는 `start`(진입점·앱 생성), `plan`(참고 앱 분석), `code`(구현·OS 연동·성능·agent CLI), `design`(네이티브 UI·디자인 자료), `ship`(빌드·테스트·배포)으로 나눕니다. 강제 순서가 아닌 목적별 분류이므로 기존 앱에서는 필요한 단계부터 시작합니다. 플랫폼 독립 기획·UX는 `common/`을 사용합니다.

Apple의 각 OS는 자체 전문 절차를 갖습니다. iOS·iPadOS 각각 다섯 단계와 specs를 갖추고, 전문 절차에서 기기별 요구사항과 `apple/shared/skills/<단계>/`의 공통 기반 지침을 함께 적용합니다. resolver는 OS 전문 절차를 `path`, 공유 기반 절차를 `references`로 반환합니다. macOS의 AppKit 도구·템플릿·데스크톱 예제는 UIKit·모바일 절차와 다르므로 유지합니다. 역할별 실제 위치는 `routing.json`을 기준으로 확인합니다.

선택적으로 사용할 예제 기획서는 [iOS specs](skills/baa/platforms/apple/ios/specs/README.md), [iPadOS specs](skills/baa/platforms/apple/ipados/specs/README.md), [macOS specs](skills/baa/platforms/apple/macos/specs/README.md)에 있습니다. 기존 앱 작업에서는 예제를 강제하지 않습니다.

모바일의 내부 `scaffold` 역할은 데스크톱과 같은 명명 방식인 `start/new-ios-app`, `start/new-ipados-app`, `start/new-android-app`에 연결됩니다. Apple은 `apple/shared/skills/start/new-apple-app/template`의 Xcode 프로젝트·앱 진입점·제목 모델·XCTest/XCUITest 타깃·빌드 스크립트를 공유하고, 각 OS가 SwiftUI 화면을 제공합니다. Android는 Kotlin·Compose 앱, Gradle Wrapper, manifest·리소스와 unit·기기 테스트를 포함합니다. 이 템플릿은 신규 앱에만 적용합니다.

```sh
python3 skills/baa/scripts/new-app.py ios MyPhoneApp com.example.myphoneapp ~/Developer
python3 skills/baa/scripts/new-app.py ipados MyPadApp com.example.mypadapp ~/Developer
python3 skills/baa/scripts/new-app.py android MyAndroidApp com.example.myandroidapp ~/Developer
python3 skills/baa/scripts/new-app.py windows MyWindowsApp com.example.mywindowsapp ~/Developer
```

생성기는 기존 기획 문서를 보존하고 파일·프로젝트 충돌 시 중단하며, 앱 설치나 Git 명령은 실행하지 않습니다. Apple 신규 템플릿 기준은 Swift 6·Xcode 16 이상·iOS/iPadOS 17.0 이상이며 `--min-os`로 더 높은 최소 OS를 지정할 수 있습니다. Android는 Gradle 8.14.3·AGP 8.11.2·Kotlin 2.3.20·Compose BOM 2025.09.00·compile/target SDK 36·minSdk 26을 고정하며 사용 전 실제 설치 도구를 확인합니다. 기존 프로젝트의 버전은 유지합니다. Android 첫 빌드는 의존성을 다운로드할 수 있고 Gradle 라이선스를 템플릿에 보존합니다. 제품 아이콘과 실기기 서명 설정은 후속 작업입니다.

[플랫폼 구성 점검 기록](docs/platform-coverage.md)에 보완 항목과 의도적으로 구분한 차이를 정리했습니다. 모바일 UX·구조 검토·OS 연동·성능·기존 앱 검증·화면 비교 자료를 라우팅에 연결했고, [Android specs](skills/baa/platforms/android/specs/README.md)도 추가했습니다.

UI 작업에는 [디자인 검색·결정 흐름](skills/baa/common/baa-ux-design/design-intelligence.md)을 적용합니다. ui-ux-pro-max가 설치되어 있으면 실제 로컬 스킬에서 필요한 검색을 수행하고 플랫폼·기술 적합성을 확인한 결정만 담당자에게 전달합니다. 신규 시각 방향은 디자인 시스템 후보를 검토하고, 기존 화면의 작은 수정은 기존 체계를 유지하며 해당 문제만 검색합니다. 조율자가 기존 MASTER·화면별 결정을 보존하고 공통 문서를 한 번만 갱신합니다. [UI 검토 기준](skills/baa/common/baa-ux-design/ui-review.md)은 네이티브 플랫폼에 맞춰 검증 단계에 연결됩니다. 외부 스킬이 없어도 BAA 내장 기준으로 진행하며 검색 DB를 포함하거나 자동 설치하지 않습니다.

Windows 새 앱은 TypeScript/Vite 화면과 Rust 호스트, 별도 `.dev` 설정으로 생성합니다. 기존 앱의 프런트엔드는 유지합니다. 실제 Windows 빌드·실행은 Windows 환경에서 검증하며 웹 미리보기와 구분합니다.

## 개발과 검증

```sh
python3 -m unittest discover -s tests -v
bash -n scripts/link-skills.sh
claude plugin validate .
python3 skills/baa/scripts/resolve.py --entrypoint baa-apple --platform macos --step native-design
python3 skills/baa/scripts/resolve.py --entrypoint baa-android --platform android --step code
```

검사는 공개 진입점 네 개, 플랫폼 범위 제한, 내부 연결과 상대 링크, 중앙 스킬 단독 복사, 설치 충돌 보호, 원본 dev 템플릿의 보호 동작을 확인합니다. 앱 런타임이나 모든 자연어 판단의 정확성을 보증하는 검사는 아닙니다. macOS 전용 템플릿 검사는 macOS에서 실행하며 다른 OS에서는 건너뜁니다.

숫자 버전은 두지 않고 Git commit 기준으로 업데이트합니다. 일부 검증 도구는 version 누락을 권고할 수 있습니다.

## 출처와 라이선스

[MIT](LICENSE). BAA는 [Dave Ebbelaar](https://github.com/daveebbelaar)의 [BAMA](https://github.com/daveebbelaar/bama)와 [BAWA](https://github.com/daveebbelaar/bawa)를 참고했습니다. 원본 사용 조건과 가져온 commit은 [라이선스 폴더](skills/baa/LICENSES)에 보존합니다.
