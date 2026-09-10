# 전기화학 특성화와 매개변수 활용

[English](../en/04_ELECTROCHEMICAL_DATA.md) · [README](../../README-KR.md)

## 상수보다 함수와 시험 조건을 저장한다
유용한 대상은 하나의 상수보다 $D_s(\theta,T)$, $\kappa_e(c_e,T)$, $U(\theta,T,history)$, $i_0(c_e,c_s,T)$인 경우가 많다. 상수가 의도한 근사라면 그렇게 표시한다. 시험법, 농도 정의, 전극 면적 정규화, 온도, 휴지 시간, 전류율, 불확실성을 값과 함께 기록한다. [S01, S05]

| 측정 | 주로 제약하는 것 | 필수 주의사항 |
|---|---|---|
| 저율·셀 OCV | 평형 전압·용량 구간 | 유한 전류는 정확한 평형이 아니며 이완·이력이 남음 |
| 반쪽전지 OCP | 전극별 평형 곡선 | 해체·재조립으로 조건이 달라질 수 있음 |
| GITT/PITT | 확산 관련 응답 | 형상·상 거동·열역학 기울기가 추정에 영향 |
| 펄스·HPPC | 과도 저항·RC 응답 | 펄스 길이·SOC·온도·이력 의존 |
| EIS | 주파수별 선형 응답 | 여기 크기·휴지·정상성·복소 부호 필요 |
| 전류율·주행 부하 | 결합된 동적 응답 | 전압이 맞아도 내부 계수 각각이 식별되는 것은 아님 |

CALCE에는 저전류·증분 OCV와 동적 프로파일 예가 있고, NASA 열화 자료에는 시계열과 임피던스 채널이 있다. LG HG2 원문은 계측기 풀스케일의 0.1% 정확도를 명시한다. 이를 각 측정값의 0.1%라고 바꾸면 안 된다. [S07, S08, S10]

## 식별 순서
독립 측정한 형상·조성을 먼저 고정한다. 다음은 전극 용량 균형과 평형 관계이다. 이후 여러 펄스 길이, 전류율, 온도, 전극 수준 관측으로 수송·반응 속도를 제약한다. 열 경계 매개변수는 적절한 열 관측에서 구하며 전압 오차를 줄이기 위해 임의로 조절하지 않는다. 평가는 별도 프로토콜·셀을 남겨 수행한다.

확산 시간 척도에는 대략 $R^2/D_s$가 포함되어 반경과 확산계수가 서로 보상할 수 있다. 활성 면적과 반응 속도 계수도 상쇄될 수 있다. 유일한 물리 식별을 주장하려면 민감도, 프로파일 우도·사후 상관, 독립 시험이 필요하다. 한 방전 곡선에 모든 항목을 동시에 적합하지 않는다.

## 추가 입력 규칙
EIS의 $Z'$, $Z''$, 주파수, 장비 부호를 보존한다. Kramers-Kronig 검사는 적절한 선형·정상 조건을 전제로 하며, 실패가 하나의 소재 결함을 유일하게 지정하지 않는다. DRT 피크나 미분 용량 특징도 기작을 직접 관측한 고유 라벨이 아니다.

빠진 온도 의존성을 출처 없는 활성화 에너지로 채우지 않는다. 문헌 값은 전이 가정을 명시한 사전 정보로만 사용한다. 대체 값을 실험하기 전 원본 매개변수 묶음을 일관된 기준으로 유지한다.

## 근거 출처

- [S01: About:Energy BPX parameterisation repository](https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation)
- [S05: PyBaMM parameterisation](https://docs.pybamm.org/en/latest/source/examples/notebooks/parameterization/parameterization.html)
- [S07: CALCE battery data](https://calce.umd.edu/battery-data)
- [S08: NASA Li-ion aging catalog](https://data.nasa.gov/dataset/li-ion-battery-aging-datasets)
- [S10: LG HG2 dataset v3](https://data.mendeley.com/datasets/cp3473x7xv/3)
- [S28: PyBOP paper](https://arxiv.org/abs/2412.15859)

조사 기준일: 2026-09-10. 설계 선택은 제안이며 시뮬레이터의 실측 성능을 의미하지 않는다.
