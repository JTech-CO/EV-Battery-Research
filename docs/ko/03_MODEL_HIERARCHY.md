# 모델 계층과 필요한 증거

[English](../en/03_MODEL_HIERARCHY.md) · [README](../../README-KR.md)

## 관측량별로 정밀도를 선택한다
| 모델 | 적합한 역할 | 추가로 필요한 증거 | 주요 한계 |
|---|---|---|---|
| ECM | 빠른 단자 전압·BMS 기준 | SOC·온도·SOH별 OCV·펄스·RC 맵 | 내부 농도·반응 상태를 풀지 않음 |
| SPM | 축약 입자 확산 | 입자·OCP·반응 속도 정보 | 전해질 제약을 단순화 |
| SPMe | 전해질 효과를 포함한 축약 모델 | 전해질 수송·형상 | 축약 가정과 유효 범위 |
| DFN/P2D | 다공성 전극의 전하·질량·반응 | 일관된 상세 물성 | 실제 3D 셀·모든 화학 반응의 자동 재현 아님 |
| 공간 전기화학·열 | 온도·전류의 비균일 | 집전체·탭·이방성 물성·경계조건 | 미확보 공간 정보가 정확도를 지배할 수 있음 |
| 열화·역학 결합 | 이력과 손상 관측 | 기작별 진단·구성 관계 | 식별 가능성과 모델 형식 불확실성 |

ECM은 비교 기준, SPMe·DFN은 과학적 기준으로 두고 추가 상태를 뒷받침할 데이터가 있을 때 공간·결합 모델로 확장하는 구성을 제안한다. 이는 연구 판단이며 이번 저장소에 솔버를 구현하라는 뜻은 아니다. [S02-S05]

## DFN의 핵심 계약
대표적인 구형 입자의 확산식은 다음과 같다.

$$\partial_t c_s=\frac{1}{r^2}\partial_r(r^2D_s\partial_r c_s).$$

입자 중심에서는 반경 방향 플럭스가 0이다. 표면에서는 선택한 부호 정의에 따라 계면 전류밀도와 패러데이 상수로 플럭스를 연결한다. 고체·전해질 전위에는 전하 보존이, 전해질 염에는 별도의 수송 수지가 필요하다. 초기 농도, 집전체 경계, 계면 연속 조건, 전위 기준도 지정해야 한다. [S02]

차원이 있는 계면 전류밀도의 일반적인 Butler-Volmer 표현은 다음과 같다.

$$j=i_0\left[e^{\alpha_aF\eta/(RT)}-e^{-\alpha_cF\eta/(RT)}\right].$$

$i_0$의 단위와 농도 정규화 방식은 방정식의 일부이다. 구형 BPX의 몰 단위 반응 속도 상수를 다른 구현체의 교환 전류 함수에 그대로 넣으면 안 된다.

## 모델 형식의 한계
원본 LFP README는 고율·저SOC 오차, 원통형 셀의 공간 비균일, LFP에 대한 기본 Fick·Butler-Volmer 기술의 한계를 명시한다. 이를 유효 범위로 보존하고 무관한 열 물성을 조정해 가리지 않는다. 수렴한 모델이라도 물리 가정이 틀렸다면 여전히 틀린 모델이다.

이번에는 과학 솔버를 실행하지 않았으므로 정확도나 실행 시간 벤치마크를 제시하지 않는다. 계산 비용은 나중에 솔버·격자·허용 오차·하드웨어를 고정한 상태에서 측정해야 한다.

## 근거 출처

- [S01: About:Energy BPX parameterisation repository](https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation)
- [S02: PyBaMM DFN equations](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/DFN.html)
- [S03: PyBaMM thermal models](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/thermal-models.html)
- [S04: PyBaMM coupled degradation](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/coupled-degradation.html)
- [S05: PyBaMM parameterisation](https://docs.pybamm.org/en/latest/source/examples/notebooks/parameterization/parameterization.html)

조사 기준일: 2026-09-10. 설계 선택은 제안이며 시뮬레이터의 실측 성능을 의미하지 않는다.
