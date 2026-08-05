from __future__ import annotations

import textwrap

import streamlit as st


def html(content: str) -> None:
    """Render HTML directly without Markdown interpreting indentation."""

    cleaned = textwrap.dedent(content).strip()
    st.html(cleaned)


def apply_styles() -> None:
    html(
        """
        <style>
        :root {
            --ink: #15213B;
            --muted: #69758C;
            --primary: #5B6CFF;
            --secondary: #8255E8;
            --cyan: #20C8E8;
            --surface: #FFFFFF;
            --background: #F6F8FF;
            --line: #E6EAF3;
        }

        html, body, [class*="css"] {
            font-family: Inter, ui-sans-serif, system-ui, -apple-system,
                         BlinkMacSystemFont, "Segoe UI", sans-serif;
        }

        .stApp {
            color: var(--ink);
            background:
                radial-gradient(circle at 7% 4%, rgba(91,108,255,.13), transparent 25%),
                radial-gradient(circle at 94% 5%, rgba(130,85,232,.13), transparent 25%),
                linear-gradient(180deg, #FBFCFF 0%, var(--background) 100%);
        }

        .block-container {
            max-width: 1240px;
            padding-top: 1.1rem;
            padding-bottom: 4rem;
        }

        header[data-testid="stHeader"] {
            background: transparent;
            height: 0;
        }

        #MainMenu, footer, [data-testid="stToolbar"] {
            visibility: hidden;
        }

        h1, h2, h3, h4, p, label {
            color: var(--ink);
        }

        .topbar {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: .85rem 1.05rem;
            margin-bottom: 1.15rem;
            border-radius: 20px;
            background: rgba(255,255,255,.90);
            border: 1px solid rgba(255,255,255,.97);
            box-shadow: 0 12px 34px rgba(30,41,59,.08);
            backdrop-filter: blur(15px);
        }

        .brand {
            display: flex;
            align-items: center;
            gap: .8rem;
        }

        .brand-logo {
            width: 46px;
            height: 46px;
            border-radius: 15px;
            display: grid;
            place-items: center;
            color: white;
            font-size: 1.25rem;
            font-weight: 900;
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            box-shadow: 0 12px 28px rgba(91,108,255,.28);
        }

        .brand-title {
            font-size: 1.18rem;
            font-weight: 900;
            line-height: 1.1;
            letter-spacing: -.02em;
        }

        .brand-subtitle {
            color: var(--muted);
            font-size: .78rem;
            margin-top: .2rem;
        }

        .hero {
            display: grid;
            grid-template-columns: 1.35fr .65fr;
            gap: 1.3rem;
            padding: 2.8rem;
            border-radius: 30px;
            overflow: hidden;
            position: relative;
            background:
                radial-gradient(circle at 80% 20%, rgba(255,255,255,.20), transparent 24%),
                linear-gradient(135deg, #365CFF 0%, #7047EF 56%, #9A4DE0 100%);
            box-shadow: 0 28px 68px rgba(72,70,200,.24);
        }

        .hero-copy {
            position: relative;
            z-index: 2;
        }

        .hero-badge {
            display: inline-flex;
            padding: .42rem .75rem;
            border-radius: 999px;
            color: white;
            font-size: .8rem;
            font-weight: 750;
            background: rgba(255,255,255,.14);
            border: 1px solid rgba(255,255,255,.22);
            margin-bottom: 1.1rem;
        }

        .hero h1 {
            color: white !important;
            font-size: clamp(2.8rem, 5vw, 4.7rem);
            line-height: .98;
            letter-spacing: -.055em;
            margin: 0 0 1rem;
        }

        .hero p {
            color: rgba(255,255,255,.92) !important;
            font-size: 1.06rem;
            line-height: 1.7;
            max-width: 720px;
        }

        .hero-panel {
            position: relative;
            z-index: 2;
            align-self: center;
            padding: 1.2rem;
            border-radius: 22px;
            background: rgba(255,255,255,.14);
            border: 1px solid rgba(255,255,255,.22);
            backdrop-filter: blur(14px);
        }

        .hero-stat {
            padding: .85rem 0;
            color: white;
            border-bottom: 1px solid rgba(255,255,255,.14);
        }

        .hero-stat:last-child {
            border-bottom: none;
        }

        .hero-stat strong {
            display: block;
            font-size: 1.38rem;
        }

        .hero-stat span {
            color: rgba(255,255,255,.78);
            font-size: .82rem;
        }

        .feature-card {
            height: 100%;
            min-height: 175px;
            padding: 1.35rem;
            border-radius: 22px;
            background: white;
            border: 1px solid var(--line);
            box-shadow: 0 12px 34px rgba(30,41,59,.07);
        }

        .feature-icon {
            width: 44px;
            height: 44px;
            border-radius: 14px;
            display: grid;
            place-items: center;
            margin-bottom: .9rem;
            background: linear-gradient(
                135deg,
                rgba(91,108,255,.12),
                rgba(130,85,232,.12)
            );
            font-size: 1.18rem;
        }

        .feature-card h3 {
            margin: .1rem 0 .45rem;
            font-size: 1.02rem;
        }

        .feature-card p {
            margin: 0;
            color: var(--muted) !important;
            font-size: .91rem;
            line-height: 1.55;
        }

        .page-label {
            color: var(--primary);
            font-size: .78rem;
            font-weight: 900;
            letter-spacing: .12em;
            text-transform: uppercase;
        }

        .page-title {
            font-size: 2.2rem;
            font-weight: 950;
            letter-spacing: -.04em;
            margin: .2rem 0 .3rem;
        }

        .page-subtitle {
            color: var(--muted);
            margin-bottom: 1.3rem;
        }

        .steps {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: .75rem;
            margin: .9rem 0 1.25rem;
        }

        .step-card {
            padding: .9rem 1rem;
            border-radius: 16px;
            background: white;
            border: 1px solid var(--line);
            color: var(--muted);
            font-size: .87rem;
            font-weight: 750;
            box-shadow: 0 8px 24px rgba(30,41,59,.04);
        }

        .step-card b {
            color: var(--primary);
            margin-right: .35rem;
        }

        div[data-testid="stForm"] {
            padding: 1.4rem;
            border-radius: 24px;
            background: white;
            border: 1px solid var(--line);
            box-shadow: 0 16px 48px rgba(30,41,59,.07);
        }

        button[data-baseweb="tab"] {
            color: var(--muted) !important;
            font-weight: 760 !important;
        }

        button[data-baseweb="tab"][aria-selected="true"] {
            color: var(--primary) !important;
        }

        div[data-baseweb="select"] > div {
            background: white !important;
            color: var(--ink) !important;
            border-color: #DDE3EE !important;
            border-radius: 12px !important;
        }

        div[data-baseweb="select"] span,
        div[role="option"] {
            color: var(--ink) !important;
        }

        div[role="listbox"] {
            background: white !important;
        }

        div.stButton > button,
        div[data-testid="stFormSubmitButton"] > button {
            width: 100%;
            min-height: 49px;
            color: white !important;
            font-weight: 850;
            border: 0;
            border-radius: 14px;
            background: linear-gradient(90deg, var(--primary), var(--secondary));
            box-shadow: 0 12px 30px rgba(91,108,255,.24);
        }

        .result-grid {
            display: grid;
            grid-template-columns: .78fr 1.22fr;
            gap: 1rem;
            padding: 1.2rem;
            border-radius: 26px;
            background: white;
            border: 1px solid var(--line);
            box-shadow: 0 18px 50px rgba(30,41,59,.08);
            margin-top: 1rem;
        }

        .score-card {
            padding: 1.35rem;
            border-radius: 20px;
            background: linear-gradient(
                145deg,
                rgba(91,108,255,.08),
                rgba(130,85,232,.08)
            );
            border: 1px solid rgba(91,108,255,.14);
        }

        .score-label {
            color: var(--muted);
            font-size: .78rem;
            text-transform: uppercase;
            letter-spacing: .1em;
            font-weight: 850;
        }

        .score-value {
            font-size: 4.3rem;
            line-height: 1;
            font-weight: 950;
            letter-spacing: -.075em;
            margin: .65rem 0 .25rem;
            background: linear-gradient(90deg, var(--primary), var(--secondary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .score-scale {
            color: var(--muted);
            font-size: .88rem;
        }

        .risk-pill {
            display: inline-flex;
            margin-top: .95rem;
            padding: .58rem .82rem;
            border-radius: 999px;
            font-weight: 850;
        }

        .risk-high {
            background: #FEE4E2;
            color: #B42318;
            border: 1px solid #FDA29B;
        }

        .risk-medium {
            background: #FEF0C7;
            color: #B54708;
            border: 1px solid #FEC84B;
        }

        .risk-low {
            background: #D1FADF;
            color: #027A48;
            border: 1px solid #6CE9A6;
        }

        .summary-card {
            padding: 1.35rem;
            border-radius: 20px;
            background: #FAFBFF;
            border: 1px solid var(--line);
        }

        .summary-card p {
            color: var(--muted) !important;
            line-height: 1.65;
        }

        .insight-card {
            padding: .92rem 1rem;
            border-radius: 15px;
            background: white;
            border: 1px solid var(--line);
            margin-bottom: .65rem;
            box-shadow: 0 7px 20px rgba(30,41,59,.04);
        }

        .action-card {
            display: grid;
            grid-template-columns: 40px 1fr;
            gap: .8rem;
            padding: 1rem;
            border-radius: 17px;
            background: linear-gradient(
                135deg,
                rgba(91,108,255,.08),
                rgba(130,85,232,.08)
            );
            border: 1px solid rgba(91,108,255,.14);
            margin-bottom: .7rem;
        }

        .action-number {
            width: 36px;
            height: 36px;
            display: grid;
            place-items: center;
            border-radius: 12px;
            color: white;
            font-weight: 850;
            background: linear-gradient(135deg, var(--primary), var(--secondary));
        }

        .edubot {
            padding: 1.25rem 1.35rem;
            border-radius: 20px;
            color: white;
            background: linear-gradient(135deg, #172554, #4338CA 58%, #7C3AED);
            box-shadow: 0 18px 45px rgba(49,46,129,.18);
        }

        .edubot h3,
        .edubot p {
            color: white !important;
        }

        .edubot-tag {
            display: inline-flex;
            padding: .35rem .6rem;
            border-radius: 999px;
            background: rgba(255,255,255,.14);
            border: 1px solid rgba(255,255,255,.18);
            font-size: .76rem;
            font-weight: 750;
            margin-bottom: .65rem;
        }

        @media (max-width: 850px) {
            .hero,
            .result-grid {
                grid-template-columns: 1fr;
            }

            .steps {
                grid-template-columns: 1fr;
            }

            .hero {
                padding: 2rem;
            }
        }
        </style>
        """
    )


def render_topbar() -> None:
    html(
        """
        <div class="topbar">
            <div class="brand">
                <div class="brand-logo">↗</div>
                <div>
                    <div class="brand-title">EduPath AI</div>
                    <div class="brand-subtitle">
                        Predice hoy. Impulsa el mañana.
                    </div>
                </div>
            </div>
        </div>
        """
    )
