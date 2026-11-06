---
name: baa-apple-performance
description: BAA Apple 모바일 성능 측정 전문 스킬. iOS/iPadOS 작업의 performance 단계를 배정받았을 때 현재 앱 구조와 실제 도구로 수행합니다.
---

# Apple 모바일 성능 측정

[BAA 실행 계약](../../../../../EXECUTION.md)을 먼저 따른다. 전달된 대상 플랫폼, 목적, 소유 파일과 완료 기준을 이어받는다.
이 스킬은 BAA 내부 실행용이며 플랫폼 선택이나 팀 생성을 다시 시작하지 않는다. 다른 작업자의 변경을 되돌리지 않는다.

## 수행

느린 시나리오, 기기·OS·build configuration·데이터와 측정 지표를 먼저 고정한다. 실제 증상이 없는 곳을 추측성 캐시·비동기 계층으로 변경하지 않는다.
Xcode Instruments의 Time Profiler, SwiftUI/animation·hitch, Allocations/Leaks와 현재 프로젝트의 signpost/metric 중 증상에 맞는 도구를 선택한다. 명령줄 자동화는 설치된 Instruments CLI 도움말로 확인한다.
UI thread에서 parsing/image decode/파일·DB 작업이 있는지 추적한다. SwiftUI 재계산과 identity, 불필요한 state publish, UIKit reuse·constraint 작업을 근거로 좁힌다.
이미지는 표시 크기에 맞는 decode/downsample, 목록은 기존 lazy/reuse, 비동기는 수명과 취소를 유지한다. 측정 없이 NSCache·Task.detached·새 저장 계층을 추가하지 않는다.
메모리 경고·foreground/background 전환과 작업 취소를 변경 영향에 맞춰 확인한다. 성능을 위해 데이터 보존·접근성·정확성을 줄이지 않는다.
iOS/iPadOS 각각 관련 실제 기기에서 같은 시나리오의 전후 수치를 비교한다. Simulator의 성능 수치를 실기기 성능으로 보고하지 않는다.
완료: 원인·수정·동일 조건의 전후 측정과 기능 회귀 확인이 있거나 측정 환경 한계가 명시된다.

## 다음 스킬과 인계

이 문서의 후속 역할은 실행 패키지 루트에서 `python3 scripts/resolve.py --entrypoint <호출 진입점> --platform <배정된 플랫폼> --step <역할>`로 확인한 정확한 이름·경로로 호출한다.
resolver가 반환한 path의 PROCEDURE.md를 읽는다. 내부 문서를 Skill 도구나 슬래시 명령으로 호출하지 않는다. 현재 단계로 재귀 호출하지 않으며 요청하지 않은 배포·설치·커밋을 추가하지 않는다.
변경 파일, source 상태·타깃·환경, 검사와 화면·로그 경로, 미검증·공유 변경 요청을 조율자에게 반환한다.

공식 참고: [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/), [SwiftUI](https://developer.apple.com/documentation/swiftui), [UIKit](https://developer.apple.com/documentation/uikit), [XCTest](https://developer.apple.com/documentation/xctest). 구현 API의 가용성·서명은 현재 SDK와 프로젝트 최소 OS에서 확인한다.
