---
name: baa-apple-scaffold
description: BAA Apple 앱 초기 프로젝트 전문 스킬. iOS/iPadOS 작업의 scaffold 단계를 배정받았을 때 현재 앱 구조와 실제 도구로 수행합니다.
---

# Apple 앱 초기 프로젝트

[BAA 실행 계약](../../../../../EXECUTION.md)을 먼저 따른다. 전달된 대상 플랫폼, 목적, 소유 파일과 완료 기준을 이어받는다.
이 스킬은 BAA 내부 실행용이며 플랫폼 선택이나 팀 생성을 다시 시작하지 않는다. 다른 작업자의 변경을 되돌리지 않는다.

## 수행

명령 구성과 결과 수집은 [실행 검증 상세](../../verification.md)를 읽고 프로젝트에 맞게 적용한다.

기존 `.xcodeproj`/`.xcworkspace`, project generator, Swift package와 타깃을 조사한다. 기존 프로젝트가 있으면 새 앱 뼈대를 만들지 않는다.
신규 앱의 제품명, iOS/iPadOS 선택, 지원 OS, SwiftUI/UIKit 선택을 요구와 실제 도구로 확정한다. 설치된 Xcode의 템플릿이나 저장소의 기존 생성 도구를 우선한다. Swift Package 하나를 iOS 실행 앱으로 간주하지 않는다.
확정된 Xcode 앱 타깃, 필요한 테스트 타깃, 최소 한 화면과 저장/재실행 가능한 핵심 상태만 만든다. iPhone 전용이면 iPad 타깃을 추가하지 않고, Universal이면 동일 앱 타깃의 device family를 확인한다.
Debug/dev configuration과 release와 공존하는 bundle ID, 표시 이름, 서명·provisioning을 구성한다. App Group·Keychain group을 production과 자동 공유하거나 데이터를 이관하지 않는다.
새 패키지/코드 생성기를 추가하기 전에 기존 의존성과 Xcode 기능으로 가능한지 확인한다. project 생성 도구·스키마는 설치 버전의 문서로 확인한다.
실제 scheme과 destination으로 최소 앱을 build한 뒤 dev 타깃에서 첫 화면을 확인한다. 이후 resolver의 `native-design`, `design-system`, `app-icon` 또는 현재 story의 `code`로 이어간다.
완료: 생성된 타깃과 dev 식별자가 확인되고 최소 앱의 빌드·실행 결과가 기록되거나 환경 제약이 보고되어 있다.

## 다음 스킬과 인계

이 문서의 후속 역할은 실행 패키지 루트에서 `python3 scripts/resolve.py --entrypoint <호출 진입점> --platform <배정된 플랫폼> --step <역할>`로 확인한 정확한 이름·경로로 호출한다.
resolver가 반환한 path의 PROCEDURE.md를 읽는다. 내부 문서를 Skill 도구나 슬래시 명령으로 호출하지 않는다. 현재 단계로 재귀 호출하지 않으며 요청하지 않은 배포·설치·커밋을 추가하지 않는다.
변경 파일, source 상태·타깃·환경, 검사와 화면·로그 경로, 미검증·공유 변경 요청을 조율자에게 반환한다.

공식 참고: [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/), [SwiftUI](https://developer.apple.com/documentation/swiftui), [UIKit](https://developer.apple.com/documentation/uikit), [XCTest](https://developer.apple.com/documentation/xctest). 구현 API의 가용성·서명은 현재 SDK와 프로젝트 최소 OS에서 확인한다.
