# 출처별 데이터 입력 절차

[English](../en/16_INGESTION_RECIPES.md) · [README](../../README-KR.md)

## 동봉되어 오프라인으로 실행한 부분
저장소 루트에서 `python scripts/export_curated.py`를 실행하면 BPX 스냅샷 두 개의 매개변수·내장 기준 곡선을 내보내고 OCP 함수를 제한적으로 계산하며 EPA 속도를 m/s로 바꾼다. 배터리 동역학을 적분하지는 않는다. `python scripts/fetch_sources.py`는 드라이런이며 `python scripts/compare_originals.py`는 현재 원본 파일이 없음을 보고한다.

네트워크가 가능한 환경의 수집 순서는 다음과 같다.

```bash
python scripts/fetch_sources.py
python scripts/fetch_sources.py --execute --acknowledge-cc-by-sa
python scripts/compare_originals.py
```

두 번째 명령 전에는 원본 라이선스를 읽어야 한다. 실제 다운로드 결과는 별도 날짜의 보고서로 남긴다. 과거 수집이 성공한 것처럼 준비 단계의 감사 기록을 고치지 않는다.

## 다른 자료군: 구현된 수집기가 아닌 입력 명세
**NASA MAT.** 바깥쪽 사이클 종류, 주변 온도, 시작 시간을 유지한다. 실측 전압·전류·온도, 충방전 계측 채널, 상대 시간, 용량을 추출한다. EIS 배열은 원문을 기준으로 주파수·채널 의미를 확인한다. MATLAB v7.3/HDF5와 이전 MAT는 인코딩이 다르므로 헤더를 읽고 파서를 선택한다. MATLAB 날짜 벡터를 경과 초로 착각하지 않는다. [S08, S09]

**CALCE·HG2.** 파일별 단위·부호, 온도·프로토콜 이름, 계측 범위, 시계 초기화를 확인한다. 단계별로 정규화한다. 용량이 누적·단계·사이클 기준인지 이미 가공된 값인지 구분한다. 이해하지 못한 열을 조용히 삭제하지 않는다. 이번에는 원시 파일 내용을 검사하지 못했다. [S07, S10]

**MATR.** 셀 설명·사이클 요약·사이클 내부 기록을 원래 셀 ID로 연결한다. `Qdlin`, `Tdlin`, dQ/dV는 원시 측정이 아니다. 신뢰할 수 없는 pickle을 역직렬화하지 않는다. 비실행형 수치 원본 형식이나 격리·검토한 변환 경로를 사용한다. 모델 코드 접근에는 별도 학술 라이선스 조건이 있다. [S25]

**CT·파손 스프레드시트.** 라이선스·readme, 좌표 단위, 상 라벨, 시편 ID, 유발·지그 조건, 결측 규칙을 먼저 확인한다. 회색 영상·분할 체적·수치 생성 상은 다르다. 참조한 XLSX는 열거나 파싱하지 않았으므로 정확한 시트 스키마를 확인했다고 주장하지 않는다. [S13-S16]

추후 어댑터에는 권리가 확인된 작은 시험 파일, 단위·부호 테스트, 원본·정규화 행 수 대조, 제외 정책을 먼저 마련한 뒤 전체 컬렉션을 처리한다.

## 근거 출처

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
