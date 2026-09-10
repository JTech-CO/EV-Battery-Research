# 팩·BMS·차량 경계조건

[English](../en/08_PACK_BMS_AND_VEHICLE.md) · [README](../../README-KR.md)

## 팩은 단순 배율이 아니다
이상적인 $V_{pack}\approx N_sV_{cell}$, $Q_{pack}\approx N_pQ_{cell}$ 관계는 동일하고 균형 잡힌 셀의 점검식이지 완전한 팩 모델이 아니다. 실제 전기 연결망에는 접속 저항과 셀별 상태를 포함한 노드·분기 제약이 필요하다. 병렬 셀의 전류는 같지 않을 수 있고, 직렬 셀은 같은 스트링 전류를 받아도 한계 전압·온도에 서로 다른 시점에 도달한다.

노드·엣지 토폴로지, 셀 그룹, 용접·버스바·컨택터·퓨즈 저항, 초기 SOC·SOH 분포, 배치 상관, 냉각 접촉, 센서 위치를 확보한다. 전기망과 열망은 따로 보존한다. 사진이나 정격 팩 에너지 하나로 OEM 토폴로지를 추정하지 않는다. Battery Archive의 모듈 연구는 중간 스케일의 근거지만 완성차 팩 모델을 확정하지는 않는다. [S11]

## 제어와 관측
밸런싱 전류·임계값, 충전기 전력·전류·전압 한계, 온도별 충전 수용성, 센서 지연·양자화·드리프트, BMS 필터를 기록한다. 모델의 실제 상태와 표시 SOC·SOH를 구분한다. 냉각·전류 제한의 폐루프 제어는 셀 특성을 가릴 수 있다. 관측 전류는 독립적인 자극만이 아니라 제어기의 반응이기도 하다.

## 속도를 향후 배터리 부하로 바꾸기
EPA 자료는 **시간에 따른 규정 속도**이다. 동봉 US06은 배터리 전류 기록이 아니다. 추후 부하 모델에는 차량 질량·회전 관성, 경사, 구름 저항, 공기 밀도, 항력·전면적, 구동계 효율, 보조 부하가 필요하다. 개략적인 휠 힘은 다음과 같다.

$$F=m_{eq}\dot v+mgC_{rr}\cos\gamma+mg\sin\gamma+\tfrac12\rho_{air}C_dAv^2.$$

$P_{wheel}=Fv$에 구동·회생 효율과 제어 한계를 명시한다. 전류는 $P=VI$를 통해 팩 전압과 한계에 의존하고, 전압도 상태·전류에 의존하므로 고정 환산 계수가 아니다. 공조·냉각 펌프·배터리 예열·충전 부대 손실도 별도 항목이다.

1초 간격 프로파일의 미분에는 보간·필터 규칙이 필요하다. 회생 에너지는 제동 요구나 충전 수용 한계를 넘을 수 없다. 이번에는 배터리 부하·주행거리·팩 에너지 예측값을 합성하지 않았다. [S17, S18]

## 공개 정보의 공백
공개 셀 자료와 표준 속도 곡선은 투명한 가상 시나리오를 정의할 수 있게 해 줄 뿐, 제조사와 동등한 팩 성능을 주장하게 해 주지는 않는다. 가정한 차량·팩·제어 값을 모두 표시하고 실제 차량 계측과 분리한다.

## 근거 출처

- [S03: PyBaMM thermal models](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/thermal-models.html)
- [S11: Battery Archive study summaries](https://batteryarchive.org/study_summaries.html)
- [S17: EPA dynamometer schedules](https://www.epa.gov/vehicle-and-fuel-emissions-testing/dynamometer-drive-schedules)
- [S18: EPA US06 numeric schedule](https://www.epa.gov/system/files/other-files/2025-03/us06col.txt)
- [S20: BLAST battery lifetime models](https://www.nlr.gov/transportation/blast)

조사 기준일: 2026-09-10. 설계 선택은 제안이며 시뮬레이터의 실측 성능을 의미하지 않는다.
