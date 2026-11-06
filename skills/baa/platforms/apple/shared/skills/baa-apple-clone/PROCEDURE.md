---
name: baa-apple-clone
description: BAA 참고 앱 화면 조사 전문 스킬. iOS/iPadOS 작업의 clone 단계를 배정받았을 때 현재 앱 구조와 실제 도구로 수행합니다.
---

# 참고 앱 화면 조사

[BAA 실행 계약](../../../../../EXECUTION.md)을 먼저 따른다. 전달된 대상 플랫폼, 목적, 소유 파일과 완료 기준을 이어받는다.
이 스킬은 BAA 내부 실행용이며 플랫폼 선택이나 팀 생성을 다시 시작하지 않는다. 다른 작업자의 변경을 되돌리지 않는다.

## 수행

참고 앱의 이름, 조사할 화면과 사용자 흐름을 정한다. BAA가 지정한 iOS/iPadOS 기기·OS·앱 버전을 기록한다.
실행 가능한 Simulator/실기기와 해당 앱의 접근 가능 여부를 확인한다. 다른 앱의 private 데이터나 컨테이너를 읽지 않는다.
기존 UI 테스트 또는 사용 가능한 컴퓨터 조작 도구로 기본 화면, 편집, sheet/popover, 설정, 오류·빈 상태를 조사한다.
캡처는 대상 앱의 화면만 포함한다. Simulator에서는 `xcrun simctl io <udid> screenshot <파일>`을 사용할 수 있지만 터치·스크롤 조작은 별도 UI 도구가 필요하다. screenshot 명령이 조작을 대신한다고 하지 않는다.
iOS는 뒤로 가기·탭·키보드, iPadOS는 다중 열·좁은 창·포인터 등 실제 지원 조작을 함께 기록한다.
화면 인덱스에 이미지 경로, 기기·화면 크기·배율, 진입/종료 동작, 관찰된 상태와 미확인 상태를 남긴다.
공통 화면 인덱스를 다른 담당자와 동시에 쓰지 말고 배정된 플랫폼 절에 반환한다. 다음 단계는 resolver의 `user-stories`다.
완료: 요청한 흐름이 이미지와 관찰 기록에 연결되거나 접근 불가 항목의 이유가 명시되어 있다.

## 다음 스킬과 인계

이 문서의 후속 역할은 실행 패키지 루트에서 `python3 scripts/resolve.py --entrypoint <호출 진입점> --platform <배정된 플랫폼> --step <역할>`로 확인한 정확한 이름·경로로 호출한다.
resolver가 반환한 path의 PROCEDURE.md를 읽는다. 내부 문서를 Skill 도구나 슬래시 명령으로 호출하지 않는다. 현재 단계로 재귀 호출하지 않으며 요청하지 않은 배포·설치·커밋을 추가하지 않는다.
변경 파일, source 상태·타깃·환경, 검사와 화면·로그 경로, 미검증·공유 변경 요청을 조율자에게 반환한다.

공식 참고: [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/), [SwiftUI](https://developer.apple.com/documentation/swiftui), [UIKit](https://developer.apple.com/documentation/uikit), [XCTest](https://developer.apple.com/documentation/xctest). 구현 API의 가용성·서명은 현재 SDK와 프로젝트 최소 OS에서 확인한다.
