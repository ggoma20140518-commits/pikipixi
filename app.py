import streamlit as st
import base64
from pathlib import Path

# ── 페이지 설정 ──
st.set_page_config(
    page_title="PIKIPIXI | 모발과학연구소",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── 이미지 로드 헬퍼 ──
IMG_DIR = Path(__file__).parent / "images"

def img_to_base64(filename: str) -> str:
    path = IMG_DIR / filename
    return base64.b64encode(path.read_bytes()).decode()

def img_tag(filename: str, width: str = "100%", border_radius: str = "12px") -> str:
    b64 = img_to_base64(filename)
    return f'<img src="data:image/png;base64,{b64}" style="width:{width};border-radius:{border_radius};object-fit:cover;">'

# ── 글로벌 CSS ──
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700;900&family=Playfair+Display:ital,wght@0,400;0,700;1,400&display=swap');

/* 기본 */
html, body, [data-testid="stAppViewContainer"] {
    background-color: #FAF8F5;
    color: #2C2C2C;
    font-family: 'Noto Sans KR', sans-serif;
}
[data-testid="stHeader"] { background: transparent; }
.block-container { padding-top: 1rem; max-width: 1200px; }

/* 탭 스타일 */
.stTabs [data-baseweb="tab-list"] {
    gap: 0;
    justify-content: center;
    border-bottom: 2px solid #E8E0D8;
    background: transparent;
}
.stTabs [data-baseweb="tab"] {
    font-family: 'Playfair Display', serif;
    font-size: 1.1rem;
    font-weight: 400;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #999;
    padding: 12px 40px;
    border: none;
    background: transparent;
}
.stTabs [aria-selected="true"] {
    color: #2C2C2C !important;
    border-bottom: 3px solid #2C2C2C !important;
    background: transparent !important;
}

/* 히어로 */
.hero-wrap {
    position: relative;
    width: 100%;
    overflow: hidden;
    border-radius: 0;
    margin-bottom: 0;
}
.hero-wrap img {
    width: 100%;
    display: block;
    border-radius: 0 !important;
}
.hero-overlay {
    position: absolute;
    inset: 0;
    background: linear-gradient(180deg, rgba(0,0,0,0.05) 0%, rgba(0,0,0,0.35) 100%);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: 4rem;
    font-weight: 700;
    color: #fff;
    letter-spacing: 12px;
    text-shadow: 0 2px 20px rgba(0,0,0,0.3);
    margin-bottom: 8px;
}
.hero-sub {
    font-family: 'Noto Sans KR', sans-serif;
    font-size: 1rem;
    font-weight: 300;
    color: rgba(255,255,255,0.85);
    letter-spacing: 6px;
    text-transform: uppercase;
}

/* 섹션 스타일 */
.section-num {
    font-family: 'Playfair Display', serif;
    font-size: 0.85rem;
    color: #B8A99A;
    letter-spacing: 4px;
    margin-bottom: 8px;
}
.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.8rem;
    font-weight: 700;
    color: #2C2C2C;
    margin-bottom: 16px;
    line-height: 1.4;
}
.section-body {
    font-size: 1rem;
    line-height: 1.9;
    color: #555;
    font-weight: 300;
}
.divider {
    width: 60px;
    height: 2px;
    background: #C4B5A5;
    margin: 50px auto;
}

/* 제품 카드 */
.product-card {
    background: #fff;
    border-radius: 16px;
    overflow: hidden;
    box-shadow: 0 4px 24px rgba(0,0,0,0.06);
    transition: transform 0.3s, box-shadow 0.3s;
    height: 100%;
}
.product-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 12px 36px rgba(0,0,0,0.12);
}
.product-card img {
    width: 100%;
    aspect-ratio: 1;
    object-fit: cover;
}
.product-info {
    padding: 20px 24px 24px;
}
.product-category {
    font-size: 0.75rem;
    color: #B8A99A;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 6px;
}
.product-name {
    font-family: 'Playfair Display', serif;
    font-size: 1.2rem;
    font-weight: 700;
    color: #2C2C2C;
    margin-bottom: 8px;
}
.product-desc {
    font-size: 0.9rem;
    color: #777;
    line-height: 1.6;
    font-weight: 300;
}

/* 효능 섹션 */
.effect-card {
    background: #fff;
    border-radius: 16px;
    overflow: hidden;
    box-shadow: 0 2px 16px rgba(0,0,0,0.05);
}
.effect-card img {
    width: 100%;
    height: 220px;
    object-fit: cover;
}
.effect-text {
    padding: 16px 20px;
    font-size: 0.9rem;
    color: #555;
    text-align: center;
    font-weight: 400;
}

/* 히어로 크기 */
.hero-wrap img {
    min-height: 500px;
}

/* 제품 미리보기 축소 */
.product-preview {
    max-width: 280px;
    margin: 0 auto;
}
.product-preview .product-card img {
    aspect-ratio: 1;
    max-height: 280px;
}

/* 브랜드 배너 */
.brand-banner {
    position: relative;
    border-radius: 20px;
    padding: 80px 40px;
    text-align: center;
    color: #fff;
    margin: 40px 0;
    overflow: hidden;
}
.brand-banner img {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    z-index: 0;
}
.brand-banner .banner-overlay {
    position: absolute;
    inset: 0;
    background: rgba(0,0,0,0.55);
    z-index: 1;
}
.brand-banner h2 {
    position: relative;
    z-index: 2;
    font-family: 'Playfair Display', serif;
    font-size: 2rem;
    margin-bottom: 12px;
    letter-spacing: 6px;
}
.brand-banner p {
    position: relative;
    z-index: 2;
    font-size: 0.95rem;
    color: rgba(255,255,255,0.85);
    font-weight: 300;
    letter-spacing: 2px;
}

/* Quote */
.quote-box {
    background: linear-gradient(135deg, #F5EDE6 0%, #EDE4DB 100%);
    border-left: 4px solid #C4B5A5;
    padding: 28px 32px;
    border-radius: 0 12px 12px 0;
    margin: 24px 0;
}
.quote-box p {
    font-family: 'Playfair Display', serif;
    font-size: 1.15rem;
    font-style: italic;
    color: #5A4E43;
    line-height: 1.8;
    margin: 0;
}

/* 푸터 */
.footer {
    text-align: center;
    padding: 40px 0 24px;
    color: #aaa;
    font-size: 0.8rem;
    letter-spacing: 2px;
    border-top: 1px solid #E8E0D8;
    margin-top: 60px;
}
</style>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════
# 네비게이션 바
# ═══════════════════════════════════════
st.markdown(f"""
<div style="display:flex;align-items:center;justify-content:center;padding:20px 0 10px;">
    <span style="font-family:'Playfair Display',serif;font-size:2rem;font-weight:700;letter-spacing:8px;color:#2C2C2C;">
        PIKIPIXI
    </span>
</div>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════
# 탭 구성: MAIN / ABOUT / PRODUCT
# ═══════════════════════════════════════
tab_main, tab_about, tab_product = st.tabs(["HOME", "ABOUT", "PRODUCT"])

# ─────────────────────────────────────
# HOME 탭
# ─────────────────────────────────────
with tab_main:
    # 히어로 이미지
    st.markdown(f"""
    <div class="hero-wrap">
        {img_tag("image1.png", border_radius="0")}
        <div class="hero-overlay">
            <div class="hero-title">PIKIPIXI</div>
            <div class="hero-sub">모발과학연구소 &nbsp;·&nbsp; Hair Science Lab</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='height:40px'></div>", unsafe_allow_html=True)

    # 간단한 소개
    st.markdown("""
    <div style="text-align:center;max-width:700px;margin:0 auto;padding:20px 0 40px;">
        <div class="section-num">BROKEN? WE FIX!</div>
        <div class="section-title">손상되고 지친 당신의 머릿결,<br>우리의 루틴이 끝까지 지켜냅니다</div>
        <div class="section-body">
            까다롭게 고르고 검증한 단 하나의 루틴.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 제품 미리보기
    _, col1, _, col2, _ = st.columns([1, 3, 1, 3, 1], gap="medium")
    with col1:
        st.markdown(f"""
        <div class="product-preview">
            <div class="product-card">
                {img_tag("image9.png", border_radius="16px 16px 0 0")}
                <div class="product-info">
                    <div class="product-category">Hair Essence</div>
                    <div class="product-name">헤어 에센스</div>
                    <div class="product-desc">깊은 보습과 윤기를 선사하는 고농축 에센스</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="product-preview">
            <div class="product-card">
                {img_tag("image10.png", border_radius="16px 16px 0 0")}
                <div class="product-info">
                    <div class="product-category">Hair Mist</div>
                    <div class="product-name">헤어 미스트</div>
                    <div class="product-desc">가볍게 뿌리는 향기로운 헤어 케어 미스트</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="footer">© 2026 PIKIPIXI. All Rights Reserved.</div>', unsafe_allow_html=True)


# ─────────────────────────────────────
# ABOUT 탭
# ─────────────────────────────────────
with tab_about:

    st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)

    # Brand Story 헤더
    st.markdown("""
    <div style="text-align:center;margin-bottom:50px;">
        <div class="section-num">OUR STORY</div>
        <div class="section-title" style="font-size:2.2rem;">Brand Story</div>
    </div>
    """, unsafe_allow_html=True)

    # ── 01. The Problem ──
    col_left, col_right = st.columns([5, 5], gap="large")
    with col_left:
        st.markdown(f"""
        <div style="border-radius:16px;overflow:hidden;box-shadow:0 4px 24px rgba(0,0,0,0.08);">
            {img_tag("image2.png", border_radius="16px")}
        </div>
        """, unsafe_allow_html=True)
    with col_right:
        st.markdown("""
        <div style="display:flex;flex-direction:column;justify-content:center;height:100%;padding:20px 0;">
            <div class="section-num">CHAPTER 01</div>
            <div class="section-title">The Problem<br><span style="font-family:'Noto Sans KR';font-size:1.2rem;font-weight:400;">속도의 시대, 잃어버린 '나다움'</span></div>
            <div class="section-body">
                AI와 SNS로 대변되는 눈부시게 빠른 세상. 유행은 매일같이 쏟아지고,
                우리는 그 획일화된 흐름 속에서 정작 소중한 '자신의 개성'을 돌볼 틈을 잃어갑니다.
                바쁜 일상 속에서 수많은 제품을 일일이 써보며 나에게 맞는 정답을 찾기란 불가능에 가깝습니다.
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    # ── 02. Our Solution ──
    col_left2, col_right2 = st.columns([5, 5], gap="large")
    with col_left2:
        st.markdown("""
        <div style="display:flex;flex-direction:column;justify-content:center;height:100%;padding:20px 0;">
            <div class="section-num">CHAPTER 02</div>
            <div class="section-title">Our Solution<br><span style="font-family:'Noto Sans KR';font-size:1.2rem;font-weight:400;">까다롭게 고르고 검증한 단 하나의 루틴</span></div>
            <div class="section-body">
                그래서 PIKIPIXI 모발과학연구소가 대신 고민했습니다.
                연구 데이터와 정밀한 분석을 통해, 복잡한 과정은 덜어내고 확실한 효과만 남겼습니다.
            </div>
            <div class="quote-box" style="margin-top:20px;">
                <p>BROKEN? WE FIX!<br>
                손상되고 지친 당신의 머릿결, 우리의 루틴이 당신의 스타일과 자신감을 끝까지 지켜냅니다.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with col_right2:
        st.markdown(f"""
        <div style="border-radius:16px;overflow:hidden;box-shadow:0 4px 24px rgba(0,0,0,0.08);">
            {img_tag("image3.png", border_radius="16px")}
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    # ── 03. The Secret ──
    col_left3, col_right3 = st.columns([5, 5], gap="large")
    with col_left3:
        st.markdown(f"""
        <div style="border-radius:16px;overflow:hidden;box-shadow:0 4px 24px rgba(0,0,0,0.08);">
            {img_tag("image4.png", border_radius="16px")}
        </div>
        """, unsafe_allow_html=True)
    with col_right3:
        st.markdown("""
        <div style="display:flex;flex-direction:column;justify-content:center;height:100%;padding:20px 0;">
            <div class="section-num">CHAPTER 03</div>
            <div class="section-title">The Secret<br><span style="font-family:'Noto Sans KR';font-size:1.2rem;font-weight:400;">K-뷰티의 정수</span></div>
            <div class="section-body">
                예로부터 전해 내려온 K-뷰티의 모발 관리 비법을 현대 과학으로 재해석하여,
                그 어디에서도 경험하지 못한 독보적인 부드러운 사용감을 구현했습니다.
            </div>
            <div style="height:20px;"></div>
            <div class="section-body">
                전통의 지혜와 현대 과학의 만남, 그것이 우리가 제안하는 새로운 모발 솔루션입니다.
            </div>
        </div>
        """, unsafe_allow_html=True)

    # 브랜드 배너
    st.markdown(f"""
    <div class="brand-banner">
        {img_tag("image5.png", border_radius="0")}
        <div class="banner-overlay"></div>
        <h2>PIKIPIXI</h2>
        <p>모발과학연구소 &nbsp;·&nbsp; Hair Science Lab</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="footer">© 2026 PIKIPIXI. All Rights Reserved.</div>', unsafe_allow_html=True)


# ─────────────────────────────────────
# PRODUCT 탭
# ─────────────────────────────────────
with tab_product:

    st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align:center;margin-bottom:50px;">
        <div class="section-num">OUR PRODUCTS</div>
        <div class="section-title" style="font-size:2.2rem;">Product Collection</div>
    </div>
    """, unsafe_allow_html=True)

    # ═══ 헤어 에센스 ═══
    st.markdown("""
    <div style="text-align:center;margin-bottom:30px;">
        <div class="section-num">01</div>
        <div class="section-title">헤어 에센스<br><span style="font-family:'Playfair Display';font-size:1rem;color:#B8A99A;">Hair Essence</span></div>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4, gap="medium")
    with c1:
        st.markdown(f"""
        <div class="product-card">
            {img_tag("image9.png", border_radius="16px 16px 0 0")}
            <div class="product-info">
                <div class="product-category">용기 이미지</div>
                <div class="product-name">PIKIPIXI Essence</div>
                <div class="product-desc">홀로그램 로고가 감성적인 무드를 연출합니다.</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
        <div class="product-card">
            {img_tag("image6.png", border_radius="16px 16px 0 0")}
            <div class="product-info">
                <div class="product-category">용기 이미지</div>
                <div class="product-name">SUNSHINE</div>
                <div class="product-desc">고급스러운 블랙 캡의 시그니처 보틀 디자인.</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown(f"""
        <div class="product-card">
            {img_tag("image12.png", border_radius="16px 16px 0 0")}
            <div class="product-info">
                <div class="product-category">향조 설명</div>
                <div class="product-name">Floral Woody Note</div>
                <div class="product-desc">라벤더, 라즈베리, 샌달우드가 어우러진 향조로 모발에 은은한 향기를 더합니다.</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with c4:
        st.markdown(f"""
        <div class="product-card">
            {img_tag("image14.png", border_radius="16px 16px 0 0")}
            <div class="product-info">
                <div class="product-category">제품 효능</div>
                <div class="product-name">Before &amp; After</div>
                <div class="product-desc">부드럽고 윤기 나는 건강한 머릿결로 변화시킵니다.</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    # ═══ 헤어 미스트 ═══
    st.markdown("""
    <div style="text-align:center;margin-bottom:30px;">
        <div class="section-num">02</div>
        <div class="section-title">헤어 미스트<br><span style="font-family:'Playfair Display';font-size:1rem;color:#B8A99A;">Hair Mist</span></div>
    </div>
    """, unsafe_allow_html=True)

    m1, m2, m3, m4 = st.columns(4, gap="medium")
    with m1:
        st.markdown(f"""
        <div class="product-card">
            {img_tag("image10.png", border_radius="16px 16px 0 0")}
            <div class="product-info">
                <div class="product-category">용기 이미지</div>
                <div class="product-name">PIKIPIXI Mist</div>
                <div class="product-desc">미세한 분사로 모발 전체에 고르게 도포됩니다.</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with m2:
        st.markdown(f"""
        <div class="product-card">
            {img_tag("image7.png", border_radius="16px 16px 0 0")}
            <div class="product-info">
                <div class="product-category">용기 이미지</div>
                <div class="product-name">PUPPY</div>
                <div class="product-desc">화이트 캡의 부드럽고 감각적인 보틀 디자인.</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with m3:
        st.markdown(f"""
        <div class="product-card">
            {img_tag("image13.png", border_radius="16px 16px 0 0")}
            <div class="product-info">
                <div class="product-category">향조 설명</div>
                <div class="product-name">Warm Gourmand Note</div>
                <div class="product-desc">커피, 바닐라, 시트러스가 조화를 이루는 구르망 향조.</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with m4:
        st.markdown(f"""
        <div class="product-card">
            {img_tag("image15.png", border_radius="16px 16px 0 0")}
            <div class="product-info">
                <div class="product-category">제품 효능</div>
                <div class="product-name">Deep Care Routine</div>
                <div class="product-desc">하루 종일 촉촉한 머릿결을 유지합니다.</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="footer">© 2026 PIKIPIXI. All Rights Reserved.</div>', unsafe_allow_html=True)
