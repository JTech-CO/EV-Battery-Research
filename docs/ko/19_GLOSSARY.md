# 기술 용어집

[English](../en/19_GLOSSARY.md) · [README](../../README-KR.md)

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

## 근거 출처

- [S01: About:Energy BPX parameterisation repository](https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation)
- [S02: PyBaMM DFN equations](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/DFN.html)
- [S05: PyBaMM parameterisation](https://docs.pybamm.org/en/latest/source/examples/notebooks/parameterization/parameterization.html)
- [S06: BPX official standard download and change notes](https://bpxstandard.com/bpx-standard/)
- [S07: CALCE battery data](https://calce.umd.edu/battery-data)
- [S08: NASA Li-ion aging catalog](https://data.nasa.gov/dataset/li-ion-battery-aging-datasets)

조사 기준일: 2026-09-10. 설계 선택은 제안이며 시뮬레이터의 실측 성능을 의미하지 않는다.
