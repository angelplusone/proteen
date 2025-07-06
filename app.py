import streamlit as st
import streamlit.components.v1 as components

# 페이지 설정
st.set_page_config(
    page_title="Proteen 노벨 프로젝트",
    page_icon="🏆",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Unsplash 이미지 URL들
hero_img = "https://images.unsplash.com/photo-1464983953574-0892a716854b?auto=format&fit=crop&w=1200&q=80"
team_img = "https://images.unsplash.com/photo-1513258496099-48168024aec0?auto=format&fit=crop&w=800&q=80"
kname_img = "https://images.unsplash.com/photo-1519125323398-675f0ddb6308?auto=format&fit=crop&w=800&q=80"
activity_img = "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=800&q=80"
survey_img = "https://images.unsplash.com/photo-1503676382389-4809596d5290?auto=format&fit=crop&w=800&q=80"
nobel_img = "https://images.unsplash.com/photo-1578662996442-48f60103fc96?auto=format&fit=crop&w=800&q=80"

# HTML 콘텐츠
html_content = """
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Proteen 노벨 프로젝트</title>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- Bootstrap Icons -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.0/font/bootstrap-icons.css" rel="stylesheet">
    <!-- AOS Animation -->
    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
    <style>
        body { font-family: 'Segoe UI', 'Malgun Gothic', Arial, sans-serif; }
        .hero-section { 
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 100px 0;
            position: relative;
            overflow: hidden;
        }
        .hero-section::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="grain" width="100" height="100" patternUnits="userSpaceOnUse"><circle cx="50" cy="50" r="1" fill="white" opacity="0.1"/></pattern></defs><rect width="100" height="100" fill="url(%23grain)"/></svg>');
            opacity: 0.3;
        }
        .hero-content { position: relative; z-index: 2; }
        .section-img { 
            width: 100%; 
            border-radius: 15px; 
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }
        .section-img:hover { transform: translateY(-5px); }
        .card { 
            border: none; 
            border-radius: 15px; 
            box-shadow: 0 5px 20px rgba(0,0,0,0.08);
            transition: all 0.3s ease;
        }
        .card:hover { 
            transform: translateY(-5px); 
            box-shadow: 0 15px 40px rgba(0,0,0,0.15);
        }
        .btn { border-radius: 25px; padding: 0.75rem 2rem; font-weight: 600; }
        .btn:hover { transform: translateY(-2px); }
        .feature-icon { 
            width: 80px; 
            height: 80px; 
            border-radius: 50%; 
            display: flex; 
            align-items: center; 
            justify-content: center; 
            margin: 0 auto 1rem;
            font-size: 2rem;
        }
        .bg-gradient-primary { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }
        .bg-gradient-success { background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%); }
        .bg-gradient-warning { background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); }
        .bg-gradient-info { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }
        .floating { animation: floating 3s ease-in-out infinite; }
        @keyframes floating {
            0% { transform: translateY(0px); }
            50% { transform: translateY(-10px); }
            100% { transform: translateY(0px); }
        }
    </style>
</head>
<body>
    <!-- Hero Section -->
    <section class="hero-section">
        <div class="container">
            <div class="row align-items-center">
                <div class="col-lg-6 hero-content" data-aos="fade-right">
                    <h1 class="display-4 fw-bold mb-4">
                        <i class="bi bi-trophy-fill text-warning floating me-3"></i>
                        Proteen(프로틴) 노벨 프로젝트
                    </h1>
                    <p class="lead fs-4 mb-5">
                        Coding을 사랑하는 십대 정보영재들의 글로벌 도전!<br>
                        한글의 세계화와 글로벌 소통을 실현하는 혁신적인 프로젝트
                    </p>
                    <div class="d-flex gap-3">
                        <button class="btn btn-warning btn-lg" onclick="scrollToSection('project')">
                            <i class="bi bi-arrow-down me-2"></i>프로젝트 보기
                        </button>
                        <button class="btn btn-outline-light btn-lg" onclick="scrollToSection('team')">
                            <i class="bi bi-people me-2"></i>팀 소개
                        </button>
                    </div>
                </div>
                <div class="col-lg-6" data-aos="fade-left">
                    <img src="""" + hero_img + """" class="img-fluid rounded-3 shadow-lg" alt="Hero Image">
                </div>
            </div>
        </div>
    </section>

    <!-- Project Section -->
    <section id="project" class="py-5">
        <div class="container">
            <div class="row">
                <div class="col-12 text-center mb-5">
                    <h2 class="display-5 fw-bold text-primary mb-3">
                        <i class="bi bi-lightbulb-fill me-3"></i>프로젝트 소개
                    </h2>
                    <p class="lead text-muted">한글의 세계화를 위한 혁신적인 글로벌 프로젝트</p>
                </div>
            </div>
            <div class="row g-4">
                <div class="col-md-6 col-lg-4" data-aos="fade-up" data-aos-delay="100">
                    <div class="card h-100">
                        <div class="card-body text-center p-4">
                            <div class="feature-icon bg-gradient-primary text-white mb-3">
                                <i class="bi bi-translate"></i>
                            </div>
                            <h5 class="card-title fw-bold">K-Name Maker</h5>
                            <p class="card-text">
                                외국인들의 이름을 한글로 변환하여 스티커로 제공하는 혁신적인 서비스입니다. 
                                이름을 한글로 바꿔주는 것은 단순한 번역이 아니라, 한국 문화에 대한 관심과 소통의 시작입니다.
                            </p>
                        </div>
                    </div>
                </div>
                <div class="col-md-6 col-lg-4" data-aos="fade-up" data-aos-delay="200">
                    <div class="card h-100">
                        <div class="card-body text-center p-4">
                            <div class="feature-icon bg-gradient-success text-white mb-3">
                                <i class="bi bi-globe"></i>
                            </div>
                            <h5 class="card-title fw-bold">글로벌 탐방</h5>
                            <p class="card-text">
                                스웨덴과 영국의 노벨상 수상자 행적을 따라가며, 다양한 박물관, 미술관, 교육기관을 탐방합니다. 
                                현지에서 K-Name Maker를 시연하고, 한글의 세계화 가능성을 직접 실험합니다.
                            </p>
                        </div>
                    </div>
                </div>
                <div class="col-md-6 col-lg-4" data-aos="fade-up" data-aos-delay="300">
                    <div class="card h-100">
                        <div class="card-body text-center p-4">
                            <div class="feature-icon bg-gradient-warning text-white mb-3">
                                <i class="bi bi-code-slash"></i>
                            </div>
                            <h5 class="card-title fw-bold">기술 활용</h5>
                            <p class="card-text">
                                한글라이즈와 로마나이저 라이브러리를 활용한 이름 변환 기술을 개발하고, 
                                현장에서 수집한 데이터를 분석하여 서비스의 효과를 검증합니다.
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Team Section -->
    <section id="team" class="py-5 bg-light">
        <div class="container">
            <div class="row">
                <div class="col-12 text-center mb-5">
                    <h2 class="display-5 fw-bold text-primary mb-3">
                        <i class="bi bi-people-fill me-3"></i>팀 소개
                    </h2>
                    <p class="lead text-muted">중학교 1학년 정보영재 4명과 교사 1명으로 구성된 Proteen 팀</p>
                </div>
            </div>
            <div class="row g-4">
                <div class="col-md-6 col-lg-4" data-aos="fade-up" data-aos-delay="100">
                    <div class="card text-center">
                        <div class="card-body p-4">
                            <div class="bg-primary bg-opacity-10 rounded-circle d-inline-flex p-4 mb-3">
                                <i class="bi bi-person-fill text-primary fs-1"></i>
                            </div>
                            <h5 class="card-title fw-bold">학생 1 - 팀장</h5>
                            <p class="card-text text-muted">프로젝트 기획, 개발 총괄</p>
                            <div class="d-flex justify-content-center gap-2">
                                <span class="badge bg-primary">Python</span>
                                <span class="badge bg-success">Web Dev</span>
                                <span class="badge bg-info">Leadership</span>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-md-6 col-lg-4" data-aos="fade-up" data-aos-delay="200">
                    <div class="card text-center">
                        <div class="card-body p-4">
                            <div class="bg-success bg-opacity-10 rounded-circle d-inline-flex p-4 mb-3">
                                <i class="bi bi-person-fill text-success fs-1"></i>
                            </div>
                            <h5 class="card-title fw-bold">학생 2 - 디자이너</h5>
                            <p class="card-text text-muted">UI/UX 디자인, 프론트엔드</p>
                            <div class="d-flex justify-content-center gap-2">
                                <span class="badge bg-primary">HTML/CSS</span>
                                <span class="badge bg-warning">Bootstrap</span>
                                <span class="badge bg-info">Design</span>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-md-6 col-lg-4" data-aos="fade-up" data-aos-delay="300">
                    <div class="card text-center">
                        <div class="card-body p-4">
                            <div class="bg-warning bg-opacity-10 rounded-circle d-inline-flex p-4 mb-3">
                                <i class="bi bi-person-fill text-warning fs-1"></i>
                            </div>
                            <h5 class="card-title fw-bold">학생 3 - 연구원</h5>
                            <p class="card-text text-muted">데이터 분석, 알고리즘</p>
                            <div class="d-flex justify-content-center gap-2">
                                <span class="badge bg-primary">Python</span>
                                <span class="badge bg-danger">Data Science</span>
                                <span class="badge bg-info">Research</span>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-md-6 col-lg-4" data-aos="fade-up" data-aos-delay="400">
                    <div class="card text-center">
                        <div class="card-body p-4">
                            <div class="bg-info bg-opacity-10 rounded-circle d-inline-flex p-4 mb-3">
                                <i class="bi bi-person-fill text-info fs-1"></i>
                            </div>
                            <h5 class="card-title fw-bold">학생 4 - 문화전문가</h5>
                            <p class="card-text text-muted">다국어 지원, 문화 연구</p>
                            <div class="d-flex justify-content-center gap-2">
                                <span class="badge bg-primary">Linguistics</span>
                                <span class="badge bg-success">Culture</span>
                                <span class="badge bg-warning">Research</span>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-md-6 col-lg-4" data-aos="fade-up" data-aos-delay="500">
                    <div class="card text-center">
                        <div class="card-body p-4">
                            <div class="bg-danger bg-opacity-10 rounded-circle d-inline-flex p-4 mb-3">
                                <i class="bi bi-person-workspace text-danger fs-1"></i>
                            </div>
                            <h5 class="card-title fw-bold">교사 - 멘토</h5>
                            <p class="card-text text-muted">프로젝트 지도, 멘토링</p>
                            <div class="d-flex justify-content-center gap-2">
                                <span class="badge bg-primary">Education</span>
                                <span class="badge bg-success">Leadership</span>
                                <span class="badge bg-info">Mentoring</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- K-Name Maker Section -->
    <section id="kname" class="py-5">
        <div class="container">
            <div class="row">
                <div class="col-12 text-center mb-5">
                    <h2 class="display-5 fw-bold text-primary mb-3">
                        <i class="bi bi-type me-3"></i>K-Name Maker
                    </h2>
                    <p class="lead text-muted">이름을 한글로 변환하고 스티커로 출력하는 혁신적인 서비스</p>
                </div>
            </div>
            <div class="row align-items-center">
                <div class="col-lg-6" data-aos="fade-right">
                    <img src="""" + kname_img + """" class="section-img mb-4" alt="K-Name Maker">
                    <h4 class="fw-bold mb-3">서비스 특징</h4>
                    <ul class="list-unstyled">
                        <li class="mb-2"><i class="bi bi-check-circle-fill text-success me-2"></i>실시간 이름 변환</li>
                        <li class="mb-2"><i class="bi bi-check-circle-fill text-success me-2"></i>정확한 한글 발음 가이드</li>
                        <li class="mb-2"><i class="bi bi-check-circle-fill text-success me-2"></i>즉석 스티커 출력</li>
                        <li class="mb-2"><i class="bi bi-check-circle-fill text-success me-2"></i>다국어 지원 (한국어, 영어, 스웨덴어)</li>
                    </ul>
                </div>
                <div class="col-lg-6" data-aos="fade-left">
                    <div class="card border-0 shadow-lg">
                        <div class="card-body p-5">
                            <h4 class="fw-bold mb-4">실시간 이름 변환</h4>
                            <div class="mb-4">
                                <label class="form-label fw-bold">이름 입력</label>
                                <input type="text" class="form-control form-control-lg" id="nameInput" placeholder="예: Brian, Anna, Maria...">
                            </div>
                            <button class="btn btn-primary btn-lg w-100" onclick="convertName()">
                                <i class="bi bi-arrow-right-circle me-2"></i>한글 이름 생성
                            </button>
                            <div id="result" class="mt-4 p-3 bg-light rounded" style="display:none;">
                                <h5 class="fw-bold text-primary">변환 결과</h5>
                                <div id="koreanName" class="fs-4 fw-bold text-center py-3"></div>
                                <div id="pronunciation" class="text-muted text-center"></div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Activity Section -->
    <section id="activity" class="py-5 bg-light">
        <div class="container">
            <div class="row">
                <div class="col-12 text-center mb-5">
                    <h2 class="display-5 fw-bold text-primary mb-3">
                        <i class="bi bi-globe me-3"></i>현장 활동
                    </h2>
                    <p class="lead text-muted">스웨덴과 영국에서의 노벨상 수상자 행적 탐방 및 현지 활동</p>
                </div>
            </div>
            <div class="row g-4">
                <div class="col-lg-6" data-aos="fade-up">
                    <div class="card h-100">
                        <img src="""" + activity_img + """" class="card-img-top" alt="Sweden">
                        <div class="card-body p-4">
                            <div class="d-flex align-items-center mb-3">
                                <div class="bg-primary bg-opacity-10 rounded-circle p-3 me-3">
                                    <i class="bi bi-geo-alt-fill text-primary fs-4"></i>
                                </div>
                                <h4 class="fw-bold mb-0">스웨덴 탐방</h4>
                            </div>
                            <ul class="list-unstyled">
                                <li class="mb-2"><i class="bi bi-check-circle-fill text-success me-2"></i>노벨상 수상자 행적 탐방</li>
                                <li class="mb-2"><i class="bi bi-check-circle-fill text-success me-2"></i>스톡홀름 노벨 박물관</li>
                                <li class="mb-2"><i class="bi bi-check-circle-fill text-success me-2"></i>현지인 대상 K-Name Maker 체험</li>
                                <li class="mb-2"><i class="bi bi-check-circle-fill text-success me-2"></i>한글 문화 소개 활동</li>
                            </ul>
                        </div>
                    </div>
                </div>
                <div class="col-lg-6" data-aos="fade-up" data-aos-delay="100">
                    <div class="card h-100">
                        <img src="""" + nobel_img + """" class="card-img-top" alt="UK">
                        <div class="card-body p-4">
                            <div class="d-flex align-items-center mb-3">
                                <div class="bg-success bg-opacity-10 rounded-circle p-3 me-3">
                                    <i class="bi bi-geo-alt-fill text-success fs-4"></i>
                                </div>
                                <h4 class="fw-bold mb-0">영국 탐방</h4>
                            </div>
                            <ul class="list-unstyled">
                                <li class="mb-2"><i class="bi bi-check-circle-fill text-success me-2"></i>런던 과학 박물관</li>
                                <li class="mb-2"><i class="bi bi-check-circle-fill text-success me-2"></i>대학 연구소 방문</li>
                                <li class="mb-2"><i class="bi bi-check-circle-fill text-success me-2"></i>한글 교육 프로그램 진행</li>
                                <li class="mb-2"><i class="bi bi-check-circle-fill text-success me-2"></i>문화 교류 활동</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Survey Section -->
    <section id="survey" class="py-5">
        <div class="container">
            <div class="row">
                <div class="col-12 text-center mb-5">
                    <h2 class="display-5 fw-bold text-primary mb-3">
                        <i class="bi bi-graph-up me-3"></i>설문/분석
                    </h2>
                    <p class="lead text-muted">현장에서 수집한 데이터 분석 및 프로젝트 개선 방향</p>
                </div>
            </div>
            <div class="row g-4">
                <div class="col-md-6 col-lg-3" data-aos="fade-up" data-aos-delay="100">
                    <div class="card text-center">
                        <div class="card-body p-4">
                            <div class="bg-primary bg-opacity-10 rounded-circle d-inline-flex p-3 mb-3">
                                <i class="bi bi-star-fill text-primary fs-1"></i>
                            </div>
                            <h3 class="fw-bold text-primary">4.8</h3>
                            <p class="text-muted mb-0">만족도</p>
                        </div>
                    </div>
                </div>
                <div class="col-md-6 col-lg-3" data-aos="fade-up" data-aos-delay="200">
                    <div class="card text-center">
                        <div class="card-body p-4">
                            <div class="bg-success bg-opacity-10 rounded-circle d-inline-flex p-3 mb-3">
                                <i class="bi bi-people-fill text-success fs-1"></i>
                            </div>
                            <h3 class="fw-bold text-success">150+</h3>
                            <p class="text-muted mb-0">참여자</p>
                        </div>
                    </div>
                </div>
                <div class="col-md-6 col-lg-3" data-aos="fade-up" data-aos-delay="300">
                    <div class="card text-center">
                        <div class="card-body p-4">
                            <div class="bg-warning bg-opacity-10 rounded-circle d-inline-flex p-3 mb-3">
                                <i class="bi bi-translate text-warning fs-1"></i>
                            </div>
                            <h3 class="fw-bold text-warning">95%</h3>
                            <p class="text-muted mb-0">정확도</p>
                        </div>
                    </div>
                </div>
                <div class="col-md-6 col-lg-3" data-aos="fade-up" data-aos-delay="400">
                    <div class="card text-center">
                        <div class="card-body p-4">
                            <div class="bg-info bg-opacity-10 rounded-circle d-inline-flex p-3 mb-3">
                                <i class="bi bi-lightbulb-fill text-info fs-1"></i>
                            </div>
                            <h3 class="fw-bold text-info">12</h3>
                            <p class="text-muted mb-0">개선사항</p>
                        </div>
                    </div>
                </div>
            </div>
            <div class="row mt-5">
                <div class="col-lg-8 mx-auto">
                    <div class="card border-0 shadow">
                        <div class="card-body p-5">
                            <h4 class="fw-bold mb-4">설문 결과 분석</h4>
                            <p class="mb-4">
                                현장에서 수집한 한글 발음의 난이도, 체험의 흥미도, 실제 이름과의 유사도 등 
                                다양한 데이터를 설문을 통해 수집하고, 이를 시각화하여 프로젝트의 효과와 보완점을 분석합니다.
                            </p>
                            <div class="row g-3">
                                <div class="col-md-6">
                                    <h6 class="fw-bold">주요 설문 항목</h6>
                                    <ul class="list-unstyled">
                                        <li><i class="bi bi-check2 text-success me-2"></i>한글 발음 난이도</li>
                                        <li><i class="bi bi-check2 text-success me-2"></i>체험 흥미도</li>
                                        <li><i class="bi bi-check2 text-success me-2"></i>실제 이름 유사도</li>
                                        <li><i class="bi bi-check2 text-success me-2"></i>한국 문화 관심도</li>
                                    </ul>
                                </div>
                                <div class="col-md-6">
                                    <h6 class="fw-bold">분석 결과</h6>
                                    <ul class="list-unstyled">
                                        <li><i class="bi bi-graph-up text-primary me-2"></i>높은 만족도 (4.8/5.0)</li>
                                        <li><i class="bi bi-graph-up text-primary me-2"></i>문화 교류 효과</li>
                                        <li><i class="bi bi-graph-up text-primary me-2"></i>한글 인식도 향상</li>
                                        <li><i class="bi bi-graph-up text-primary me-2"></i>서비스 개선 방향 도출</li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="bg-dark text-white py-4">
        <div class="container text-center">
            <p class="mb-0">&copy; 2024 Proteen 노벨 프로젝트. All rights reserved.</p>
        </div>
    </footer>

    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <!-- AOS Animation -->
    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <script>
        // Initialize AOS
        AOS.init({
            duration: 1000,
            once: true,
            offset: 100
        });

        // K-Name Maker functionality
        function convertName() {
            const nameInput = document.getElementById('nameInput');
            const result = document.getElementById('result');
            const koreanName = document.getElementById('koreanName');
            const pronunciation = document.getElementById('pronunciation');
            
            if (!nameInput.value.trim()) {
                alert('이름을 입력해주세요!');
                return;
            }
            
            const name = nameInput.value.trim().toLowerCase();
            const conversions = {
                'brian': '브라이언',
                'anna': '안나',
                'maria': '마리아',
                'john': '존',
                'sarah': '사라',
                'michael': '마이클',
                'emma': '엠마',
                'david': '데이비드',
                'lisa': '리사',
                'james': '제임스'
            };
            
            const korean = conversions[name] || name.split('').map(char => {
                const charMap = {
                    'a': '아', 'b': '브', 'c': '크', 'd': '드', 'e': '에',
                    'f': '프', 'g': '그', 'h': '흐', 'i': '이', 'j': '지',
                    'k': '크', 'l': '르', 'm': '므', 'n': '느', 'o': '오',
                    'p': '프', 'q': '크', 'r': '르', 's': '스', 't': '트',
                    'u': '우', 'v': '브', 'w': '우', 'x': '크스', 'y': '이',
                    'z': '즈'
                };
                return charMap[char] || char;
            }).join('');
            
            koreanName.textContent = korean;
            pronunciation.textContent = `발음: ${korean}`;
            
            result.style.display = 'block';
            result.classList.add('result-animation');
            
            setTimeout(() => {
                result.classList.remove('result-animation');
            }, 500);
        }

        // Smooth scroll function
        function scrollToSection(sectionId) {
            const element = document.getElementById(sectionId);
            if (element) {
                element.scrollIntoView({ behavior: 'smooth' });
            }
        }
    </script>
</body>
</html>
"""

# Streamlit 앱
def main():
    # CSS 스타일 제거
    st.markdown(
        """
        <style>
        .block-container { padding-top: 0 !important; }
        .stApp { background: transparent !important; }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # HTML 컴포넌트 렌더링
    components.html(html_content, height=2000, scrolling=True)

if __name__ == "__main__":
    main() 
