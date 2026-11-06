---
name: baa-android-distribute
description: BAA Android 배포 준비 전문 스킬. Android 작업의 distribute 단계를 배정받았을 때 현재 앱 구조와 실제 도구로 수행합니다.
---

# Android 배포 준비

[BAA 실행 계약](../../../../EXECUTION.md)을 먼저 따른다. 전달된 대상 플랫폼, 목적, 소유 파일과 완료 기준을 이어받는다.
이 스킬은 BAA 내부 실행용이며 플랫폼 선택이나 팀 생성을 다시 시작하지 않는다. 다른 작업자의 변경을 되돌리지 않는다.

## 수행

명시적 release/패키징/스토어 요청일 때 적용한다. dev 설치와 release artifact 생성·외부 배포를 구분한다.
release variant/flavor, applicationId, versionCode/versionName의 기존 정책, signing config, min/target SDK·manifest·권한·privacy와 ProGuard/R8 설정을 확인한다. 키와 비밀번호를 코드·문서·로그에 출력하지 않는다.
기존 Gradle wrapper/CI의 확인된 bundle/assemble release task를 사용하고 릴리즈 shrink/obfuscation 결과·mapping·native symbol 등 현재 프로젝트 산출물을 보존한다.
release artifact의 package·서명·권한을 확인하고 필요 시 이미 허용된 별도 테스트 경로에서 동작을 검증한다. 사용자 release 앱을 제거·덮어쓰거나 기존 데이터를 이관하지 않는다.
AAB/APK 생성, 내부 배포, Play Console 업로드·트랙 rollout을 구분하여 현재 요청이 허용한 단계만 수행한다. 파일 생성 성공을 스토어 배포 완료로 보고하지 않는다.
완료: artifact·서명 검증·검사 결과와 실제 외부 제출 여부, 남은 단계가 명시된다.

## 다음 스킬과 인계

이 문서의 후속 역할은 실행 패키지 루트에서 `python3 scripts/resolve.py --entrypoint <호출 진입점> --platform <배정된 플랫폼> --step <역할>`로 확인한 정확한 이름·경로로 호출한다.
resolver가 반환한 path의 PROCEDURE.md를 읽는다. 내부 문서를 Skill 도구나 슬래시 명령으로 호출하지 않는다. 현재 단계로 재귀 호출하지 않으며 요청하지 않은 배포·설치·커밋을 추가하지 않는다.
변경 파일, source 상태·타깃·환경, 검사와 화면·로그 경로, 미검증·공유 변경 요청을 조율자에게 반환한다.

공식 참고: [Android UI](https://developer.android.com/design/ui/mobile), [Compose architecture](https://developer.android.com/develop/ui/compose/architecture), [Lifecycle coroutines](https://developer.android.com/topic/libraries/architecture/coroutines), [Testing](https://developer.android.com/training/testing), [Adaptive layouts](https://developer.android.com/develop/ui/compose/build-adaptive-apps). 실제 Compose/Views 및 설치 의존성 버전에 맞는 API를 확인한다.
