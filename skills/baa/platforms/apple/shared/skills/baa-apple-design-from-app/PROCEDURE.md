---
name: baa-apple-design-from-app
description: BAA Apple 참고 디자인 재현 전문 스킬. iOS/iPadOS 작업의 design-from-app 단계를 배정받았을 때 현재 앱 구조와 실제 도구로 수행합니다.
---

# Apple 참고 디자인 재현

[BAA 실행 계약](../../../../../EXECUTION.md)을 먼저 따른다. 전달된 대상 플랫폼, 목적, 소유 파일과 완료 기준을 이어받는다.
이 스킬은 BAA 내부 실행용이며 플랫폼 선택이나 팀 생성을 다시 시작하지 않는다. 다른 작업자의 변경을 되돌리지 않는다.

## 수행

참고 이미지의 기기, 해상도, 픽셀 배율, OS, 텍스트·테마·상태를 확인한다. 창 screenshot을 iPhone/iPad 디자인으로 단순 확대·축소하지 않는다.
`clone`에서 대상 흐름을 확인하고 현재 화면과 참고 화면의 정보 순서·탐색·공통 부품을 대응시킨다. 브랜드, 로고, 소유 자산은 구현 요구와 사용 권한을 별도로 확인한다.
측정은 실제 image metadata와 기기 배율을 사용한다. 자동으로 pixels/2를 적용하지 않고 point 좌표와 pixel 좌표를 구분한다.
`native-design` 기준에 맞춰 시스템 부품으로 표현 가능한 의도를 먼저 구현하고, 커스텀 부품이 필요하면 `design-kit`으로 연결한다. existing tokens를 통해 간격·폰트·색을 조정한다.
같은 데이터·viewport·배율·테마의 실행 화면을 얻어 구조, 글자, 여백, 색상 순으로 비교한다. 다른 OS의 렌더링이나 상태까지 픽셀 불일치로 오판하지 않는다.
비교 도구가 사용 가능하면 차이 이미지를 보조 자료로 쓰고 가시적 차이와 동작을 직접 확인한다. 해결되지 않은 차이를 기록하고 같은 입력 없는 재시도를 반복하지 않는다.
완료: 재현 범위, 변경한 토큰/부품, 동일 조건의 전후 화면과 남은 차이가 기록되어 있다.

## 다음 스킬과 인계

이 문서의 후속 역할은 실행 패키지 루트에서 `python3 scripts/resolve.py --entrypoint <호출 진입점> --platform <배정된 플랫폼> --step <역할>`로 확인한 정확한 이름·경로로 호출한다.
resolver가 반환한 path의 PROCEDURE.md를 읽는다. 내부 문서를 Skill 도구나 슬래시 명령으로 호출하지 않는다. 현재 단계로 재귀 호출하지 않으며 요청하지 않은 배포·설치·커밋을 추가하지 않는다.
변경 파일, source 상태·타깃·환경, 검사와 화면·로그 경로, 미검증·공유 변경 요청을 조율자에게 반환한다.

공식 참고: [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/), [SwiftUI](https://developer.apple.com/documentation/swiftui), [UIKit](https://developer.apple.com/documentation/uikit), [XCTest](https://developer.apple.com/documentation/xctest). 구현 API의 가용성·서명은 현재 SDK와 프로젝트 최소 OS에서 확인한다.
