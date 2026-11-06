---
name: baa-android-app-icon
description: BAA Android 앱 아이콘 전문 스킬. Android 작업의 app-icon 단계를 배정받았을 때 현재 앱 구조와 실제 도구로 수행합니다.
---

# Android 앱 아이콘

[BAA 실행 계약](../../../../EXECUTION.md)을 먼저 따른다. 전달된 대상 플랫폼, 목적, 소유 파일과 완료 기준을 이어받는다.
이 스킬은 BAA 내부 실행용이며 플랫폼 선택이나 팀 생성을 다시 시작하지 않는다. 다른 작업자의 변경을 되돌리지 않는다.

## 수행

기존 launcher resource, manifest의 icon/roundIcon, adaptive icon XML과 foreground/background·monochrome 자산을 읽는다.
제품 의미와 기존 브랜드를 유지하고 사용 가능한 원본과 생성 도구를 재사용한다. Android Studio asset 도구 또는 기존 resource 생성 스크립트의 실제 지원 형식을 사용한다.
현재 minSdk/target과 launcher 요구에 맞는 adaptive/fallback·themed icon을 준비한다. safe zone·mask·density별 표시를 실제 문서와 device에서 확인하고 iOS/macOS 자산 형식을 등록하지 않는다.
dev 변형의 manifest/resource overlay가 실제로 새 icon을 참조하는지 build 결과와 설치 화면에서 확인한다. production 앱을 제거하거나 launcher 데이터를 지우지 않는다.
요청 범위에 해당하는 light/dark·themed icon·launcher mask에서 아이콘이 읽히는지 확인한다. 지원하지 않는 상태는 미검증으로 남긴다.
완료: 올바른 dev 타깃 resource 연결과 필요한 appearance의 실제 표시 근거가 있다.

## 다음 스킬과 인계

이 문서의 후속 역할은 실행 패키지 루트에서 `python3 scripts/resolve.py --entrypoint <호출 진입점> --platform <배정된 플랫폼> --step <역할>`로 확인한 정확한 이름·경로로 호출한다.
resolver가 반환한 path의 PROCEDURE.md를 읽는다. 내부 문서를 Skill 도구나 슬래시 명령으로 호출하지 않는다. 현재 단계로 재귀 호출하지 않으며 요청하지 않은 배포·설치·커밋을 추가하지 않는다.
변경 파일, source 상태·타깃·환경, 검사와 화면·로그 경로, 미검증·공유 변경 요청을 조율자에게 반환한다.

공식 참고: [Android UI](https://developer.android.com/design/ui/mobile), [Compose architecture](https://developer.android.com/develop/ui/compose/architecture), [Lifecycle coroutines](https://developer.android.com/topic/libraries/architecture/coroutines), [Testing](https://developer.android.com/training/testing), [Adaptive layouts](https://developer.android.com/develop/ui/compose/build-adaptive-apps). 실제 Compose/Views 및 설치 의존성 버전에 맞는 API를 확인한다.
