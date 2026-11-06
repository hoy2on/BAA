---
name: baa-android-performance
description: BAA Android 성능 측정 전문 스킬. Android 작업의 performance 단계를 배정받았을 때 현재 앱 구조와 실제 도구로 수행합니다.
---

# Android 성능 측정

[BAA 실행 계약](../../../../EXECUTION.md)을 먼저 따른다. 전달된 대상 플랫폼, 목적, 소유 파일과 완료 기준을 이어받는다.
이 스킬은 BAA 내부 실행용이며 플랫폼 선택이나 팀 생성을 다시 시작하지 않는다. 다른 작업자의 변경을 되돌리지 않는다.

## 수행

증상과 재현 시나리오, 실제 기기/OS, build variant·데이터·측정 지표를 고정한다. emulator 결과를 실제 기기 성능으로 보고하지 않는다.
기존 profiler·Perfetto/System Trace, CPU/memory profiler, JankStats/Macrobenchmark가 있으면 증상에 필요한 도구를 선택한다. benchmark dependency는 필요성과 현재 구성을 확인한 뒤에만 추가한다.
UI thread의 blocking I/O·decode·DB work, Compose recomposition/state read·stable keys, RecyclerView binding/reuse와 layout 비용을 trace로 좁힌다.
기존 dispatcher·lazy/reuse·image sizing/caching으로 원인을 수정한다. 측정 없이 global cache·GlobalScope·새 architecture를 넣지 않는다.
동일 device·variant·scenario에서 startup/frames/memory 등 전후 지표를 비교하고 correctness·취소·메모리 수명·접근성 회귀를 확인한다.
thermal·debugger·background 부하 차이를 기록하고 release/profileable 측정과 debug 실행을 구분한다.
완료: 근거가 있는 원인과 수정, 비교 가능한 전후 측정·기능 검증 또는 실제 환경 제약이 있다.

## 다음 스킬과 인계

이 문서의 후속 역할은 실행 패키지 루트에서 `python3 scripts/resolve.py --entrypoint <호출 진입점> --platform <배정된 플랫폼> --step <역할>`로 확인한 정확한 이름·경로로 호출한다.
resolver가 반환한 path의 PROCEDURE.md를 읽는다. 내부 문서를 Skill 도구나 슬래시 명령으로 호출하지 않는다. 현재 단계로 재귀 호출하지 않으며 요청하지 않은 배포·설치·커밋을 추가하지 않는다.
변경 파일, source 상태·타깃·환경, 검사와 화면·로그 경로, 미검증·공유 변경 요청을 조율자에게 반환한다.

공식 참고: [Android UI](https://developer.android.com/design/ui/mobile), [Compose architecture](https://developer.android.com/develop/ui/compose/architecture), [Lifecycle coroutines](https://developer.android.com/topic/libraries/architecture/coroutines), [Testing](https://developer.android.com/training/testing), [Adaptive layouts](https://developer.android.com/develop/ui/compose/build-adaptive-apps). 실제 Compose/Views 및 설치 의존성 버전에 맞는 API를 확인한다.
