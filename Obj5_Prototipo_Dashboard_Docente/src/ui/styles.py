"""
Módulo de Estilos Customizados (Inspirado en Tailwind CSS - tailwindcss.com).
Proporciona tema oscuro Slate/Zinc, tipografía Inter & Plus Jakarta Sans,
gradientes neón (Cyan, Indigo, Purple), tarjetas Glassmorphic y badges nítidos.
"""

import streamlit as st


def apply_custom_styles() -> None:
    """Inyecta CSS global avanzado con estética idéntica a tailwindcss.com."""
    st.markdown(
        """
        <style>
        /* 1. Fuentes Modernas (Inter & Plus Jakarta Sans) */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap');

        html, body, [class*="css"], .stApp {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
            background-color: #0F172A !important;
            color: #F8FAFC !important;
        }

        /* Fondo general con patrón sutil de malla radial estilo Tailwind */
        .stApp {
            background-image: 
                radial-gradient(at 0% 0%, rgba(56, 189, 248, 0.07) 0px, transparent 50%),
                radial-gradient(at 100% 0%, rgba(129, 140, 248, 0.07) 0px, transparent 50%),
                radial-gradient(at 50% 100%, rgba(192, 132, 252, 0.04) 0px, transparent 50%) !important;
            background-attachment: fixed !important;
        }

        /* 2. Banner Principal con Gradiente de Texto e Iluminación Tailwind */
        .tailwind-header-banner {
            position: relative;
            background: linear-gradient(135deg, rgba(30, 41, 59, 0.85) 0%, rgba(15, 23, 42, 0.95) 100%);
            backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 20px;
            padding: 28px 36px;
            margin-bottom: 28px;
            box-shadow: 0 20px 35px -10px rgba(0, 0, 0, 0.5), 0 0 20px rgba(56, 189, 248, 0.05);
            overflow: hidden;
        }

        .tailwind-header-banner::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 2px;
            background: linear-gradient(90deg, #38BDF8 0%, #818CF8 50%, #C084FC 100%);
        }

        .tailwind-header-title {
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            font-size: 2.25rem !important;
            font-weight: 800 !important;
            letter-spacing: -0.03em !important;
            background: linear-gradient(135deg, #38BDF8 0%, #818CF8 40%, #C084FC 100%);
            -webkit-background-clip: text !important;
            -webkit-text-fill-color: transparent !important;
            margin: 0 0 8px 0 !important;
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .tailwind-header-subtitle {
            font-size: 1.05rem;
            color: #94A3B8 !important;
            margin: 0;
            font-weight: 400;
            line-height: 1.5;
        }

        .tailwind-badge-pill {
            background: rgba(56, 189, 248, 0.1);
            color: #38BDF8;
            border: 1px solid rgba(56, 189, 248, 0.25);
            padding: 4px 12px;
            border-radius: 9999px;
            font-size: 0.75rem;
            font-weight: 700;
            letter-spacing: 0.05em;
            text-transform: uppercase;
            display: inline-block;
            margin-bottom: 10px;
        }

        /* 3. Badges de Alerta (Rose, Amber, Emerald) Estilo Tailwind */
        .badge-alto {
            background-color: rgba(244, 63, 94, 0.12) !important;
            color: #FB7185 !important;
            border: 1px solid rgba(244, 63, 94, 0.3) !important;
            padding: 4px 12px !important;
            border-radius: 9999px !important;
            font-weight: 700 !important;
            font-size: 0.8rem !important;
            display: inline-flex !important;
            align-items: center !important;
            gap: 6px !important;
        }

        .badge-medio {
            background-color: rgba(245, 158, 11, 0.12) !important;
            color: #FBBF24 !important;
            border: 1px solid rgba(245, 158, 11, 0.3) !important;
            padding: 4px 12px !important;
            border-radius: 9999px !important;
            font-weight: 700 !important;
            font-size: 0.8rem !important;
            display: inline-flex !important;
            align-items: center !important;
            gap: 6px !important;
        }

        .badge-bajo {
            background-color: rgba(16, 185, 129, 0.12) !important;
            color: #34D399 !important;
            border: 1px solid rgba(16, 185, 129, 0.3) !important;
            padding: 4px 12px !important;
            border-radius: 9999px !important;
            font-weight: 700 !important;
            font-size: 0.8rem !important;
            display: inline-flex !important;
            align-items: center !important;
            gap: 6px !important;
        }

        /* 4. Tarjetas KPI / Métricas Personalizadas */
        .tailwind-kpi-card {
            background: rgba(30, 41, 59, 0.7);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 16px;
            padding: 20px 24px;
            transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
            position: relative;
            overflow: hidden;
        }

        .tailwind-kpi-card:hover {
            transform: translateY(-2px);
            border-color: rgba(56, 189, 248, 0.3);
            box-shadow: 0 12px 25px -5px rgba(0, 0, 0, 0.4), 0 0 15px rgba(56, 189, 248, 0.1);
        }

        .tailwind-kpi-card.accent-cyan { border-top: 3px solid #38BDF8; }
        .tailwind-kpi-card.accent-rose { border-top: 3px solid #F43F5E; }
        .tailwind-kpi-card.accent-amber { border-top: 3px solid #F59E0B; }
        .tailwind-kpi-card.accent-emerald { border-top: 3px solid #10B981; }

        .tailwind-kpi-label {
            font-size: 0.875rem;
            font-weight: 600;
            color: #94A3B8;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 6px;
        }

        .tailwind-kpi-value {
            font-family: 'Plus Jakarta Sans', sans-serif;
            font-size: 2.25rem;
            font-weight: 800;
            color: #F8FAFC;
            line-height: 1.1;
        }

        /* 5. Personalización de Pestañas (st.tabs) Estilo Navbar Tailwind */
        .stTabs [data-baseweb="tab-list"] {
            gap: 12px !important;
            background-color: rgba(30, 41, 59, 0.5) !important;
            padding: 6px !important;
            border-radius: 14px !important;
            border: 1px solid rgba(255, 255, 255, 0.06) !important;
        }

        .stTabs [data-baseweb="tab"] {
            border-radius: 10px !important;
            color: #94A3B8 !important;
            font-weight: 600 !important;
            font-size: 0.95rem !important;
            padding: 10px 20px !important;
            transition: all 0.2s ease !important;
            border: none !important;
            background-color: transparent !important;
        }

        .stTabs [aria-selected="true"] {
            background-color: rgba(56, 189, 248, 0.15) !important;
            color: #38BDF8 !important;
            border: 1px solid rgba(56, 189, 248, 0.3) !important;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2) !important;
        }

        /* 6. Inputs, Selectboxes & Sliders */
        div[data-baseweb="select"] > div {
            background-color: #1E293B !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            border-radius: 10px !important;
            color: #F8FAFC !important;
        }

        div[data-baseweb="select"] > div:hover {
            border-color: #38BDF8 !important;
        }

        input[type="number"] {
            background-color: #1E293B !important;
            color: #F8FAFC !important;
            border-radius: 10px !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
        }

        /* 7. Tablas y Dataframes */
        [data-testid="stDataFrame"] {
            background: #1E293B !important;
            border-radius: 14px !important;
            border: 1px solid rgba(255, 255, 255, 0.08) !important;
            overflow: hidden !important;
        }

        /* 8. Contenedores y Alertas */
        div.stAlert {
            border-radius: 12px !important;
            backdrop-filter: blur(10px) !important;
        }

        /* 9. Barra Lateral (Sidebar) */
        [data-testid="stSidebar"] {
            background-color: #0B0F19 !important;
            border-right: 1px solid rgba(255, 255, 255, 0.06) !important;
        }

        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
        """,
        unsafe_allow_html=True
    )


def render_header_banner() -> None:
    """Renderiza el banner superior con estilo visual idéntico a Tailwind CSS."""
    st.markdown(
        """
        <div class="tailwind-header-banner">
            <span class="tailwind-badge-pill">Plataforma de Inteligencia Educativa v2.5</span>
            <h1 class="tailwind-header-title">🏫 Sistema de Apoyo a la Decisión Docente</h1>
            <p class="tailwind-header-subtitle">
                Modelado predictivo e inferencia de Machine Learning para la prevención y detección temprana del rezago escolar en Educación Primaria.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


def render_kpi_card(title: str, value: str, accent_color: str = "cyan", subtext: str = "") -> str:
    """
    Retorna el código HTML para renderizar una tarjeta KPI con estilo Tailwind.
    Accent colors: 'cyan', 'rose', 'amber', 'emerald'.
    """
    sub_html = f"<div style='font-size: 0.78rem; color: #64748B; margin-top: 4px;'>{subtext}</div>" if subtext else ""
    return f"""
    <div class="tailwind-kpi-card accent-{accent_color}">
        <div class="tailwind-kpi-label">{title}</div>
        <div class="tailwind-kpi-value">{value}</div>
        {sub_html}
    </div>
    """
