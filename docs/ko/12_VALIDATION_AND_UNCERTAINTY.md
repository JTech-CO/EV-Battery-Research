# 검증과 불확실성 계획

[English](../en/12_VALIDATION_AND_UNCERTAINTY.md) · [README](../../README-KR.md)

## 증거 수준을 구분한다
데이터 QA, 수치 검증, 보정, 원본 기준 재현, 독립 검증, 배포 적합성은 서로 다르다. 이 저장소에서 수행하는 것은 로컬 데이터·패키지 QA와 결정적인 변환뿐이다. 솔버 결과, 보정된 모델 정확도, 안전 인증, 차량 적용 적합성은 제공하지 않는다.

원문 NMC 곡선은 매개변수 개발 자료와 겹칠 수 있으며 통계적 독립성이 확인되지 않았다. 따라서 깨끗한 홀드아웃이 아니라 **원문 기준 곡선**으로 표시한다. 재현 이후에는 다른 프로토콜·셀/배치·온도를 별도로 남겨 독립 평가한다.

## 제안하는 검증 단계
1. 단위·부호·식별자·스키마·입력 완전성·출처를 검사한다.
2. 추후 솔버에서는 초기 일관성, 리튬·전하·에너지 수지, 한계, 격자·시간·허용 오차 수렴을 검사한다.
3. 무관한 계수를 임의 조절하지 않고 원문 곡선을 재현한다.
4. 매개변수를 고정하고 홀드아웃 전류·SOC·온도를 평가한다.
5. 해당 관측과 경계조건이 확보된 후 열화·역학·팩 검증을 추가한다.

## 달성값이 아닌 공학적 목표 초안
| 관측량 | 정의된 영역에서의 시작 목표 예 | 필수 조건 |
|---|---|---|
| 셀 전압 | RMSE 20 mV 이하 | 최대 오차·편향·SOC/율/온도별 결과·계측 불확실성 |
| 기준 방전 용량 | 상대 오차 2% 이하 | 전류·온도·차단·기준 정의 동일 |
| 표면 실측 온도 | RMSE 2 K 이하 | 실제 센서 시계열과 경계조건, 챔버 설정값 제외 |
| 열화 예측 | 홀드아웃 점의 오차·구간 포함률 사전 정의 | 셀 단위 재표본화·중도 종료·예측 기간 정의 |
| 팩 거동 | 셀 한계·분기 전류 오차 사전 정의 | 토폴로지·제어·센서 매핑 확보 |

이 숫자는 검토를 시작하기 위한 제안이지 표준·논문 성능·보증이 아니다. 운용 영역과 계측 불확실성에 맞춰 수정해야 한다. 이번 패키지에서는 이 목표를 시험하거나 달성하지 않았다.

## 불확실성 보고
계측 오차, 매개변수 불확실성, 제조 분산, 보간·처리 오차, 모델 불일치, 영역 밖 사용을 구분한다. 근거가 있으면 공분산·사후 분포 앙상블을 사용하고 상관된 매개변수를 독립 분포로 취급하지 않는다. 인접 샘플 대신 셀 단위로 부트스트랩하여 유효 표본 수를 부풀리지 않는다.

전체 평균뿐 아니라 실패 조건과 잔차 구조도 보고한다. 그럴듯한 단자 곡선은 관측하지 않은 내부 농도·석출·SEI 상태를 검증하지 않는다. 향후 사용자 화면에는 근거 영역과 신뢰 상태를 표시하고 무음 외삽을 피해야 한다.

## 근거 출처

- [S01: About:Energy BPX parameterisation repository](https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation)
- [S05: PyBaMM parameterisation](https://docs.pybamm.org/en/latest/source/examples/notebooks/parameterization/parameterization.html)
- [S07: CALCE battery data](https://calce.umd.edu/battery-data)
- [S10: LG HG2 dataset v3](https://data.mendeley.com/datasets/cp3473x7xv/3)
- [S25: Severson/Attia original data-processing repository](https://github.com/rdbraatz/data-driven-prediction-of-battery-cycle-life-before-capacity-degradation)
- [S28: PyBOP paper](https://arxiv.org/abs/2412.15859)

조사 기준일: 2026-09-10. 설계 선택은 제안이며 시뮬레이터의 실측 성능을 의미하지 않는다.
