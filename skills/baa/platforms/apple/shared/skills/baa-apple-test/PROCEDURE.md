---
name: baa-apple-test
description: BAA Apple 모바일 테스트 전문 스킬. iOS/iPadOS 작업의 test 단계를 배정받았을 때 현재 앱 구조와 실제 도구로 수행합니다.
---

# Apple 모바일 테스트

[BAA 실행 계약](../../../../../EXECUTION.md)을 먼저 따른다. 전달된 대상 플랫폼, 목적, 소유 파일과 완료 기준을 이어받는다.
이 스킬은 BAA 내부 실행용이며 플랫폼 선택이나 팀 생성을 다시 시작하지 않는다. 다른 작업자의 변경을 되돌리지 않는다.

## 수행

명령 구성과 결과 수집은 [실행 검증 상세](../../verification.md)를 읽고 프로젝트에 맞게 적용한다.

요구사항과 변경 지점에서 logic/unit, integration, UI와 실제 하드웨어 검증이 필요한 경계를 정한다. 기존 Swift Testing/XCTest/XCUITest 타깃을 재사용하고 새 프레임워크를 관례적으로 추가하지 않는다.
unit 테스트는 순수 변환·저장·실패·취소 등 변경한 로직을 작은 데이터로 확인한다. 데이터 migration은 이전 store fixture로 열림과 보존을 확인하며 사용자 store를 쓰지 않는다.
XCUITest는 접근성 identifier·의미 있는 label로 대상 화면을 찾아 입력·탭·결과·재실행을 검증한다. 고정 sleep 대신 실제 상태를 기다리고 animation/permission 환경 문제를 기능 결함과 구분한다.
기존 dev configuration과 격리된 테스트 데이터/launch argument를 사용한다. runtime 앱에 test-only 경로를 추가할 때 production API나 무인 인증 우회를 만들지 않는다.
iOS는 취소·뒤로 가기·keyboard와 지원 화면 크기, iPadOS는 좁은/넓은 창·split navigation·입력 방식·scene 복원 중 영향받는 사례를 추가한다.
같은 destination에서 병렬 UI runner와 수동 조작을 동시에 수행하지 않는다. 카메라·마이크·background session·실기기 권한은 실제 기기가 필요한 범위를 보고한다.
검사 명령, xcresult/로그/이미지, 소스 상태와 결과를 반환하고 `build-and-verify`의 유효한 증거를 재사용한다.
완료: 변경한 실패 경계와 사용자 흐름이 적절한 레벨의 검사로 확인되고 환경 문제·미검증이 명시된다.

## 다음 스킬과 인계

이 문서의 후속 역할은 실행 패키지 루트에서 `python3 scripts/resolve.py --entrypoint <호출 진입점> --platform <배정된 플랫폼> --step <역할>`로 확인한 정확한 이름·경로로 호출한다.
resolver가 반환한 path의 PROCEDURE.md를 읽는다. 내부 문서를 Skill 도구나 슬래시 명령으로 호출하지 않는다. 현재 단계로 재귀 호출하지 않으며 요청하지 않은 배포·설치·커밋을 추가하지 않는다.
변경 파일, source 상태·타깃·환경, 검사와 화면·로그 경로, 미검증·공유 변경 요청을 조율자에게 반환한다.

공식 참고: [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/), [SwiftUI](https://developer.apple.com/documentation/swiftui), [UIKit](https://developer.apple.com/documentation/uikit), [XCTest](https://developer.apple.com/documentation/xctest). 구현 API의 가용성·서명은 현재 SDK와 프로젝트 최소 OS에서 확인한다.
