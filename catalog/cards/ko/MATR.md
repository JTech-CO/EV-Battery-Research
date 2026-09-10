# MATR / Severson-Attia cycle-life data

[English](../en/MATR.md) | [카탈로그](../../resources.json)

**ID:** `MATR` · **우선순위:** P1 · **유형:** `experimental_dataset`

## 확인한 범위
MAT 구조체·Python 사전 형식, 셀 설명·사이클 요약·사이클 내부 시계열로 구성된다.

## 권장 활용
초기 수명 예측에서 셀·배치 홀드아웃을 적용하고 Qdlin·dQ/dV의 파생 이력을 보존한다.

초기 사이클에서 수명을 추정하는 연구에 유용하다. 원저자 저장소에서 데이터 처리 코드와 별도 학술 라이선스의 모델 코드를 구분하므로 권리도 따로 확인해야 한다.

## 금지할 일반화
별도 학술 모델 코드 라이선스를 데이터 라이선스로 대체하거나 같은 셀의 인접 사이클을 분할하지 않는다.

## 수집·권리 상태
상태: `metadata_only`. 권리: `data_license_not_reverified`. 원본 바이트 파일 다운로드: **미완료**. 내용 스냅샷은 별도 provenance를 확인하며 원본 바이트와 동일하다고 주장하지 않는다.

## 다음 수집 작업
MATR는 이번에 자바스크립트 껍데기만 확인됐다. 공식 내보내기·라이선스를 확보하고 비신뢰 pickle 역직렬화를 피한다.

## 출처
- [S25: Severson/Attia original data-processing repository](https://github.com/rdbraatz/data-driven-prediction-of-battery-cycle-life-before-capacity-degradation)
- [S26: MATR Experimental Data Platform](https://data.matr.io/1/)

확인일: 2026-09-10. 우선순위는 공학적 판단이며 측정한 품질 점수가 아니다.
