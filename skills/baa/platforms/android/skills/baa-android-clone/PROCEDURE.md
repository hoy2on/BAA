---
name: baa-android-clone
description: BAA Android 참고 앱 조사 전문 스킬. Android 작업의 clone 단계를 배정받았을 때 현재 앱 구조와 실제 도구로 수행합니다.
---

# Android 참고 앱 조사

[BAA 실행 계약](../../../../EXECUTION.md)을 먼저 따른다. 전달된 대상 플랫폼, 목적, 소유 파일과 완료 기준을 이어받는다.
이 스킬은 BAA 내부 실행용이며 플랫폼 선택이나 팀 생성을 다시 시작하지 않는다. 다른 작업자의 변경을 되돌리지 않는다.

## 수행

참고 앱·버전·OS·요청 흐름과 조사할 phone/tablet 범위를 정한다. `adb devices -l` 등으로 실제 연결 대상 serial과 해상도·밀도를 확인한다.
기존 UI Automator/Espresso/Compose test 또는 사용 가능한 조작 도구로 핵심 화면, 입력, back, sheet/dialog, 권한 거부와 오류 상태를 관찰한다. 다른 앱 private storage를 읽거나 인증을 우회하지 않는다.
캡처는 대상 앱 화면만 보이도록 준비한다. `adb -s <serial> exec-out screencap -p > <파일>`은 표시 화면 전체를 캡처하므로 앱이 foreground이고 민감한 overlay가 없는지 확인한다. 캡처가 조작을 대신하지 않는다.
이미지에 기기·orientation·pixels·density·font scale·theme를 연결하고 dp와 pixel을 구분한다. IME와 navigation/system bar를 앱 콘텐츠로 오인하지 않는다.
화면 index와 진입/종료·system back·상태 변화를 기록하고 배정된 플랫폼 절만 반환한다. 다음 단계는 resolver의 `user-stories`다.
완료: 요구 흐름의 화면·동작·대상 환경과 미확인 부분이 기록되어 있다.

## 다음 스킬과 인계

이 문서의 후속 역할은 실행 패키지 루트에서 `python3 scripts/resolve.py --entrypoint <호출 진입점> --platform <배정된 플랫폼> --step <역할>`로 확인한 정확한 이름·경로로 호출한다.
resolver가 반환한 path의 PROCEDURE.md를 읽는다. 내부 문서를 Skill 도구나 슬래시 명령으로 호출하지 않는다. 현재 단계로 재귀 호출하지 않으며 요청하지 않은 배포·설치·커밋을 추가하지 않는다.
변경 파일, source 상태·타깃·환경, 검사와 화면·로그 경로, 미검증·공유 변경 요청을 조율자에게 반환한다.

공식 참고: [Android UI](https://developer.android.com/design/ui/mobile), [Compose architecture](https://developer.android.com/develop/ui/compose/architecture), [Lifecycle coroutines](https://developer.android.com/topic/libraries/architecture/coroutines), [Testing](https://developer.android.com/training/testing), [Adaptive layouts](https://developer.android.com/develop/ui/compose/build-adaptive-apps). 실제 Compose/Views 및 설치 의존성 버전에 맞는 API를 확인한다.
