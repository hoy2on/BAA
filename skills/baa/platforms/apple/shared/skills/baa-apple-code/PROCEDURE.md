---
name: baa-apple-code
description: BAA Swift·SwiftUI·UIKit 구현 전문 스킬. iOS/iPadOS 작업의 code 단계를 배정받았을 때 현재 앱 구조와 실제 도구로 수행합니다.
---

# Swift·SwiftUI·UIKit 구현

[BAA 실행 계약](../../../../../EXECUTION.md)을 먼저 따른다. 전달된 대상 플랫폼, 목적, 소유 파일과 완료 기준을 이어받는다.
이 스킬은 BAA 내부 실행용이며 플랫폼 선택이나 팀 생성을 다시 시작하지 않는다. 다른 작업자의 변경을 되돌리지 않는다.

## 수행

먼저 수정 지점의 호출부, 모델, 저장소, 화면·테스트와 실제 Swift 언어/SDK/최소 OS를 확인한다. 새 버전 문법이나 관찰 체계를 기존 앱 전체에 강제하지 않는다.
SwiftUI에서는 기존 상태 소유권을 유지한다. 뷰가 소유하는 상태와 외부에서 받은 값·Binding을 구분하고 identity는 안정적인 모델 ID를 사용한다. `body`에서 I/O·데이터 갱신을 시작하지 않는다.
UI 상태는 기존 main actor 규칙에서 갱신한다. 무거운 계산·파일 작업을 UI 경로에서 분리하고 기존 actor/비동기 API를 재사용한다. Task 취소·뷰 수명과 오류 전달을 확인하며 경고를 없애기 위해 임의의 unchecked Sendable을 추가하지 않는다.
UIKit은 기존 controller/view 수명, reuse와 delegate를 따른다. SwiftUI bridge가 필요할 때 UIViewRepresentable/UIViewControllerRepresentable의 update·해제와 Coordinator 소유권을 확인한다. AppKit 타입을 iOS 코드에 넣지 않는다.
저장 모델 변경은 현재 persistence의 migration을 사용하고 기존 파일·데이터를 보존한다. UI 선택을 배열 index에 묶어 삭제/정렬 뒤 다른 항목이 선택되지 않도록 한다.
iOS는 push/pop·sheet dismissal·키보드와 safe area, iPadOS는 같은 상태의 multi-column 전환·다중 scene·창 크기 변경에서 선택과 편집을 보존한다.
최소 동작을 구현하고 기존 unit/UI 테스트에 영향받는 경계 사례를 확인한다. UI 검증은 resolver의 `build-and-verify`와 `test`, 모양은 `native-design`, OS API는 `os-integrations`를 사용한다.
완료: 요청한 코드와 호환성이 구현되고 실제 검증 범위와 실패/미검증 항목이 연결되어 있다.

## 다음 스킬과 인계

이 문서의 후속 역할은 실행 패키지 루트에서 `python3 scripts/resolve.py --entrypoint <호출 진입점> --platform <배정된 플랫폼> --step <역할>`로 확인한 정확한 이름·경로로 호출한다.
resolver가 반환한 path의 PROCEDURE.md를 읽는다. 내부 문서를 Skill 도구나 슬래시 명령으로 호출하지 않는다. 현재 단계로 재귀 호출하지 않으며 요청하지 않은 배포·설치·커밋을 추가하지 않는다.
변경 파일, source 상태·타깃·환경, 검사와 화면·로그 경로, 미검증·공유 변경 요청을 조율자에게 반환한다.

공식 참고: [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/), [SwiftUI](https://developer.apple.com/documentation/swiftui), [UIKit](https://developer.apple.com/documentation/uikit), [XCTest](https://developer.apple.com/documentation/xctest). 구현 API의 가용성·서명은 현재 SDK와 프로젝트 최소 OS에서 확인한다.
