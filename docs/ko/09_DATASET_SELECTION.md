# 데이터셋 선정과 정합 전략

[English](../en/09_DATASET_SELECTION.md) · [README](../../README-KR.md)

## 권장 수집 조합
| 필요 영역 | 우선 후보 | 활용 방식 |
|---|---|---|
| 일관된 전기화학 기준 | About:Energy NMC, 별도의 LFP 예제 | 같은 셀의 매개변수와 기준 곡선 유지 |
| 동적 전기·온도 시험 | LG HG2, 선택한 CALCE 컬렉션 | 정확한 셀·프로토콜 안에서 독립 비교 |
| 열화·임피던스 이력 | NASA PCoE, Sandia/Archive, CALCE, MATR | 기준 시험·셀/배치 홀드아웃·이력 분석 |
| 조건 상호작용·팽창 | ILCC, Michigan 후보 | 원시 파일과 지그·조건 정보를 먼저 확보 |
| 파손 발열·역학 신호 | NLR Failure, ORNL/Sandia v2 | 별도의 파손 영역 검증 |
| 미세구조 사전 정보 | NLR 미세구조 라이브러리 | 동의 조건 아래 재구성 상의 출처 유지 |
| 차량 요구 입력 | EPA 프로파일 | 규정 속도 경계, 차량 부하 변환은 별도 |
| 모델·스키마 참고 | PyBaMM, BPX, BLAST, Materials Project | 정의·사전 정보이지 실험 정답은 아님 |

이는 파일 수가 아니라 상보성에 따른 공학적 우선순위이다. 접근·권리 제약은 개별 카드를 확인한다. 일부 원본 페이지는 차단됐고, 파일 목록이 자바스크립트 전용이거나 요청·동의를 요구하는 경우도 있었다. 우회·대리 제출은 수행하지 않았다.

## 같은 셀인지 확인하는 관문
자료를 결합하기 전에 제조사·변형 모델, 양·음극 조성, 형식, 용량, 전극 형상, 화성·배치, 전해질, 온도, SOC 정의, 전류율, 차단 전압, 휴지, 열화 상태를 비교한다. 불일치 자료가 무조건 쓸모없다는 뜻은 아니다. 직접 보정 근거에서 전이 사전 정보·외부 비교로 역할이 달라진다는 뜻이며 이를 명시한다.

“같은 화학계”보다 “같은 상용 셀”이, 그보다 “같은 배치·시편”이 강한 정합 조건이다. NMC811 확산, NMC111 OCP, 다른 셀의 열전도율, 무관한 열화식을 조립한 뒤 실측 가상 셀이라고 표현하지 않는다. 그런 전이가 필요하면 가정과 불확실성 모델을 문서화한다.

## 제안하는 세 가지 증거 묶음
**A: 원본 기준 재현.** 동봉 About:Energy 두 세트와 원래의 검증 파일이다. 매개변수 의미와 원본 기준 재현에 적합하지만 독립 검증의 증거는 아니다.

**B: 정합된 전기화학·열 셀.** 하나의 상용 변형 모델에 대한 온도별 펄스·충방전·엔트로피/열량·형상이다. 이 전체 묶음은 아직 확보하지 못했다.

**C: 열화·모듈 현실성.** 달력·사이클 조건 행렬, 팽창·EIS 진단, 전기·열·제어 정보가 명시된 모듈을 더한다. 현재 데이터가 아니라 후속 증거 목표이다.

파일 사본이 아니라 원래의 개체를 센다. 보정 자료, 원문 기준 곡선, 진정한 홀드아웃을 서로 다른 라벨로 보존한다.

## 근거 출처

- [S01: About:Energy BPX parameterisation repository](https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation)
- [S07: CALCE battery data](https://calce.umd.edu/battery-data)
- [S08: NASA Li-ion aging catalog](https://data.nasa.gov/dataset/li-ion-battery-aging-datasets)
- [S09: NASA PCoE data repository](https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/)
- [S10: LG HG2 dataset v3](https://data.mendeley.com/datasets/cp3473x7xv/3)
- [S11: Battery Archive study summaries](https://batteryarchive.org/study_summaries.html)
- [S13: Mechanically induced thermal runaway v2](https://data.mendeley.com/datasets/sn2kv34r4h/2)
- [S14: Battery Failure Databank](https://www.nlr.gov/transportation/battery-failure)
- [S15: Battery Microstructures Library](https://www.nlr.gov/transportation/microstructure)
- [S17: EPA dynamometer schedules](https://www.epa.gov/vehicle-and-fuel-emissions-testing/dynamometer-drive-schedules)
- [S25: Severson/Attia original data-processing repository](https://github.com/rdbraatz/data-driven-prediction-of-battery-cycle-life-before-capacity-degradation)

조사 기준일: 2026-09-10. 설계 선택은 제안이며 시뮬레이터의 실측 성능을 의미하지 않는다.
