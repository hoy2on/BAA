# Android 실행 검증

`scaffold`, `build-and-verify`, `test`에서 실행 명령을 구성할 때 읽는다. 프로젝트의 wrapper·기존 스크립트를 우선한다.
모듈명·dev flavor/build type·serial은 실제 구성에서 확인한다. `app`, `debug`, 현재 연결된 첫 기기를 자동 선택하지 않는다.

## 실제 task와 기기 확인

```sh
./gradlew projects
./gradlew tasks --all
adb devices -l
```

Windows 호스트에서는 저장소의 실제 `gradlew.bat`를 사용한다. 조회한 모듈과 변형에서 assemble/test/lint task를 선택한다.
예를 들어 `:app:assembleDevDebug`는 그 task가 실제로 있고 dev ID가 분리된 경우에만 쓴다.
SDK·AGP·Kotlin 호환 오류는 wrapper·catalog·설치 도구를 확인하고, 실행 편의를 위해 전체 버전을 올리지 않는다.

## 빌드·검사와 설치 구분

```sh
./gradlew "$BAA_ASSEMBLE_TASK" "$BAA_UNIT_TEST_TASK" "$BAA_LINT_TASK"
```

task와 APK 결과 경로, APK의 실제 applicationId·서명·변형을 확인한다.
`apkanalyzer manifest application-id`나 저장소의 기존 APK 검사 도구를 사용하고 Gradle 문자열만으로 설치 대상을 추정하지 않는다.
release와 다른 고정 dev ID임을 확인한 뒤에만 선택 기기에 설치한다. split APK는 기존 split 설치 흐름을 사용한다.

```sh
adb -s "$BAA_SERIAL" install -r "$BAA_DEV_APK"
adb -s "$BAA_SERIAL" shell am start -W -n "$BAA_DEV_COMPONENT"
adb -s "$BAA_SERIAL" exec-out screencap -p > "$BAA_SCREENSHOT"
```

`BAA_DEV_COMPONENT`는 dev APK의 실제 launcher다. 서명 충돌이 발생해도 release uninstall·`pm clear`·데이터 삭제로 해결하지 않는다.
실제 전경 앱과 화면에 개인정보가 없는지 확인하고 캡처한다. 캡처 명령만으로 입력·뒤로 가기·저장 성공을 선언하지 않는다.

## 기기 테스트와 증거

```sh
ANDROID_SERIAL="$BAA_SERIAL" ./gradlew "$BAA_CONNECTED_TEST_TASK"
```

설치 AGP와 기존 runner가 해당 serial 제한을 따르는지 로그에서 확인한다. 다중 기기 실행이나 Gradle Managed Devices는 현재 프로젝트 방식과 선택 대상을 명시한다.
unit XML/HTML, instrumentation 결과, lint 보고서 경로는 해당 모듈의 실제 출력에서 찾는다. `UP-TO-DATE`·`NO-SOURCE`나 테스트 0개를 새 런타임 검증으로 보고하지 않는다.
실패 시 Gradle의 첫 실패 task·exception과 선택 기기의 관련 crash/logcat을 보존한다. 다른 앱 로그를 일괄 수집하거나 전체 log buffer를 지우지 않는다.

변경 흐름에 맞춰 system back·IME·Activity 재생성·회전·상태 복원·font scale·라이트/다크를 선택한다.
large-screen/foldable 지원은 현재 창 크기·pane 전환을 확인하고, 에뮬레이터 결과와 실제 센서·성능·기기 권한 검증을 구분한다.
source 상태, 모듈/variant, dev package, serial/OS, 명령·종료 코드, 테스트/로그·화면과 남은 기기 검증을 반환한다.

공식 참고: [명령줄 빌드](https://developer.android.com/build/building-cmdline), [명령줄 테스트](https://developer.android.com/studio/test/command-line), [adb](https://developer.android.com/tools/adb).
