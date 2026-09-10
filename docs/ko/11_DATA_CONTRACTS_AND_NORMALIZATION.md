# 데이터 계약과 정규화

[English](../en/11_DATA_CONTRACTS_AND_NORMALIZATION.md) · [README](../../README-KR.md)

## 세 층을 유지한다
`data/curated`에는 과학적 의미를 가능한 한 보존하되 직렬화가 달라졌음을 명시한 수집 스냅샷을 둔다. `data/raw`는 추후 검증된 원본 바이트 전용이며 Git에서 제외한다. `data/derived`에는 변환 이력이 있는 정규화 레코드와 적합식 표본을 둔다. 정제하면서 수집 스냅샷을 덮어쓰지 않는다.

스키마는 셀 식별, 매개변수 근거, 정규화 기준 곡선, 일반 물리량 근거를 기술한다. JSON Schema는 구조를 검사할 뿐 과학적 진실이나 BPX 적합성을 증명하지 않는다. 미확인 개체 ID·불확실성·실측 온도는 null이다. 데이터셋 내부 논리 ID를 제조사 시리얼 번호처럼 표시하지 않는다.

## 표준화 규칙
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

## 처리 규칙
비유한 수와 열 길이 불일치를 거부한다. 시간 순서는 세그먼트별로 검사한다. 사이클마다 시계가 초기화되는 것은 반드시 손상 데이터라는 뜻은 아니다. 재표본화 전에 중복과 처리 정책을 보존한다. 충전·휴지·방전 불연속, 결측 블록, 시험 종료 경계를 가로질러 보간하지 않는다. 보간은 새로운 독립 관측을 만들거나 실질 샘플링 주파수를 높여 주지 않는다.

OCP 식은 Python `eval`이 아니라 작은 AST 허용 목록으로 해석한다. 동봉 스크립트는 원본 전극의 화학양론비 구간 안에서만 표본화하고 전해질 함수를 임의의 농도 구간으로 외삽하지 않는다. 문법·영역 검사가 통과해도 과학적으로 적합하지 않을 수 있으므로 모델 검증과 구분한다.

CSV는 UTF-8과 ASCII 기계용 키를 사용한다. 영문·한국어 설명은 카탈로그와 문서에 둔다. 물리 단위는 열 이름이나 전용 필드에 기록하며, 표시 언어 때문에 저장된 숫자가 달라지면 안 된다.

## 근거 출처

- [S01: About:Energy BPX parameterisation repository](https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation)
- [S05: PyBaMM parameterisation](https://docs.pybamm.org/en/latest/source/examples/notebooks/parameterization/parameterization.html)
- [S07: CALCE battery data](https://calce.umd.edu/battery-data)
- [S08: NASA Li-ion aging catalog](https://data.nasa.gov/dataset/li-ion-battery-aging-datasets)
- [S17: EPA dynamometer schedules](https://www.epa.gov/vehicle-and-fuel-emissions-testing/dynamometer-drive-schedules)
- [S18: EPA US06 numeric schedule](https://www.epa.gov/system/files/other-files/2025-03/us06col.txt)

조사 기준일: 2026-09-10. 설계 선택은 제안이며 시뮬레이터의 실측 성능을 의미하지 않는다.
