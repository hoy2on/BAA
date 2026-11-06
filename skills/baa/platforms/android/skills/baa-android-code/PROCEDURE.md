---
name: baa-android-code
description: BAA Kotlin·Compose·Views 구현 전문 스킬. Android 작업의 code 단계를 배정받았을 때 현재 앱 구조와 실제 도구로 수행합니다.
---

# Kotlin·Compose·Views 구현

[BAA 실행 계약](../../../../EXECUTION.md)을 먼저 따른다. 전달된 대상 플랫폼, 목적, 소유 파일과 완료 기준을 이어받는다.
이 스킬은 BAA 내부 실행용이며 플랫폼 선택이나 팀 생성을 다시 시작하지 않는다. 다른 작업자의 변경을 되돌리지 않는다.

## 수행

호출부, 상태 소유자, 저장소, navigation, Gradle 의존성과 지원 SDK를 읽고 기존 Compose/Views/다른 framework를 유지한다. 기존 Views 화면을 요청 없이 Compose로 전환하지 않는다.
Compose는 state를 아래로, event를 위로 전달하고 기존 state holder/ViewModel을 재사용한다. composable body에서 DB/network writes를 하지 않고 effect는 적절한 key·수명·취소를 갖는다.
설치된 lifecycle 라이브러리를 확인해 lifecycle-aware Flow 수집을 사용한다. ViewModel 수명과 화면 표시 수명을 구분하고 화면을 떠난 뒤 불필요한 작업이 계속되지 않도록 한다.
CPU와 blocking I/O를 UI thread에서 분리하되 기존 dispatcher와 suspend API를 사용한다. GlobalScope·임의 무한 scope를 만들지 않고 cancellation을 정상 오류와 구분한다.
Views에서는 fragment view lifecycle, listener/adapter 해제, RecyclerView stable ID·reuse와 saved state를 유지한다. Compose와 Views bridge는 실제 사용하는 AndroidView/ComposeView 수명 규칙을 확인한다.
저장 schema 변경은 기존 Room/SQLite/파일 migration을 사용하고 destructive migration·사용자 데이터 초기화로 오류를 숨기지 않는다. 선택과 리스트 identity는 모델 ID를 사용한다.
뒤로 가기·IME/insets·activity 재생성·rotation 등 영향받는 경계를 테스트하고 `build-and-verify`, `test`로 연결한다.
완료: 요구 동작과 실패·취소·복원 경로가 현재 앱 구조에서 구현되고 검증 근거가 있다.

## 다음 스킬과 인계

이 문서의 후속 역할은 실행 패키지 루트에서 `python3 scripts/resolve.py --entrypoint <호출 진입점> --platform <배정된 플랫폼> --step <역할>`로 확인한 정확한 이름·경로로 호출한다.
resolver가 반환한 path의 PROCEDURE.md를 읽는다. 내부 문서를 Skill 도구나 슬래시 명령으로 호출하지 않는다. 현재 단계로 재귀 호출하지 않으며 요청하지 않은 배포·설치·커밋을 추가하지 않는다.
변경 파일, source 상태·타깃·환경, 검사와 화면·로그 경로, 미검증·공유 변경 요청을 조율자에게 반환한다.

공식 참고: [Android UI](https://developer.android.com/design/ui/mobile), [Compose architecture](https://developer.android.com/develop/ui/compose/architecture), [Lifecycle coroutines](https://developer.android.com/topic/libraries/architecture/coroutines), [Testing](https://developer.android.com/training/testing), [Adaptive layouts](https://developer.android.com/develop/ui/compose/build-adaptive-apps). 실제 Compose/Views 및 설치 의존성 버전에 맞는 API를 확인한다.
