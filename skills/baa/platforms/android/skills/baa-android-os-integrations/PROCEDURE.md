---
name: baa-android-os-integrations
description: BAA Android OS 기능 연동 전문 스킬. Android 작업의 os-integrations 단계를 배정받았을 때 현재 앱 구조와 실제 도구로 수행합니다.
---

# Android OS 기능 연동

[BAA 실행 계약](../../../../EXECUTION.md)을 먼저 따른다. 전달된 대상 플랫폼, 목적, 소유 파일과 완료 기준을 이어받는다.
이 스킬은 BAA 내부 실행용이며 플랫폼 선택이나 팀 생성을 다시 시작하지 않는다. 다른 작업자의 변경을 되돌리지 않는다.

## 수행

manifest, runtime permission, exported component, intent filter, targetSdk와 OS 차이를 현재 요구에 맞춰 확인한다.
파일은 기존 Activity Result/Storage Access Framework·MediaStore와 URI 권한 수명을 사용한다. 접근한 URI가 영구 파일 경로라고 가정하지 않는다.
share/deep link/App Link·notification/foreground service·background work는 기존 앱 route·저장 서비스와 연결한다. intent extras·URI·MIME·경로·크기를 검증하고 외부 입력으로 임의 컴포넌트나 파일 접근을 허용하지 않는다.
권한은 필요한 순간에 요청하고 거부·다시 묻지 않음·설정 복귀·앱 재시작을 다룬다. 검증 편의를 위해 모든 권한 grant·pm clear·release uninstall을 실행하지 않는다.
수명과 OS 제한에 맞는 기존 WorkManager/service/Activity 흐름을 사용한다. desktop 상주 process 전제나 iOS background API를 가져오지 않는다.
선택 기기에서 정상·취소·거부·외부 입력·background 경로 중 변경 영향을 확인하고 하드웨어 의존 항목은 실제 기기 근거를 남긴다.
완료: 요청 연동의 권한·수명·신뢰 경계와 실패 경로가 구현되고 검증 범위가 명시된다.

## 다음 스킬과 인계

이 문서의 후속 역할은 실행 패키지 루트에서 `python3 scripts/resolve.py --entrypoint <호출 진입점> --platform <배정된 플랫폼> --step <역할>`로 확인한 정확한 이름·경로로 호출한다.
resolver가 반환한 path의 PROCEDURE.md를 읽는다. 내부 문서를 Skill 도구나 슬래시 명령으로 호출하지 않는다. 현재 단계로 재귀 호출하지 않으며 요청하지 않은 배포·설치·커밋을 추가하지 않는다.
변경 파일, source 상태·타깃·환경, 검사와 화면·로그 경로, 미검증·공유 변경 요청을 조율자에게 반환한다.

공식 참고: [Android UI](https://developer.android.com/design/ui/mobile), [Compose architecture](https://developer.android.com/develop/ui/compose/architecture), [Lifecycle coroutines](https://developer.android.com/topic/libraries/architecture/coroutines), [Testing](https://developer.android.com/training/testing), [Adaptive layouts](https://developer.android.com/develop/ui/compose/build-adaptive-apps). 실제 Compose/Views 및 설치 의존성 버전에 맞는 API를 확인한다.
