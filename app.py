import streamlit as st
import streamlit.components.v1 as components

# 페이지 설정
st.set_page_config(
    page_title="Proteen 노벨 프로젝트",
    page_icon="🏆",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS 스타일
css = """
<style>
body {
    font-family: 'Segoe UI', 'Malgun Gothic', Arial, sans-serif;
    margin: 0;
    background: #f7f9fb;
    color: #222;
}
header {
    background: #1a237e;
    color: #fff;
    padding: 2rem 1rem 1rem 1rem;
    position: relative;
}
.nav-right {
    position: absolute;
    top: 1rem;
    right: 1rem;
    display: flex;
    gap: 1rem;
    align-items: center;
}
#homeBtn {
    background: #fff;
    color: #1a237e;
    border: none;
    border-radius: 4px;
    padding: 0.5rem 1rem;
    font-weight: bold;
    cursor: pointer;
    transition: background 0.2s;
}
#homeBtn:hover {
    background: #e3e6f3;
}
#langSelect {
    padding: 0.4rem 0.8rem;
    border-radius: 4px;
    border: 1px solid #ccc;
}
nav {
    background: #283593;
    color: #fff;
    padding: 0.5rem 0;
}
nav ul {
    list-style: none;
    display: flex;
    justify-content: center;
    gap: 2rem;
    margin: 0;
    padding: 0;
}
nav a {
    color: #fff;
    text-decoration: none;
    font-weight: 500;
    padding: 0.5rem 0.8rem;
    border-radius: 4px;
    transition: background 0.2s;
}
nav a:hover, nav a.active {
    background: #3949ab;
}
main {
    max-width: 900px;
    margin: 2rem auto;
    background: #fff;
    border-radius: 12px;
    box-shadow: 0 2px 12px rgba(30,40,80,0.08);
    padding: 2rem;
}
.page-section {
    display: block;
}
@media (max-width: 600px) {
    main {
        padding: 1rem;
    }
    nav ul {
        gap: 0.5rem;
        font-size: 0.95rem;
    }
    .nav-right {
        flex-direction: column;
        gap: 0.5rem;
        right: 0.5rem;
        top: 0.5rem;
    }
}
</style>
"""

# HTML 콘텐츠
html_content = """
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Proteen 노벨 프로젝트</title>
</head>
<body>
    <header>
        <div class="nav-right">
            <button id="homeBtn">홈</button>
            <select id="langSelect">
                <option value="ko">한국어</option>
                <option value="en">English</option>
                <option value="sv">Svenska</option>
            </select>
        </div>
        <h1 id="main-title">Proteen(프로틴) 노벨 프로젝트</h1>
        <p id="main-slogan">Coding을 사랑하는 십대 정보영재들의 글로벌 도전!</p>
    </header>
    <nav>
        <ul>
            <li><a href="#home" class="nav-link" data-section="home">홈</a></li>
            <li><a href="#project" class="nav-link" data-section="project">프로젝트 소개</a></li>
            <li><a href="#team" class="nav-link" data-section="team">팀 소개</a></li>
            <li><a href="#kname" class="nav-link" data-section="kname">K-Name Maker</a></li>
            <li><a href="#activity" class="nav-link" data-section="activity">현장 활동</a></li>
            <li><a href="#survey" class="nav-link" data-section="survey">설문/분석</a></li>
        </ul>
    </nav>
    <main>
        <section id="home" class="page-section">
            <h2>홈</h2>
            <p>Proteen 팀과 노벨 프로젝트에 오신 것을 환영합니다!</p>
        </section>
        <section id="project" class="page-section" style="display:none;">
            <h2>프로젝트 소개</h2>
            <p>프로젝트 개요, K-Name Maker의 취지, 해외 탐방 개요 등</p>
        </section>
        <section id="team" class="page-section" style="display:none;">
            <h2>팀 소개</h2>
            <p>중1 정보영재 4명과 교사 1명으로 구성된 Proteen 팀을 소개합니다.</p>
        </section>
        <section id="kname" class="page-section" style="display:none;">
            <h2>K-Name Maker</h2>
            <p>이름을 한글로 변환하고 스티커로 출력하는 서비스</p>
        </section>
        <section id="activity" class="page-section" style="display:none;">
            <h2>현장 활동</h2>
            <p>스웨덴/영국 탐방, 한글라이즈/로마나이저 활용, 설문조사 등</p>
        </section>
        <section id="survey" class="page-section" style="display:none;">
            <h2>설문/분석</h2>
            <p>설문 결과 시각화, 프로젝트 보완점 등</p>
        </section>
    </main>
    <script>
        // 네비게이션: 섹션 전환
        const navLinks = document.querySelectorAll('.nav-link');
        const sections = document.querySelectorAll('.page-section');
        navLinks.forEach(link => {
            link.addEventListener('click', e => {
                e.preventDefault();
                const target = link.getAttribute('data-section');
                sections.forEach(sec => {
                    sec.style.display = sec.id === target ? 'block' : 'none';
                });
                navLinks.forEach(l => l.classList.remove('active'));
                link.classList.add('active');
            });
        });
        // 홈 버튼: 홈 섹션으로 이동
        const homeBtn = document.getElementById('homeBtn');
        homeBtn.addEventListener('click', () => {
            sections.forEach(sec => {
                sec.style.display = sec.id === 'home' ? 'block' : 'none';
            });
            navLinks.forEach(l => l.classList.remove('active'));
            document.querySelector('.nav-link[data-section="home"]').classList.add('active');
        });
        // 언어 전환: 텍스트 다국어 지원
        const langSelect = document.getElementById('langSelect');
        const translations = {
            ko: {
                'main-title': 'Proteen(프로틴) 노벨 프로젝트',
                'main-slogan': 'Coding을 사랑하는 십대 정보영재들의 글로벌 도전!',
                home: '홈',
                project: '프로젝트 소개',
                team: '팀 소개',
                kname: 'K-Name Maker',
                activity: '현장 활동',
                survey: '설문/분석',
                homeText: 'Proteen 팀과 노벨 프로젝트에 오신 것을 환영합니다!',
                projectText: '프로젝트 개요, K-Name Maker의 취지, 해외 탐방 개요 등',
                teamText: '중1 정보영재 4명과 교사 1명으로 구성된 Proteen 팀을 소개합니다.',
                knameText: '이름을 한글로 변환하고 스티커로 출력하는 서비스',
                activityText: '스웨덴/영국 탐방, 한글라이즈/로마나이저 활용, 설문조사 등',
                surveyText: '설문 결과 시각화, 프로젝트 보완점 등',
                homeBtn: '홈'
            },
            en: {
                'main-title': 'Proteen Nobel Project',
                'main-slogan': 'Teenage coding prodigies on a global challenge!',
                home: 'Home',
                project: 'Project',
                team: 'Team',
                kname: 'K-Name Maker',
                activity: 'Field Activity',
                survey: 'Survey/Analysis',
                homeText: 'Welcome to the Proteen team and Nobel Project!',
                projectText: 'Project overview, K-Name Maker, global exploration, etc.',
                teamText: 'Meet Proteen: 4 gifted 7th graders and 1 teacher.',
                knameText: 'Convert your name to Korean and print as a sticker!',
                activityText: 'Sweden/UK tour, Hangulize/Romanizer, survey, etc.',
                surveyText: 'Survey results, project improvements, and more.',
                homeBtn: 'Home'
            },
            sv: {
                'main-title': 'Proteen Nobelprojekt',
                'main-slogan': 'Tonåriga kodgenier på en global utmaning!',
                home: 'Hem',
                project: 'Projekt',
                team: 'Team',
                kname: 'K-Name Maker',
                activity: 'Fältaktivitet',
                survey: 'Enkät/Analys',
                homeText: 'Välkommen till Proteen-teamet och Nobelprojektet!',
                projectText: 'Projektöversikt, K-Name Maker, global utforskning, etc.',
                teamText: 'Möt Proteen: 4 begåvade sjundeklassare och 1 lärare.',
                knameText: 'Konvertera ditt namn till koreanska och skriv ut som klistermärke!',
                activityText: 'Sverige/UK-resa, Hangulize/Romanizer, enkät, etc.',
                surveyText: 'Enkätresultat, projektförbättringar m.m.',
                homeBtn: 'Hem'
            }
        };
        function setLanguage(lang) {
            document.getElementById('main-title').textContent = translations[lang]['main-title'];
            document.getElementById('main-slogan').textContent = translations[lang]['main-slogan'];
            // 네비게이션
            const navIds = ['home','project','team','kname','activity','survey'];
            navIds.forEach(id => {
                document.querySelector(`.nav-link[data-section="${id}"]`).textContent = translations[lang][id];
            });
            // 섹션별 텍스트
            document.querySelector('#home h2').textContent = translations[lang]['home'];
            document.querySelector('#home p').textContent = translations[lang]['homeText'];
            document.querySelector('#project h2').textContent = translations[lang]['project'];
            document.querySelector('#project p').textContent = translations[lang]['projectText'];
            document.querySelector('#team h2').textContent = translations[lang]['team'];
            document.querySelector('#team p').textContent = translations[lang]['teamText'];
            document.querySelector('#kname h2').textContent = translations[lang]['kname'];
            document.querySelector('#kname p').textContent = translations[lang]['knameText'];
            document.querySelector('#activity h2').textContent = translations[lang]['activity'];
            document.querySelector('#activity p').textContent = translations[lang]['activityText'];
            document.querySelector('#survey h2').textContent = translations[lang]['survey'];
            document.querySelector('#survey p').textContent = translations[lang]['surveyText'];
            // 홈 버튼
            document.getElementById('homeBtn').textContent = translations[lang]['homeBtn'];
        }
        langSelect.addEventListener('change', e => {
            setLanguage(e.target.value);
        });
        // 초기 언어 설정
        setLanguage('ko');
    </script>
</body>
</html>
"""

# Streamlit 앱
def main():
    st.markdown(css, unsafe_allow_html=True)
    
    # HTML 컴포넌트 렌더링
    components.html(html_content, height=800, scrolling=True)

if __name__ == "__main__":
    main() 