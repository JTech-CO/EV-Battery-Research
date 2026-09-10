# 연구 요약과 핵심 판단

[English](../en/00_RESEARCH_SUMMARY.md) · [README](../../README-KR.md)

## 판단
향후 연구는 서로 다른 배터리 자료를 섞기보다 **내부적으로 일관된 하나의 기준 셀**에서 시작하는 것이 좋다. 첫 기준은 About:Energy의 NMC111/흑연 12.5 Ah 파우치 예제이며, LFP/흑연 2 Ah 원통형 예제는 별도 화학계와 모델 한계의 비교 대상으로 둔다. 어느 쪽도 최신 양산 전기차 팩을 검증한 자료는 아니다. 원본은 BPX 0.1이며, 특성화 결과·문헌 값·추정 열 물성이 섞여 있다고 명시한다. [S01]

최종적으로 검증해야 할 것은 전류·초기 상태·온도·냉각·사용 이력이 단자 전압, 물질 상태, 발열, 열화 관측량으로 연결되는 관계이다. 시각화가 정교하거나 DFN 해가 수치적으로 수렴했다는 사실만으로 물리적 정확성이 확보되지는 않는다.

## 데이터의 네 층
| 구분 | 필요한 정보 | 이번 패키지 상태 |
|---|---|---|
| 물성·구성 관계 | 형상, 전극 평형 전위, 확산, 반응 속도, 전해질 수송, 열 물성 | 기준 셀 두 종류 확보, 근거 수준은 혼합 |
| 실험 | 충방전·펄스·휴지·EIS·열량·열화·팽창 | NMC 내장 기준 곡선 확보, 나머지는 카탈로그 |
| 경계·제어 조건 | 냉각, 팩 토폴로지, 차량 부하, BMS 한계, 센서 | US06 속도 입력 확보, OEM 팩 정보는 미확보 |
| 증거·관리 | 개체 ID, 단위, 시험법, 불확실성, 권리, 버전, 보정·홀드아웃 구분 | 스키마·목록·출처·수집 기록 제공 |

## 실제 동봉 범위
원문 텍스트를 **전사·재직렬화한 JSON 두 개**, 그 안의 매개변수 104항목, NMC 내장 기준 곡선 114점, EPA 규정 속도 601점을 담았다. 공개 OCP 적합식에서 계산한 404점은 파생값이며 새로운 실측값이 아니다. 필요 데이터 목록 139행도 확보한 실측값 139개라는 뜻이 아니다.

자료 카드 23개에는 실험 컬렉션뿐 아니라 교환 규격과 소프트웨어 참고 자료가 포함된다. 따라서 “실험 데이터셋 23개 전체 다운로드”로 소개하면 안 된다. About:Energy 원본 Git blob 16개는 재수집 대상으로 고정했으나 원본 바이트 파일은 이번에 다운로드하지 못했다. 시뮬레이션·보정·학습·원본과의 JSON 동등성 검증·계정 변경·깃허브 게시도 수행하지 않았다.

## 우선순위
먼저 원본 BPX와 동봉 스냅샷을 대조하고 같은 셀의 검증 CSV 전체를 확보한다. 다음은 같은 셀의 독립적인 온도·열 측정이다. 그 뒤에 식별 가능한 열화 기작과 명시적인 모듈·팩 정보를 추가한다. 공개 자료로 검증 영역이 분명한 연구 모델을 구성할 수 있지만, 특정 제조사 전기차를 그대로 재현했다고 주장할 근거는 아직 없다.

## 근거 출처

- [S01: About:Energy BPX parameterisation repository](https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation)
- [S06: BPX official standard download and change notes](https://bpxstandard.com/bpx-standard/)
- [S10: LG HG2 dataset v3](https://data.mendeley.com/datasets/cp3473x7xv/3)
- [S17: EPA dynamometer schedules](https://www.epa.gov/vehicle-and-fuel-emissions-testing/dynamometer-drive-schedules)
- [S18: EPA US06 numeric schedule](https://www.epa.gov/system/files/other-files/2025-03/us06col.txt)

조사 기준일: 2026-09-10. 설계 선택은 제안이며 시뮬레이터의 실측 성능을 의미하지 않는다.
