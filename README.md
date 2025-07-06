# 🏆 Proteen(프로틴) 노벨 프로젝트

<div align="center">

![Proteen Logo](https://img.shields.io/badge/Proteen-Nobel%20Project-blue?style=for-the-badge&logo=trophy)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.0-7952B3?style=for-the-badge&logo=bootstrap)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28.1-FF4B4B?style=for-the-badge&logo=streamlit)

**Coding을 사랑하는 십대 정보영재들의 글로벌 도전!**

[🌐 Live Demo](https://proteen-nobel.streamlit.app) | [📖 프로젝트 소개](#프로젝트-소개) | [👥 팀 소개](#팀-소개)

</div>

---

## 📋 목차

- [프로젝트 소개](#프로젝트-소개)
- [주요 기능](#주요-기능)
- [기술 스택](#기술-스택)
- [설치 및 실행](#설치-및-실행)
- [배포 방법](#배포-방법)
- [팀 소개](#팀-소개)
- [프로젝트 구조](#프로젝트-구조)
- [기여하기](#기여하기)
- [라이선스](#라이선스)

---

## 🎯 프로젝트 소개

**Proteen(프로틴)**은 중학교 1학년 정보영재 4명과 교사 1명으로 구성된 팀이 진행하는 혁신적인 노벨 프로젝트입니다. 

### 🌍 프로젝트 비전
한국에 대한 글로벌 관심이 높아지는 시대적 흐름에 맞춰, **K-Name Maker**라는 독창적인 서비스를 통해 한글의 세계화를 실현하고자 합니다.

### 🎨 핵심 아이디어
사람들이 처음 만날 때 가장 먼저 묻는 것은 **"이름"**입니다. 외국어를 배울 때 가장 먼저 하고 싶어하는 것도 자신의 이름을 그 나라 언어로 표현하는 것입니다. 

우리는 이 자연스러운 욕구를 활용하여, 외국인들이 자신의 이름을 한글로 변환하고 스티커로 받아갈 수 있는 **즉석 서비스**를 개발했습니다.

---

## ✨ 주요 기능

### 🌐 K-Name Maker
- **실시간 이름 변환**: 외국 이름을 한글로 즉시 변환
- **스티커 출력**: 변환된 이름을 스티커로 즉석 출력
- **발음 가이드**: 정확한 한글 발음 제공
- **다국어 지원**: 한국어, 영어, 스웨덴어

### 🗺️ 글로벌 탐방
- **스웨덴 탐방**: 노벨상 수상자 행적, 스톡홀름 노벨 박물관
- **영국 탐방**: 런던 과학 박물관, 대학 연구소 방문
- **현지 체험**: 현지인 대상 K-Name Maker 서비스 제공

### 📊 데이터 분석
- **설문 조사**: 한글 발음 난이도, 흥미도, 유사도 측정
- **결과 시각화**: 수집된 데이터의 그래프 분석
- **개선 방향**: 프로젝트 보완점 도출

---

## 🛠️ 기술 스택

### Frontend
- **HTML5** - 시맨틱 마크업
- **CSS3** - 현대적인 스타일링
- **Bootstrap 5.3.0** - 반응형 UI 프레임워크
- **Bootstrap Icons** - 아이콘 라이브러리
- **AOS Animation** - 스크롤 애니메이션

### Backend & Deployment
- **Python 3.8+** - 메인 프로그래밍 언어
- **Streamlit 1.28.1** - 웹 애플리케이션 프레임워크
- **GitHub** - 버전 관리 및 코드 호스팅
- **Streamlit Cloud** - 클라우드 배포 플랫폼

### Libraries & Tools
- **한글라이즈(Hangulize)** - 이름 한글화 라이브러리
- **로마나이저(Romanizer)** - 발음 표기 라이브러리
- **Pandas** - 데이터 분석 및 처리
- **Matplotlib/Plotly** - 데이터 시각화

---

## 🚀 설치 및 실행

### 1. 저장소 클론
```bash
git clone https://github.com/YOUR_USERNAME/proteen-nobel.git
cd proteen-nobel
```

### 2. 가상환경 생성 (선택사항)
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. 의존성 설치
```bash
pip install -r requirements.txt
```

### 4. 로컬 실행
```bash
streamlit run app.py
```

### 5. 브라우저에서 확인
```
http://localhost:8501
```

---

## 🌐 배포 방법

### Streamlit Cloud 배포

1. **GitHub에 코드 업로드**
   ```bash
   git add .
   git commit -m "Initial commit: Proteen Nobel Project"
   git push origin main
   ```

2. **Streamlit Cloud 접속**
   - [share.streamlit.io](https://share.streamlit.io) 방문
   - GitHub 계정으로 로그인

3. **배포 설정**
   - Repository: `YOUR_USERNAME/proteen-nobel`
   - Branch: `main`
   - Main file path: `app.py`

4. **배포 완료**
   - 자동으로 배포 URL 생성
   - 실시간 업데이트 지원

---

## 👥 팀 소개

<div align="center">

| 역할 | 이름 | 담당 분야 | 기술 스택 |
|------|------|-----------|-----------|
| 🧑‍💻 **팀장** | 학생 1 | 프로젝트 기획, 개발 총괄 | Python, Web Dev |
| 🎨 **디자이너** | 학생 2 | UI/UX 디자인, 프론트엔드 | HTML/CSS, Bootstrap |
| 🔬 **연구원** | 학생 3 | 데이터 분석, 알고리즘 | Python, Data Science |
| 🌍 **문화전문가** | 학생 4 | 다국어 지원, 문화 연구 | Linguistics, Research |
| 👨‍🏫 **멘토** | 교사 | 프로젝트 지도, 멘토링 | Education, Leadership |

</div>

### 🎯 팀 비전
> "미래의 노벨상 수상자를 꿈꾸는 청소년들이 글로벌 시민으로서 한글의 아름다움을 세계에 전파하는 프로젝트"

---

## 📁 프로젝트 구조

```
proteen-nobel/
├── 📄 app.py                 # Streamlit 메인 애플리케이션
├── 📄 requirements.txt       # Python 의존성 목록
├── 📄 index.html            # 메인 HTML 파일
├── 📄 style.css             # 커스텀 CSS 스타일
├── 📄 script.js             # JavaScript 기능
├── 📁 assets/               # 이미지 및 리소스
│   ├── 🖼️ hero-bg.jpg
│   ├── 🖼️ team-photo.jpg
│   └── 🖼️ kname-demo.jpg
├── 📁 docs/                 # 문서
│   ├── 📄 project-plan.md
│   ├── 📄 survey-results.md
│   └── 📄 field-report.md
└── 📄 README.md             # 프로젝트 소개서
```

---

## 🤝 기여하기

프로젝트에 기여하고 싶으시다면:

1. **Fork** 이 저장소
2. **Feature branch** 생성 (`git checkout -b feature/AmazingFeature`)
3. **Commit** 변경사항 (`git commit -m 'Add some AmazingFeature'`)
4. **Push** 브랜치 (`git push origin feature/AmazingFeature`)
5. **Pull Request** 생성

### 🐛 버그 리포트
버그를 발견하셨다면 [Issues](https://github.com/YOUR_USERNAME/proteen-nobel/issues)에 등록해 주세요.

---

## 📄 라이선스

이 프로젝트는 **MIT License** 하에 배포됩니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.

---

## 🙏 감사의 말

- **충청북도교육청** - 프로젝트 지원
- **노벨상 수상자들** - 영감과 동기 부여
- **한글학회** - 한글 문화 연구 지원
- **Streamlit 팀** - 훌륭한 배포 플랫폼 제공

---

<div align="center">

**Proteen 노벨 프로젝트** - 한글의 세계화를 위한 청소년들의 도전! 🌍🇰🇷

[⬆️ 맨 위로](#-proteen프로틴-노벨-프로젝트)

</div> 
