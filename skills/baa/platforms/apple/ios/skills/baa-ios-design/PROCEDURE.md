---
name: baa-ios-design
description: BAA iOS 네이티브 디자인 전문 스킬. iOS 작업의 design 단계를 배정받았을 때 현재 앱 구조와 실제 도구로 수행합니다.
---

# iOS 네이티브 디자인

[BAA 실행 계약](../../../../../EXECUTION.md)을 먼저 따른다. 전달된 대상 플랫폼, 목적, 소유 파일과 완료 기준을 이어받는다.
이 스킬은 BAA 내부 실행용이며 플랫폼 선택이나 팀 생성을 다시 시작하지 않는다. 다른 작업자의 변경을 되돌리지 않는다.

## 수행

기존 iPhone 탐색·view hierarchy와 화면의 목적, 상태, 사용자 주 동작을 먼저 확인한다. 새 화면이 아니라면 디자인 변경 대상 밖의 탐색 흐름을 유지한다.
탭은 주요 목적지, navigation stack은 계층 이동, sheet는 독립 과업이라는 기존 구조를 확인한다. system back gesture와 취소 경로를 막지 않고 입력 중 dismissal의 데이터 보존을 확인한다.
safe area와 keyboard가 나타날 때 주요 동작과 입력 필드가 가려지지 않도록 한다. 화면 크기를 UIScreen 전체 크기로 고정하지 않고 실제 container에 반응한다.
기존 system control과 앱 토큰을 사용하고 버튼의 보이는 모양과 실제 hit area, icon-only label을 확인한다. hover/desktop 메뉴만으로 접근할 수 있는 필수 기능을 만들지 않는다.
Dynamic Type, VoiceOver 읽기 순서와 action, contrast, Reduce Motion, 긴 번역과 RTL 중 변경 영향이 있는 상태를 확인한다. 상태는 색만으로 전달하지 않는다.
라이트·다크, 작은 지원 iPhone과 큰 글자, 키보드 열린 상태, 빈/로딩/오류 상태를 실제 runtime에서 확인한다. 특정 OS 재료 효과 때문에 최소 OS를 바꾸지 않는다.
추가 디자인은 resolver의 `design-system`, `design-kit`, `layout-grid`, `app-icon`, 구현·검증은 `code`, `build-and-verify`, `test`로 연결한다.
완료: 변경 화면의 구조·문구·조작이 목적과 완료 기준을 충족하며 실제 iPhone 증거와 남은 항목이 있다.

## 다음 스킬과 인계

이 문서의 후속 역할은 실행 패키지 루트에서 `python3 scripts/resolve.py --entrypoint <호출 진입점> --platform <배정된 플랫폼> --step <역할>`로 확인한 정확한 이름·경로로 호출한다.
resolver가 반환한 path의 PROCEDURE.md를 읽는다. 내부 문서를 Skill 도구나 슬래시 명령으로 호출하지 않는다. 현재 단계로 재귀 호출하지 않으며 요청하지 않은 배포·설치·커밋을 추가하지 않는다.
변경 파일, source 상태·타깃·환경, 검사와 화면·로그 경로, 미검증·공유 변경 요청을 조율자에게 반환한다.

공식 참고: [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/), [SwiftUI](https://developer.apple.com/documentation/swiftui), [UIKit](https://developer.apple.com/documentation/uikit), [XCTest](https://developer.apple.com/documentation/xctest). 구현 API의 가용성·서명은 현재 SDK와 프로젝트 최소 OS에서 확인한다.
