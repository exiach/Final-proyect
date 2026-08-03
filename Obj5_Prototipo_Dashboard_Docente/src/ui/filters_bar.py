"""
Componente UI: Barra Horizontal Superior de Filtros y Configuración.
Ubicada sobre las pestañas principales para ofrecer una experiencia de usuario (UX) ágil e intuitiva.
"""

import pandas as pd
import streamlit as st
from typing import Tuple, Any
from config import ORDEN_GRADOS


def sort_grado_key(g: Any) -> int:
    """Clave de ordenamiento para los grados escolares."""
    g_upper = str(g).strip().upper()
    for i, val in enumerate(ORDEN_GRADOS):
        if val in g_upper:
            return i
    return 99


def render_top_filters_bar(df_data: pd.DataFrame) -> Tuple[str, pd.DataFrame, str, str, str, str]:
    """
    Renderiza una barra horizontal superior de controles y filtros con 4 columnas.
    
    Args:
        df_data (pd.DataFrame): Dataset completo disponible.
        
    Returns:
        Tuple[str, pd.DataFrame, str, str, str, str]:
        (modelo_sel, df_filtrado, sel_gestion, gestion_predicha, sel_grado, sel_paralelo)
    """
    st.markdown(
        """
        <div style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 1.15rem; font-weight: 700; color: #F8FAFC; margin-bottom: 12px; display: flex; align-items: center; gap: 8px;">
            <span>🎛️</span> Panel de Control y Filtros de Grupo
        </div>
        """,
        unsafe_allow_html=True
    )
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        modelo_seleccionado = st.selectbox(
            "🧠 Modelo Predictivo ML",
            ["Random Forest (Recomendado)", "Red Neuronal (MLP)"],
            help="Algoritmo de IA para inferencia de riesgo."
        )
        
    with col2:
        gestiones = ["Todas"] + sorted(list(df_data['gestion'].dropna().unique().astype(str)), reverse=True)
        sel_gestion = st.selectbox(
            "📅 Gestión Base (Año)",
            gestiones,
            help="Año académico de origen sobre el cual se evalúa al estudiante."
        )
        
    with col3:
        unique_grados = sorted(list(df_data['anio_escolaridad'].dropna().unique()), key=sort_grado_key)
        grados = ["Todos"] + unique_grados
        sel_grado = st.selectbox(
            "🎓 Año de Escolaridad",
            grados,
            help="Nivel o grado escolar."
        )
        
    with col4:
        paralelos = ["Todos"] + sorted(list(df_data['paralelo'].dropna().unique()))
        sel_paralelo = st.selectbox(
            "🅰️ Paralelo",
            paralelos,
            help="Sección o paralelo del curso."
        )

    # Calcular gestión proyectada/predicha (T+1)
    if sel_gestion != "Todas" and sel_gestion.isdigit():
        gestion_predicha = str(int(sel_gestion) + 1)
    else:
        gestion_predicha = "Próximo Año"

    # Aplicar filtrado al dataset
    df_filtered = df_data.copy()
    if sel_gestion != "Todas":
        df_filtered = df_filtered[df_filtered['gestion'].astype(str) == sel_gestion]
    if sel_grado != "Todos":
        df_filtered = df_filtered[df_filtered['anio_escolaridad'] == sel_grado]
    if sel_paralelo != "Todos":
        df_filtered = df_filtered[df_filtered['paralelo'] == sel_paralelo]

    # Banner informativo de contexto seleccionado con estilo Tailwind Cyan Alert Box
    g_info = f"Gestión Base <b style='color:#38BDF8;'>{sel_gestion}</b> ➔ Alertas <b style='color:#818CF8;'>{gestion_predicha}</b>" if sel_gestion != "Todas" else "Todas las Gestiones Históricas"
    
    st.markdown(
        f"""
        <div style="background: rgba(30, 41, 59, 0.7); backdrop-filter: blur(10px); border: 1px solid rgba(56, 189, 248, 0.25); border-left: 4px solid #38BDF8; padding: 14px 20px; border-radius: 12px; margin: 16px 0 24px 0; font-size: 0.92rem; color: #CBD5E1; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 10px;">
            <div>
                <span style="font-weight: 700; color: #38BDF8; margin-right: 6px;">📍 CONTEXTO ACTIVO:</span> {g_info}
            </div>
            <div style="display: flex; gap: 16px; font-weight: 600; font-size: 0.85rem;">
                <span style="background: rgba(255,255,255,0.06); padding: 4px 10px; border-radius: 6px; border: 1px solid rgba(255,255,255,0.08);">Grado: <span style="color: #F8FAFC;">{sel_grado}</span></span>
                <span style="background: rgba(255,255,255,0.06); padding: 4px 10px; border-radius: 6px; border: 1px solid rgba(255,255,255,0.08);">Paralelo: <span style="color: #F8FAFC;">{sel_paralelo}</span></span>
                <span style="background: rgba(56, 189, 248, 0.15); color: #38BDF8; padding: 4px 10px; border-radius: 6px; border: 1px solid rgba(56, 189, 248, 0.3);">Estudiantes: <b>{len(df_filtered)}</b></span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    return modelo_seleccionado, df_filtered, sel_gestion, gestion_predicha, sel_grado, sel_paralelo
