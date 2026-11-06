---
name: baa-apple-os-integrations
description: BAA Apple 모바일 OS 연동 전문 스킬. iOS/iPadOS 작업의 os-integrations 단계를 배정받았을 때 현재 앱 구조와 실제 도구로 수행합니다.
---

# Apple 모바일 OS 연동

[BAA 실행 계약](../../../../../EXECUTION.md)을 먼저 따른다. 전달된 대상 플랫폼, 목적, 소유 파일과 완료 기준을 이어받는다.
이 스킬은 BAA 내부 실행용이며 플랫폼 선택이나 팀 생성을 다시 시작하지 않는다. 다른 작업자의 변경을 되돌리지 않는다.

## 수행

요청한 연동에 필요한 API, entitlement, usage description, extension/target과 최소 OS를 현재 프로젝트와 공식 문서에서 확인한다. AppKit/Carbon/Windows API를 사용하지 않는다.
파일 가져오기·내보내기는 기존 document picker/FileDocument/UIDocument와 security-scoped URL 수명을 따른다. sandbox 밖 파일을 영구 접근할 수 있다고 가정하지 않는다.
공유·URL/deep link·App Intents·알림은 현재 앱의 route와 저장 경로로 연결한다. 외부 입력의 형식·권한·경로를 검증하고 UI가 준비되기 전 이벤트와 반복 이벤트를 처리한다.
카메라·마이크·사진·위치는 필요한 순간에만 권한을 요청하고 denied/restricted와 설정 복귀를 다룬다. 검증을 위해 모든 권한을 자동 grant하거나 production 권한을 reset하지 않는다.
background task와 audio/session은 OS가 허용하는 수명에서 취소·복원·오류를 처리한다. 영구 실행 desktop process 전제를 가져오지 않는다.
iPadOS는 문서 다중 창, drag/drop·pointer/keyboard 등 연동되는 scene을 구분한다. 같은 공유 저장소 변경은 배정된 한 담당자만 수행한다.
실기기 의존 API를 Simulator 성공으로 대체하지 않는다. deep link/공유 payload와 권한 거부의 재현·로그를 남기고 `test`로 연결한다.
완료: 정상·거부·취소 경로가 구현되고 실제 대상 환경의 검증과 미검증이 구분된다.

## 다음 스킬과 인계

이 문서의 후속 역할은 실행 패키지 루트에서 `python3 scripts/resolve.py --entrypoint <호출 진입점> --platform <배정된 플랫폼> --step <역할>`로 확인한 정확한 이름·경로로 호출한다.
resolver가 반환한 path의 PROCEDURE.md를 읽는다. 내부 문서를 Skill 도구나 슬래시 명령으로 호출하지 않는다. 현재 단계로 재귀 호출하지 않으며 요청하지 않은 배포·설치·커밋을 추가하지 않는다.
변경 파일, source 상태·타깃·환경, 검사와 화면·로그 경로, 미검증·공유 변경 요청을 조율자에게 반환한다.

공식 참고: [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/), [SwiftUI](https://developer.apple.com/documentation/swiftui), [UIKit](https://developer.apple.com/documentation/uikit), [XCTest](https://developer.apple.com/documentation/xctest). 구현 API의 가용성·서명은 현재 SDK와 프로젝트 최소 OS에서 확인한다.
