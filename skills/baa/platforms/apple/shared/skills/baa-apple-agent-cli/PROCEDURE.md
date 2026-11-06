---
name: baa-apple-agent-cli
description: BAA Apple 모바일 자동화 진입점 전문 스킬. iOS/iPadOS 작업의 agent-cli 단계를 배정받았을 때 현재 앱 구조와 실제 도구로 수행합니다.
---

# Apple 모바일 자동화 진입점

[BAA 실행 계약](../../../../../EXECUTION.md)을 먼저 따른다. 전달된 대상 플랫폼, 목적, 소유 파일과 완료 기준을 이어받는다.
이 스킬은 BAA 내부 실행용이며 플랫폼 선택이나 팀 생성을 다시 시작하지 않는다. 다른 작업자의 변경을 되돌리지 않는다.

## 수행

사용자가 앱 자동화·agent 제어를 요청했을 때만 적용한다. 현재 앱의 App Intents/URL route/UI test bridge와 테스트 진입점을 확인한다.
iOS/iPadOS 앱은 desktop처럼 상시 실행되는 CLI/MCP 서버나 자유로운 local socket daemon이라고 가정하지 않는다. 실제 요구가 OS 자동화면 App Intents/Shortcuts, 테스트 제어면 기존 XCUITest를 우선한다.
명령별 입력 schema, 권한, 읽기/변경 효과, 처리 완료/오류 응답을 정의하고 기존 서비스 호출로 연결한다. UI·데이터 쓰기 경로를 복제하지 않는다.
외부 URL/payload는 인증·형식·크기·허용 명령을 검증하며 파일 경로나 임의 코드 실행을 노출하지 않는다. dev-only 테스트 bridge가 필요하면 release에서 비활성화되는 실제 build 조건을 확인한다.
호스트 CLI/MCP가 정말 필요하면 이미 허용된 기기/Xcode/테스트 도구를 호출하는 호스트 쪽 흐름과 모바일 앱 역할을 구분한다. 제어 채널이 없으면 연결됐다고 하지 않는다.
foreground/background·잠금·앱 종료 상태에서 가능한 범위를 확인하고 데이터 단일 writer와 scene 갱신을 유지한다.
완료: 지원 명령과 실행 한계가 명시되고 실제 연결에서 입력 검증·정상·실패 응답이 확인된다.

## 다음 스킬과 인계

이 문서의 후속 역할은 실행 패키지 루트에서 `python3 scripts/resolve.py --entrypoint <호출 진입점> --platform <배정된 플랫폼> --step <역할>`로 확인한 정확한 이름·경로로 호출한다.
resolver가 반환한 path의 PROCEDURE.md를 읽는다. 내부 문서를 Skill 도구나 슬래시 명령으로 호출하지 않는다. 현재 단계로 재귀 호출하지 않으며 요청하지 않은 배포·설치·커밋을 추가하지 않는다.
변경 파일, source 상태·타깃·환경, 검사와 화면·로그 경로, 미검증·공유 변경 요청을 조율자에게 반환한다.

공식 참고: [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/), [SwiftUI](https://developer.apple.com/documentation/swiftui), [UIKit](https://developer.apple.com/documentation/uikit), [XCTest](https://developer.apple.com/documentation/xctest). 구현 API의 가용성·서명은 현재 SDK와 프로젝트 최소 OS에서 확인한다.
