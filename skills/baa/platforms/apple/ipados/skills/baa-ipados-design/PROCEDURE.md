---
name: baa-ipados-design
description: BAA iPadOS 네이티브 디자인 전문 스킬. iPadOS 작업의 design 단계를 배정받았을 때 현재 앱 구조와 실제 도구로 수행합니다.
---

# iPadOS 네이티브 디자인

[BAA 실행 계약](../../../../../EXECUTION.md)을 먼저 따른다. 전달된 대상 플랫폼, 목적, 소유 파일과 완료 기준을 이어받는다.
이 스킬은 BAA 내부 실행용이며 플랫폼 선택이나 팀 생성을 다시 시작하지 않는다. 다른 작업자의 변경을 되돌리지 않는다.

## 수행

기존 iPad 지원 타깃·device family, scene와 탐색 구조를 읽고 iPhone 공유 코드와 iPad별 화면 경계를 확인한다. iPad를 단순히 확대된 iPhone 화면으로 만들지 않는다.
폭이 충분하면 기존 split/list-detail/sidebar 패턴을 사용하고 좁은 창으로 바뀔 때 같은 선택·편집 상태가 유지되도록 한다. trait/실제 container 폭을 사용하고 기기 모델로 열 수를 고정하지 않는다.
회전·창 크기 변경·멀티태스킹에서 column, toolbar, inspector와 주요 동작이 접근 가능한지 확인한다. 기존 지원 OS에서 사용할 수 있는 windowing/scene API를 선택하며 새 OS 기능을 강제하지 않는다.
popover는 실제 source/anchor에 연결하고 compact 환경에서 presentation 전환과 취소·입력 보존을 확인한다. iPhone 전용 full-screen 동작을 iPad에 일괄 적용하지 않는다.
터치와 Apple Pencil 기능은 실제 요구가 있을 때만 추가한다. 포인터·hardware keyboard focus/shortcut, drag/drop와 context menu는 기존 지원 동작을 보존하고 필수 기능은 터치만으로도 접근 가능하게 한다.
Dynamic Type·VoiceOver·contrast·Reduce Motion과 긴 문구를 확인한다. 다중 scene을 지원하면 scene별 선택·문서 상태와 복원을 구분하고 shared persistence를 새로 복제하지 않는다.
실제 iPad destination에서 narrow/wide 창, 회전, 관련 키보드·포인터와 sheet/popover를 확인한다. iPhone snapshot을 iPad 검증 근거로 사용하지 않는다.
추가 디자인은 `design-system`, `design-kit`, `layout-grid`, 구현·검증은 `code`, `build-and-verify`, `test`의 resolver로 연결한다.
완료: iPad의 실제 크기 변화와 입력 경로에서 상태·탐색·접근성이 보존된 증거가 있다.

## 다음 스킬과 인계

이 문서의 후속 역할은 실행 패키지 루트에서 `python3 scripts/resolve.py --entrypoint <호출 진입점> --platform <배정된 플랫폼> --step <역할>`로 확인한 정확한 이름·경로로 호출한다.
resolver가 반환한 path의 PROCEDURE.md를 읽는다. 내부 문서를 Skill 도구나 슬래시 명령으로 호출하지 않는다. 현재 단계로 재귀 호출하지 않으며 요청하지 않은 배포·설치·커밋을 추가하지 않는다.
변경 파일, source 상태·타깃·환경, 검사와 화면·로그 경로, 미검증·공유 변경 요청을 조율자에게 반환한다.

공식 참고: [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/), [SwiftUI](https://developer.apple.com/documentation/swiftui), [UIKit](https://developer.apple.com/documentation/uikit), [XCTest](https://developer.apple.com/documentation/xctest). 구현 API의 가용성·서명은 현재 SDK와 프로젝트 최소 OS에서 확인한다.
