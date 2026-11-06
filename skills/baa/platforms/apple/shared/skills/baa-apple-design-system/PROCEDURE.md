---
name: baa-apple-design-system
description: BAA Apple 디자인 토큰 전문 스킬. iOS/iPadOS 작업의 design-system 단계를 배정받았을 때 현재 앱 구조와 실제 도구로 수행합니다.
---

# Apple 디자인 토큰

[BAA 실행 계약](../../../../../EXECUTION.md)을 먼저 따른다. 전달된 대상 플랫폼, 목적, 소유 파일과 완료 기준을 이어받는다.
이 스킬은 BAA 내부 실행용이며 플랫폼 선택이나 팀 생성을 다시 시작하지 않는다. 다른 작업자의 변경을 되돌리지 않는다.

## 수행

기존 색상 자산, 폰트, 간격/모서리/모션 정의, ButtonStyle과 UIKit appearance를 조사한다. 화면 수정만을 위해 새 Theme 계층이나 사용자 accent picker를 만들지 않는다.
중복된 값 중 실제로 같은 의미인 것만 기존 공통 정의로 모은다. 브랜드·상태 색 의미는 여러 플랫폼에서 공유하되 iOS/iPadOS의 타입·컨트롤 치수를 macOS 값과 같게 만들지 않는다.
semantic Color/UIColor와 기존 asset의 light/dark 설정을 사용하고 텍스트 대비·Increase Contrast·색 구분 없이도 상태를 알 수 있는 표현을 확인한다. 하드코딩한 흰색 글자가 모든 accent 위에서 읽힌다고 가정하지 않는다.
시스템 text style과 Dynamic Type를 우선한다. custom font가 이미 있으면 scaled sizing과 Bold Text를 확인하고 기존 앱의 글자 체계를 유지한다.
아이콘은 기존 자산·SF Symbols 가용성·언어 방향을 확인한다. animation은 existing duration과 Reduce Motion을 따르며 특정 iOS 효과 때문에 최소 OS를 올리지 않는다.
기존 문서 한 곳에 바뀐 토큰의 사용처와 예외를 갱신하고 대상 화면부터 치환한다. iPad에 공통 토큰을 사용하되 화면 밀도와 컨테이너 폭 차이는 레이아웃으로 처리한다.
resolver의 `build-and-verify`로 대상 iOS/iPadOS 화면을 라이트·다크와 변경한 글자 크기에서 확인한다.
완료: 실제 사용처가 기존 토큰을 사용하고 테마·접근성 상태의 확인 근거가 있다.

## 다음 스킬과 인계

이 문서의 후속 역할은 실행 패키지 루트에서 `python3 scripts/resolve.py --entrypoint <호출 진입점> --platform <배정된 플랫폼> --step <역할>`로 확인한 정확한 이름·경로로 호출한다.
resolver가 반환한 path의 PROCEDURE.md를 읽는다. 내부 문서를 Skill 도구나 슬래시 명령으로 호출하지 않는다. 현재 단계로 재귀 호출하지 않으며 요청하지 않은 배포·설치·커밋을 추가하지 않는다.
변경 파일, source 상태·타깃·환경, 검사와 화면·로그 경로, 미검증·공유 변경 요청을 조율자에게 반환한다.

공식 참고: [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/), [SwiftUI](https://developer.apple.com/documentation/swiftui), [UIKit](https://developer.apple.com/documentation/uikit), [XCTest](https://developer.apple.com/documentation/xctest). 구현 API의 가용성·서명은 현재 SDK와 프로젝트 최소 OS에서 확인한다.
