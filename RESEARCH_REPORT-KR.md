# 전기차 배터리 연구 | 통합 보고서

[English](RESEARCH_REPORT.md) · [README](README-KR.md)

2026-09-10 · 연구·데이터 준비 자료이며 시뮬레이터는 포함하지 않는다.

00. [연구 요약과 핵심 판단](#chapter-00)
01. [작동 원리와 화학·물리 반응](#chapter-01)
02. [셀 구조와 소재 식별](#chapter-02)
03. [모델 계층과 필요한 증거](#chapter-03)
04. [전기화학 특성화와 매개변수 활용](#chapter-04)
05. [열 거동과 냉각 경계조건](#chapter-05)
06. [열화 기작과 식별 가능성](#chapter-06)
07. [역학·미세구조·파손](#chapter-07)
08. [팩·BMS·차량 경계조건](#chapter-08)
09. [데이터셋 선정과 정합 전략](#chapter-09)
10. [수집·크롤링 범위와 재사용 조건](#chapter-10)
11. [데이터 계약과 정규화](#chapter-11)
12. [검증과 불확실성 계획](#chapter-12)
13. [공백 분석과 후속 연구 관문](#chapter-13)
14. [확보한 수치 데이터 점검](#chapter-14)
15. [BPX 의미와 버전 관리](#chapter-15)
16. [출처별 데이터 입력 절차](#chapter-16)
17. [향후 과학 엔진 프로젝트에 넘길 사항](#chapter-17)
18. [출처와 접근 감사 기록](#chapter-18)
19. [기술 용어집](#chapter-19)


---

<a id="chapter-00"></a>

## 00. 연구 요약과 핵심 판단

### 판단
향후 연구는 서로 다른 배터리 자료를 섞기보다 **내부적으로 일관된 하나의 기준 셀**에서 시작하는 것이 좋다. 첫 기준은 About:Energy의 NMC111/흑연 12.5 Ah 파우치 예제이며, LFP/흑연 2 Ah 원통형 예제는 별도 화학계와 모델 한계의 비교 대상으로 둔다. 어느 쪽도 최신 양산 전기차 팩을 검증한 자료는 아니다. 원본은 BPX 0.1이며, 특성화 결과·문헌 값·추정 열 물성이 섞여 있다고 명시한다. [S01]

최종적으로 검증해야 할 것은 전류·초기 상태·온도·냉각·사용 이력이 단자 전압, 물질 상태, 발열, 열화 관측량으로 연결되는 관계이다. 시각화가 정교하거나 DFN 해가 수치적으로 수렴했다는 사실만으로 물리적 정확성이 확보되지는 않는다.

### 데이터의 네 층
| 구분 | 필요한 정보 | 이번 패키지 상태 |
|---|---|---|
| 물성·구성 관계 | 형상, 전극 평형 전위, 확산, 반응 속도, 전해질 수송, 열 물성 | 기준 셀 두 종류 확보, 근거 수준은 혼합 |
| 실험 | 충방전·펄스·휴지·EIS·열량·열화·팽창 | NMC 내장 기준 곡선 확보, 나머지는 카탈로그 |
| 경계·제어 조건 | 냉각, 팩 토폴로지, 차량 부하, BMS 한계, 센서 | US06 속도 입력 확보, OEM 팩 정보는 미확보 |
| 증거·관리 | 개체 ID, 단위, 시험법, 불확실성, 권리, 버전, 보정·홀드아웃 구분 | 스키마·목록·출처·수집 기록 제공 |

### 실제 동봉 범위
원문 텍스트를 **전사·재직렬화한 JSON 두 개**, 그 안의 매개변수 104항목, NMC 내장 기준 곡선 114점, EPA 규정 속도 601점을 담았다. 공개 OCP 적합식에서 계산한 404점은 파생값이며 새로운 실측값이 아니다. 필요 데이터 목록 139행도 확보한 실측값 139개라는 뜻이 아니다.

자료 카드 23개에는 실험 컬렉션뿐 아니라 교환 규격과 소프트웨어 참고 자료가 포함된다. 따라서 “실험 데이터셋 23개 전체 다운로드”로 소개하면 안 된다. About:Energy 원본 Git blob 16개는 재수집 대상으로 고정했으나 원본 바이트 파일은 이번에 다운로드하지 못했다. 시뮬레이션·보정·학습·원본과의 JSON 동등성 검증·계정 변경·깃허브 게시도 수행하지 않았다.

### 우선순위
먼저 원본 BPX와 동봉 스냅샷을 대조하고 같은 셀의 검증 CSV 전체를 확보한다. 다음은 같은 셀의 독립적인 온도·열 측정이다. 그 뒤에 식별 가능한 열화 기작과 명시적인 모듈·팩 정보를 추가한다. 공개 자료로 검증 영역이 분명한 연구 모델을 구성할 수 있지만, 특정 제조사 전기차를 그대로 재현했다고 주장할 근거는 아직 없다.

### 근거 출처

- [S01: About:Energy BPX parameterisation repository](https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation)
- [S06: BPX official standard download and change notes](https://bpxstandard.com/bpx-standard/)
- [S10: LG HG2 dataset v3](https://data.mendeley.com/datasets/cp3473x7xv/3)
- [S17: EPA dynamometer schedules](https://www.epa.gov/vehicle-and-fuel-emissions-testing/dynamometer-drive-schedules)
- [S18: EPA US06 numeric schedule](https://www.epa.gov/system/files/other-files/2025-03/us06col.txt)

조사 기준일: 2026-09-10. 설계 선택은 제안이며 시뮬레이터의 실측 성능을 의미하지 않는다.


---

<a id="chapter-01"></a>

## 01. 작동 원리와 화학·물리 반응

### 리튬과 전하의 이동
방전할 때 음극 활물질에서 리튬 이온이 빠져나오고 전자는 외부 회로로 이동한다. 이온은 전해질로 채워진 기공과 분리막을 통과하며, 전자는 전도성 전극·집전체를 따라 흐른다. 분리막은 전극의 전자적 접촉을 차단하면서 이온 이동을 허용해야 한다. 충전에서는 삽입·탈리의 순방향이 반대가 된다. 산화·환원을 뜻하는 anode/cathode는 반응 방향에 따라 달라질 수 있으므로 문서와 코드에서는 음극·양극 명칭을 일관되게 사용한다.

흑연 음극의 방전 반쪽 반응은 다음처럼 나타낼 수 있다.

$$\mathrm{Li_xC_6\rightarrow Li_{x-\delta}C_6+\delta Li^++\delta e^-}.$$

양극은 대응하는 리튬과 전자를 받아들인다. LFP는 LiFePO4/FePO4 계와 연결되며, 층상 NMC는 조성에 따른 리튬 점유 상태를 갖는다. 이 개략적인 물질 수지는 반응 속도나 보편적인 상전이 법칙까지 지정하지 않는다. 선택한 연속체 모델이 별도의 구성 관계를 제공해야 한다. [S01, S02]

### 혼동하면 안 되는 상태량
전극의 화학양론비는 $\theta=c_s/c_{s,max}$이다. 셀 SOC는 기준 시험에 대한 사용 가능 전하 좌표이며 어느 한 전극의 화학양론비와 동일하지 않다. 전극의 사용 구간은 용량 균형, 차단 전압, 리튬 재고량과 연결된다. 용량 기준 SOH를 $Q_{ref,aged}/Q_{ref,fresh}$로 정의하려면 신품과 열화 후 시험 조건을 맞춰야 한다. BMS SOC·SOH는 추정기 출력이지 직접 관측한 정답은 아니다.

**방전 전류를 양수**로 정의한 이상적 쿨롱 계수 관계는 다음과 같다.

$$\dot z=-I/(3600Q_{ref,Ah}).$$

효율, 부반응 전류, 용량 변화는 별도로 명시해야 한다. 분모를 임의로 바꾸어 상태 정의의 변화를 숨기면 안 된다.

### 전압 손실과 발열의 원인
평형 전압은 양극과 음극의 화학 퍼텐셜 차이와 연결된다. 부하가 걸리면 전자·이온 저항, 반응 과전압, 농도 구배가 단자 전압을 바꾼다. 온도는 확산과 반응 속도를 변화시키고, 농도와 상 이력은 평형·수송 관계에 영향을 줄 수 있다. 모든 전류·SOC·온도에서 이를 하나의 일정한 내부 저항으로 대체할 수는 없다. [S02, S03]

흔히 쓰는 Arrhenius 표현은 다음과 같다.

$$k(T)=k(T_{ref})\exp\left[-\frac{E_a}{R}\left(\frac1T-\frac1{T_{ref}}\right)\right].$$

절대온도 K, 활성화 에너지 J/mol, 기준 온도, 검증된 범위를 기록해야 한다. 한 구간의 적합 계수를 동결·분해 영역이나 다른 전해질 조성까지 자동으로 외삽해서는 안 된다.

### 확보해야 할 근거
셀·반쪽전지의 평형 관계, 전극 용량·화학양론비 구간, 초기 리튬 재고, 수송 함수, 반응 속도 정의, 온도 의존성을 확보한다. 필요한 화학계에서는 상 분율과 히스테리시스 이력도 기록한다. 충방전·EIS·GITT·구조 분석은 서로 다른 부분을 제약하는 상보적인 자료이다.

### 근거 출처

- [S01: About:Energy BPX parameterisation repository](https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation)
- [S02: PyBaMM DFN equations](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/DFN.html)
- [S03: PyBaMM thermal models](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/thermal-models.html)
- [S05: PyBaMM parameterisation](https://docs.pybamm.org/en/latest/source/examples/notebooks/parameterization/parameterization.html)
- [S07: CALCE battery data](https://calce.umd.edu/battery-data)

조사 기준일: 2026-09-10. 설계 선택은 제안이며 시뮬레이터의 실측 성능을 의미하지 않는다.


---

<a id="chapter-02"></a>

## 02. 셀 구조와 소재 식별

### 형상 자체가 물리 모델의 일부이다
활물질 입자, 다공성 전극·분리막·집전체 층, 권취·적층 셀, 모듈·팩을 최소 네 스케일로 나눠야 한다. 두께 방향 1차원 전극 모델과 입자 반경 방향 확산을 결합해도 실제 권취 셀을 3차원으로 복원한 것은 아니다. 전기화학 층을 균질화하더라도 탭 위치, 집전체 저항, 이방성 열전달이 중요할 수 있다. [S02, S03]

| 스케일 | 필요한 데이터 | 잘못된 대체 |
|---|---|---|
| 입자 | 입도 분포·상 조성·확산·표면적·팽창 | 모든 소재에 같은 구형 반경 적용 |
| 전극 | 두께·로딩·활물질/바인더/기공 분율·수송 효율 | 기공률만으로 수송 결정 |
| 셀 | 층수·면적·집전체·탭·케이스·질량·냉각 접촉 | 외형 직경만으로 내부 활성 면적 결정 |
| 모듈·팩 | 전기 연결망·접촉·열 네트워크·구속 | 셀 출력에 Ns·Np만 곱하기 |

균일한 구형 입자 모델에서 $a_s=3\epsilon_s/R$이다. 이 식으로 복원한 활성 체적 분율은 **가정에 의존한 파생값**이지 별도의 독립 실측값이 아니다. 굴곡도 인자, 경로 길이 비, 수송 효율 역시 동일한 정의가 아니므로 수치 옆에 원문의 정의를 보존한다.

### 소재 이름만으로 묶지 않는다
NMC111, 고니켈 NMC, NCA, 혼합 양극은 같은 매개변수 식별자가 아니다. 흑연·실리콘 혼합 음극에는 상별 기여가 필요하다. 연구용 LFP 18650 자료가 대형 자동차 각형 LFP 셀을 식별해 주는 것도 아니다. 정확한 변형 모델·배치·화성·저장 이력·개체 ID를 기록하고 빠진 값은 null로 남긴다.

About:Energy 파우치 예제는 전극 면적과 전극 쌍 34개를 지정한다. 이는 외부 셀 34개가 아니다. 팩 병렬 개수로 착각하면 면적·용량·발열 스케일링이 잘못된다. [S01]

### 미세구조 수집
CT 복셀 크기, 원시·분할 여부, 상 라벨, 시야, 해상도, 캘린더링, 재구성 조건을 보존한다. NLR 자료는 탄소·바인더 영역을 수치적으로 생성한다고 명시한다. 모든 분할 영역을 직접 계측한 구조로 표기해서는 안 된다. 분할 방법과 미해상 기공이 형상 지표에 주는 영향을 평가한 뒤 유효 수송 물성에 연결한다. [S15]

필요 항목은 `catalog/parameter_requirements.csv`에 있다. 이 목록에는 이번 패키지에 없는 값도 포함된다. OEM 도면·용접 접촉 분포·소재 구성 시험의 부재는 연구 공백으로 남겨야 하며, 출처 없는 상수로 채우면 안 된다.

### 근거 출처

- [S01: About:Energy BPX parameterisation repository](https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation)
- [S02: PyBaMM DFN equations](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/DFN.html)
- [S03: PyBaMM thermal models](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/thermal-models.html)
- [S15: Battery Microstructures Library](https://www.nlr.gov/transportation/microstructure)
- [S16: Microstructure library agreement](https://www.nlr.gov/transportation/microstructure-library-disclaimer)

조사 기준일: 2026-09-10. 설계 선택은 제안이며 시뮬레이터의 실측 성능을 의미하지 않는다.


---

<a id="chapter-03"></a>

## 03. 모델 계층과 필요한 증거

### 관측량별로 정밀도를 선택한다
| 모델 | 적합한 역할 | 추가로 필요한 증거 | 주요 한계 |
|---|---|---|---|
| ECM | 빠른 단자 전압·BMS 기준 | SOC·온도·SOH별 OCV·펄스·RC 맵 | 내부 농도·반응 상태를 풀지 않음 |
| SPM | 축약 입자 확산 | 입자·OCP·반응 속도 정보 | 전해질 제약을 단순화 |
| SPMe | 전해질 효과를 포함한 축약 모델 | 전해질 수송·형상 | 축약 가정과 유효 범위 |
| DFN/P2D | 다공성 전극의 전하·질량·반응 | 일관된 상세 물성 | 실제 3D 셀·모든 화학 반응의 자동 재현 아님 |
| 공간 전기화학·열 | 온도·전류의 비균일 | 집전체·탭·이방성 물성·경계조건 | 미확보 공간 정보가 정확도를 지배할 수 있음 |
| 열화·역학 결합 | 이력과 손상 관측 | 기작별 진단·구성 관계 | 식별 가능성과 모델 형식 불확실성 |

ECM은 비교 기준, SPMe·DFN은 과학적 기준으로 두고 추가 상태를 뒷받침할 데이터가 있을 때 공간·결합 모델로 확장하는 구성을 제안한다. 이는 연구 판단이며 이번 저장소에 솔버를 구현하라는 뜻은 아니다. [S02-S05]

### DFN의 핵심 계약
대표적인 구형 입자의 확산식은 다음과 같다.

$$\partial_t c_s=\frac{1}{r^2}\partial_r(r^2D_s\partial_r c_s).$$

입자 중심에서는 반경 방향 플럭스가 0이다. 표면에서는 선택한 부호 정의에 따라 계면 전류밀도와 패러데이 상수로 플럭스를 연결한다. 고체·전해질 전위에는 전하 보존이, 전해질 염에는 별도의 수송 수지가 필요하다. 초기 농도, 집전체 경계, 계면 연속 조건, 전위 기준도 지정해야 한다. [S02]

차원이 있는 계면 전류밀도의 일반적인 Butler-Volmer 표현은 다음과 같다.

$$j=i_0\left[e^{\alpha_aF\eta/(RT)}-e^{-\alpha_cF\eta/(RT)}\right].$$

$i_0$의 단위와 농도 정규화 방식은 방정식의 일부이다. 구형 BPX의 몰 단위 반응 속도 상수를 다른 구현체의 교환 전류 함수에 그대로 넣으면 안 된다.

### 모델 형식의 한계
원본 LFP README는 고율·저SOC 오차, 원통형 셀의 공간 비균일, LFP에 대한 기본 Fick·Butler-Volmer 기술의 한계를 명시한다. 이를 유효 범위로 보존하고 무관한 열 물성을 조정해 가리지 않는다. 수렴한 모델이라도 물리 가정이 틀렸다면 여전히 틀린 모델이다.

이번에는 과학 솔버를 실행하지 않았으므로 정확도나 실행 시간 벤치마크를 제시하지 않는다. 계산 비용은 나중에 솔버·격자·허용 오차·하드웨어를 고정한 상태에서 측정해야 한다.

### 근거 출처

- [S01: About:Energy BPX parameterisation repository](https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation)
- [S02: PyBaMM DFN equations](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/DFN.html)
- [S03: PyBaMM thermal models](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/thermal-models.html)
- [S04: PyBaMM coupled degradation](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/coupled-degradation.html)
- [S05: PyBaMM parameterisation](https://docs.pybamm.org/en/latest/source/examples/notebooks/parameterization/parameterization.html)

조사 기준일: 2026-09-10. 설계 선택은 제안이며 시뮬레이터의 실측 성능을 의미하지 않는다.


---

<a id="chapter-04"></a>

## 04. 전기화학 특성화와 매개변수 활용

### 상수보다 함수와 시험 조건을 저장한다
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

### 식별 순서
독립 측정한 형상·조성을 먼저 고정한다. 다음은 전극 용량 균형과 평형 관계이다. 이후 여러 펄스 길이, 전류율, 온도, 전극 수준 관측으로 수송·반응 속도를 제약한다. 열 경계 매개변수는 적절한 열 관측에서 구하며 전압 오차를 줄이기 위해 임의로 조절하지 않는다. 평가는 별도 프로토콜·셀을 남겨 수행한다.

확산 시간 척도에는 대략 $R^2/D_s$가 포함되어 반경과 확산계수가 서로 보상할 수 있다. 활성 면적과 반응 속도 계수도 상쇄될 수 있다. 유일한 물리 식별을 주장하려면 민감도, 프로파일 우도·사후 상관, 독립 시험이 필요하다. 한 방전 곡선에 모든 항목을 동시에 적합하지 않는다.

### 추가 입력 규칙
EIS의 $Z'$, $Z''$, 주파수, 장비 부호를 보존한다. Kramers-Kronig 검사는 적절한 선형·정상 조건을 전제로 하며, 실패가 하나의 소재 결함을 유일하게 지정하지 않는다. DRT 피크나 미분 용량 특징도 기작을 직접 관측한 고유 라벨이 아니다.

빠진 온도 의존성을 출처 없는 활성화 에너지로 채우지 않는다. 문헌 값은 전이 가정을 명시한 사전 정보로만 사용한다. 대체 값을 실험하기 전 원본 매개변수 묶음을 일관된 기준으로 유지한다.

### 근거 출처

- [S01: About:Energy BPX parameterisation repository](https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation)
- [S05: PyBaMM parameterisation](https://docs.pybamm.org/en/latest/source/examples/notebooks/parameterization/parameterization.html)
- [S07: CALCE battery data](https://calce.umd.edu/battery-data)
- [S08: NASA Li-ion aging catalog](https://data.nasa.gov/dataset/li-ion-battery-aging-datasets)
- [S10: LG HG2 dataset v3](https://data.mendeley.com/datasets/cp3473x7xv/3)
- [S28: PyBOP paper](https://arxiv.org/abs/2412.15859)

조사 기준일: 2026-09-10. 설계 선택은 제안이며 시뮬레이터의 실측 성능을 의미하지 않는다.


---

<a id="chapter-05"></a>

## 05. 열 거동과 냉각 경계조건

### 발열과 열 제거를 분리한다
공간 열 도메인의 기본 수지는 다음과 같다.

$$\rho c_p\partial_tT=\nabla\cdot(\mathbf{k}\nabla T)+q_{gen}.$$

접촉·대류·복사·냉각수 경계를 별도로 정의해야 한다. 집중정수 모델은 공간 온도를 대표 상태로 치환하므로 모델이 풀지 않는 코어·표면 온도 차이를 독립적으로 예측할 수 없다. 이방성 열전도율, 비열, 밀도, 센서 위치, 냉각 형상이 필요하다. [S03]

방전 전류를 양수로 두고 평형에 가까운 열역학 가정과 일관된 OCV를 사용한 셀 전체 진단식은 다음과 같다.

$$\dot Q_{irr}=I(U_{OCV}-V),\qquad \dot Q_{rev}=-IT\frac{\partial U_{OCV}}{\partial T}.$$

이는 상세 모델의 모든 비평형 혼합·부반응 발열을 대신하지 않는다. 분포형 옴·반응·엔트로피 발열을 쓰면서 같은 전체 손실을 다시 더하면 중복 계산이다. 단자 손실에 포함된 탭·버스바 저항의 열은 실제 발생 도메인에 배분한다. 엔트로피 항을 사용하기 전에 전류와 반응 부호를 반드시 맞춘다.

### 열 데이터 계약
센서 좌표와 부착 방법, 표면·코어·챔버의 구분, 샘플링, 보정·지연, 전류·전압 동기화, 냉각수 입출구 온도와 질량 유량, 접촉 압력, 열량계 경계를 기록한다. 일정한 챔버 설정값은 셀 온도 실측 시계열이 아니다. 열전달과 비열이 서로 보상하는 단일 곡선보다 분리 식별이 가능한 실험을 사용한다.

동봉 BPX는 일부 열 물성이 추정값이라고 명시하고 엔트로피 입력은 문헌에서 가져온다. NMC 내장 온도 배열은 모두 298.15 K이며, 확보한 원문만으로 코어나 표면 센서 실측이라고 확정할 수 없다. 따라서 정규화 파일에서는 `reference_temperature_K`로 저장하고 표면·코어 온도는 null로 남겼다. [S01]

### 파손 발열은 다른 영역이다
NLR 파손 데이터뱅크는 유도된 열폭주에서 몸체·분출물의 열과 질량을 제공한다. 조건별 파손 에너지와 변동성의 경계를 정하는 데 유용하지만 정상 사이클 발열이나 보편적 반응 속도 모델의 보정 자료는 아니다. 명시된 스프레드시트 개정은 2024년 2월이며 웹페이지의 최근 관리 날짜와 구분해야 한다. [S14]

다음 수집에서는 냉각 시각화보다 같은 셀의 정상 충방전 열량과 독립적인 열 이완 측정을 우선한다. 이번 패키지로 열 정확도가 검증된 것은 아니다.

### 근거 출처

- [S01: About:Energy BPX parameterisation repository](https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation)
- [S03: PyBaMM thermal models](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/thermal-models.html)
- [S14: Battery Failure Databank](https://www.nlr.gov/transportation/battery-failure)

조사 기준일: 2026-09-10. 설계 선택은 제안이며 시뮬레이터의 실측 성능을 의미하지 않는다.


---

<a id="chapter-06"></a>

## 06. 열화 기작과 식별 가능성

### 용량 감소는 관측량이지 고유한 기작이 아니다
순환 가능한 리튬 재고 손실(LLI), 활물질 손실(LAM), SEI 성장, 리튬 석출·박리와 비활성 리튬, 입자 균열, 전해질 고갈, 접촉 열화, 가스 관련 팽창을 구분한다. 기작이 결합되면 수지 관리가 달라진다. 균열은 새로운 SEI 형성 면적을 만들 수 있고 석출된 리튬 경로도 재고량을 줄일 수 있다. 재고 수지 없이 용량 손실 항을 각각 더하면 같은 리튬을 두 번 계산할 수 있다. [S04]

| 기작·상태 | 필요한 증거 | 단독으로 부족한 근거 |
|---|---|---|
| LLI·전극 균형 | 조건을 맞춘 OCP/DVA와 보조 진단 | 총 용량 감소 |
| LAM | 전극 용량·구조·전기화학 진단 | 저항 증가만 관측 |
| SEI | 피막·수송 근거, 열화 조건 행렬 | 임의의 제곱근 시간 적합 |
| 석출·비활성 리튬 | 기작에 민감한 측정과 충전 이력 | 하나의 전압 이상 |
| 균열·팽창 | 기계적 지그 조건과 구조 진단 | 조건이 없는 셀 두께 변화 |

첫 열화 모델은 관측량으로 식별할 수 있는 최소한의 모델이어야 한다. 상세 기작망이 결정되지 않는 상황에서는 반경험식이 검증 영역 안에서 더 정직한 예측기가 될 수 있다. 이런 선택을 명시하고 적합 계수를 직접 측정한 소재 물성처럼 표현하지 않는다.

### 실험 설계
달력 시간, 전하 처리량, 사이클 수, 휴지, 평균 SOC, DOD, 전류율, 온도 이력을 보존한다. 등가 완전 사이클을 방전 Ah/기준 용량으로 정의할 수도 있고, 충전·방전 절댓값 처리량/(기준 용량의 두 배)로 정의할 수도 있다. 두 정의를 섞지 않는다. 용량·저항 비교에는 조건을 맞춘 기준 성능 시험이 필요하다.

NASA·Sandia/Archive·CALCE·Oxford·ILCC·MATR는 서로 다른 이력과 관측량을 제공한다. 이를 보편적인 전기차 열화 곡선으로 그대로 합칠 수 없다. 행 수보다 셀 식별, 프로토콜, 중도 종료 여부, 불확실성의 정합성이 중요하다. [S07-S12, S23, S25]

### 누출과 불확실성
적합 전에 셀·배치·원 연구 전체를 기준으로 분할한다. 초기 수명 예측에 같은 셀의 말기 이력이 들어가면 안 된다. 보간 용량과 dQ/dV 같은 파생 특징은 처리 이력을 보존한다. 미러·재포장 자료는 원 연구와 개체 ID로 중복을 제거한다.

매개변수·사후 분포의 상관관계, 관측하지 못한 상태의 불확실성, 대안적 모델 형식을 보고한다. 전압 잔차가 작다는 이유만으로 SEI 두께나 석출 리튬 질량이 검증되지는 않는다. 최적화가 조정한 항을 곧바로 보편적인 원인으로 해석하지 않는다.

### 근거 출처

- [S04: PyBaMM coupled degradation](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/coupled-degradation.html)
- [S07: CALCE battery data](https://calce.umd.edu/battery-data)
- [S08: NASA Li-ion aging catalog](https://data.nasa.gov/dataset/li-ion-battery-aging-datasets)
- [S09: NASA PCoE data repository](https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/)
- [S11: Battery Archive study summaries](https://batteryarchive.org/study_summaries.html)
- [S23: Iowa State ILCC dataset landing](https://doi.org/10.25380/iastate.22582234)
- [S25: Severson/Attia original data-processing repository](https://github.com/rdbraatz/data-driven-prediction-of-battery-cycle-life-before-capacity-degradation)
- [S28: PyBOP paper](https://arxiv.org/abs/2412.15859)

조사 기준일: 2026-09-10. 설계 선택은 제안이며 시뮬레이터의 실측 성능을 의미하지 않는다.


---

<a id="chapter-07"></a>

## 07. 역학·미세구조·파손

### 결합 수준
정상 작동에서는 조성 의존 팽창, 열 변형, 지그 압력, 접촉 변화를 측정 근거가 있을 때만 전기·열 모델과 연결한다. 가역 팽창과 비가역 팽윤, 가스 축적, 크리프를 분리한다. 강한 클램프 아래의 두께 센서는 자유 팽창을 측정하지 않는다. 구성 모델에는 소재·지그 형상, 강성, 초기 하중, 온도, 하중 이력이 필요하다.

Michigan 팽창 연구는 역학 관측과 사이클 조건을 연결하는 유망한 후보지만 이번에는 원본 파일에 접근하지 못했다. 따라서 파일·라이선스·지그 정보를 확보했다고 주장하지 않는다. NLR 미세구조 자료에는 동의 절차가 있고, 사용자를 대신해 동의하지 않았다. [S11, S15, S16, S24]

### 재구성 불확실성
원시 영상, 분할 결과, 수치 생성된 상 라벨은 다른 산출물로 저장한다. 복셀 간격과 물리 좌표를 보존한다. 픽셀 자체에는 길이 단위가 없다. 기공률·입자 표면적·수송 텐서를 구하기 전에 분할 민감도를 평가한다. 바인더 상을 수치 생성했다면 그 구조에서 계산한 수송 결과는 재구성 의존 계산값이지 직접 실측값이 아니다.

### 파손 자료는 별도 연구 가지이다
ORNL/Sandia의 Mendeley v2에는 역학·전압·온도 이력과 시편 정보가 있고, NLR 파손 데이터뱅크에는 열량 분배와 질량 결과가 있다. 전자는 변형과 연결된 파손 응답, 후자는 전체 에너지와 분출 결과를 제약한다. 이들을 모았다고 완전한 다상 화학 분해·가스 유동 모델이 만들어지는 것은 아니다. [S13, S14]

추가로 필요한 것은 화학계·SOC별 반응망, 반응 엔탈피·속도, 압력·벤트 경계, 유효 단락 저항, 케이스·지그 역학, 열 차단재, 모듈 전파 관측이다. 값은 특정 시험 영역과 시편에 연결해야 한다. 하나의 개시 온도나 총 발열량은 보편적인 소재 상수가 아니다.

이번 패키지는 **데이터 해석과 모델 검증 계획만** 제공한다. 배터리 파괴 시험, 고장 유발, 보호 장치 변경, 안전 인증을 수행하는 지침은 넣지 않는다. 향후 안전 주장은 적절한 전문 시험·경계조건·관련 규제 절차가 필요하며 적합된 시뮬레이터가 이를 대체하지 않는다.

### 근거 출처

- [S11: Battery Archive study summaries](https://batteryarchive.org/study_summaries.html)
- [S13: Mechanically induced thermal runaway v2](https://data.mendeley.com/datasets/sn2kv34r4h/2)
- [S14: Battery Failure Databank](https://www.nlr.gov/transportation/battery-failure)
- [S15: Battery Microstructures Library](https://www.nlr.gov/transportation/microstructure)
- [S16: Microstructure library agreement](https://www.nlr.gov/transportation/microstructure-library-disclaimer)
- [S24: Michigan expansion dataset landing](https://deepblue.lib.umich.edu/data/concern/data_sets/5d86p0488)

조사 기준일: 2026-09-10. 설계 선택은 제안이며 시뮬레이터의 실측 성능을 의미하지 않는다.


---

<a id="chapter-08"></a>

## 08. 팩·BMS·차량 경계조건

### 팩은 단순 배율이 아니다
이상적인 $V_{pack}\approx N_sV_{cell}$, $Q_{pack}\approx N_pQ_{cell}$ 관계는 동일하고 균형 잡힌 셀의 점검식이지 완전한 팩 모델이 아니다. 실제 전기 연결망에는 접속 저항과 셀별 상태를 포함한 노드·분기 제약이 필요하다. 병렬 셀의 전류는 같지 않을 수 있고, 직렬 셀은 같은 스트링 전류를 받아도 한계 전압·온도에 서로 다른 시점에 도달한다.

노드·엣지 토폴로지, 셀 그룹, 용접·버스바·컨택터·퓨즈 저항, 초기 SOC·SOH 분포, 배치 상관, 냉각 접촉, 센서 위치를 확보한다. 전기망과 열망은 따로 보존한다. 사진이나 정격 팩 에너지 하나로 OEM 토폴로지를 추정하지 않는다. Battery Archive의 모듈 연구는 중간 스케일의 근거지만 완성차 팩 모델을 확정하지는 않는다. [S11]

### 제어와 관측
밸런싱 전류·임계값, 충전기 전력·전류·전압 한계, 온도별 충전 수용성, 센서 지연·양자화·드리프트, BMS 필터를 기록한다. 모델의 실제 상태와 표시 SOC·SOH를 구분한다. 냉각·전류 제한의 폐루프 제어는 셀 특성을 가릴 수 있다. 관측 전류는 독립적인 자극만이 아니라 제어기의 반응이기도 하다.

### 속도를 향후 배터리 부하로 바꾸기
EPA 자료는 **시간에 따른 규정 속도**이다. 동봉 US06은 배터리 전류 기록이 아니다. 추후 부하 모델에는 차량 질량·회전 관성, 경사, 구름 저항, 공기 밀도, 항력·전면적, 구동계 효율, 보조 부하가 필요하다. 개략적인 휠 힘은 다음과 같다.

$$F=m_{eq}\dot v+mgC_{rr}\cos\gamma+mg\sin\gamma+\tfrac12\rho_{air}C_dAv^2.$$

$P_{wheel}=Fv$에 구동·회생 효율과 제어 한계를 명시한다. 전류는 $P=VI$를 통해 팩 전압과 한계에 의존하고, 전압도 상태·전류에 의존하므로 고정 환산 계수가 아니다. 공조·냉각 펌프·배터리 예열·충전 부대 손실도 별도 항목이다.

1초 간격 프로파일의 미분에는 보간·필터 규칙이 필요하다. 회생 에너지는 제동 요구나 충전 수용 한계를 넘을 수 없다. 이번에는 배터리 부하·주행거리·팩 에너지 예측값을 합성하지 않았다. [S17, S18]

### 공개 정보의 공백
공개 셀 자료와 표준 속도 곡선은 투명한 가상 시나리오를 정의할 수 있게 해 줄 뿐, 제조사와 동등한 팩 성능을 주장하게 해 주지는 않는다. 가정한 차량·팩·제어 값을 모두 표시하고 실제 차량 계측과 분리한다.

### 근거 출처

- [S03: PyBaMM thermal models](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/thermal-models.html)
- [S11: Battery Archive study summaries](https://batteryarchive.org/study_summaries.html)
- [S17: EPA dynamometer schedules](https://www.epa.gov/vehicle-and-fuel-emissions-testing/dynamometer-drive-schedules)
- [S18: EPA US06 numeric schedule](https://www.epa.gov/system/files/other-files/2025-03/us06col.txt)
- [S20: BLAST battery lifetime models](https://www.nlr.gov/transportation/blast)

조사 기준일: 2026-09-10. 설계 선택은 제안이며 시뮬레이터의 실측 성능을 의미하지 않는다.


---

<a id="chapter-09"></a>

## 09. 데이터셋 선정과 정합 전략

### 권장 수집 조합
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

### 같은 셀인지 확인하는 관문
자료를 결합하기 전에 제조사·변형 모델, 양·음극 조성, 형식, 용량, 전극 형상, 화성·배치, 전해질, 온도, SOC 정의, 전류율, 차단 전압, 휴지, 열화 상태를 비교한다. 불일치 자료가 무조건 쓸모없다는 뜻은 아니다. 직접 보정 근거에서 전이 사전 정보·외부 비교로 역할이 달라진다는 뜻이며 이를 명시한다.

“같은 화학계”보다 “같은 상용 셀”이, 그보다 “같은 배치·시편”이 강한 정합 조건이다. NMC811 확산, NMC111 OCP, 다른 셀의 열전도율, 무관한 열화식을 조립한 뒤 실측 가상 셀이라고 표현하지 않는다. 그런 전이가 필요하면 가정과 불확실성 모델을 문서화한다.

### 제안하는 세 가지 증거 묶음
**A: 원본 기준 재현.** 동봉 About:Energy 두 세트와 원래의 검증 파일이다. 매개변수 의미와 원본 기준 재현에 적합하지만 독립 검증의 증거는 아니다.

**B: 정합된 전기화학·열 셀.** 하나의 상용 변형 모델에 대한 온도별 펄스·충방전·엔트로피/열량·형상이다. 이 전체 묶음은 아직 확보하지 못했다.

**C: 열화·모듈 현실성.** 달력·사이클 조건 행렬, 팽창·EIS 진단, 전기·열·제어 정보가 명시된 모듈을 더한다. 현재 데이터가 아니라 후속 증거 목표이다.

파일 사본이 아니라 원래의 개체를 센다. 보정 자료, 원문 기준 곡선, 진정한 홀드아웃을 서로 다른 라벨로 보존한다.

### 근거 출처

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


---

<a id="chapter-10"></a>

## 10. 수집·크롤링 범위와 재사용 조건

### 실제 수행 내용
공개 1차 페이지를 검색·열람하고 메타데이터를 기록했다. 연결된 GitHub 읽기 API로 About:Energy 매개변수 텍스트와 파일 트리·blob 식별자를 확인했다. BPX JSON 두 개는 전사·재직렬화했고, EPA 일반 텍스트의 US06 수치는 CSV로 전사했다. 직접 원본 바이트 다운로드는 성공하지 못했다. 열화·CT·스프레드시트 전체 아카이브는 다운로드하지 않았다. `metadata/retrieval_audit.json`에 기록했다.

동봉 파일은 “원시 다운로드”가 아니라 **내용 스냅샷**이다. 로컬 SHA-256은 확보 이후 파일의 무결성을 확인하지만, 받지 못한 원본과 전사 결과가 같다는 것을 입증하지는 못한다. 수집기는 불변 Git blob SHA-1과 로컬 SHA-256, 바이트 크기, 후속 수집 시각을 분리한다. Git tree SHA를 커밋 SHA로 표시하지 않는다.

### 권리 구분
| 출처 | 확인·미해결 조건 | 저장소 처리 |
|---|---|---|
| About:Energy | CC BY-SA 4.0 확인 | 스냅샷·변형 자료의 저작자 표시·동일조건변경허락 유지 |
| LG HG2 / Mendeley 역학 파손 v2 | 페이지의 CC BY 4.0 확인 | 이번에는 메타데이터만, 추후 수집도 출처 유지 |
| NASA 열화 | 카탈로그에 라이선스 미지정 | 일괄 퍼블릭 도메인으로 추정하지 않음 |
| CALCE / Battery Archive | 출처 표시·연구별 허가 | 파일별 검토, 요청은 보내지 않음 |
| NLR 미세구조 | 별도 동의 조건 | 사용자가 직접 검토·동의, 체적 데이터 미동봉 |
| NLR 파손 스프레드시트 | 파일의 조건·readme 미확인 | 스프레드시트 미동봉 |
| EPA | 과학·교육 목적 사용 안내, 상업 이용 일괄 보장 아님 | 연구용 속도 스냅샷과 별도 고지, 상업 이용 재검토 |
| BPX 규격 | 공개 변경 안내·연락처 입력 폼 | 폼 미제출, 규격 PDF 미동봉 |

원본 코드의 라이선스가 제3자 데이터를 재허가하지 않는다. 출처를 삭제하거나 CC BY-SA 변형 자료를 MIT로 바꾸면 안 된다. 메타데이터나 다운로드 링크의 공개만으로 재배포 권리가 확정되지 않는다. 이 문서는 운영상 권리 점검이며 특정 관할의 법률 의견은 아니다. [S01, S06-S19]

### 재현 가능한 수집
동봉 수집기는 범용 웹 스파이더가 아니라 **허용 목록 기반**이다. 기본은 드라이런이다. 실행·라이선스 확인을 명시하면 검증한 About:Energy Git blob 16개만 요청하고 크기·Git 해시를 확인한 뒤 로컬 SHA-256과 수집 보고서를 남긴다. 저장소·권리·URL·경로 가정의 변경을 거부하고 제한된 재시도와 동일 호스트 리다이렉트만 허용한다. 성공한 실시간 네트워크 다운로드 경로는 이번에 입증하지 못했다.

큰 자료는 공식 API·내보내기·사용자가 직접 동의한 경로를 사용한다. 버전·DOI, 제공된 서버 해시, 약관, 파일 목록, 수집 기록을 보존한다. 로그에는 API 키나 개인 연락처를 넣지 않는다. 숨은 엔드포인트·인증·CAPTCHA를 우회하거나 약관에 묵시적으로 대리 동의하지 않는다.

### 근거 출처

- [S01: About:Energy BPX parameterisation repository](https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation)
- [S06: BPX official standard download and change notes](https://bpxstandard.com/bpx-standard/)
- [S07: CALCE battery data](https://calce.umd.edu/battery-data)
- [S08: NASA Li-ion aging catalog](https://data.nasa.gov/dataset/li-ion-battery-aging-datasets)
- [S10: LG HG2 dataset v3](https://data.mendeley.com/datasets/cp3473x7xv/3)
- [S12: Battery Archive access page](https://www.batteryarchive.org/)
- [S13: Mechanically induced thermal runaway v2](https://data.mendeley.com/datasets/sn2kv34r4h/2)
- [S14: Battery Failure Databank](https://www.nlr.gov/transportation/battery-failure)
- [S16: Microstructure library agreement](https://www.nlr.gov/transportation/microstructure-library-disclaimer)
- [S19: EPA disclaimers and copyright status](https://www.epa.gov/web-policies-and-procedures/epa-disclaimers)
- [S25: Severson/Attia original data-processing repository](https://github.com/rdbraatz/data-driven-prediction-of-battery-cycle-life-before-capacity-degradation)

조사 기준일: 2026-09-10. 설계 선택은 제안이며 시뮬레이터의 실측 성능을 의미하지 않는다.


---

<a id="chapter-11"></a>

## 11. 데이터 계약과 정규화

### 세 층을 유지한다
`data/curated`에는 과학적 의미를 가능한 한 보존하되 직렬화가 달라졌음을 명시한 수집 스냅샷을 둔다. `data/raw`는 추후 검증된 원본 바이트 전용이며 Git에서 제외한다. `data/derived`에는 변환 이력이 있는 정규화 레코드와 적합식 표본을 둔다. 정제하면서 수집 스냅샷을 덮어쓰지 않는다.

스키마는 셀 식별, 매개변수 근거, 정규화 기준 곡선, 일반 물리량 근거를 기술한다. JSON Schema는 구조를 검사할 뿐 과학적 진실이나 BPX 적합성을 증명하지 않는다. 미확인 개체 ID·불확실성·실측 온도는 null이다. 데이터셋 내부 논리 ID를 제조사 시리얼 번호처럼 표시하지 않는다.

### 표준화 규칙
| 물리량 | 저장 규칙 | 함께 보존할 것 |
|---|---|---|
| 시간 | 초, 세그먼트 안에서 단조 증가 | 원래 시간표·초기화 이력 |
| 전류 | 방전 양수 | 원시 전류·원문 부호 정의 |
| 온도 | K | 원래 섭씨·설정값·센서 의미 |
| 용량 | 기준 프로토콜이 있는 Ah | 쿨롱 사용 여부·차단·전류율·온도 |
| 전위 | 셀 V 또는 명시한 V vs Li/Li+ | 전극·기준 전극 구분 |
| EIS | 실수·허수 ohm과 Hz | 원래 부호·여기·휴지 조건 |
| 속도 | m/s | 원래 mph·규정/실측 구분 |

이번 변환은 $T_K=T_C+273.15$, $1\,Ah=3600\,C$, $1\,mph=0.44704\,m/s$를 사용한다. About:Energy 내장 방전 전류는 음수이므로 원시값을 남긴 채 부호를 반전한다. 파일에서 많이 나타나는 부호만 보고 원문의 정의를 추측하지 않는다.

### 처리 규칙
비유한 수와 열 길이 불일치를 거부한다. 시간 순서는 세그먼트별로 검사한다. 사이클마다 시계가 초기화되는 것은 반드시 손상 데이터라는 뜻은 아니다. 재표본화 전에 중복과 처리 정책을 보존한다. 충전·휴지·방전 불연속, 결측 블록, 시험 종료 경계를 가로질러 보간하지 않는다. 보간은 새로운 독립 관측을 만들거나 실질 샘플링 주파수를 높여 주지 않는다.

OCP 식은 Python `eval`이 아니라 작은 AST 허용 목록으로 해석한다. 동봉 스크립트는 원본 전극의 화학양론비 구간 안에서만 표본화하고 전해질 함수를 임의의 농도 구간으로 외삽하지 않는다. 문법·영역 검사가 통과해도 과학적으로 적합하지 않을 수 있으므로 모델 검증과 구분한다.

CSV는 UTF-8과 ASCII 기계용 키를 사용한다. 영문·한국어 설명은 카탈로그와 문서에 둔다. 물리 단위는 열 이름이나 전용 필드에 기록하며, 표시 언어 때문에 저장된 숫자가 달라지면 안 된다.

### 근거 출처

- [S01: About:Energy BPX parameterisation repository](https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation)
- [S05: PyBaMM parameterisation](https://docs.pybamm.org/en/latest/source/examples/notebooks/parameterization/parameterization.html)
- [S07: CALCE battery data](https://calce.umd.edu/battery-data)
- [S08: NASA Li-ion aging catalog](https://data.nasa.gov/dataset/li-ion-battery-aging-datasets)
- [S17: EPA dynamometer schedules](https://www.epa.gov/vehicle-and-fuel-emissions-testing/dynamometer-drive-schedules)
- [S18: EPA US06 numeric schedule](https://www.epa.gov/system/files/other-files/2025-03/us06col.txt)

조사 기준일: 2026-09-10. 설계 선택은 제안이며 시뮬레이터의 실측 성능을 의미하지 않는다.


---

<a id="chapter-12"></a>

## 12. 검증과 불확실성 계획

### 증거 수준을 구분한다
데이터 QA, 수치 검증, 보정, 원본 기준 재현, 독립 검증, 배포 적합성은 서로 다르다. 이 저장소에서 수행하는 것은 로컬 데이터·패키지 QA와 결정적인 변환뿐이다. 솔버 결과, 보정된 모델 정확도, 안전 인증, 차량 적용 적합성은 제공하지 않는다.

원문 NMC 곡선은 매개변수 개발 자료와 겹칠 수 있으며 통계적 독립성이 확인되지 않았다. 따라서 깨끗한 홀드아웃이 아니라 **원문 기준 곡선**으로 표시한다. 재현 이후에는 다른 프로토콜·셀/배치·온도를 별도로 남겨 독립 평가한다.

### 제안하는 검증 단계
1. 단위·부호·식별자·스키마·입력 완전성·출처를 검사한다.
2. 추후 솔버에서는 초기 일관성, 리튬·전하·에너지 수지, 한계, 격자·시간·허용 오차 수렴을 검사한다.
3. 무관한 계수를 임의 조절하지 않고 원문 곡선을 재현한다.
4. 매개변수를 고정하고 홀드아웃 전류·SOC·온도를 평가한다.
5. 해당 관측과 경계조건이 확보된 후 열화·역학·팩 검증을 추가한다.

### 달성값이 아닌 공학적 목표 초안
| 관측량 | 정의된 영역에서의 시작 목표 예 | 필수 조건 |
|---|---|---|
| 셀 전압 | RMSE 20 mV 이하 | 최대 오차·편향·SOC/율/온도별 결과·계측 불확실성 |
| 기준 방전 용량 | 상대 오차 2% 이하 | 전류·온도·차단·기준 정의 동일 |
| 표면 실측 온도 | RMSE 2 K 이하 | 실제 센서 시계열과 경계조건, 챔버 설정값 제외 |
| 열화 예측 | 홀드아웃 점의 오차·구간 포함률 사전 정의 | 셀 단위 재표본화·중도 종료·예측 기간 정의 |
| 팩 거동 | 셀 한계·분기 전류 오차 사전 정의 | 토폴로지·제어·센서 매핑 확보 |

이 숫자는 검토를 시작하기 위한 제안이지 표준·논문 성능·보증이 아니다. 운용 영역과 계측 불확실성에 맞춰 수정해야 한다. 이번 패키지에서는 이 목표를 시험하거나 달성하지 않았다.

### 불확실성 보고
계측 오차, 매개변수 불확실성, 제조 분산, 보간·처리 오차, 모델 불일치, 영역 밖 사용을 구분한다. 근거가 있으면 공분산·사후 분포 앙상블을 사용하고 상관된 매개변수를 독립 분포로 취급하지 않는다. 인접 샘플 대신 셀 단위로 부트스트랩하여 유효 표본 수를 부풀리지 않는다.

전체 평균뿐 아니라 실패 조건과 잔차 구조도 보고한다. 그럴듯한 단자 곡선은 관측하지 않은 내부 농도·석출·SEI 상태를 검증하지 않는다. 향후 사용자 화면에는 근거 영역과 신뢰 상태를 표시하고 무음 외삽을 피해야 한다.

### 근거 출처

- [S01: About:Energy BPX parameterisation repository](https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation)
- [S05: PyBaMM parameterisation](https://docs.pybamm.org/en/latest/source/examples/notebooks/parameterization/parameterization.html)
- [S07: CALCE battery data](https://calce.umd.edu/battery-data)
- [S10: LG HG2 dataset v3](https://data.mendeley.com/datasets/cp3473x7xv/3)
- [S25: Severson/Attia original data-processing repository](https://github.com/rdbraatz/data-driven-prediction-of-battery-cycle-life-before-capacity-degradation)
- [S28: PyBOP paper](https://arxiv.org/abs/2412.15859)

조사 기준일: 2026-09-10. 설계 선택은 제안이며 시뮬레이터의 실측 성능을 의미하지 않는다.


---

<a id="chapter-13"></a>

## 13. 공백 분석과 후속 연구 관문

### 현실성을 크게 제한하는 미확보 증거
현재 기준에는 같은 셀의 독립적인 열 검증, 넓은 온도 구간의 특성화, 기작별 열화 계수, 시편·배치 추적성, OEM 팩 토폴로지·제어·냉각 정보가 부족하다. LFP 상전이·히스테리시스와 복합 전극 역학에도 기본 교환 파일을 넘는 증거가 필요하다. 이는 명시적인 데이터 공백이지 물리 기반 모델링 자체가 불가능하다는 뜻은 아니다.

| 관문 | 다음 단계 전 필요한 증거 | 중단·재검토 조건 |
|---|---|---|
| G0 출처 | 원본 대조·권리·단위·식별자 | 출처 미해결·전사 불일치 은폐 |
| G1 셀 기준 | 같은 셀의 정의·원문 곡선 재현 | 임의 계수 보상으로 모델 오차 숨김 |
| G2 전기화학·열 | 여러 온도·독립적인 실측 열 관측 | 추정 물성·설정값을 실측 검증처럼 사용 |
| G3 열화 | 달력·사이클 행렬·기작 관련 진단 | 용량만으로 모든 기작 적합 |
| G4 모듈·팩 | 전기·열 그래프·제어·동기화 관측 | 셀 배율만으로 OEM 팩 정확도 주장 |
| G5 일반화 | 홀드아웃·불확실성·영역 밖 평가 | 누출·미러 중복·무조건 외삽 |

### 즉시 수행할 수집 대기 목록
고정한 About:Energy blob 16개를 받고 의미적 동등성을 비교한다. CSV 전체 헤더와 시험 조건을 먼저 읽은 뒤 어댑터를 만든다. 공식 내보내기에서 HG2와 역학 파손 자료의 파일 목록을 확보한다. 선택한 CALCE·NASA 권리를 검토하고 필요한 Battery Archive 연구만 요청한다. 차단된 Oxford·ILCC·Michigan 원문에 재접근하여 라이선스와 버전을 확인한다. 어느 작업도 이미 끝난 것으로 표시하지 않는다.

다음으로 가치 있는 수집이 가장 큰 아카이브라는 보장은 없다. 잘 특성화되고 같은 셀로 연결된 열량·펄스·OCV 자료가 수천 개의 비정합 수명 곡선보다 더 많은 불확실성을 줄일 수 있다. 이 우선순위는 후속 민감도·식별 가능성 분석으로 재검토한다.

### 후속 연구의 산출물
고정된 셀 식별 문서, 버전별 매개변수 출처 맵, 보정·홀드아웃 프로토콜 표, 미관측량 장부, 불확실성 예산, 권리 검토된 원시 데이터 목록을 만든다. 이들이 검토된 뒤 별도의 구현 작업에서 과학 커널이나 UI를 작성한다.

이 저장소는 일정이나 성능을 보장하지 않는다. 필요한 증거 관문과 현재 열린 항목을 기록한다. 향후 자료는 초기 스냅샷을 보존한 채 날짜가 있는 개정으로 추가하며, 원본을 몰래 교체하거나 실패한 검증 범위를 숨기지 않는다.

### 근거 출처

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


---

<a id="chapter-14"></a>

## 14. 확보한 수치 데이터 점검

### 확보 목록
| 산출물 | 내용 | 근거 상태 |
|---|---|---|
| LFP BPX 스냅샷 | 2 Ah 흑연/LFP 18650, BPX 0.1 | 원문 전사·재직렬화, 원본 바이트 미확보 |
| NMC BPX 스냅샷 | 12.5 Ah 흑연/NMC111 파우치, BPX 0.1 | 동일 방식, 원문 기준 곡선 포함 |
| 매개변수 내보내기 | 두 세트의 104항목 | 조건·적합식·추정값 포함, 독립 실측 104개가 아님 |
| NMC 곡선 | C/20 76점과 1C 38점 | 원문 내장 기준값, 사이클러 원시 CSV 전체 아님 |
| OCP 표본 | 전극당 101점, 합계 404점 | 원본 화학양론비 구간에서 공개 함수를 계산 |
| US06 속도 | 0~600초, 601점 | EPA 일반 텍스트를 전사한 규정 입력 |

두 세트의 기준 온도는 298.15 K이다. LFP의 2.0/3.65 V, NMC의 2.7/4.2 V는 **해당 원본 예제의 전압 한계**이지 보편적인 운용 한계가 아니다. 2 Ah와 12.5 Ah도 원본의 정격 용량이다. 열 물성은 일부 추정이고 엔트로피 입력은 문헌에 근거한다. [S01]

### 결정적 점검과 적분
NMC 1C 구간의 방전 전류 12.5 A를 3,700초 적분하면 약 **12.8472 Ah**, C/20의 0.625 A를 75,000초 적분하면 **13.0208 Ah**이다. 이는 확보한 구간의 적분이지 용량 재측정·인증이 아니다. 정격 12.5 Ah와 같아야 하는 값도 아니다. 마지막 보존 전압은 각각 약 2.9047 V와 2.8947 V로 BPX 하한보다 높다. 관측을 만들어 2.7 V까지 연장하지 않는다.

전류·전압을 사다리꼴 적분한 구간 에너지는 약 46.2534 Wh와 48.3844 Wh이다. 보존된 점 사이를 선형 보간한 결과이며 빠진 고주파 거동을 복원한 것은 아니다. 자세한 값과 가정은 `reports/numeric_audit.json`에 있다.

US06의 최대 속도는 80.3 mph이다. 규정 속도를 사다리꼴 적분한 600초 구간 거리는 약 12,887.582 m이다. 이는 **전기차 주행가능거리**, 실측 운행거리, 배터리 에너지 요구가 아니다. [S18]

### 아직 해결하지 못한 점검
원본 바이트 다운로드와 원본·스냅샷 전체 의미 대조는 성공하지 못했다. 패키지의 체크섬은 로컬 배포본 무결성만 입증한다. 일정한 298.15 K를 실측 열 응답으로 인정하지 않는다. LFP 검증 CSV 전체와 두 셀의 주행 사이클 CSV는 목록에 있으나 미수집이다. 이 산술 점검만으로 모델 정확도를 주장할 수 없다.

### 근거 출처

- [S01: About:Energy BPX parameterisation repository](https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation)
- [S18: EPA US06 numeric schedule](https://www.epa.gov/system/files/other-files/2025-03/us06col.txt)

조사 기준일: 2026-09-10. 설계 선택은 제안이며 시뮬레이터의 실측 성능을 의미하지 않는다.


---

<a id="chapter-15"></a>

## 15. BPX 의미와 버전 관리

### 구형 스냅샷과 현재 문서를 구분한다
동봉 About:Energy 예제는 **BPX 0.1**을 명시하며 2022년 12월에 매개변수화됐다. 공식 다운로드 페이지의 1.1 안내에는 SPMe, 단일 상태 히스테리시스, 복합 전극, LAM/LLI 상태, 별도 셀 상태 기술이 추가돼 있다. 공개 변경 안내만으로 동봉 구형 파일이 현재 파서와 호환된다고 확정할 수 없다. 전체 규격 다운로드에는 연락처 입력이 필요하며 해당 폼은 제출하지 않았다. [S01, S06]

의미적 마이그레이션 없이 버전 헤더만 올리지 않는다. BPX 1.1 적합성 결과는 제공하지 않는다. 저장소의 스키마 네 개는 연구 데이터용이며 공식 BPX 스키마를 재구현한 것이 아니다.

### 마이그레이션 검토 표
| 구형 객체 | 확인 사항 |
|---|---|
| `Header.BPX` | 원래 버전 유지, 대상 규격·변환 도구 버전 별도 기록 |
| 셀·초기·주변 온도 | 물성의 기준 조건과 실험·초기 상태 분리 |
| 전극 면적·병렬 전극 쌍 | 면적·층 정규화 확인, 팩 Ns/Np와 혼동 금지 |
| 반응 속도 상수 | 몰 속도·패러데이 인자·농도 정규화를 대상 반응식과 대조 |
| OCP 식·표 | 변수 정의·화학양론비 구간·보간 방식 확인 |
| 엔트로피·열 물성 | 문헌·추정 출처 유지, 실측으로 승격 금지 |
| 검증 전류 | 원문 방전 음수와 정규화 과정을 함께 보존 |
| 열화 상태 | 상태 기술과 향후 변화를 결정하는 속도 법칙 구분 |

### 버전 장부
출처 URL, blob·릴리스·DOI, 라이선스, 확보 방식, 로컬 해시, 파서 버전, 변환 스크립트 개정, 의미 변화 목록을 기록한다. About:Energy tree SHA는 tree로 기록했고 커밋 식별자를 만들어내지 않았다. 수집기는 변경 가능한 브랜치 대신 개별 blob을 고정한다.

열람한 PyBaMM `latest` 문서는 개발 빌드와 안정 버전 간 차이를 경고한다. 이번 패키지는 검증하지 않은 안정 솔버 버전을 지정하거나 PyBaMM을 설치하지 않는다. 구현 단계에서 실제 시험한 릴리스를 선택하고 매개변수·스키마 호환성 보고서를 남긴다.

첫 마이그레이션 검사는 원문 기준 프로토콜에서 값·함수 거동·초기 상태·전압/용량 스케일·전류 부호를 대조해야 한다. JSON 구문 검사만 통과한 것으로는 부족하다. 원본과 변환본을 모두 보존하여 변경 필드를 검토할 수 있게 한다.

### 근거 출처

- [S01: About:Energy BPX parameterisation repository](https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation)
- [S02: PyBaMM DFN equations](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/DFN.html)
- [S05: PyBaMM parameterisation](https://docs.pybamm.org/en/latest/source/examples/notebooks/parameterization/parameterization.html)
- [S06: BPX official standard download and change notes](https://bpxstandard.com/bpx-standard/)

조사 기준일: 2026-09-10. 설계 선택은 제안이며 시뮬레이터의 실측 성능을 의미하지 않는다.


---

<a id="chapter-16"></a>

## 16. 출처별 데이터 입력 절차

### 동봉되어 오프라인으로 실행한 부분
저장소 루트에서 `python scripts/export_curated.py`를 실행하면 BPX 스냅샷 두 개의 매개변수·내장 기준 곡선을 내보내고 OCP 함수를 제한적으로 계산하며 EPA 속도를 m/s로 바꾼다. 배터리 동역학을 적분하지는 않는다. `python scripts/fetch_sources.py`는 드라이런이며 `python scripts/compare_originals.py`는 현재 원본 파일이 없음을 보고한다.

네트워크가 가능한 환경의 수집 순서는 다음과 같다.

```bash
python scripts/fetch_sources.py
python scripts/fetch_sources.py --execute --acknowledge-cc-by-sa
python scripts/compare_originals.py
```

두 번째 명령 전에는 원본 라이선스를 읽어야 한다. 실제 다운로드 결과는 별도 날짜의 보고서로 남긴다. 과거 수집이 성공한 것처럼 준비 단계의 감사 기록을 고치지 않는다.

### 다른 자료군: 구현된 수집기가 아닌 입력 명세
**NASA MAT.** 바깥쪽 사이클 종류, 주변 온도, 시작 시간을 유지한다. 실측 전압·전류·온도, 충방전 계측 채널, 상대 시간, 용량을 추출한다. EIS 배열은 원문을 기준으로 주파수·채널 의미를 확인한다. MATLAB v7.3/HDF5와 이전 MAT는 인코딩이 다르므로 헤더를 읽고 파서를 선택한다. MATLAB 날짜 벡터를 경과 초로 착각하지 않는다. [S08, S09]

**CALCE·HG2.** 파일별 단위·부호, 온도·프로토콜 이름, 계측 범위, 시계 초기화를 확인한다. 단계별로 정규화한다. 용량이 누적·단계·사이클 기준인지 이미 가공된 값인지 구분한다. 이해하지 못한 열을 조용히 삭제하지 않는다. 이번에는 원시 파일 내용을 검사하지 못했다. [S07, S10]

**MATR.** 셀 설명·사이클 요약·사이클 내부 기록을 원래 셀 ID로 연결한다. `Qdlin`, `Tdlin`, dQ/dV는 원시 측정이 아니다. 신뢰할 수 없는 pickle을 역직렬화하지 않는다. 비실행형 수치 원본 형식이나 격리·검토한 변환 경로를 사용한다. 모델 코드 접근에는 별도 학술 라이선스 조건이 있다. [S25]

**CT·파손 스프레드시트.** 라이선스·readme, 좌표 단위, 상 라벨, 시편 ID, 유발·지그 조건, 결측 규칙을 먼저 확인한다. 회색 영상·분할 체적·수치 생성 상은 다르다. 참조한 XLSX는 열거나 파싱하지 않았으므로 정확한 시트 스키마를 확인했다고 주장하지 않는다. [S13-S16]

추후 어댑터에는 권리가 확인된 작은 시험 파일, 단위·부호 테스트, 원본·정규화 행 수 대조, 제외 정책을 먼저 마련한 뒤 전체 컬렉션을 처리한다.

### 근거 출처

- [S01: About:Energy BPX parameterisation repository](https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation)
- [S07: CALCE battery data](https://calce.umd.edu/battery-data)
- [S08: NASA Li-ion aging catalog](https://data.nasa.gov/dataset/li-ion-battery-aging-datasets)
- [S09: NASA PCoE data repository](https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/)
- [S10: LG HG2 dataset v3](https://data.mendeley.com/datasets/cp3473x7xv/3)
- [S13: Mechanically induced thermal runaway v2](https://data.mendeley.com/datasets/sn2kv34r4h/2)
- [S14: Battery Failure Databank](https://www.nlr.gov/transportation/battery-failure)
- [S15: Battery Microstructures Library](https://www.nlr.gov/transportation/microstructure)
- [S25: Severson/Attia original data-processing repository](https://github.com/rdbraatz/data-driven-prediction-of-battery-cycle-life-before-capacity-degradation)

조사 기준일: 2026-09-10. 설계 선택은 제안이며 시뮬레이터의 실측 성능을 의미하지 않는다.


---

<a id="chapter-17"></a>

## 17. 향후 과학 엔진 프로젝트에 넘길 사항

### 범위 경계
이 저장소는 연구·데이터 준비 자산이다. 인터랙티브 배터리 모델, 물리 시간 적분기, 솔버 연동, 학습된 예측기, 웹앱, 배포 파이프라인을 포함하지 않는다. 데이터 변환 스크립트가 있다는 사실이 시뮬레이터 개발 착수를 뜻하지는 않는다.

후속 개발 지시에는 목표 화학계·셀 식별, 출력 관측량, 운용 영역, 허용 오차, 실험 홀드아웃, 계산·실행 예산, 화면에서 허용할 주장 범위를 명시해야 한다. 과학 커널은 렌더링·UI와 독립적으로 시험할 수 있어야 한다.

### 입력·출력 계약 제안
실험 설명은 버전이 있는 셀 매개변수, 초기 상태, 전류·전력·전압 제어 프로토콜, 열 경계, 종료 조건, 요청 관측량을 참조한다. 명시적인 제어기 없이 서로 모순되는 제어 입력을 허용하지 않는다. 출력에는 시간, 단자 물리량, 상태 출처, 보존 잔차, 영역 위반, 솔버 설정, 불확실성을 남긴다.

각 필드는 실측 입력, 지정 경계, 적합 매개변수, 추정 사전 정보, 예측 상태 중 무엇인지 표시해야 한다. 입자·이온 애니메이션이 실제 해석 상태를 나타내지 않으면 개략도라고 표시한다. 보간·모델 생성점을 실험실 측정값처럼 제시할 수 없다.

### 구현 수락 조건
자동 입력 전에 원본·스냅샷 대조를 요구한다. 단위·부호를 강제하고 안전하지 않은 식 평가를 금지한다. 사전 정보의 출처를 유지하고 보정·시험 분할을 고정한다. 수치 수렴·보존 검사를 추가하고 실패 조건을 보고한다. 그 후에 독립 데이터와 커널 예측을 비교한다.

추후 UI가 여러 모델 수준을 제공하더라도 전환 과정에서 화학계·상 거동·열 가정·열화 정의를 조용히 바꾸면 안 된다. 화면이 연속적으로 움직이는 것이 물리적으로 동등한 모델 변환을 뜻하지는 않는다.

### 코딩 에이전트에 넘길 자료
이 보고서, 출처 목록, 필요 매개변수 목록, 수집·권리 장부, 스키마, 정확한 수집 스냅샷, QA 결과를 제공한다. 첫 작업은 새로 받은 원본으로 입력 경로를 검증하는 것이어야 하며, 빠진 과학을 그럴듯한 상수로 채우는 일이 되어서는 안 된다. 미측정값은 명시적인 사전 정보나 미해결 요구사항으로 유지한다.

사용자 계정의 저장소는 생성·수정하지 않았다. ZIP은 혼합 라이선스 고지를 유지한 상태에서 검토 후 게시할 수 있는 로컬 연구 스냅샷이다.

### 근거 출처

- [S01: About:Energy BPX parameterisation repository](https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation)
- [S02: PyBaMM DFN equations](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/DFN.html)
- [S05: PyBaMM parameterisation](https://docs.pybamm.org/en/latest/source/examples/notebooks/parameterization/parameterization.html)
- [S06: BPX official standard download and change notes](https://bpxstandard.com/bpx-standard/)

조사 기준일: 2026-09-10. 설계 선택은 제안이며 시뮬레이터의 실측 성능을 의미하지 않는다.


---

<a id="chapter-18"></a>

## 18. 출처와 접근 감사 기록

모든 확인일은 2026-09-10이다. 문서 열람·메타데이터 확보·원시 수치 다운로드는 서로 다른 상태이다.

### S01. About:Energy BPX parameterisation repository

[공식 출처](https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation)

접근: `read_via_GitHub_connector` · 권리: `CC-BY-SA-4.0`

라이선스 제목과 매개변수·파일 트리를 확인했다. 원본 바이트 다운로드는 실패했고 내용 스냅샷을 동봉했다.

### S02. PyBaMM DFN equations

[공식 출처](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/DFN.html)

접근: `read` · 권리: `reference_only`

DFN 방정식과 초기·경계조건을 열람했다. latest는 개발 문서이므로 안정 버전 설치 추천으로 해석하지 않는다.

### S03. PyBaMM thermal models

[공식 출처](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/thermal-models.html)

접근: `read` · 권리: `reference_only`

열 도메인·발열 항·접촉 저항·냉각 경계를 확인했다.

### S04. PyBaMM coupled degradation

[공식 출처](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/coupled-degradation.html)

접근: `read` · 권리: `reference_only`

결합 열화 모델 구조를 확인했다. 모든 계수가 식별 가능하다는 증거는 아니다.

### S05. PyBaMM parameterisation

[공식 출처](https://docs.pybamm.org/en/latest/source/examples/notebooks/parameterization/parameterization.html)

접근: `read` · 권리: `reference_only`

매개변수 함수와 특성화 흐름을 확인했다.

### S06. BPX official standard download and change notes

[공식 출처](https://bpxstandard.com/bpx-standard/)

접근: `read_public_page_only` · 권리: `form_gated_documents`

공개 1.1 변경 안내만 확인했다. 연락처 폼 미제출, 규격 전체 미다운로드이다.

### S07. CALCE battery data

[공식 출처](https://calce.umd.edu/battery-data)

접근: `read` · 권리: `no_blanket_license_verified`

공개 자료·출처 표시 안내를 확인했다. 선택 파일의 권리는 추가 검토가 필요하다.

### S08. NASA Li-ion aging catalog

[공식 출처](https://data.nasa.gov/dataset/li-ion-battery-aging-datasets)

접근: `read` · 권리: `license_not_specified`

열화 카탈로그가 라이선스를 미지정한다고 표시한다. 기여자 자료까지 일괄 퍼블릭 도메인으로 추정하지 않는다.

### S09. NASA PCoE data repository

[공식 출처](https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/)

접근: `read` · 권리: `per_dataset_review`

Battery·Randomized Battery의 공식 ZIP 링크를 확인했으나 다운로드하지 않았다.

### S10. LG HG2 dataset v3

[공식 출처](https://data.mendeley.com/datasets/cp3473x7xv/3)

접근: `read_metadata` · 권리: `CC-BY-4.0`

DOI 10.17632/cp3473x7xv.3, 2020-03-05 v3, CC BY 4.0을 확인했다. 파일 목록·수치 원본은 미확보이다.

### S11. Battery Archive study summaries

[공식 출처](https://batteryarchive.org/study_summaries.html)

접근: `read` · 권리: `institution_specific`

원 데이터 보관·연계 기관의 연구 설명을 확인했다. 원본 파일·권리는 별도로 확보해야 한다.

### S12. Battery Archive access page

[공식 출처](https://www.batteryarchive.org/)

접근: `read` · 권리: `permission_request`

전체 CSV는 이메일 요청 경로가 있다. 이메일을 보내지 않았다.

### S13. Mechanically induced thermal runaway v2

[공식 출처](https://data.mendeley.com/datasets/sn2kv34r4h/2)

접근: `read_metadata` · 권리: `CC-BY-4.0`

DOI 10.17632/sn2kv34r4h.2, 2024-09-24 v2, CC BY 4.0을 확인했다. 수치 원본은 미수집이다.

### S14. Battery Failure Databank

[공식 출처](https://www.nlr.gov/transportation/battery-failure)

접근: `read_metadata` · 권리: `spreadsheet_terms_not_verified`

스프레드시트 개정은 2024년 2월이다. 파일 전체·readme·이용 조건을 검사하지 않았다.

### S15. Battery Microstructures Library

[공식 출처](https://www.nlr.gov/transportation/microstructure)

접근: `read_metadata` · 권리: `custom_agreement`

재구성 구조에서 탄소·바인더 영역은 수치 생성이라고 명시한다.

### S16. Microstructure library agreement

[공식 출처](https://www.nlr.gov/transportation/microstructure-library-disclaimer)

접근: `read` · 권리: `custom_agreement_not_accepted`

고지 유지·기여 표시 등의 조건을 읽었으나 동의하지 않았다.

### S17. EPA dynamometer schedules

[공식 출처](https://www.epa.gov/vehicle-and-fuel-emissions-testing/dynamometer-drive-schedules)

접근: `read` · 권리: `scientific_educational_use_policy`

속도 프로파일 목록을 확인했다. 배터리 전류 실측 자료가 아니다.

### S18. EPA US06 numeric schedule

[공식 출처](https://www.epa.gov/system/files/other-files/2025-03/us06col.txt)

접근: `numeric_text_captured` · 권리: `see_S19`

0~600초 601행을 전사했다. 원본 바이트 파일이 아니라 내용 스냅샷이다.

### S19. EPA disclaimers and copyright status

[공식 출처](https://www.epa.gov/web-policies-and-procedures/epa-disclaimers)

접근: `read` · 권리: `custom_site_policy`

과학·교육 목적 배포 안내와 상업 이용 보호 가능성을 확인했다.

### S20. BLAST battery lifetime models

[공식 출처](https://www.nlr.gov/transportation/blast)

접근: `read` · 권리: `code_and_data_licenses_separate`

반경험적 수명 모델의 공식 설명을 확인했다. 모델 계수는 원시 관측이 아니다.

### S21. Materials Project API guide

[공식 출처](https://docs.materialsproject.org/downloading-data/using-the-api)

접근: `read` · 권리: `API_terms_review`

공식 API 안내를 확인했다. 소재 계산은 제조 셀의 직접 실측값이 아니다.

### S22. Oxford Battery Degradation Dataset 1

[공식 출처](https://ora.ox.ac.uk/objects/uuid:03ba4b01-cfed-46d3-9b1a-7d4a7bdf6fac)

접근: `access_blocked` · 권리: `not_reverified`

Oxford 공식 원문 접근이 차단됐다. 연구 범위는 S11과 교차 참조했다.

### S23. Iowa State ILCC dataset landing

[공식 출처](https://doi.org/10.25380/iastate.22582234)

접근: `access_blocked` · 권리: `not_reverified`

S11에 연결된 기관 DOI이다. 원시 파일에 접근하지 못했다.

### S24. Michigan expansion dataset landing

[공식 출처](https://deepblue.lib.umich.edu/data/concern/data_sets/5d86p0488)

접근: `access_blocked` · 권리: `not_reverified`

Michigan 원시 파일에 접근하지 못했다. 지그·권리·셀 정합성은 미해결이다.

### S25. Severson/Attia original data-processing repository

[공식 출처](https://github.com/rdbraatz/data-driven-prediction-of-battery-cycle-life-before-capacity-degradation)

접근: `read_via_GitHub_connector` · 권리: `data_license_not_established`

원저자 README는 접근 가능한 처리 코드와 별도 학술 라이선스의 모델 코드를 구분한다.

### S26. MATR Experimental Data Platform

[공식 출처](https://data.matr.io/1/)

접근: `javascript_shell_only` · 권리: `not_reverified`

자바스크립트 페이지 껍데기만 반환됐다. 숨은 API나 수치 파일을 가져오지 않았다.

### S27. BatteryML paper

[공식 출처](https://arxiv.org/abs/2310.14714)

접근: `search_metadata_reviewed` · 권리: `reference_only`

배터리 처리·벤치마크 논문의 검색 메타데이터를 검토했다. 개별 원본 권리와 분할 규칙은 유지해야 한다.

### S28. PyBOP paper

[공식 출처](https://arxiv.org/abs/2412.15859)

접근: `search_metadata_reviewed` · 권리: `reference_only`

매개변수 식별 프레임워크 논문의 검색 메타데이터를 검토했다. 도구가 관측 비식별성을 없애지는 않는다.



---

<a id="chapter-19"></a>

## 19. 기술 용어집

| 용어 | 한국어 | 해석 |
|---|---|---|
| SOC | 충전 상태 | 기준 시험에 따른 사용 가능 전하 좌표이며 전극 화학양론비와 다르다. |
| SOH | 건강 상태 | 용량·저항 등 정의와 기준 조건을 명시한다. |
| OCP / OCV | 평형 전극 전위 / 개방 회로 전압 | 전극·기준 전극·휴지·측정 조건을 표시한다. |
| DFN / P2D | 다공성 전극 전기화학 모델 | 전극 두께와 대표 입자 차원은 실제 3D 형상과 다르다. |
| SPM / SPMe | 단일 입자 모델 / 전해질 포함 | 축약 가정과 운용 영역이 있는 모델이다. |
| ECM | 등가회로 모델 | 단자 거동의 근사이며 내부 화학을 직접 풀지 않는다. |
| SEI | 고체 전해질 계면층 | 계면층과 관련 기작이며 모든 용량 감소와 같은 뜻이 아니다. |
| LLI / LAM | 리튬 재고 / 활물질 손실 | 보조 증거가 필요한 서로 다른 내부 상태이다. |
| EIS | 전기화학 임피던스 분광 | 주파수·여기·휴지·SOC/온도·복소 부호를 기록한다. |
| GITT / PITT | 정전류 / 정전위 간헐 적정 | 확산 추정은 모델과 실험 가정에 의존한다. |
| HPPC | 하이브리드 펄스 출력 특성화 | 펄스 길이는 저항·응답 정의의 일부이다. |
| DOD / EFC | 방전 깊이 / 등가 완전 사이클 | SOC·전하 처리량의 분모와 계수 방식을 명시한다. |
| C-rate | 기준 용량 대비 전류율 | 기준 Ah와 실제 A를 함께 기록한다. |
| BPX | 배터리 매개변수 교환 형식 | 버전이 있는 매개변수 의미 체계이며 자동 모델 검증이 아니다. |
| Semantic capture | 내용 스냅샷 | 원본 파일과 바이트가 동일하다는 뜻이 아니다. |
| Ground truth | 기준 관측 | BMS 추정·합성 데이터·적합 곡선과 같은 뜻이 아니다. |
| Identifiability | 식별 가능성 | 작은 잔차만으로 유일한 물리 매개변수가 식별되지는 않는다. |
| Model discrepancy | 모델 구조 불일치 | 매개변수 불확실성만으로 모두 숨기지 않는다. |

### 근거 출처

- [S01: About:Energy BPX parameterisation repository](https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation)
- [S02: PyBaMM DFN equations](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/DFN.html)
- [S05: PyBaMM parameterisation](https://docs.pybamm.org/en/latest/source/examples/notebooks/parameterization/parameterization.html)
- [S06: BPX official standard download and change notes](https://bpxstandard.com/bpx-standard/)
- [S07: CALCE battery data](https://calce.umd.edu/battery-data)
- [S08: NASA Li-ion aging catalog](https://data.nasa.gov/dataset/li-ion-battery-aging-datasets)

조사 기준일: 2026-09-10. 설계 선택은 제안이며 시뮬레이터의 실측 성능을 의미하지 않는다.
