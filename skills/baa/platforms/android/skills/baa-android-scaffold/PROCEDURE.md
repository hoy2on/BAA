---
name: baa-android-scaffold
description: BAA Android 초기 프로젝트 전문 스킬. Android 작업의 scaffold 단계를 배정받았을 때 현재 앱 구조와 실제 도구로 수행합니다.
---

# Android 초기 프로젝트

[BAA 실행 계약](../../../../EXECUTION.md)을 먼저 따른다. 전달된 대상 플랫폼, 목적, 소유 파일과 완료 기준을 이어받는다.
이 스킬은 BAA 내부 실행용이며 플랫폼 선택이나 팀 생성을 다시 시작하지 않는다. 다른 작업자의 변경을 되돌리지 않는다.

## 수행

명령 구성과 결과 수집은 [실행 검증 상세](../../verification.md)를 읽고 프로젝트에 맞게 적용한다.

Gradle wrapper, settings/modules, version catalog, plugin, minSdk/targetSdk, build type/flavor와 기존 앱 타깃을 먼저 조사한다. 기존 앱이 있으면 새 프로젝트를 만들지 않는다.
신규 앱은 설치 Android Studio/확인된 기존 저장소 template의 Gradle 구성을 사용한다. SDK·AGP·Kotlin·Compose 버전을 임의로 발명하지 않고 설치 도구·호환성 문서와 기존 catalog에서 정한다.
요구에 맞는 Compose 또는 기존 Views 앱 타깃과 unit/instrumentation test만 최소 생성한다. applicationId는 release와 공존하는 dev 변형을 사용하고 production 데이터·계정을 자동 공유하지 않는다.
첫 화면·최소 핵심 상태·manifest/launcher를 구성하고 필요한 권한만 선언한다. 단일 사용을 위한 repository/DI/multi-module 계층이나 서버를 추가하지 않는다.
Gradle task 목록에서 실제 모듈·변형의 assemble/test/lint task를 확인해 최소 빌드 후 선택한 emulator/기기에서 dev 앱을 실행한다.
생성 후 `native-design`, `design-system`, `app-icon`, story의 `code`로 연결한다. 새로운 dependency는 기존 기능을 검토한 뒤 필요한 것만 추가한다.
완료: 생성된 모듈·dev 식별자·기본 화면과 실제 build/launch 결과 또는 환경 제약이 기록된다.

## 다음 스킬과 인계

이 문서의 후속 역할은 실행 패키지 루트에서 `python3 scripts/resolve.py --entrypoint <호출 진입점> --platform <배정된 플랫폼> --step <역할>`로 확인한 정확한 이름·경로로 호출한다.
resolver가 반환한 path의 PROCEDURE.md를 읽는다. 내부 문서를 Skill 도구나 슬래시 명령으로 호출하지 않는다. 현재 단계로 재귀 호출하지 않으며 요청하지 않은 배포·설치·커밋을 추가하지 않는다.
변경 파일, source 상태·타깃·환경, 검사와 화면·로그 경로, 미검증·공유 변경 요청을 조율자에게 반환한다.

공식 참고: [Android UI](https://developer.android.com/design/ui/mobile), [Compose architecture](https://developer.android.com/develop/ui/compose/architecture), [Lifecycle coroutines](https://developer.android.com/topic/libraries/architecture/coroutines), [Testing](https://developer.android.com/training/testing), [Adaptive layouts](https://developer.android.com/develop/ui/compose/build-adaptive-apps). 실제 Compose/Views 및 설치 의존성 버전에 맞는 API를 확인한다.
