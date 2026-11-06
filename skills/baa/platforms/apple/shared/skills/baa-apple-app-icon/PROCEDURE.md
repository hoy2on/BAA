---
name: baa-apple-app-icon
description: BAA iOS·iPadOS 앱 아이콘 전문 스킬. iOS/iPadOS 작업의 app-icon 단계를 배정받았을 때 현재 앱 구조와 실제 도구로 수행합니다.
---

# iOS·iPadOS 앱 아이콘

[BAA 실행 계약](../../../../../EXECUTION.md)을 먼저 따른다. 전달된 대상 플랫폼, 목적, 소유 파일과 완료 기준을 이어받는다.
이 스킬은 BAA 내부 실행용이며 플랫폼 선택이나 팀 생성을 다시 시작하지 않는다. 다른 작업자의 변경을 되돌리지 않는다.

## 수행

기존 asset catalog, AppIcon set/설정, Info.plist, 빌드 타깃과 지원 OS를 확인한다. 현재 Xcode가 지원하는 실제 아이콘 형식을 사용한다.
아이콘의 제품 의미와 기존 브랜드를 유지하고 요청한 변경 범위만 만든다. 기존 raster/vector 원본과 generation script를 재사용하고 라이선스를 확인한다.
현재 icon 형식에서 요구하는 크기·appearance와 투명도 제약을 공식 문서와 Xcode 검증으로 확인한다. macOS .icns나 Windows .ico를 모바일 자산으로 등록하지 않는다.
Icon Composer가 현재 프로젝트와 OS에서 사용되는 경우에만 그 흐름을 사용한다. 구형 catalog를 요청 없이 변환하지 않는다.
iOS와 iPadOS dev 타깃에 아이콘을 연결하고 build 경고를 확인한다. 실제 대상 launcher/설정 등 필요한 표시 위치에서 light/dark/tinted 등 지원 상태를 확인한다.
아이콘 교체를 위해 release 앱을 제거하지 않는다. 캡처와 생성한 자산의 경로를 반환한다.
완료: 올바른 dev 타깃에 연결되어 검증된 자산과 확인하지 못한 appearance가 구분되어 있다.

## 다음 스킬과 인계

이 문서의 후속 역할은 실행 패키지 루트에서 `python3 scripts/resolve.py --entrypoint <호출 진입점> --platform <배정된 플랫폼> --step <역할>`로 확인한 정확한 이름·경로로 호출한다.
resolver가 반환한 path의 PROCEDURE.md를 읽는다. 내부 문서를 Skill 도구나 슬래시 명령으로 호출하지 않는다. 현재 단계로 재귀 호출하지 않으며 요청하지 않은 배포·설치·커밋을 추가하지 않는다.
변경 파일, source 상태·타깃·환경, 검사와 화면·로그 경로, 미검증·공유 변경 요청을 조율자에게 반환한다.

공식 참고: [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/), [SwiftUI](https://developer.apple.com/documentation/swiftui), [UIKit](https://developer.apple.com/documentation/uikit), [XCTest](https://developer.apple.com/documentation/xctest). 구현 API의 가용성·서명은 현재 SDK와 프로젝트 최소 OS에서 확인한다.
