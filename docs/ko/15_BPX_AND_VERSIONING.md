# BPX 의미와 버전 관리

[English](../en/15_BPX_AND_VERSIONING.md) · [README](../../README-KR.md)

## 구형 스냅샷과 현재 문서를 구분한다
동봉 About:Energy 예제는 **BPX 0.1**을 명시하며 2022년 12월에 매개변수화됐다. 공식 다운로드 페이지의 1.1 안내에는 SPMe, 단일 상태 히스테리시스, 복합 전극, LAM/LLI 상태, 별도 셀 상태 기술이 추가돼 있다. 공개 변경 안내만으로 동봉 구형 파일이 현재 파서와 호환된다고 확정할 수 없다. 전체 규격 다운로드에는 연락처 입력이 필요하며 해당 폼은 제출하지 않았다. [S01, S06]

의미적 마이그레이션 없이 버전 헤더만 올리지 않는다. BPX 1.1 적합성 결과는 제공하지 않는다. 저장소의 스키마 네 개는 연구 데이터용이며 공식 BPX 스키마를 재구현한 것이 아니다.

## 마이그레이션 검토 표
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

## 버전 장부
출처 URL, blob·릴리스·DOI, 라이선스, 확보 방식, 로컬 해시, 파서 버전, 변환 스크립트 개정, 의미 변화 목록을 기록한다. About:Energy tree SHA는 tree로 기록했고 커밋 식별자를 만들어내지 않았다. 수집기는 변경 가능한 브랜치 대신 개별 blob을 고정한다.

열람한 PyBaMM `latest` 문서는 개발 빌드와 안정 버전 간 차이를 경고한다. 이번 패키지는 검증하지 않은 안정 솔버 버전을 지정하거나 PyBaMM을 설치하지 않는다. 구현 단계에서 실제 시험한 릴리스를 선택하고 매개변수·스키마 호환성 보고서를 남긴다.

첫 마이그레이션 검사는 원문 기준 프로토콜에서 값·함수 거동·초기 상태·전압/용량 스케일·전류 부호를 대조해야 한다. JSON 구문 검사만 통과한 것으로는 부족하다. 원본과 변환본을 모두 보존하여 변경 필드를 검토할 수 있게 한다.

## 근거 출처

- [S01: About:Energy BPX parameterisation repository](https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation)
- [S02: PyBaMM DFN equations](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/DFN.html)
- [S05: PyBaMM parameterisation](https://docs.pybamm.org/en/latest/source/examples/notebooks/parameterization/parameterization.html)
- [S06: BPX official standard download and change notes](https://bpxstandard.com/bpx-standard/)

조사 기준일: 2026-09-10. 설계 선택은 제안이며 시뮬레이터의 실측 성능을 의미하지 않는다.
