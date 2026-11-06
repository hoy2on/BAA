---
name: baa-android-native-design
description: BAA Android 네이티브 디자인 전문 스킬. Android 작업의 native-design 단계를 배정받았을 때 현재 앱 구조와 실제 도구로 수행합니다.
---

# Android 네이티브 디자인

[BAA 실행 계약](../../../../EXECUTION.md)을 먼저 따른다. 전달된 대상 플랫폼, 목적, 소유 파일과 완료 기준을 이어받는다.
이 스킬은 BAA 내부 실행용이며 플랫폼 선택이나 팀 생성을 다시 시작하지 않는다. 다른 작업자의 변경을 되돌리지 않는다.

## 수행

대상 화면의 목적, 기존 navigation·Material 버전·앱 theme·지원 창 범위를 확인한다. 기존 component와 시스템 control을 우선한다.
주요 destination과 하위 탐색을 구분하고 기존 navigation bar/rail/drawer·app bar 체계를 유지한다. system/predictive back은 현재 SDK·navigation 라이브러리 규칙에 맞추고 핵심 동작을 hover에 숨기지 않는다.
edge-to-edge/system bar·display cutout·IME insets를 실제 targetSdk와 창에서 확인한다. 전체 화면 pixel 크기를 고정해 padding으로 맞추지 않는다.
기존 typography·sp·dp·theme semantic color를 사용하고 Dynamic color는 기존 정책을 유지한다. 화면 수정 때문에 색상 설정·새 theme engine을 만들지 않는다.
font scale·TalkBack 읽기 순서·의미 있는 semantics·터치 영역·contrast·Reduce Motion/animation 관련 설정을 확인한다. selected·error 등 상태를 색만으로 나타내지 않는다.
phone/tablet/foldable/desktop 지원이 있으면 실제 window size에 맞춰 navigation·list-detail 배치를 확인한다. 물리 기기 이름만으로 large-screen 분기를 고정하지 않는다.
수정한 화면을 light/dark, 긴 문구, 큰 글자와 필요한 window 상태에서 실행하고 `layout-grid`, `build-and-verify`, `test`로 연결한다.
완료: 현재 Android 관례와 기존 앱 스타일에 맞고 실제 대상의 화면·입력 근거가 있다.

## 다음 스킬과 인계

이 문서의 후속 역할은 실행 패키지 루트에서 `python3 scripts/resolve.py --entrypoint <호출 진입점> --platform <배정된 플랫폼> --step <역할>`로 확인한 정확한 이름·경로로 호출한다.
resolver가 반환한 path의 PROCEDURE.md를 읽는다. 내부 문서를 Skill 도구나 슬래시 명령으로 호출하지 않는다. 현재 단계로 재귀 호출하지 않으며 요청하지 않은 배포·설치·커밋을 추가하지 않는다.
변경 파일, source 상태·타깃·환경, 검사와 화면·로그 경로, 미검증·공유 변경 요청을 조율자에게 반환한다.

공식 참고: [Android UI](https://developer.android.com/design/ui/mobile), [Compose architecture](https://developer.android.com/develop/ui/compose/architecture), [Lifecycle coroutines](https://developer.android.com/topic/libraries/architecture/coroutines), [Testing](https://developer.android.com/training/testing), [Adaptive layouts](https://developer.android.com/develop/ui/compose/build-adaptive-apps). 실제 Compose/Views 및 설치 의존성 버전에 맞는 API를 확인한다.
