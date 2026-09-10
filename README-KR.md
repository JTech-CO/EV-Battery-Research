# EV Battery Research

[English](README.md) · [한국어 통합 보고서](RESEARCH_REPORT-KR.md) · [영문 통합 보고서](RESEARCH_REPORT.md)

**사실적인 전기차 배터리 시뮬레이터의 후속 구축을 위한 공개 데이터 조사·연구·증거 준비 패키지이다. 시뮬레이터와 웹앱은 포함하지 않는다.**

조사 기준: **2026-09-10** · 버전: **1.0.0** · 혼합 라이선스: [제3자 고지](THIRD_PARTY_NOTICES-KR.md).

## 먼저 읽을 문서
무관한 화학·열·열화 값을 섞기보다 하나의 일관된 셀 매개변수와 연결된 관측에서 시작한다. [연구 요약](docs/ko/00_RESEARCH_SUMMARY.md), [데이터셋 선정](docs/ko/09_DATASET_SELECTION.md), [실제 확보 자료 점검](docs/ko/14_CAPTURED_DATA_AUDIT.md)을 먼저 확인한다.

## 실제 동봉 내용
| 항목 | 수량 | 이 수량이 뜻하지 않는 것 |
|---|---:|---|
| 연구 문서 | 영문 20장 + 한국어 20장 | 완성된 과학 엔진 |
| 자료 카드 | 언어별 23개 | 실험 데이터셋 23개 전체 다운로드 |
| 출처 기록 | 28개 | 모든 원시 파일 접근 성공 |
| 필요 데이터 | 영·한 설명 139항목 | 확보한 목표 셀 실측값 139개 |
| BPX 내용 스냅샷 | 구형 0.1 두 개, 매개변수 104항목 | 원본 바이트 대조 완료·모든 값 실측 |
| NMC 원문 기준 곡선 | 114점 | 독립 홀드아웃·사이클러 원시 전체 |
| EPA US06 | 규정 속도 601점 | 배터리 전류 실측 |
| OCP 적합식 표 | 계산된 404점 | 새로운 실험 관측 |
| 수집 매니페스트 | blob 16개, 원본 예상 1,740,269바이트 | 이번에 다운로드 완료한 원시 파일 |
| 데이터 스키마 | JSON Schema 4개 | 공식 BPX 적합성 검증 |

준비 환경에서 직접 바이트 다운로드가 실패했다. BPX JSON 두 개와 속도 CSV는 **원문 텍스트를 수동 전사·재직렬화한 내용 스냅샷**이며 별도 출처 기록이 있다. 전체 사이클·열화 아카이브, 원본 검증 CSV, CT 체적, 파손 스프레드시트는 미수집이다. 공개 데이터를 모두 복제한 자료나 OEM 디지털 트윈이 아니라 연구용 시작 코퍼스이다.

## 폴더 구성
```text
README.md / README-KR.md           진입 문서
RESEARCH_REPORT.md / -KR.md        통합 읽기 버전
docs/en/ 와 docs/ko/               상세 연구 문서
catalog/                          자료 카드와 139항목 요구 목록
data/curated/                      출처가 있는 원문 내용 스냅샷
data/derived/                      정규화 레코드와 적합식 표
metadata/                         출처·권리·수집·체크섬
schemas/                          연구 데이터 계약
scripts/ 와 tests/                데이터 준비와 오프라인 QA
reports/                          실제 QA·산술 점검 결과
```

## 로컬 데이터 점검
Python 3.10 이상이 필요하다. 변환·단위 테스트는 표준 라이브러리를 사용하고, 전체 JSON Schema 검사는 `jsonschema`를 사용한다.

```bash
python -m pip install -r requirements.txt
python scripts/validate_package.py --verify-checksums
python scripts/export_curated.py
python scripts/audit_numeric.py
python -m unittest discover -s tests -v
python scripts/validate_package.py
```

배포본은 Python 3.13.5와 jsonschema 4.26.0에서 점검했다. 로컬 QA는 모델 정확도 시험이 아니다. [한국어 QA 보고서](reports/QA_REPORT-KR.md) · [검증 JSON](reports/package_validation.json).

## 추후 원본 수집
```bash
python scripts/fetch_sources.py
# 원본 라이선스를 읽고 네트워크가 가능한 환경에서 실행:
python scripts/fetch_sources.py --execute --acknowledge-cc-by-sa
python scripts/compare_originals.py
```

첫 명령은 네트워크 요청을 하지 않는다. 실시간 다운로드 성공 경로는 이번에 입증하지 못했다. 다른 포털은 개별 카드의 정식 절차를 따른다. 범용 스크래퍼·동의 우회 기능은 없다. 새 원본은 Git에서 제외한 `data/raw/`에 저장된다.

## 연구 문서
| 번호 | 문서 |
|---|---|
| 00 | [연구 요약과 핵심 판단](docs/ko/00_RESEARCH_SUMMARY.md) |
| 01 | [작동 원리와 화학·물리 반응](docs/ko/01_PHYSICS_AND_CHEMISTRY.md) |
| 02 | [셀 구조와 소재 식별](docs/ko/02_CELL_STRUCTURE_AND_MATERIALS.md) |
| 03 | [모델 계층과 필요한 증거](docs/ko/03_MODEL_HIERARCHY.md) |
| 04 | [전기화학 특성화와 매개변수 활용](docs/ko/04_ELECTROCHEMICAL_DATA.md) |
| 05 | [열 거동과 냉각 경계조건](docs/ko/05_THERMAL_AND_COOLING.md) |
| 06 | [열화 기작과 식별 가능성](docs/ko/06_DEGRADATION_AND_IDENTIFIABILITY.md) |
| 07 | [역학·미세구조·파손](docs/ko/07_MECHANICS_MICROSTRUCTURE_AND_FAILURE.md) |
| 08 | [팩·BMS·차량 경계조건](docs/ko/08_PACK_BMS_AND_VEHICLE.md) |
| 09 | [데이터셋 선정과 정합 전략](docs/ko/09_DATASET_SELECTION.md) |
| 10 | [수집·크롤링 범위와 재사용 조건](docs/ko/10_ACQUISITION_AND_RIGHTS.md) |
| 11 | [데이터 계약과 정규화](docs/ko/11_DATA_CONTRACTS_AND_NORMALIZATION.md) |
| 12 | [검증과 불확실성 계획](docs/ko/12_VALIDATION_AND_UNCERTAINTY.md) |
| 13 | [공백 분석과 후속 연구 관문](docs/ko/13_GAPS_AND_RESEARCH_ROADMAP.md) |
| 14 | [확보한 수치 데이터 점검](docs/ko/14_CAPTURED_DATA_AUDIT.md) |
| 15 | [BPX 의미와 버전 관리](docs/ko/15_BPX_AND_VERSIONING.md) |
| 16 | [출처별 데이터 입력 절차](docs/ko/16_INGESTION_RECIPES.md) |
| 17 | [향후 과학 엔진 프로젝트에 넘길 사항](docs/ko/17_FUTURE_ENGINE_HANDOFF.md) |
| 18 | [출처와 접근 감사 기록](docs/ko/18_SOURCES_AND_ACCESS_AUDIT.md) |
| 19 | [기술 용어집](docs/ko/19_GLOSSARY.md) |

## 라이선스와 게시
새 코드·테스트는 MIT, 자체 연구 설명은 CC BY 4.0이다. About:Energy 스냅샷·변형 자료는 **CC BY-SA 4.0**을 유지한다. EPA의 과학·교육 사용에는 별도 고지가 있고 **상업 이용을 일괄 보장하지 않는다**. 전체 저장소를 MIT라고 표시하거나 데이터 출처를 삭제하지 않는다. 게시 전 [LICENSE](LICENSE), [범위별 라이선스 맵](metadata/license_map.json)을 확인한다.

이 작업은 GitHub 저장소를 생성·수정·게시하지 않았다. 원 자료 제공자의 보증·후원을 뜻하지 않는다. 연구 스냅샷과 함께 원 데이터 제공자·원 논문을 인용한다.
