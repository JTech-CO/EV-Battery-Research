# 작동 원리와 화학·물리 반응

[English](../en/01_PHYSICS_AND_CHEMISTRY.md) · [README](../../README-KR.md)

## 리튬과 전하의 이동
방전할 때 음극 활물질에서 리튬 이온이 빠져나오고 전자는 외부 회로로 이동한다. 이온은 전해질로 채워진 기공과 분리막을 통과하며, 전자는 전도성 전극·집전체를 따라 흐른다. 분리막은 전극의 전자적 접촉을 차단하면서 이온 이동을 허용해야 한다. 충전에서는 삽입·탈리의 순방향이 반대가 된다. 산화·환원을 뜻하는 anode/cathode는 반응 방향에 따라 달라질 수 있으므로 문서와 코드에서는 음극·양극 명칭을 일관되게 사용한다.

흑연 음극의 방전 반쪽 반응은 다음처럼 나타낼 수 있다.

$$\mathrm{Li_xC_6\rightarrow Li_{x-\delta}C_6+\delta Li^++\delta e^-}.$$

양극은 대응하는 리튬과 전자를 받아들인다. LFP는 LiFePO4/FePO4 계와 연결되며, 층상 NMC는 조성에 따른 리튬 점유 상태를 갖는다. 이 개략적인 물질 수지는 반응 속도나 보편적인 상전이 법칙까지 지정하지 않는다. 선택한 연속체 모델이 별도의 구성 관계를 제공해야 한다. [S01, S02]

## 혼동하면 안 되는 상태량
전극의 화학양론비는 $\theta=c_s/c_{s,max}$이다. 셀 SOC는 기준 시험에 대한 사용 가능 전하 좌표이며 어느 한 전극의 화학양론비와 동일하지 않다. 전극의 사용 구간은 용량 균형, 차단 전압, 리튬 재고량과 연결된다. 용량 기준 SOH를 $Q_{ref,aged}/Q_{ref,fresh}$로 정의하려면 신품과 열화 후 시험 조건을 맞춰야 한다. BMS SOC·SOH는 추정기 출력이지 직접 관측한 정답은 아니다.

**방전 전류를 양수**로 정의한 이상적 쿨롱 계수 관계는 다음과 같다.

$$\dot z=-I/(3600Q_{ref,Ah}).$$

효율, 부반응 전류, 용량 변화는 별도로 명시해야 한다. 분모를 임의로 바꾸어 상태 정의의 변화를 숨기면 안 된다.

## 전압 손실과 발열의 원인
평형 전압은 양극과 음극의 화학 퍼텐셜 차이와 연결된다. 부하가 걸리면 전자·이온 저항, 반응 과전압, 농도 구배가 단자 전압을 바꾼다. 온도는 확산과 반응 속도를 변화시키고, 농도와 상 이력은 평형·수송 관계에 영향을 줄 수 있다. 모든 전류·SOC·온도에서 이를 하나의 일정한 내부 저항으로 대체할 수는 없다. [S02, S03]

흔히 쓰는 Arrhenius 표현은 다음과 같다.

$$k(T)=k(T_{ref})\exp\left[-\frac{E_a}{R}\left(\frac1T-\frac1{T_{ref}}\right)\right].$$

절대온도 K, 활성화 에너지 J/mol, 기준 온도, 검증된 범위를 기록해야 한다. 한 구간의 적합 계수를 동결·분해 영역이나 다른 전해질 조성까지 자동으로 외삽해서는 안 된다.

## 확보해야 할 근거
셀·반쪽전지의 평형 관계, 전극 용량·화학양론비 구간, 초기 리튬 재고, 수송 함수, 반응 속도 정의, 온도 의존성을 확보한다. 필요한 화학계에서는 상 분율과 히스테리시스 이력도 기록한다. 충방전·EIS·GITT·구조 분석은 서로 다른 부분을 제약하는 상보적인 자료이다.

## 근거 출처

- [S01: About:Energy BPX parameterisation repository](https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation)
- [S02: PyBaMM DFN equations](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/DFN.html)
- [S03: PyBaMM thermal models](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/thermal-models.html)
- [S05: PyBaMM parameterisation](https://docs.pybamm.org/en/latest/source/examples/notebooks/parameterization/parameterization.html)
- [S07: CALCE battery data](https://calce.umd.edu/battery-data)

조사 기준일: 2026-09-10. 설계 선택은 제안이며 시뮬레이터의 실측 성능을 의미하지 않는다.
