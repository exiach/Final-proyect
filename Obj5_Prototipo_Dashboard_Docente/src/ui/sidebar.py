"""
Componente UI: Barra Lateral Simplificada.
Dedicada a la carga de archivos de nuevas gestiones (2025) y leyendas normativas estilo Tailwind Docs Sidebar.
"""

import pandas as pd
import streamlit as st
from config import PALETA_RIESGO
from src.data_loader import merge_uploaded_data


def render_sidebar(df_data: pd.DataFrame) -> pd.DataFrame:
    """
    Renderiza la barra lateral simplificada con uploader de archivos e información.
    
    Args:
        df_data (pd.DataFrame): Dataset base actual.
        
    Returns:
        pd.DataFrame: Dataset actualizado (si se cargaron nuevos datos).
    """
    st.sidebar.markdown(
        """
        <div style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 1.1rem; font-weight: 700; color: #F8FAFC; margin-bottom: 16px; border-bottom: 1px solid rgba(255,255,255,0.08); padding-bottom: 8px;">
            ⚙️ Herramientas de Carga
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # 1. Carga dinámica de una nueva gestión desde la interfaz
    st.sidebar.markdown(
        """
        <div style="font-size: 0.85rem; font-weight: 600; color: #38BDF8; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 6px;">
            📂 Cargar Datos de Nueva Gestión
        </div>
        """,
        unsafe_allow_html=True
    )
    
    uploaded_file = st.sidebar.file_uploader(
        "Subir boletín/dataset (CSV o XLSX):",
        type=["csv", "xlsx"],
        help="El archivo debe incluir la columna gestión, los metadatos requeridos y las nueve calificaciones completas."
    )
    
    df_current = df_data.copy()
    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith(".csv"):
                df_up = pd.read_csv(uploaded_file)
            else:
                df_up = pd.read_excel(uploaded_file)
            
            df_current = merge_uploaded_data(df_current, df_up)
            st.sidebar.success(f"✅ ¡Se cargaron registros para la gestión {df_up['gestion'].iloc[0]}!")
        except Exception as ex:
            st.sidebar.error(f"⚠️ Error al procesar archivo: {ex}")

    # 2. Leyenda y Guía Normativa de Alertas
    st.sidebar.markdown("<hr style='border-color: rgba(255,255,255,0.08); margin: 20px 0;'>", unsafe_allow_html=True)
    
    st.sidebar.markdown(
        """
        <div style="font-size: 0.85rem; font-weight: 600; color: #818CF8; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 12px;">
            ℹ️ Leyenda de Alertas Tempranas
        </div>
        """,
        unsafe_allow_html=True
    )
    
    for cat, info in PALETA_RIESGO.items():
        badge_cls = {
            "Alto Riesgo": "badge-alto",
            "Medio Riesgo": "badge-medio",
            "Bajo Riesgo": "badge-bajo",
            "Sin datos": "",
        }[cat]
        st.sidebar.markdown(
            f"""
            <div style="background: rgba(30, 41, 59, 0.6); border: 1px solid rgba(255,255,255,0.06); padding: 12px; border-radius: 10px; margin-bottom: 10px;">
                <span class="{badge_cls}" style="margin-bottom: 6px;">{info['badge']}</span>
                <div style="font-size: 0.82rem; color: #94A3B8; margin-top: 6px; line-height: 1.4;">{info['rec']}</div>
            </div>
            """,
            unsafe_allow_html=True
        )
        
    return df_current
