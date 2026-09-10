# 역학·미세구조·파손

[English](../en/07_MECHANICS_MICROSTRUCTURE_AND_FAILURE.md) · [README](../../README-KR.md)

## 결합 수준
정상 작동에서는 조성 의존 팽창, 열 변형, 지그 압력, 접촉 변화를 측정 근거가 있을 때만 전기·열 모델과 연결한다. 가역 팽창과 비가역 팽윤, 가스 축적, 크리프를 분리한다. 강한 클램프 아래의 두께 센서는 자유 팽창을 측정하지 않는다. 구성 모델에는 소재·지그 형상, 강성, 초기 하중, 온도, 하중 이력이 필요하다.

Michigan 팽창 연구는 역학 관측과 사이클 조건을 연결하는 유망한 후보지만 이번에는 원본 파일에 접근하지 못했다. 따라서 파일·라이선스·지그 정보를 확보했다고 주장하지 않는다. NLR 미세구조 자료에는 동의 절차가 있고, 사용자를 대신해 동의하지 않았다. [S11, S15, S16, S24]

## 재구성 불확실성
원시 영상, 분할 결과, 수치 생성된 상 라벨은 다른 산출물로 저장한다. 복셀 간격과 물리 좌표를 보존한다. 픽셀 자체에는 길이 단위가 없다. 기공률·입자 표면적·수송 텐서를 구하기 전에 분할 민감도를 평가한다. 바인더 상을 수치 생성했다면 그 구조에서 계산한 수송 결과는 재구성 의존 계산값이지 직접 실측값이 아니다.

## 파손 자료는 별도 연구 가지이다
ORNL/Sandia의 Mendeley v2에는 역학·전압·온도 이력과 시편 정보가 있고, NLR 파손 데이터뱅크에는 열량 분배와 질량 결과가 있다. 전자는 변형과 연결된 파손 응답, 후자는 전체 에너지와 분출 결과를 제약한다. 이들을 모았다고 완전한 다상 화학 분해·가스 유동 모델이 만들어지는 것은 아니다. [S13, S14]

추가로 필요한 것은 화학계·SOC별 반응망, 반응 엔탈피·속도, 압력·벤트 경계, 유효 단락 저항, 케이스·지그 역학, 열 차단재, 모듈 전파 관측이다. 값은 특정 시험 영역과 시편에 연결해야 한다. 하나의 개시 온도나 총 발열량은 보편적인 소재 상수가 아니다.

이번 패키지는 **데이터 해석과 모델 검증 계획만** 제공한다. 배터리 파괴 시험, 고장 유발, 보호 장치 변경, 안전 인증을 수행하는 지침은 넣지 않는다. 향후 안전 주장은 적절한 전문 시험·경계조건·관련 규제 절차가 필요하며 적합된 시뮬레이터가 이를 대체하지 않는다.

## 근거 출처

- [S11: Battery Archive study summaries](https://batteryarchive.org/study_summaries.html)
- [S13: Mechanically induced thermal runaway v2](https://data.mendeley.com/datasets/sn2kv34r4h/2)
- [S14: Battery Failure Databank](https://www.nlr.gov/transportation/battery-failure)
- [S15: Battery Microstructures Library](https://www.nlr.gov/transportation/microstructure)
- [S16: Microstructure library agreement](https://www.nlr.gov/transportation/microstructure-library-disclaimer)
- [S24: Michigan expansion dataset landing](https://deepblue.lib.umich.edu/data/concern/data_sets/5d86p0488)

조사 기준일: 2026-09-10. 설계 선택은 제안이며 시뮬레이터의 실측 성능을 의미하지 않는다.
