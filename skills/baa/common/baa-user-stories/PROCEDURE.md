---
name: baa-user-stories
description: 공통 사용자 요구와 플랫폼별 완료 기준을 STORY 목록으로 정리합니다. BAA의 기능 목록·백로그·개발 순서 결정 단계에 사용합니다.
---

# User stories

[공통 실행 규칙](../../EXECUTION.md)을 먼저 읽는다. BAA가 전달한 선택 플랫폼, 작업 목적, 현재 단계, 파일 소유권과 완료 기준을 유지한다. 플랫폼을 다시 선택하거나 전체 기획을 반복하지 않는다.

후속 스킬은 실행 패키지 루트에서 `python3 scripts/resolve.py --entrypoint <호출 진입점> --platform <선택 플랫폼> --step <단계>`로 조회한다. 반환된 이름과 문서 경로를 사용하며 원본 BAMA·BAWA의 짧은 이름이나 외부 설치 경로를 추정하지 않는다. 반환된 path의 PROCEDURE.md를 읽어 수행한다. 내부 이름을 Skill 도구나 슬래시 명령으로 호출하지 않는다.

공유 문서의 최종 편집자는 BAA 조율자 한 명이다. 플랫폼 담당자는 공유 BRIEF/STORIES/GLOSSARY/연구·검토 문서를 동시에 수정하지 않고 변경 제안과 근거를 조율자에게 반환한다. 단독 실행에서는 현재 담당자가 그 역할을 맡는다.

화면 목록을 사용자의 행동과 확인 가능한 완료 기준으로 바꾼다. BAMA·BAWA의 story, 의존성, milestone, UX 블록과 검증 태그를 유지한다.

## Read and map

존재하는 BRIEF, 연구 기능 행렬, 화면 인덱스와 작업 문서를 읽는다. 조율자가 공통 STORY를 한 곳에서 관리하며 플랫폼별로 같은 기능을 중복 story로 복제하지 않는다. 기존 프로젝트의 작업 관리 형식이 있으면 거기에 같은 정보를 보완한다.

```markdown
### S-012 항목 완료
As the user, 나는 항목을 완료하고 실수했으면 취소할 수 있다.
Platforms: macos, windows, ios, ipados, android 중 이번 대상
Screens: 참고 화면 또는 확인할 실행 상태
Depends: S-004
Acceptance:
- [unit][shared] 완료 규칙과 취소 시 데이터가 보존된다.
- [snap][<platform>] 완료 상태가 지정 화면에서 보인다.
- [self/manual][<platform>] 해당 플랫폼 입력·탐색 방식으로 완료와 취소를 수행한다.
Status: todo
Platform status: <platform>: todo / doing / done / blocked / not-applicable
```

story 하나는 한 행동을 다룬다. 화면과 그 화면에만 있는 제어를 같은 story에서 완성한다. acceptance는 `[snap]`, `[unit]`, `[self]`, `[manual]` 중 확인 방법과 적용 플랫폼을 명시한다. 공유 코드 테스트를 각 플랫폼의 화면 통과로 해석하지 않는다. 키·메뉴·뒤로 가기·권한 흐름은 플랫폼별 기준을 적는다.

의존 story가 먼저 끝나도록 순서를 정하고, data/API 계약이 같아야 하는 부분과 허용할 플랫폼 차이를 구분한다. `todo`, `doing`, `done`, `dropped`의 원본 상태를 유지하며 필요한 환경 대기는 이유와 재개 조건을 함께 기록한다. 전체 story는 대상 플랫폼의 필수 조건이 충족됐을 때만 done이다. 플랫폼 담당자는 상태 변경을 제안하고 조율자가 최종 반영한다.

## Milestones

각 milestone은 실행해서 쓸 수 있는 흐름으로 끝난다. 원본의 Core loop → Organize → Time → Speed → System → Polish는 앱에 맞는 예시로 사용한다. 필요한 행동만 남기고 플랫폼별 OS 연동은 해당 story에 적는다. story 수가 많으면 범위와 의존성을 다시 살피되 고정 개수 때문에 요구사항을 임의 삭제하지 않는다.

seed data는 사용자가 실제로 만들 수 있는 값과 상태로 구성한다. 아직 없는 기능의 데이터를 주입해 구현된 것처럼 보여주지 않는다. 제외한 요구는 이유와 함께 Dropped 또는 Later로 남기고, 사용자 요청의 계정·공유·서비스를 관례적으로 제외하지 않는다.

## UX and handoff

새 화면·행동·문구가 있는 story는 `ux-design`을 조회해 `UX:` 블록과 공통 용어를 채운다. 이후 milestone은 구현 직전 `improve-loop`에서 부족한 UX를 보완한다. 디자인만 요청받은 기존 화면에는 해당 화면·상태의 기준만 정하고 전체 backlog를 만들지 않는다.

완료 기준: 이번 범위의 주요 행동, 포함 기능과 참고 화면이 story 또는 명시적 제외 사유에 연결되고, 필요한 UX·플랫폼별 검증 기준·의존성과 진행 상태가 일치한다.
