---
name: baa-ios
description: BAA iOS 플랫폼 담당자 진입점. 배정된 iOS 작업을 공통 기획과 해당 플랫폼 코딩·디자인·검증 스킬로 연결합니다.
---

# BAA iOS 담당자

[실행 계약](../../../../../EXECUTION.md)을 먼저 읽는다. 이 플랫폼을 직접 지정해 호출하면 iOS이 선택된 것으로 취급한다.
BAA 조율자가 배정한 호출 진입점·허용 범위·플랫폼·프로젝트·목적·현재 단계·소유 파일·완료 기준을 이어받는다. 대상 플랫폼을 다시 묻거나 신규 기획부터 재시작하지 않는다.
현재 요청과 배정된 iOS 대상이 충돌하면 조율자에게 알리고 수정 전에 확인한다. 다른 플랫폼으로 자동 전환하지 않는다. 실행 호스트를 보고 플랫폼을 바꾸지 않는다.

## 대상과 소유권

프로젝트의 실제 모듈·타깃·기술·지원 OS·dev 식별자·build/test 명령을 읽고 배정된 화면·동작의 호출부를 확인한다.
공유 소스·모델·번역·프로젝트 구성은 조율자가 정한 소유자만 수정한다. 타인의 변경을 되돌리지 않는다.
추가 공유 변경이 필요하면 변경 내용과 영향을 요청하고 독립 작업을 먼저 진행한다. 이 담당자는 하위 팀을 자동 생성하지 않는다.
같은 기기·출력·고정 dev 설치본을 쓰는 실행만 조율하여 순차 수행한다.

## 단계 연결

실행 패키지 루트의 `python3 scripts/resolve.py --entrypoint <호출 진입점> --platform ios --step <역할>` 결과로 해당 스킬의 정확한 이름과 PROCEDURE.md를 찾는다.
한 번에 필요한 역할 하나를 호출하고, 그 스킬의 다음 역할도 같은 ios resolver로 찾는다. 다른 플랫폼의 동명 스킬을 호출하지 않는다.
기획·일반 UX·개선 순환은 공통 스킬이며, 코딩·네이티브 UI·OS API·빌드·테스트는 플랫폼 매핑을 사용한다.

- 조사·기획: `research` → 필요하면 `clone` → `app-brief` → `user-stories` → `ux-design`.
- 신규 앱: `scaffold` → `native-design`와 필요한 `design-system`·`app-icon` → 현재 story의 `code`.
- 기존 기능: `code`와 필요한 `os-integrations`·`performance` → `build-and-verify`와 `test`.
- 디자인만 수정: `ux-design`(흐름·문구 문제일 때), `native-design` → 필요한 `design-system`·`design-kit`·`design-from-app`·`layout-grid`·`app-icon` → `build-and-verify`·`test`.
- 구조 검토: `improve-architecture`; 개발 목록 반복: 요청한 범위의 `improve-loop`.
- agent 제어 또는 배포는 각각 명시된 작업일 때만 `agent-cli`, `distribute`를 호출한다.

이미 있는 brief/story·디자인 문서는 재사용하고 현재 요청에 필요한 단계부터 시작한다.
조율자가 공통 문서를 작성 중이면 별도 복제본을 만들거나 같은 파일을 덮어쓰지 않는다.
하위 스킬에서 현재 router로 다시 연결돼도 같은 단계를 재귀 호출하지 않고 현재 단계의 역할을 실행한다.

## 플랫폼 판정과 인계

iOS/iPadOS 공통 Apple 코딩·토큰·OS연동 스킬을 사용하되 전달된 device family와 목적을 유지한다. iPhone과 iPad가 같은 타깃을 공유해도 실행 destination과 화면·입력 검증은 별개다.
iOS는 iPhone navigation·터치·keyboard·safe area·Dynamic Type의 변경 영향을 확인하고 iPadOS를 요청하지 않았다면 새 iPad 지원을 추가하지 않는다.
실행 환경·권한이 없으면 구현·정적 확인과 런타임 대기를 분리한다. 다른 OS 도구나 빈 결과를 실행 성공으로 보고하지 않는다.
완료 기준별 변경 파일, 소스 상태·타깃·환경, 검사·화면·로그, 미검증과 공유 변경 요청을 조율자에게 반환한다.
완료: 배정한 역할이 올바른 플랫폼 스킬로 연결되고 요청 범위의 구현·검증·환경 대기가 구분되어 있다.
