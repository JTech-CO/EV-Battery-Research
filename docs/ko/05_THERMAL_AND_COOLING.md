# 열 거동과 냉각 경계조건

[English](../en/05_THERMAL_AND_COOLING.md) · [README](../../README-KR.md)

## 발열과 열 제거를 분리한다
공간 열 도메인의 기본 수지는 다음과 같다.

$$\rho c_p\partial_tT=\nabla\cdot(\mathbf{k}\nabla T)+q_{gen}.$$

접촉·대류·복사·냉각수 경계를 별도로 정의해야 한다. 집중정수 모델은 공간 온도를 대표 상태로 치환하므로 모델이 풀지 않는 코어·표면 온도 차이를 독립적으로 예측할 수 없다. 이방성 열전도율, 비열, 밀도, 센서 위치, 냉각 형상이 필요하다. [S03]

방전 전류를 양수로 두고 평형에 가까운 열역학 가정과 일관된 OCV를 사용한 셀 전체 진단식은 다음과 같다.

$$\dot Q_{irr}=I(U_{OCV}-V),\qquad \dot Q_{rev}=-IT\frac{\partial U_{OCV}}{\partial T}.$$

이는 상세 모델의 모든 비평형 혼합·부반응 발열을 대신하지 않는다. 분포형 옴·반응·엔트로피 발열을 쓰면서 같은 전체 손실을 다시 더하면 중복 계산이다. 단자 손실에 포함된 탭·버스바 저항의 열은 실제 발생 도메인에 배분한다. 엔트로피 항을 사용하기 전에 전류와 반응 부호를 반드시 맞춘다.

## 열 데이터 계약
센서 좌표와 부착 방법, 표면·코어·챔버의 구분, 샘플링, 보정·지연, 전류·전압 동기화, 냉각수 입출구 온도와 질량 유량, 접촉 압력, 열량계 경계를 기록한다. 일정한 챔버 설정값은 셀 온도 실측 시계열이 아니다. 열전달과 비열이 서로 보상하는 단일 곡선보다 분리 식별이 가능한 실험을 사용한다.

동봉 BPX는 일부 열 물성이 추정값이라고 명시하고 엔트로피 입력은 문헌에서 가져온다. NMC 내장 온도 배열은 모두 298.15 K이며, 확보한 원문만으로 코어나 표면 센서 실측이라고 확정할 수 없다. 따라서 정규화 파일에서는 `reference_temperature_K`로 저장하고 표면·코어 온도는 null로 남겼다. [S01]

## 파손 발열은 다른 영역이다
NLR 파손 데이터뱅크는 유도된 열폭주에서 몸체·분출물의 열과 질량을 제공한다. 조건별 파손 에너지와 변동성의 경계를 정하는 데 유용하지만 정상 사이클 발열이나 보편적 반응 속도 모델의 보정 자료는 아니다. 명시된 스프레드시트 개정은 2024년 2월이며 웹페이지의 최근 관리 날짜와 구분해야 한다. [S14]

다음 수집에서는 냉각 시각화보다 같은 셀의 정상 충방전 열량과 독립적인 열 이완 측정을 우선한다. 이번 패키지로 열 정확도가 검증된 것은 아니다.

## 근거 출처

- [S01: About:Energy BPX parameterisation repository](https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation)
- [S03: PyBaMM thermal models](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/thermal-models.html)
- [S14: Battery Failure Databank](https://www.nlr.gov/transportation/battery-failure)

조사 기준일: 2026-09-10. 설계 선택은 제안이며 시뮬레이터의 실측 성능을 의미하지 않는다.
