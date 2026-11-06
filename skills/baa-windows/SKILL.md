---
name: baa-windows
description: BAA Windows 전용 진입점. 사용자가 /baa-windows로 앱 작업을 요청하면 Windows 범위에서 필요한 전문 절차를 연결합니다.
---

# BAA Windows

호출 진입점을 `baa-windows`로, 허용 대상을 Windows로 고정한다.
[중앙 BAA 절차](../baa/SKILL.md)를 읽고 같은 플랫폼 판정·단계 연결·배정·검증 절차를 수행한다.
중앙 문서를 읽어도 호출 진입점과 허용 범위를 `baa` 전체로 초기화하지 않는다.
본문이 허용 범위 밖 플랫폼을 요구하면 수정 전에 충돌을 확인하고 다른 플랫폼으로 자동 전환하지 않는다.
플랫폼 역할 조회에는 `--entrypoint baa-windows`를 전달한다. 공통 절차와 공유 파일 변경도 선택 대상에 필요한 범위로 제한한다.
