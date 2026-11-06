---
name: baa-apple-design-kit
description: BAA Apple 커스텀 컴포넌트 전문 스킬. iOS/iPadOS 작업의 design-kit 단계를 배정받았을 때 현재 앱 구조와 실제 도구로 수행합니다.
---

# Apple 커스텀 컴포넌트

[BAA 실행 계약](../../../../../EXECUTION.md)을 먼저 따른다. 전달된 대상 플랫폼, 목적, 소유 파일과 완료 기준을 이어받는다.
이 스킬은 BAA 내부 실행용이며 플랫폼 선택이나 팀 생성을 다시 시작하지 않는다. 다른 작업자의 변경을 되돌리지 않는다.

## 수행

커스텀 부품을 만들기 전에 기존 Button/List/Form/Menu/Picker와 앱 컴포넌트가 요구를 충족하는지 확인한다. 새 시각적 부품이 필요한 범위만 구현한다.
부품별 입력 값, 소유 상태, 이벤트와 normal/pressed/selected/disabled/focused/loading/error 상태를 정한다. 비즈니스 모델을 작은 부품 안에 새로 소유시키지 않는다.
SwiftUI는 기존 ButtonStyle/ToggleStyle·View, UIKit은 기존 control/subclass 패턴을 사용한다. 버튼을 도형+tap gesture로 바꾸어 기본 키보드·접근성 동작을 잃지 않는다.
색상·간격·서체는 `design-system`의 기존 토큰을 사용한다. 탭/포인터/키보드 조작 중 현재 플랫폼이 지원하는 경로와 VoiceOver label/value/action을 제공한다.
iOS에서는 터치와 Dynamic Type, iPadOS에서는 포인터와 keyboard focus, 창 폭 변화에서도 부품이 동작하도록 확인한다. iPad에서 hover에만 중요한 기능을 숨기지 않는다.
기존 preview/gallery/test host가 있으면 모든 관련 상태를 그곳에 추가한다. 부품 하나 때문에 별도 앱·거대한 gallery를 만들지 않는다.
실제 대상 화면에 연결하고 `build-and-verify`와 `test`로 화면·동작을 확인한다.
완료: 요청한 부품과 상태가 실제 화면에 연결되고 기본 조작과 접근성이 보존되어 있다.

## 다음 스킬과 인계

이 문서의 후속 역할은 실행 패키지 루트에서 `python3 scripts/resolve.py --entrypoint <호출 진입점> --platform <배정된 플랫폼> --step <역할>`로 확인한 정확한 이름·경로로 호출한다.
resolver가 반환한 path의 PROCEDURE.md를 읽는다. 내부 문서를 Skill 도구나 슬래시 명령으로 호출하지 않는다. 현재 단계로 재귀 호출하지 않으며 요청하지 않은 배포·설치·커밋을 추가하지 않는다.
변경 파일, source 상태·타깃·환경, 검사와 화면·로그 경로, 미검증·공유 변경 요청을 조율자에게 반환한다.

공식 참고: [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/), [SwiftUI](https://developer.apple.com/documentation/swiftui), [UIKit](https://developer.apple.com/documentation/uikit), [XCTest](https://developer.apple.com/documentation/xctest). 구현 API의 가용성·서명은 현재 SDK와 프로젝트 최소 OS에서 확인한다.
