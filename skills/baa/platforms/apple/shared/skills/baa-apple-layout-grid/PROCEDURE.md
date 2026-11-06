---
name: baa-apple-layout-grid
description: BAA Apple 간격·정렬 검증 전문 스킬. iOS/iPadOS 작업의 layout-grid 단계를 배정받았을 때 현재 앱 구조와 실제 도구로 수행합니다.
---

# Apple 간격·정렬 검증

[BAA 실행 계약](../../../../../EXECUTION.md)을 먼저 따른다. 전달된 대상 플랫폼, 목적, 소유 파일과 완료 기준을 이어받는다.
이 스킬은 BAA 내부 실행용이며 플랫폼 선택이나 팀 생성을 다시 시작하지 않는다. 다른 작업자의 변경을 되돌리지 않는다.

## 수행

해당 뷰의 safe area, container, existing spacing, text style과 실제 화면 크기를 읽는다. macOS 4pt 규칙이나 고정 창 여백을 모바일에 강제하지 않는다.
기준선·leading/trailing·관련 항목 사이 간격·그룹 간격을 기존 토큰에 맞춘다. SwiftUI layout priority/alignment와 UIKit constraint 충돌을 먼저 확인하고 숫자 보정으로 덮지 않는다.
텍스트와 control은 가능한 intrinsic size·system sizing을 유지한다. Dynamic Type·긴 번역에서 줄바꿈/잘림·tap 영역이 적절한지 확인한다.
iOS는 키보드·하단 홈 표시부·화면 회전의 공간 변화, iPadOS는 narrow/wide 창·split navigation·popover anchor와 다중 열 경계를 확인한다.
기존 snapshot/layout probe가 있으면 사용한다. 없으면 해당 화면의 실행 캡처와 view hierarchy/constraint 로그로 문제를 좁히며 전역 grid 검사 도구를 관례적으로 새로 만들지 않는다.
변경한 alignment와 spacing을 토큰 사용처에서 고치고 인접 화면에 영향이 있는지 확인한다.
완료: 요청한 정렬 문제의 전후 화면과 관련 크기·텍스트 상태의 확인 결과가 있다.

## 다음 스킬과 인계

이 문서의 후속 역할은 실행 패키지 루트에서 `python3 scripts/resolve.py --entrypoint <호출 진입점> --platform <배정된 플랫폼> --step <역할>`로 확인한 정확한 이름·경로로 호출한다.
resolver가 반환한 path의 PROCEDURE.md를 읽는다. 내부 문서를 Skill 도구나 슬래시 명령으로 호출하지 않는다. 현재 단계로 재귀 호출하지 않으며 요청하지 않은 배포·설치·커밋을 추가하지 않는다.
변경 파일, source 상태·타깃·환경, 검사와 화면·로그 경로, 미검증·공유 변경 요청을 조율자에게 반환한다.

공식 참고: [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/), [SwiftUI](https://developer.apple.com/documentation/swiftui), [UIKit](https://developer.apple.com/documentation/uikit), [XCTest](https://developer.apple.com/documentation/xctest). 구현 API의 가용성·서명은 현재 SDK와 프로젝트 최소 OS에서 확인한다.
