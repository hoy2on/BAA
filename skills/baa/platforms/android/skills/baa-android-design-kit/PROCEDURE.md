---
name: baa-android-design-kit
description: BAA Android 커스텀 컴포넌트 전문 스킬. Android 작업의 design-kit 단계를 배정받았을 때 현재 앱 구조와 실제 도구로 수행합니다.
---

# Android 커스텀 컴포넌트

[BAA 실행 계약](../../../../EXECUTION.md)을 먼저 따른다. 전달된 대상 플랫폼, 목적, 소유 파일과 완료 기준을 이어받는다.
이 스킬은 BAA 내부 실행용이며 플랫폼 선택이나 팀 생성을 다시 시작하지 않는다. 다른 작업자의 변경을 되돌리지 않는다.

## 수행

기존 Material component와 앱 composable/custom View가 요구를 충족하는지 확인한다. 필요한 커스텀 부품만 만든다.
입력 state·event, enabled/selected/pressed/focused/loading/error 상태와 접근성 semantics를 정한다. 앱 비즈니스 상태를 부품마다 새로 소유하지 않는다.
Compose는 기존 modifier·theme·interaction source 패턴을 유지하고 Button 같은 의미 있는 component를 단순 Box+click으로 대체하지 않는다. Views는 기존 style/custom View·state list와 focus/click 처리를 따른다.
`design-system`의 semantic colors·typography·shape·spacing을 쓰고 font scale·터치·keyboard·TalkBack action이 보존되도록 한다.
기존 preview/sample/test host에 관련 상태를 추가하고 실제 화면에 연결한다. 부품 하나 때문에 별도 sample 앱이나 UI framework를 만들지 않는다.
다크·긴 텍스트·좁은/넓은 지원 window와 disabled/selected·오류 상태를 실행해 확인한다.
완료: 요청 부품이 실제 화면에서 동작하고 상태·접근성·상호작용 검증이 있다.

## 다음 스킬과 인계

이 문서의 후속 역할은 실행 패키지 루트에서 `python3 scripts/resolve.py --entrypoint <호출 진입점> --platform <배정된 플랫폼> --step <역할>`로 확인한 정확한 이름·경로로 호출한다.
resolver가 반환한 path의 PROCEDURE.md를 읽는다. 내부 문서를 Skill 도구나 슬래시 명령으로 호출하지 않는다. 현재 단계로 재귀 호출하지 않으며 요청하지 않은 배포·설치·커밋을 추가하지 않는다.
변경 파일, source 상태·타깃·환경, 검사와 화면·로그 경로, 미검증·공유 변경 요청을 조율자에게 반환한다.

공식 참고: [Android UI](https://developer.android.com/design/ui/mobile), [Compose architecture](https://developer.android.com/develop/ui/compose/architecture), [Lifecycle coroutines](https://developer.android.com/topic/libraries/architecture/coroutines), [Testing](https://developer.android.com/training/testing), [Adaptive layouts](https://developer.android.com/develop/ui/compose/build-adaptive-apps). 실제 Compose/Views 및 설치 의존성 버전에 맞는 API를 확인한다.
