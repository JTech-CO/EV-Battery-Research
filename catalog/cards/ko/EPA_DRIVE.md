# EPA US06 and dynamometer speed schedules

[English](../en/EPA_DRIVE.md) | [카탈로그](../../resources.json)

**ID:** `EPA_DRIVE` · **우선순위:** P1 · **유형:** `prescribed_input_dataset`

## 확인한 범위
US06 0~600초 601점, 원시 단위 mph이며 SI 파생본을 따로 둔다.

## 권장 활용
차량 변수가 명시된 후속 부하 모델의 재현 가능한 속도 입력으로 사용한다.

실제 배터리 측정값이 아니라 규정된 속도 입력이다. 601행을 확보했지만 이를 바로 전류 곡선이나 전기차 주행거리로 바꾸지는 않았다.

## 금지할 일반화
속도를 전류나 전기차 주행가능거리로 직접 변환하지 않는다.

## 수집·권리 상태
상태: `semantic_capture_included`. 권리: `scientific_educational_use;commercial_not_cleared`. 원본 바이트 파일 다운로드: **미완료**. 내용 스냅샷은 별도 provenance를 확인하며 원본 바이트와 동일하다고 주장하지 않는다.

## 다음 수집 작업
과학 연구용 출처를 유지하고 상업 이용 조건은 별도 검토한다. 원본 바이트 대조는 대기 중이다.

## 출처
- [S17: EPA dynamometer schedules](https://www.epa.gov/vehicle-and-fuel-emissions-testing/dynamometer-drive-schedules)
- [S18: EPA US06 numeric schedule](https://www.epa.gov/system/files/other-files/2025-03/us06col.txt)
- [S19: EPA disclaimers and copyright status](https://www.epa.gov/web-policies-and-procedures/epa-disclaimers)

확인일: 2026-09-10. 우선순위는 공학적 판단이며 측정한 품질 점수가 아니다.
