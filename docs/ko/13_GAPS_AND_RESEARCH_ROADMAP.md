# 공백 분석과 후속 연구 관문

[English](../en/13_GAPS_AND_RESEARCH_ROADMAP.md) · [README](../../README-KR.md)

## 현실성을 크게 제한하는 미확보 증거
현재 기준에는 같은 셀의 독립적인 열 검증, 넓은 온도 구간의 특성화, 기작별 열화 계수, 시편·배치 추적성, OEM 팩 토폴로지·제어·냉각 정보가 부족하다. LFP 상전이·히스테리시스와 복합 전극 역학에도 기본 교환 파일을 넘는 증거가 필요하다. 이는 명시적인 데이터 공백이지 물리 기반 모델링 자체가 불가능하다는 뜻은 아니다.

| 관문 | 다음 단계 전 필요한 증거 | 중단·재검토 조건 |
|---|---|---|
| G0 출처 | 원본 대조·권리·단위·식별자 | 출처 미해결·전사 불일치 은폐 |
| G1 셀 기준 | 같은 셀의 정의·원문 곡선 재현 | 임의 계수 보상으로 모델 오차 숨김 |
| G2 전기화학·열 | 여러 온도·독립적인 실측 열 관측 | 추정 물성·설정값을 실측 검증처럼 사용 |
| G3 열화 | 달력·사이클 행렬·기작 관련 진단 | 용량만으로 모든 기작 적합 |
| G4 모듈·팩 | 전기·열 그래프·제어·동기화 관측 | 셀 배율만으로 OEM 팩 정확도 주장 |
| G5 일반화 | 홀드아웃·불확실성·영역 밖 평가 | 누출·미러 중복·무조건 외삽 |

## 즉시 수행할 수집 대기 목록
고정한 About:Energy blob 16개를 받고 의미적 동등성을 비교한다. CSV 전체 헤더와 시험 조건을 먼저 읽은 뒤 어댑터를 만든다. 공식 내보내기에서 HG2와 역학 파손 자료의 파일 목록을 확보한다. 선택한 CALCE·NASA 권리를 검토하고 필요한 Battery Archive 연구만 요청한다. 차단된 Oxford·ILCC·Michigan 원문에 재접근하여 라이선스와 버전을 확인한다. 어느 작업도 이미 끝난 것으로 표시하지 않는다.

다음으로 가치 있는 수집이 가장 큰 아카이브라는 보장은 없다. 잘 특성화되고 같은 셀로 연결된 열량·펄스·OCV 자료가 수천 개의 비정합 수명 곡선보다 더 많은 불확실성을 줄일 수 있다. 이 우선순위는 후속 민감도·식별 가능성 분석으로 재검토한다.

## 후속 연구의 산출물
고정된 셀 식별 문서, 버전별 매개변수 출처 맵, 보정·홀드아웃 프로토콜 표, 미관측량 장부, 불확실성 예산, 권리 검토된 원시 데이터 목록을 만든다. 이들이 검토된 뒤 별도의 구현 작업에서 과학 커널이나 UI를 작성한다.

이 저장소는 일정이나 성능을 보장하지 않는다. 필요한 증거 관문과 현재 열린 항목을 기록한다. 향후 자료는 초기 스냅샷을 보존한 채 날짜가 있는 개정으로 추가하며, 원본을 몰래 교체하거나 실패한 검증 범위를 숨기지 않는다.

## 근거 출처

- [S01: About:Energy BPX parameterisation repository](https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation)
- [S03: PyBaMM thermal models](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/thermal-models.html)
- [S04: PyBaMM coupled degradation](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/coupled-degradation.html)
- [S06: BPX official standard download and change notes](https://bpxstandard.com/bpx-standard/)
- [S10: LG HG2 dataset v3](https://data.mendeley.com/datasets/cp3473x7xv/3)
- [S11: Battery Archive study summaries](https://batteryarchive.org/study_summaries.html)
- [S14: Battery Failure Databank](https://www.nlr.gov/transportation/battery-failure)
- [S15: Battery Microstructures Library](https://www.nlr.gov/transportation/microstructure)
- [S24: Michigan expansion dataset landing](https://deepblue.lib.umich.edu/data/concern/data_sets/5d86p0488)

조사 기준일: 2026-09-10. 설계 선택은 제안이며 시뮬레이터의 실측 성능을 의미하지 않는다.
