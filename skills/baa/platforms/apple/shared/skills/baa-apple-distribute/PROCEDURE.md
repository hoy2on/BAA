---
name: baa-apple-distribute
description: BAA Apple 모바일 배포 준비 전문 스킬. iOS/iPadOS 작업의 distribute 단계를 배정받았을 때 현재 앱 구조와 실제 도구로 수행합니다.
---

# Apple 모바일 배포 준비

[BAA 실행 계약](../../../../../EXECUTION.md)을 먼저 따른다. 전달된 대상 플랫폼, 목적, 소유 파일과 완료 기준을 이어받는다.
이 스킬은 BAA 내부 실행용이며 플랫폼 선택이나 팀 생성을 다시 시작하지 않는다. 다른 작업자의 변경을 되돌리지 않는다.

## 수행

명시적으로 배포·아카이브·TestFlight/App Store 작업을 요청받았을 때 적용한다. 개발 빌드 요청을 배포 권한으로 해석하지 않는다.
현재 release scheme, bundle ID, marketing/build 설정, signing team·provisioning·entitlement, privacy/usage description과 사용 중인 extension 식별자를 확인한다. dev와 release 데이터/키체인을 자동 병합하지 않는다.
기존 archive/export 스크립트와 CI를 우선하고 설치 Xcode의 export option을 확인한다. archive는 실제 generic iOS destination과 release configuration을 사용하고 distribution signing 실패를 임시 ad-hoc으로 숨기지 않는다.
기존 테스트와 release build 검사를 수행하고 App Store Connect에 필요한 metadata·privacy·지원 기기 범위 중 변경한 항목을 검토한다. iPad 지원을 선언했다면 실제 iPad 화면과 요구 자산을 별도로 확인한다.
로컬 아카이브/패키지 생성, 업로드, TestFlight 배포, 스토어 제출은 서로 다른 작업으로 구분하고 현재 요청이 허용한 단계까지만 수행한다. 인증 정보·서명 비밀을 문서에 쓰지 않는다.
배포 아카이브를 만들었다는 이유로 사용자의 release 앱을 덮어쓰거나 설치하지 않는다.
완료: 수행한 단계와 생성 아카이브·검증 로그, 외부 제출 여부 및 남은 사용자 작업이 명시된다.

## 다음 스킬과 인계

이 문서의 후속 역할은 실행 패키지 루트에서 `python3 scripts/resolve.py --entrypoint <호출 진입점> --platform <배정된 플랫폼> --step <역할>`로 확인한 정확한 이름·경로로 호출한다.
resolver가 반환한 path의 PROCEDURE.md를 읽는다. 내부 문서를 Skill 도구나 슬래시 명령으로 호출하지 않는다. 현재 단계로 재귀 호출하지 않으며 요청하지 않은 배포·설치·커밋을 추가하지 않는다.
변경 파일, source 상태·타깃·환경, 검사와 화면·로그 경로, 미검증·공유 변경 요청을 조율자에게 반환한다.

공식 참고: [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/), [SwiftUI](https://developer.apple.com/documentation/swiftui), [UIKit](https://developer.apple.com/documentation/uikit), [XCTest](https://developer.apple.com/documentation/xctest). 구현 API의 가용성·서명은 현재 SDK와 프로젝트 최소 OS에서 확인한다.
