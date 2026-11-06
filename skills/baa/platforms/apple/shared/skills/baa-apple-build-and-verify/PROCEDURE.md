---
name: baa-apple-build-and-verify
description: BAA Apple 모바일 빌드·실행 검증 전문 스킬. iOS/iPadOS 작업의 build-and-verify 단계를 배정받았을 때 현재 앱 구조와 실제 도구로 수행합니다.
---

# Apple 모바일 빌드·실행 검증

[BAA 실행 계약](../../../../../EXECUTION.md)을 먼저 따른다. 전달된 대상 플랫폼, 목적, 소유 파일과 완료 기준을 이어받는다.
이 스킬은 BAA 내부 실행용이며 플랫폼 선택이나 팀 생성을 다시 시작하지 않는다. 다른 작업자의 변경을 되돌리지 않는다.

## 수행

명령 구성과 결과 수집은 [실행 검증 상세](../../verification.md)를 읽고 프로젝트에 맞게 적용한다.

프로젝트 지침과 `xcodebuild -list` 또는 Xcode 도구로 실제 workspace/project, scheme, dev configuration, 지원 destination을 확인한다.
`xcodebuild -showdestinations -scheme <확인한 scheme>` 등으로 대상 기기를 확인한다. iOS는 iPhone, iPadOS는 iPad destination을 지정하며 임의 scheme 이름을 만들지 않는다.
기존 build/test 스크립트가 있으면 재사용한다. 명령을 직접 구성할 때 `-workspace` 또는 `-project`, `-scheme`, dev configuration과 구체 destination을 지정하고 오류 원문·결과 bundle 경로를 보존한다.
설치 전에 만들어진 .app의 bundle ID, signing·entitlement와 dev 설정을 확인한다. Simulator는 확인한 UDID에 `simctl install/launch`, 실기기는 사용 가능한 Xcode/devicectl 흐름을 설치 버전 도움말로 확인한다. release를 제거하지 않는다.
실행 화면에서 변경한 흐름과 인접 경로를 조작한다. screenshot만으로 버튼·undo·저장 동작 성공을 선언하지 않는다. 필요에 따라 XCUITest 또는 기존 UI flow를 실행한다.
iOS는 keyboard/safe area/뒤로 가기, iPadOS는 iPad destination에서 창 폭·multi-column·회전·포인터/키보드 영향을 확인한다. 양쪽 요청이면 한 기기 결과를 양쪽 통과로 쓰지 않는다.
동일 simulator/기기와 shared DerivedData 출력·dev 설치본을 다른 담당자가 사용 중이면 해당 실행만 순차 조율한다.
완료: 소스 상태·타깃·기기·build/test 결과·화면 경로가 연결되고 미검증 항목이 남아 있다면 분리 보고된다.

## 다음 스킬과 인계

이 문서의 후속 역할은 실행 패키지 루트에서 `python3 scripts/resolve.py --entrypoint <호출 진입점> --platform <배정된 플랫폼> --step <역할>`로 확인한 정확한 이름·경로로 호출한다.
resolver가 반환한 path의 PROCEDURE.md를 읽는다. 내부 문서를 Skill 도구나 슬래시 명령으로 호출하지 않는다. 현재 단계로 재귀 호출하지 않으며 요청하지 않은 배포·설치·커밋을 추가하지 않는다.
변경 파일, source 상태·타깃·환경, 검사와 화면·로그 경로, 미검증·공유 변경 요청을 조율자에게 반환한다.

공식 참고: [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/), [SwiftUI](https://developer.apple.com/documentation/swiftui), [UIKit](https://developer.apple.com/documentation/uikit), [XCTest](https://developer.apple.com/documentation/xctest). 구현 API의 가용성·서명은 현재 SDK와 프로젝트 최소 OS에서 확인한다.
