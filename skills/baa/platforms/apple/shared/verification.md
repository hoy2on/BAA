# iOS·iPadOS 실행 검증

`scaffold`, `build-and-verify`, `test`에서 실행 명령을 구성할 때 읽는다. macOS에는 macOS 전용 빌드 절차를 사용한다.
기존 프로젝트 스크립트가 우선이다. 아래 값은 프로젝트와 도구에서 확인해 채우며 예시 scheme/configuration/기기를 임의로 실행하지 않는다.

## 프로젝트와 실행 대상 확인

```sh
xcodebuild -version
xcodebuild -list -json -workspace "$BAA_WORKSPACE"
xcodebuild -showdestinations -workspace "$BAA_WORKSPACE" -scheme "$BAA_SCHEME"
xcrun simctl list devices available
```

workspace가 없으면 실제 `.xcodeproj`와 `-project`를 사용한다. Xcode 도구가 제공되면 그 도구의 같은 조회 기능을 사용할 수 있다.
선택 scheme의 지원 플랫폼·`TARGETED_DEVICE_FAMILY`·`PRODUCT_BUNDLE_IDENTIFIER`·서명·dev configuration을 build settings에서 확인한다.
iPhone destination은 iOS, iPad destination은 iPadOS의 증거다. universal 타깃이라는 이유로 양쪽 실행을 한 번으로 대체하지 않는다.

## 빌드와 설치는 별도 단계

```sh
xcodebuild -workspace "$BAA_WORKSPACE" -scheme "$BAA_SCHEME" \
  -configuration "$BAA_DEV_CONFIGURATION" -destination "id=$BAA_DEVICE_UDID" build
```

결과 `.app`의 Info.plist 식별자와 서명·entitlement를 확인한다. 빌드 성공은 실행 성공이 아니다.
고정 dev 식별자가 확인된 Simulator 설치만 다음과 같이 수행한다. 실기기는 설치된 Xcode/devicectl 도움말과 프로젝트의 기존 흐름을 따른다.

```sh
xcrun simctl install "$BAA_DEVICE_UDID" "$BAA_DEV_APP"
xcrun simctl launch "$BAA_DEVICE_UDID" "$BAA_DEV_BUNDLE_ID"
xcrun simctl io "$BAA_DEVICE_UDID" screenshot "$BAA_SCREENSHOT"
```

Simulator를 초기화하거나 release를 제거해 설치 실패를 해결하지 않는다. 캡처는 변경 상태와 실제 전경 앱을 확인한 뒤 수행한다.
simctl screenshot은 캡처 기능이며 탭·스크롤 검증 도구가 아니다. XCUITest 또는 사용 가능한 UI 도구로 실제 조작한다.

## 테스트와 증거

```sh
xcodebuild -workspace "$BAA_WORKSPACE" -scheme "$BAA_SCHEME" \
  -configuration "$BAA_DEV_CONFIGURATION" -destination "id=$BAA_DEVICE_UDID" \
  -resultBundlePath "$BAA_NEW_RESULT_BUNDLE" test
```

실제 테스트 타깃/plan과 영향 범위를 확인하고 필요한 경우 `-only-testing`으로 줄인다. result bundle은 기존 결과를 덮어쓰지 않는 새 경로를 사용한다.
로그를 파이프로 저장할 때 빌드·테스트의 종료 코드가 보존되게 현재 shell의 `pipefail` 또는 프로젝트 도구를 사용한다.
실패 시 첫 실패 원인·실행 여부·선택 destination·xcresult를 기록한다. 테스트 0개, unavailable destination, 권한 차단을 통과로 처리하지 않는다.

정상 흐름 외에 이번 변경과 관련된 취소·뒤로 가기·키보드·상태 복원·긴 번역·큰 글자·라이트/다크를 선택한다.
iPadOS는 좁은/넓은 창과 다중 열 전환·회전·키보드/포인터를, iOS는 터치·safe area·탐색 복귀를 실제 흐름에서 확인한다.
선택 대상, source 상태, scheme/configuration, 기기/OS, 명령·종료 코드, xcresult/로그·화면, 남은 실기기 항목을 반환한다.

공식 참고: [Xcode 테스트](https://developer.apple.com/documentation/xcode/running-tests-and-interpreting-results).
명령 지원 여부는 설치된 `xcodebuild -help`, `xcrun simctl help`, `xcrun devicectl help`에서 확인한다.
