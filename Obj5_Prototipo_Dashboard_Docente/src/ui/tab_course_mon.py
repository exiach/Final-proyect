"""
Componente UI: Tab 1 - Monitoreo de Curso y Alertas Tempranas.
Renderiza métricas KPI con estética Tailwind, tabla de alertas ordenable y gráficos oscuros Plotly.
"""

import pandas as pd
import streamlit as st
import plotly.express as px
from config import SUBJECT_COLS, SUBJECT_NAMES
from src.ui.styles import render_kpi_card
from src.privacy import public_student_code


def render_tab_course_monitoring(
    df_filtered: pd.DataFrame,
    sel_gestion: str,
    gestion_predicha: str,
    sel_grado: str,
    sel_paralelo: str
) -> None:
    """
    Renderiza el contenido de la pestaña de monitoreo consolidado por curso.
    
    Args:
        df_filtered (pd.DataFrame): Dataset filtrado de estudiantes con predicciones.
        sel_gestion (str): Gestión base seleccionada.
        gestion_predicha (str): Gestión predicha (T+1).
        sel_grado (str): Grado seleccionado.
        sel_paralelo (str): Paralelo seleccionado.
    """
    st.markdown(
        f"""
        <div style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 1.35rem; font-weight: 800; color: #F8FAFC; margin-bottom: 4px;">
            📋 Alertas Tempranas Proyectadas para {gestion_predicha}
        </div>
        <div style="font-size: 0.9rem; color: #94A3B8; margin-bottom: 20px;">
            📌 Basado en datos históricos de la <b>Gestión Base {sel_gestion}</b> | 
            <b>Grado:</b> {sel_grado} | <b>Paralelo:</b> {sel_paralelo} 
            ({len(df_filtered)} estudiantes evaluados)
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # 1. Tarjetas de Métricas (KPIs Estilo Tailwind)
    total_estudiantes = len(df_filtered)
    alto_cnt = (df_filtered['nivel_riesgo'] == "Alto Riesgo").sum()
    medio_cnt = (df_filtered['nivel_riesgo'] == "Medio Riesgo").sum()
    bajo_cnt = (df_filtered['nivel_riesgo'] == "Bajo Riesgo").sum()
    sin_datos_cnt = (df_filtered['nivel_riesgo'] == "Sin datos").sum()
    
    col_kpi1, col_kpi2, col_kpi3, col_kpi4 = st.columns(4)
    with col_kpi1:
        detalle_total = f"Gestión {sel_gestion} · {sin_datos_cnt} sin datos" if sin_datos_cnt else f"Gestión {sel_gestion}"
        st.markdown(render_kpi_card("Total Alumnos", str(total_estudiantes), "cyan", detalle_total), unsafe_allow_html=True)
    with col_kpi2:
        st.markdown(render_kpi_card(f"🔴 Alto Riesgo ({gestion_predicha})", str(alto_cnt), "rose", f"{(alto_cnt/total_estudiantes*100):.1f}% del grupo" if total_estudiantes > 0 else "0%"), unsafe_allow_html=True)
    with col_kpi3:
        st.markdown(render_kpi_card(f"🟡 Alerta Temprana ({gestion_predicha})", str(medio_cnt), "amber", f"{(medio_cnt/total_estudiantes*100):.1f}% del grupo" if total_estudiantes > 0 else "0%"), unsafe_allow_html=True)
    with col_kpi4:
        st.markdown(render_kpi_card(f"🟢 Bajo Riesgo ({gestion_predicha})", str(bajo_cnt), "emerald", f"{(bajo_cnt/total_estudiantes*100):.1f}% del grupo" if total_estudiantes > 0 else "0%"), unsafe_allow_html=True)
    
    st.markdown("<hr style='border-color: rgba(255,255,255,0.08); margin: 24px 0;'>", unsafe_allow_html=True)
    
    # 2. Filtro de Riesgo para la Tabla
    col_tb1, col_tb2 = st.columns([1.2, 2.8])
    with col_tb1:
        filtro_riesgo_tb = st.multiselect(
            "Filtrar Alertas de la Tabla:",
            ["Alto Riesgo", "Medio Riesgo", "Bajo Riesgo", "Sin datos"],
            default=["Alto Riesgo", "Medio Riesgo", "Bajo Riesgo", "Sin datos"]
        )
    
    df_tabla = df_filtered[df_filtered['nivel_riesgo'].isin(filtro_riesgo_tb)].copy()
    
    if not df_tabla.empty:
        lbl_base = f"Base {sel_gestion}" if sel_gestion != "Todas" else "Año Base"
        df_display = pd.DataFrame({
            f"Alerta ({gestion_predicha})": df_tabla['badge_riesgo'],
            "Nombre del Estudiante": df_tabla['nombre_completo'],
            "Código seudónimo": df_tabla['rude'].map(public_student_code),
            "Grado": df_tabla['anio_escolaridad'],
            "Paralelo": df_tabla['paralelo'],
            f"Promedio ({lbl_base})": df_tabla['promedio_general'].round(2),
            f"Reprobadas ({lbl_base})": df_tabla['num_materias_reprobadas'].astype('Int64'),
            f"Prob. Rezago {gestion_predicha} (%)": (df_tabla['prob_rezago'] * 100).round(1),
            "Prob. del modelo (%)": (df_tabla['prob_modelo'] * 100).round(1),
            "Motivo de la alerta": df_tabla['motivo_alerta'],
            "Acción Pedagógica Recomendada": df_tabla['recomendacion']
        }).sort_values(by=f"Prob. Rezago {gestion_predicha} (%)", ascending=False)
        
        st.dataframe(df_display, use_container_width=True, hide_index=True)
    else:
        st.info("No se encontraron estudiantes para los filtros de riesgo seleccionados.")

    # 3. Visualizaciones Gráficas con Tema Oscuro Tailwind
    st.markdown("<hr style='border-color: rgba(255,255,255,0.08); margin: 28px 0;'>", unsafe_allow_html=True)
    st.markdown(
        """
        <div style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 1.25rem; font-weight: 700; color: #F8FAFC; margin-bottom: 16px;">
            📈 Análisis de Riesgo y Rendimiento del Grupo
        </div>
        """,
        unsafe_allow_html=True
    )
    g_col1, g_col2 = st.columns(2)
    
    with g_col1:
        fig_pie = px.pie(
            df_filtered,
            names='nivel_riesgo',
            title=f"Distribución de Riesgo ({gestion_predicha})",
            color='nivel_riesgo',
            color_discrete_map={
                "Alto Riesgo": "#F43F5E",
                "Medio Riesgo": "#F59E0B",
                "Bajo Riesgo": "#10B981"
                ,"Sin datos": "#94A3B8"
            },
            hole=0.55
        )
        fig_pie.update_layout(
            template="plotly_dark",
            paper_bgcolor="rgba(30, 41, 59, 0.5)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(family="Inter, sans-serif", color="#E2E8F0"),
            title_font=dict(family="Plus Jakarta Sans, sans-serif", size=16, color="#F8FAFC"),
            margin=dict(t=50, b=20, l=20, r=20),
            legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5)
        )
        st.plotly_chart(fig_pie, use_container_width=True)
        
    with g_col2:
        subjs_present = [c for c in SUBJECT_COLS if c in df_filtered.columns]
        if subjs_present:
            promedios_materias = df_filtered[subjs_present].mean().reset_index()
            promedios_materias.columns = ['Codigo', 'Promedio']
            promedios_materias['Materia'] = promedios_materias['Codigo'].map(SUBJECT_NAMES)
            promedios_materias = promedios_materias.sort_values(by='Promedio')
            
            fig_bar = px.bar(
                promedios_materias,
                x='Promedio',
                y='Materia',
                orientation='h',
                title="Promedio General por Materia",
                color='Promedio',
                color_continuous_scale=[[0, '#F43F5E'], [0.5, '#F59E0B'], [1.0, '#38BDF8']]
            )
            fig_bar.add_vline(x=51, line_dash="dash", line_color="#F43F5E", annotation_text="Aprobación (51 pts)", annotation_font_color="#F43F5E")
            fig_bar.update_layout(
                template="plotly_dark",
                paper_bgcolor="rgba(30, 41, 59, 0.5)",
                plot_bgcolor="rgba(0,0,0,0)",
                font=dict(family="Inter, sans-serif", color="#E2E8F0"),
                title_font=dict(family="Plus Jakarta Sans, sans-serif", size=16, color="#F8FAFC"),
                xaxis=dict(title="Promedio (0 - 100)", gridcolor="#334155"),
                yaxis=dict(title="", gridcolor="#334155"),
                margin=dict(t=50, b=20, l=20, r=20),
                coloraxis_showscale=False
            )
            st.plotly_chart(fig_bar, use_container_width=True)
