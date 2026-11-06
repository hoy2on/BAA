---
name: baa-android-test
description: BAA Android 테스트 전문 스킬. Android 작업의 test 단계를 배정받았을 때 현재 앱 구조와 실제 도구로 수행합니다.
---

# Android 테스트

[BAA 실행 계약](../../../../EXECUTION.md)을 먼저 따른다. 전달된 대상 플랫폼, 목적, 소유 파일과 완료 기준을 이어받는다.
이 스킬은 BAA 내부 실행용이며 플랫폼 선택이나 팀 생성을 다시 시작하지 않는다. 다른 작업자의 변경을 되돌리지 않는다.

## 수행

명령 구성과 결과 수집은 [실행 검증 상세](../../verification.md)를 읽고 프로젝트에 맞게 적용한다.

변경한 로직, persistence·migration, UI·권한·하드웨어 경계를 분리해 기존 unit/instrumentation 타깃을 선택한다.
unit 테스트는 기존 JUnit/MockK 등 현재 의존성을 사용한다. coroutine test는 설치된 test dispatcher와 가상 시간을 재사용하고 고정 sleep으로 비동기 오류를 숨기지 않는다.
Compose UI test는 semantics·stable tag/label, Views는 Espresso/UI Automator 등 기존 도구로 사용자 입력과 결과를 검증한다. navigation/IME/back·rotation/activity 재생성과 state restoration은 변경한 범위에 맞춰 포함한다.
기존 fixture와 dev package의 격리된 test store를 사용하고 production database나 계정 데이터를 초기화하지 않는다. 앱 재설치를 테스트 환경 초기화의 기본값으로 쓰지 않는다.
권한 dialog·system UI 자동화는 실제 도구의 범위를 확인하며 도구가 찾지 못하는 것을 제품 결함으로 단정하지 않는다. camera/audio/notification 등 실제 기기가 필요한 항목을 분리한다.
기기 serial과 variant에 맞는 확인된 Gradle task를 실행하고 junit/XML·logcat·screenshots·source 상태를 반환한다. 동일 기기 UI 테스트와 수동 조작을 병렬 실행하지 않는다.
완료: 요구사항의 정상·실패·취소·복원 경계가 적절한 검사로 확인되고 환경 실패·미검증이 구분된다.

## 다음 스킬과 인계

이 문서의 후속 역할은 실행 패키지 루트에서 `python3 scripts/resolve.py --entrypoint <호출 진입점> --platform <배정된 플랫폼> --step <역할>`로 확인한 정확한 이름·경로로 호출한다.
resolver가 반환한 path의 PROCEDURE.md를 읽는다. 내부 문서를 Skill 도구나 슬래시 명령으로 호출하지 않는다. 현재 단계로 재귀 호출하지 않으며 요청하지 않은 배포·설치·커밋을 추가하지 않는다.
변경 파일, source 상태·타깃·환경, 검사와 화면·로그 경로, 미검증·공유 변경 요청을 조율자에게 반환한다.

공식 참고: [Android UI](https://developer.android.com/design/ui/mobile), [Compose architecture](https://developer.android.com/develop/ui/compose/architecture), [Lifecycle coroutines](https://developer.android.com/topic/libraries/architecture/coroutines), [Testing](https://developer.android.com/training/testing), [Adaptive layouts](https://developer.android.com/develop/ui/compose/build-adaptive-apps). 실제 Compose/Views 및 설치 의존성 버전에 맞는 API를 확인한다.
