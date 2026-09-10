# 열화 기작과 식별 가능성

[English](../en/06_DEGRADATION_AND_IDENTIFIABILITY.md) · [README](../../README-KR.md)

## 용량 감소는 관측량이지 고유한 기작이 아니다
순환 가능한 리튬 재고 손실(LLI), 활물질 손실(LAM), SEI 성장, 리튬 석출·박리와 비활성 리튬, 입자 균열, 전해질 고갈, 접촉 열화, 가스 관련 팽창을 구분한다. 기작이 결합되면 수지 관리가 달라진다. 균열은 새로운 SEI 형성 면적을 만들 수 있고 석출된 리튬 경로도 재고량을 줄일 수 있다. 재고 수지 없이 용량 손실 항을 각각 더하면 같은 리튬을 두 번 계산할 수 있다. [S04]

| 기작·상태 | 필요한 증거 | 단독으로 부족한 근거 |
|---|---|---|
| LLI·전극 균형 | 조건을 맞춘 OCP/DVA와 보조 진단 | 총 용량 감소 |
| LAM | 전극 용량·구조·전기화학 진단 | 저항 증가만 관측 |
| SEI | 피막·수송 근거, 열화 조건 행렬 | 임의의 제곱근 시간 적합 |
| 석출·비활성 리튬 | 기작에 민감한 측정과 충전 이력 | 하나의 전압 이상 |
| 균열·팽창 | 기계적 지그 조건과 구조 진단 | 조건이 없는 셀 두께 변화 |

첫 열화 모델은 관측량으로 식별할 수 있는 최소한의 모델이어야 한다. 상세 기작망이 결정되지 않는 상황에서는 반경험식이 검증 영역 안에서 더 정직한 예측기가 될 수 있다. 이런 선택을 명시하고 적합 계수를 직접 측정한 소재 물성처럼 표현하지 않는다.

## 실험 설계
달력 시간, 전하 처리량, 사이클 수, 휴지, 평균 SOC, DOD, 전류율, 온도 이력을 보존한다. 등가 완전 사이클을 방전 Ah/기준 용량으로 정의할 수도 있고, 충전·방전 절댓값 처리량/(기준 용량의 두 배)로 정의할 수도 있다. 두 정의를 섞지 않는다. 용량·저항 비교에는 조건을 맞춘 기준 성능 시험이 필요하다.

NASA·Sandia/Archive·CALCE·Oxford·ILCC·MATR는 서로 다른 이력과 관측량을 제공한다. 이를 보편적인 전기차 열화 곡선으로 그대로 합칠 수 없다. 행 수보다 셀 식별, 프로토콜, 중도 종료 여부, 불확실성의 정합성이 중요하다. [S07-S12, S23, S25]

## 누출과 불확실성
적합 전에 셀·배치·원 연구 전체를 기준으로 분할한다. 초기 수명 예측에 같은 셀의 말기 이력이 들어가면 안 된다. 보간 용량과 dQ/dV 같은 파생 특징은 처리 이력을 보존한다. 미러·재포장 자료는 원 연구와 개체 ID로 중복을 제거한다.

매개변수·사후 분포의 상관관계, 관측하지 못한 상태의 불확실성, 대안적 모델 형식을 보고한다. 전압 잔차가 작다는 이유만으로 SEI 두께나 석출 리튬 질량이 검증되지는 않는다. 최적화가 조정한 항을 곧바로 보편적인 원인으로 해석하지 않는다.

## 근거 출처

- [S04: PyBaMM coupled degradation](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/coupled-degradation.html)
- [S07: CALCE battery data](https://calce.umd.edu/battery-data)
- [S08: NASA Li-ion aging catalog](https://data.nasa.gov/dataset/li-ion-battery-aging-datasets)
- [S09: NASA PCoE data repository](https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/)
- [S11: Battery Archive study summaries](https://batteryarchive.org/study_summaries.html)
- [S23: Iowa State ILCC dataset landing](https://doi.org/10.25380/iastate.22582234)
- [S25: Severson/Attia original data-processing repository](https://github.com/rdbraatz/data-driven-prediction-of-battery-cycle-life-before-capacity-degradation)
- [S28: PyBOP paper](https://arxiv.org/abs/2412.15859)

조사 기준일: 2026-09-10. 설계 선택은 제안이며 시뮬레이터의 실측 성능을 의미하지 않는다.
