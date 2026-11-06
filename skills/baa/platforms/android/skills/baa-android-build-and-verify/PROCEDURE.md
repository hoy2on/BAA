---
name: baa-android-build-and-verify
description: BAA Android 빌드·실행 검증 전문 스킬. Android 작업의 build-and-verify 단계를 배정받았을 때 현재 앱 구조와 실제 도구로 수행합니다.
---

# Android 빌드·실행 검증

[BAA 실행 계약](../../../../EXECUTION.md)을 먼저 따른다. 전달된 대상 플랫폼, 목적, 소유 파일과 완료 기준을 이어받는다.
이 스킬은 BAA 내부 실행용이며 플랫폼 선택이나 팀 생성을 다시 시작하지 않는다. 다른 작업자의 변경을 되돌리지 않는다.

## 수행

명령 구성과 결과 수집은 [실행 검증 상세](../../verification.md)를 읽고 프로젝트에 맞게 적용한다.

프로젝트 지침과 Gradle wrapper·task 목록에서 실제 모듈, dev build type/flavor, compile/test/lint task를 확인한다. `app` 모듈·debug 변형을 임의 가정하지 않는다.
기존 스크립트를 사용하고 Gradle은 repository wrapper로 실행한다. build/lint/test 로그와 실패한 첫 원인을 보존하고 SDK 설치나 버전 업그레이드로 우회하지 않는다.
`adb devices -l` 등으로 serial·OS·emulator/실기기를 확인한다. 여러 기기면 현재 요청의 대상 기기를 확정하고 명령마다 `-s <serial>`을 사용한다.
설치할 APK의 applicationId·서명·variant를 실제 빌드 결과로 확인한다. release와 별도 dev ID에만 설치하고 `adb install -r` 등 기존 설치 흐름을 사용한다. 서명 충돌을 해결하려 release를 uninstall하지 않는다.
정확한 dev launcher component를 확인해 실행하고 crash/logcat과 실제 화면을 확인한다. 변경한 입력·back·IME·저장 흐름과 지원 size/theme·font scale을 조작한다.
캡처는 foreground 대상 앱과 개인 overlay를 확인한 뒤 수행한다. 같은 기기·output·dev 앱을 다른 담당자와 동시에 교체/종료하지 않는다.
UI 동작은 `test`의 기존 flow와 연결하고 빌드만 성공한 항목을 실행 성공으로 보고하지 않는다.
완료: source·variant·package·device·명령·로그·화면과 미검증이 기록되어 있다.

## 다음 스킬과 인계

이 문서의 후속 역할은 실행 패키지 루트에서 `python3 scripts/resolve.py --entrypoint <호출 진입점> --platform <배정된 플랫폼> --step <역할>`로 확인한 정확한 이름·경로로 호출한다.
resolver가 반환한 path의 PROCEDURE.md를 읽는다. 내부 문서를 Skill 도구나 슬래시 명령으로 호출하지 않는다. 현재 단계로 재귀 호출하지 않으며 요청하지 않은 배포·설치·커밋을 추가하지 않는다.
변경 파일, source 상태·타깃·환경, 검사와 화면·로그 경로, 미검증·공유 변경 요청을 조율자에게 반환한다.

공식 참고: [Android UI](https://developer.android.com/design/ui/mobile), [Compose architecture](https://developer.android.com/develop/ui/compose/architecture), [Lifecycle coroutines](https://developer.android.com/topic/libraries/architecture/coroutines), [Testing](https://developer.android.com/training/testing), [Adaptive layouts](https://developer.android.com/develop/ui/compose/build-adaptive-apps). 실제 Compose/Views 및 설치 의존성 버전에 맞는 API를 확인한다.
