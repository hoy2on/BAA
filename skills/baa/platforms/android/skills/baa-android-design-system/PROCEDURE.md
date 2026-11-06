---
name: baa-android-design-system
description: BAA Android 테마와 토큰 전문 스킬. Android 작업의 design-system 단계를 배정받았을 때 현재 앱 구조와 실제 도구로 수행합니다.
---

# Android 테마와 토큰

[BAA 실행 계약](../../../../EXECUTION.md)을 먼저 따른다. 전달된 대상 플랫폼, 목적, 소유 파일과 완료 기준을 이어받는다.
이 스킬은 BAA 내부 실행용이며 플랫폼 선택이나 팀 생성을 다시 시작하지 않는다. 다른 작업자의 변경을 되돌리지 않는다.

## 수행

기존 Material/Compose theme, XML resources/styles, typography·spacing·shape·motion 정의와 app component를 읽는다. 같은 의미의 중복만 모으며 새 theme layer를 임의 도입하지 않는다.
semantic color와 light/dark resources를 사용한다. Compose ColorScheme과 Views theme attribute는 해당 프로젝트 기술에 맞게 사용하고 Swift Palette/XAML resource 이름을 이식하지 않는다.
font는 sp와 기존 typography를 사용하고 font scale·weight·fallback·긴 번역·RTL을 확인한다. spacing과 shape는 기존 dp 토큰을 재사용한다.
brand·status 의미는 공통 제품 요구와 맞추되 native control 치수·dynamic color·system bar 정책은 Android 기준을 따른다. custom color fill 위 text와 disabled/pressed 상태의 대비를 확인한다.
변경한 토큰의 사용처만 치환하고 공통 리소스 소유권을 지킨다. 기존 문서 한 곳에 의미와 예외를 기록하고 전체 앱 디자인 시스템을 불필요하게 재작성하지 않는다.
`build-and-verify`에서 light/dark·font scale·해당 창 크기를 비교한다.
완료: 실제 화면이 기존 토큰을 사용하고 색·글자·접근성 상태의 결과가 연결되어 있다.

## 다음 스킬과 인계

이 문서의 후속 역할은 실행 패키지 루트에서 `python3 scripts/resolve.py --entrypoint <호출 진입점> --platform <배정된 플랫폼> --step <역할>`로 확인한 정확한 이름·경로로 호출한다.
resolver가 반환한 path의 PROCEDURE.md를 읽는다. 내부 문서를 Skill 도구나 슬래시 명령으로 호출하지 않는다. 현재 단계로 재귀 호출하지 않으며 요청하지 않은 배포·설치·커밋을 추가하지 않는다.
변경 파일, source 상태·타깃·환경, 검사와 화면·로그 경로, 미검증·공유 변경 요청을 조율자에게 반환한다.

공식 참고: [Android UI](https://developer.android.com/design/ui/mobile), [Compose architecture](https://developer.android.com/develop/ui/compose/architecture), [Lifecycle coroutines](https://developer.android.com/topic/libraries/architecture/coroutines), [Testing](https://developer.android.com/training/testing), [Adaptive layouts](https://developer.android.com/develop/ui/compose/build-adaptive-apps). 실제 Compose/Views 및 설치 의존성 버전에 맞는 API를 확인한다.
