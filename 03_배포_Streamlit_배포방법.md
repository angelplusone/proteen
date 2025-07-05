# Proteen 노벨 프로젝트 - Streamlit 배포 방법

## 생성 파일
- app.py: Streamlit 앱 메인 파일 (HTML, CSS, JavaScript 포함)
- requirements.txt: 필요한 Python 패키지 목록

## 로컬 실행 방법
1. 터미널에서 cursor 폴더로 이동
2. `pip install -r requirements.txt` 실행
3. `streamlit run app.py` 실행
4. 브라우저에서 http://localhost:8501 접속

## Streamlit Cloud 배포 방법
1. GitHub에 프로젝트 업로드
2. https://share.streamlit.io/ 접속
3. GitHub 계정 연결
4. 저장소 선택 후 배포

## 주요 특징
- HTML, CSS, JavaScript를 Streamlit components.html로 임베드
- 다국어 지원 (한국어/영어/스웨덴어)
- 네비게이션 및 홈 버튼 기능 유지
- 반응형 레이아웃 지원

---

> 다음 단계: 각 섹션별 상세 콘텐츠 추가 및 K-Name Maker 기능 구현 예정 