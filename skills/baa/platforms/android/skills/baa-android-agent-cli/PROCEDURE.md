---
name: baa-android-agent-cli
description: BAA Android 자동화 진입점 전문 스킬. Android 작업의 agent-cli 단계를 배정받았을 때 현재 앱 구조와 실제 도구로 수행합니다.
---

# Android 자동화 진입점

[BAA 실행 계약](../../../../EXECUTION.md)을 먼저 따른다. 전달된 대상 플랫폼, 목적, 소유 파일과 완료 기준을 이어받는다.
이 스킬은 BAA 내부 실행용이며 플랫폼 선택이나 팀 생성을 다시 시작하지 않는다. 다른 작업자의 변경을 되돌리지 않는다.

## 수행

사용자가 agent 제어·CLI·MCP를 요청했을 때만 적용한다. 기존 instrumentation·UI Automator·App Link/intent·test bridge로 해결 가능한지 확인한다.
Android 앱을 임의 shell service나 무인 공개 endpoint로 만들지 않는다. host CLI/MCP와 device-side 앱·instrumentation 역할을 구분한다.
명령별 입력 schema·읽기/쓰기 효과·결과·오류를 정하고 기존 서비스/UI state 경로를 호출한다. adb serial과 dev package를 고정하고 임의 shell·파일 경로를 입력으로 노출하지 않는다.
component export·permission·caller 검증을 확인한다. dev-only bridge는 manifest/build variant에서 release에 노출되지 않는지 검사하고 실제 앱 인증을 우회하지 않는다.
background 제한·잠금·앱 종료와 process 수명을 명시한다. 데이터 writer를 중복 생성하지 않고 기존 state·UI 갱신 경로를 유지한다.
실제 host-device 연결에서 정상·잘못된 입력·권한 실패·취소 응답을 확인하고 endpoint가 없으면 구축됐다고 보고하지 않는다.
완료: 지원 명령·보안 경계·실행 한계와 실제 연결 검증이 있다.

## 다음 스킬과 인계

이 문서의 후속 역할은 실행 패키지 루트에서 `python3 scripts/resolve.py --entrypoint <호출 진입점> --platform <배정된 플랫폼> --step <역할>`로 확인한 정확한 이름·경로로 호출한다.
resolver가 반환한 path의 PROCEDURE.md를 읽는다. 내부 문서를 Skill 도구나 슬래시 명령으로 호출하지 않는다. 현재 단계로 재귀 호출하지 않으며 요청하지 않은 배포·설치·커밋을 추가하지 않는다.
변경 파일, source 상태·타깃·환경, 검사와 화면·로그 경로, 미검증·공유 변경 요청을 조율자에게 반환한다.

공식 참고: [Android UI](https://developer.android.com/design/ui/mobile), [Compose architecture](https://developer.android.com/develop/ui/compose/architecture), [Lifecycle coroutines](https://developer.android.com/topic/libraries/architecture/coroutines), [Testing](https://developer.android.com/training/testing), [Adaptive layouts](https://developer.android.com/develop/ui/compose/build-adaptive-apps). 실제 Compose/Views 및 설치 의존성 버전에 맞는 API를 확인한다.
