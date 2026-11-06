---
name: baa-android-design-from-app
description: BAA Android 참고 디자인 재현 전문 스킬. Android 작업의 design-from-app 단계를 배정받았을 때 현재 앱 구조와 실제 도구로 수행합니다.
---

# Android 참고 디자인 재현

[BAA 실행 계약](../../../../EXECUTION.md)을 먼저 따른다. 전달된 대상 플랫폼, 목적, 소유 파일과 완료 기준을 이어받는다.
이 스킬은 BAA 내부 실행용이며 플랫폼 선택이나 팀 생성을 다시 시작하지 않는다. 다른 작업자의 변경을 되돌리지 않는다.

## 수행

참고 화면의 앱·OS·기기·pixel 크기·density·font scale·theme·상태를 확인하고 현재 앱의 사용자 흐름에 대응시킨다.
이미지 pixel을 그대로 dp로 쓰지 않는다. reference와 실행 화면의 viewport·density·IME/system bar 조건을 맞추고 정보 순서·navigation·component를 먼저 비교한다.
`native-design`의 Android 관례를 보존하며 기존 Material/앱 component와 `design-system` 토큰으로 구현한다. 다른 플랫폼의 title bar·popover·hover 전제를 그대로 복사하지 않는다.
custom component가 필요하면 `design-kit`으로 연결하고 요청에 필요한 한 화면부터 완성한다. reference 회사의 로고·저작 자산은 사용할 권한과 교체 대상을 분리한다.
동일 데이터·theme·크기의 실행 캡처에서 구조, 글자, 간격·정렬, 색 순서로 차이를 기록한다. 자동 pixel diff는 렌더링·배율·상태가 같을 때 보조 근거로 사용한다.
해결한 차이와 남은 차이를 구분하고 `test`에서 실제 동작이 보존됐는지 확인한다.
완료: 재현 범위와 변경 부품/토큰, 전후 캡처와 미해결 차이가 연결된다.

## 다음 스킬과 인계

이 문서의 후속 역할은 실행 패키지 루트에서 `python3 scripts/resolve.py --entrypoint <호출 진입점> --platform <배정된 플랫폼> --step <역할>`로 확인한 정확한 이름·경로로 호출한다.
resolver가 반환한 path의 PROCEDURE.md를 읽는다. 내부 문서를 Skill 도구나 슬래시 명령으로 호출하지 않는다. 현재 단계로 재귀 호출하지 않으며 요청하지 않은 배포·설치·커밋을 추가하지 않는다.
변경 파일, source 상태·타깃·환경, 검사와 화면·로그 경로, 미검증·공유 변경 요청을 조율자에게 반환한다.

공식 참고: [Android UI](https://developer.android.com/design/ui/mobile), [Compose architecture](https://developer.android.com/develop/ui/compose/architecture), [Lifecycle coroutines](https://developer.android.com/topic/libraries/architecture/coroutines), [Testing](https://developer.android.com/training/testing), [Adaptive layouts](https://developer.android.com/develop/ui/compose/build-adaptive-apps). 실제 Compose/Views 및 설치 의존성 버전에 맞는 API를 확인한다.
