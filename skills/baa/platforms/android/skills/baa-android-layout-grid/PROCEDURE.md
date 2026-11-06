---
name: baa-android-layout-grid
description: BAA Android 레이아웃 정렬 전문 스킬. Android 작업의 layout-grid 단계를 배정받았을 때 현재 앱 구조와 실제 도구로 수행합니다.
---

# Android 레이아웃 정렬

[BAA 실행 계약](../../../../EXECUTION.md)을 먼저 따른다. 전달된 대상 플랫폼, 목적, 소유 파일과 완료 기준을 이어받는다.
이 스킬은 BAA 내부 실행용이며 플랫폼 선택이나 팀 생성을 다시 시작하지 않는다. 다른 작업자의 변경을 되돌리지 않는다.

## 수행

기존 dp spacing, sp typography, parent constraints와 actual window/insets를 확인한다. macOS point·Windows epx 수치를 그대로 사용하지 않는다.
leading/trailing·baseline·group spacing을 기존 토큰으로 맞춘다. Compose constraint/weight/intrinsic 측정과 Views constraint conflicts를 먼저 확인하고 반복 padding 보정으로 숨기지 않는다.
IME·system bars·cutout·edge-to-edge를 지원 SDK의 실제 동작에서 확인한다. touch target이 잘리거나 scroll container가 중첩되어 조작을 막지 않는지 확인한다.
font scale·긴 번역·RTL·light/dark에서 줄바꿈과 배치를 확인한다. 기존 지원 large-screen/foldable이면 window resize·pane 전환·hinge 영역의 영향을 확인한다.
기존 screenshot/layout 검사 도구와 UI hierarchy/logs를 재사용한다. JSON layout probe가 없다고 가정한 새 전역 검사 시스템을 만들지 않는다.
변경한 사용처의 토큰·constraint를 수정하고 인접 화면의 회귀를 확인한다.
완료: 요청 정렬 문제와 관련 창·글자 상태의 전후 실행 증거가 있다.

## 다음 스킬과 인계

이 문서의 후속 역할은 실행 패키지 루트에서 `python3 scripts/resolve.py --entrypoint <호출 진입점> --platform <배정된 플랫폼> --step <역할>`로 확인한 정확한 이름·경로로 호출한다.
resolver가 반환한 path의 PROCEDURE.md를 읽는다. 내부 문서를 Skill 도구나 슬래시 명령으로 호출하지 않는다. 현재 단계로 재귀 호출하지 않으며 요청하지 않은 배포·설치·커밋을 추가하지 않는다.
변경 파일, source 상태·타깃·환경, 검사와 화면·로그 경로, 미검증·공유 변경 요청을 조율자에게 반환한다.

공식 참고: [Android UI](https://developer.android.com/design/ui/mobile), [Compose architecture](https://developer.android.com/develop/ui/compose/architecture), [Lifecycle coroutines](https://developer.android.com/topic/libraries/architecture/coroutines), [Testing](https://developer.android.com/training/testing), [Adaptive layouts](https://developer.android.com/develop/ui/compose/build-adaptive-apps). 실제 Compose/Views 및 설치 의존성 버전에 맞는 API를 확인한다.
