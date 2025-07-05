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