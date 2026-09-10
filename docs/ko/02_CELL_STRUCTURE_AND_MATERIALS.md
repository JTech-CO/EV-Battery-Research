# 셀 구조와 소재 식별

[English](../en/02_CELL_STRUCTURE_AND_MATERIALS.md) · [README](../../README-KR.md)

## 형상 자체가 물리 모델의 일부이다
활물질 입자, 다공성 전극·분리막·집전체 층, 권취·적층 셀, 모듈·팩을 최소 네 스케일로 나눠야 한다. 두께 방향 1차원 전극 모델과 입자 반경 방향 확산을 결합해도 실제 권취 셀을 3차원으로 복원한 것은 아니다. 전기화학 층을 균질화하더라도 탭 위치, 집전체 저항, 이방성 열전달이 중요할 수 있다. [S02, S03]

| 스케일 | 필요한 데이터 | 잘못된 대체 |
|---|---|---|
| 입자 | 입도 분포·상 조성·확산·표면적·팽창 | 모든 소재에 같은 구형 반경 적용 |
| 전극 | 두께·로딩·활물질/바인더/기공 분율·수송 효율 | 기공률만으로 수송 결정 |
| 셀 | 층수·면적·집전체·탭·케이스·질량·냉각 접촉 | 외형 직경만으로 내부 활성 면적 결정 |
| 모듈·팩 | 전기 연결망·접촉·열 네트워크·구속 | 셀 출력에 Ns·Np만 곱하기 |

균일한 구형 입자 모델에서 $a_s=3\epsilon_s/R$이다. 이 식으로 복원한 활성 체적 분율은 **가정에 의존한 파생값**이지 별도의 독립 실측값이 아니다. 굴곡도 인자, 경로 길이 비, 수송 효율 역시 동일한 정의가 아니므로 수치 옆에 원문의 정의를 보존한다.

## 소재 이름만으로 묶지 않는다
NMC111, 고니켈 NMC, NCA, 혼합 양극은 같은 매개변수 식별자가 아니다. 흑연·실리콘 혼합 음극에는 상별 기여가 필요하다. 연구용 LFP 18650 자료가 대형 자동차 각형 LFP 셀을 식별해 주는 것도 아니다. 정확한 변형 모델·배치·화성·저장 이력·개체 ID를 기록하고 빠진 값은 null로 남긴다.

About:Energy 파우치 예제는 전극 면적과 전극 쌍 34개를 지정한다. 이는 외부 셀 34개가 아니다. 팩 병렬 개수로 착각하면 면적·용량·발열 스케일링이 잘못된다. [S01]

## 미세구조 수집
CT 복셀 크기, 원시·분할 여부, 상 라벨, 시야, 해상도, 캘린더링, 재구성 조건을 보존한다. NLR 자료는 탄소·바인더 영역을 수치적으로 생성한다고 명시한다. 모든 분할 영역을 직접 계측한 구조로 표기해서는 안 된다. 분할 방법과 미해상 기공이 형상 지표에 주는 영향을 평가한 뒤 유효 수송 물성에 연결한다. [S15]

필요 항목은 `catalog/parameter_requirements.csv`에 있다. 이 목록에는 이번 패키지에 없는 값도 포함된다. OEM 도면·용접 접촉 분포·소재 구성 시험의 부재는 연구 공백으로 남겨야 하며, 출처 없는 상수로 채우면 안 된다.

## 근거 출처

- [S01: About:Energy BPX parameterisation repository](https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation)
- [S02: PyBaMM DFN equations](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/DFN.html)
- [S03: PyBaMM thermal models](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/thermal-models.html)
- [S15: Battery Microstructures Library](https://www.nlr.gov/transportation/microstructure)
- [S16: Microstructure library agreement](https://www.nlr.gov/transportation/microstructure-library-disclaimer)

조사 기준일: 2026-09-10. 설계 선택은 제안이며 시뮬레이터의 실측 성능을 의미하지 않는다.
