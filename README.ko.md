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

[빠른 시작](#빠른-시작) · [동작 방식](#동작-방식) · [명령](#명령) · [설치](#설치) · [개발과 검증](#개발과-검증)

</div>

BAA는 [BAMA](https://github.com/daveebbelaar/bama)의 macOS 개발 흐름과 [BAWA](https://github.com/daveebbelaar/bawa)의 Windows 개발 흐름을 바탕으로, iOS·iPadOS·Android 전문 절차와 중앙 플랫폼 라우터를 더한 프로젝트입니다. 별도 BAMA·BAWA 설치 없이 BAA 하나를 사용합니다.

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

BAA 중앙 라우터 → 플랫폼 담당 절차 → 현재 작업에 필요한 전문 절차 → 검증·결과 통합 순서로 진행합니다.

요청에 플랫폼이 있으면 그대로 사용합니다. 없으면 현재 작업에서 확정한 범위, 지정 파일·모듈의 실제 타깃, 프로젝트의 지원 대상을 확인합니다. 대상이 분명하면 알리고 진행하며, 여러 후보가 남으면 어떤 플랫폼을 작업할지 질문합니다. 실행 중인 컴퓨터의 OS나 Swift·Kotlin 같은 언어 이름만으로 대상을 선택하지 않습니다.

새 앱은 조사 → 참고 앱 분석(선택) → 개요 → 사용자 요구사항 → 프로젝트 생성 → 디자인 → 구현·검증으로 이어집니다. 기존 앱의 기능 수정이나 디자인 개선은 필요한 단계부터 시작합니다. 디자인만 요청했는데 새 앱이나 전체 기획을 만들지 않습니다.

독립적인 플랫폼 작업은 사용 가능한 서브에이전트에 나눠 병렬로 진행합니다. 공유 파일은 한 담당자가 맡고, 같은 기기·빌드 출력·설치본을 사용하는 검증은 순서대로 진행합니다. 병렬 도구가 없으면 순차 수행합니다.

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

## 전문 스킬

| 영역 | 사용하는 절차 |
| --- | --- |
| 공통 | 조사, 앱 개요, 사용자 스토리, UX, 구조 검토, 개선 순환 |
| macOS | BAMA 기반 Swift·SwiftUI·AppKit, macOS 디자인, OS 연동, 성능, 빌드·테스트 |
| iOS·iPadOS | Swift·SwiftUI·UIKit 공유 구현, 기기별 네이티브 디자인, OS 연동, 성능, 빌드·테스트·배포 준비 |
| Android | Kotlin·Compose·Views, Android 디자인, OS 연동, 성능, Gradle·adb 검증, 배포 준비 |
| Windows | BAWA 기반 C#·WinUI, Windows 디자인, OS 연동, 성능, 빌드·테스트·배포 |

단계 이름이 같아도 플랫폼별 구현을 합치지 않습니다. 기존 앱의 UIKit·WPF·Views·크로스플랫폼 기술을 템플릿에 맞춰 바꾸지 않습니다. macOS에 원본 배포 절차가 없는 경우 실제 프로젝트의 릴리즈 절차를 조사합니다.

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

앱 빌드에는 실제 프로젝트가 사용하는 Xcode·Apple SDK, Android SDK·JDK·Gradle, Windows SDK·.NET 등의 도구가 별도로 필요합니다. 모든 도구를 설치하거나 최소 OS를 올리도록 강제하지 않습니다. UI 조작에는 실제 사용 가능한 테스트·기기·컴퓨터 조작 도구가 필요합니다.

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
      apple/           macOS·iOS·iPadOS와 공유 모바일 자료
      android/
      windows/
    scripts/resolve.py
    LICENSES/          BAMA·BAWA 원본 라이선스
    UPSTREAM.json      가져온 원본 commit
  baa-apple/           Apple 전용 진입점
  baa-android/         Android 전용 진입점
  baa-windows/         Windows 전용 진입점
scripts/link-skills.sh  로컬 직접 연결
tests/                 연결·설치·개발 앱 보호 검사
```

중앙 스킬 폴더에 내부 절차·참고 자료·도구·템플릿·출처를 포함하므로, 플러그인 설치와 skills CLI의 폴더 복사 설치에서 같은 자료를 사용합니다.

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

[MIT](LICENSE). BAA는 [Dave Ebbelaar](https://github.com/daveebbelaar)의 [BAMA](https://github.com/daveebbelaar/bama)와 [BAWA](https://github.com/daveebbelaar/bawa)를 기반으로 합니다. 원본의 전문 절차와 참고 자료·템플릿을 보존하며 중앙 라우터, 공통 절차와 모바일 전문 절차를 통합했습니다.

가져온 원본 commit은 [UPSTREAM.json](skills/baa/UPSTREAM.json), 원본 사용 조건은 [macOS 라이선스](skills/baa/LICENSES/macos-upstream.txt)와 [Windows 라이선스](skills/baa/LICENSES/windows-upstream.txt)에 기록되어 있습니다. 원본 프로젝트가 소개한 REA와 기타 참고 자료는 해당 프로젝트의 문서를 참고하세요.
