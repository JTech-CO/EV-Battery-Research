# 수집·크롤링 범위와 재사용 조건

[English](../en/10_ACQUISITION_AND_RIGHTS.md) · [README](../../README-KR.md)

## 실제 수행 내용
공개 1차 페이지를 검색·열람하고 메타데이터를 기록했다. 연결된 GitHub 읽기 API로 About:Energy 매개변수 텍스트와 파일 트리·blob 식별자를 확인했다. BPX JSON 두 개는 전사·재직렬화했고, EPA 일반 텍스트의 US06 수치는 CSV로 전사했다. 직접 원본 바이트 다운로드는 성공하지 못했다. 열화·CT·스프레드시트 전체 아카이브는 다운로드하지 않았다. `metadata/retrieval_audit.json`에 기록했다.

동봉 파일은 “원시 다운로드”가 아니라 **내용 스냅샷**이다. 로컬 SHA-256은 확보 이후 파일의 무결성을 확인하지만, 받지 못한 원본과 전사 결과가 같다는 것을 입증하지는 못한다. 수집기는 불변 Git blob SHA-1과 로컬 SHA-256, 바이트 크기, 후속 수집 시각을 분리한다. Git tree SHA를 커밋 SHA로 표시하지 않는다.

## 권리 구분
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

## 재현 가능한 수집
동봉 수집기는 범용 웹 스파이더가 아니라 **허용 목록 기반**이다. 기본은 드라이런이다. 실행·라이선스 확인을 명시하면 검증한 About:Energy Git blob 16개만 요청하고 크기·Git 해시를 확인한 뒤 로컬 SHA-256과 수집 보고서를 남긴다. 저장소·권리·URL·경로 가정의 변경을 거부하고 제한된 재시도와 동일 호스트 리다이렉트만 허용한다. 성공한 실시간 네트워크 다운로드 경로는 이번에 입증하지 못했다.

큰 자료는 공식 API·내보내기·사용자가 직접 동의한 경로를 사용한다. 버전·DOI, 제공된 서버 해시, 약관, 파일 목록, 수집 기록을 보존한다. 로그에는 API 키나 개인 연락처를 넣지 않는다. 숨은 엔드포인트·인증·CAPTCHA를 우회하거나 약관에 묵시적으로 대리 동의하지 않는다.

## 근거 출처

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
