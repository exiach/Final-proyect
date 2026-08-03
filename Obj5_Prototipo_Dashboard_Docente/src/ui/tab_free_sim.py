"""
Componente UI: Tab 3 - Simulador Libre y Posicionamiento Histórico.
Permite probar cualquier combinación de promedio y materias reprobadas de forma experimental.
"""

import pandas as pd
import streamlit as st
import plotly.express as px
from typing import Any
from src.predictor import predict_student_risk


def render_tab_free_simulation(
    df_data: pd.DataFrame,
    modelo_seleccionado: str,
    rf_model: Any,
    mlp_model: Any,
    scaler: Any
) -> None:
    """
    Renderiza el simulador libre de parámetros generales.
    
    Args:
        df_data (pd.DataFrame): Dataset base para contexto histórico.
        modelo_seleccionado (str): Nombre del modelo ML.
        rf_model (Any): Modelo RF.
        mlp_model (Any): Modelo MLP.
        scaler (Any): Escalador StandardScaler.
    """
    st.markdown(
        """
        <div style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 1.35rem; font-weight: 800; color: #F8FAFC; margin-bottom: 4px;">
            🧪 Simulador Genérico Libre (Modo Experimental)
        </div>
        <div style="font-size: 0.9rem; color: #94A3B8; margin-bottom: 20px;">
            Permite probar combinaciones libres de promedio general y materias reprobadas sin seleccionar a un estudiante en específico.
        </div>
        """,
        unsafe_allow_html=True
    )
    
    c_sim1, c_sim2 = st.columns([1, 2.2])
    
    with c_sim1:
        st.markdown(
            """
            <div style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 1.05rem; font-weight: 700; color: #F8FAFC; margin-bottom: 12px;">
                ⚙️ Parámetros Manuales
            </div>
            """,
            unsafe_allow_html=True
        )
        
        prom_libre = st.slider("Promedio General (0 - 100 pts)", 0.0, 100.0, 60.0, 1.0)
        reprob_libre = st.slider("Materias Reprobadas (0 - 9)", 0, 9, 0, 1)
        
        p_lib, r_lib, c_lib, b_lib, rec_lib = predict_student_risk(
            prom_libre, reprob_libre, modelo_seleccionado, rf_model, mlp_model, scaler
        )
        
        st.markdown(
            f"""
            <div style="background: rgba(30, 41, 59, 0.7); backdrop-filter: blur(12px); border: 1px solid rgba(255,255,255,0.08); border-radius: 16px; padding: 20px; text-align: center; margin: 16px 0;">
                <div style="font-size: 0.8rem; font-weight: 600; color: #94A3B8; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 4px;">
                    Predicción de Inferencia
                </div>
                <div style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 1.5rem; font-weight: 800; color: {c_lib}; margin-bottom: 4px;">
                    {b_lib}
                </div>
                <div style="font-size: 1.1rem; font-weight: 700; color: #F8FAFC; margin-bottom: 10px;">
                    Probabilidad de Rezago: <span style="color: #38BDF8;">{p_lib*100:.1f}%</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        st.progress(float(p_lib))
        
        if r_lib == "Alto Riesgo":
            st.error(f"⚠️ **{r_lib}**: {rec_lib}")
        elif r_lib == "Medio Riesgo":
            st.warning(f"⚠️ **{r_lib}**: {rec_lib}")
        else:
            st.success(f"✅ **{r_lib}**: {rec_lib}")
            
    with c_sim2:
        st.markdown(
            """
            <div style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 1.05rem; font-weight: 700; color: #F8FAFC; margin-bottom: 12px;">
                📊 Posicionamiento respecto a Datos Históricos
            </div>
            """,
            unsafe_allow_html=True
        )
        
        df_plot = df_data.dropna(subset=["promedio_general", "num_materias_reprobadas", "rezago"]).copy()
        df_plot["Estado"] = df_plot["rezago"].map({1: "Rezago Histórico", 0: "Estable Histórico"})
        
        fig_scat = px.scatter(
            df_plot,
            x="promedio_general",
            y="num_materias_reprobadas",
            color="Estado",
            color_discrete_map={"Rezago Histórico": "#F43F5E", "Estable Histórico": "#10B981"},
            opacity=0.35,
            title="Estudiante Simulado vs. Distribución Histórica Completa"
        )
        
        fig_scat.add_scatter(
            x=[prom_libre],
            y=[reprob_libre],
            mode='markers+text',
            marker=dict(size=20, color='#38BDF8', symbol='star', line=dict(width=2, color='#FFFFFF')),
            name='Simulación Libre',
            text=["Simulado"],
            textposition="top center",
            textfont=dict(color="#38BDF8", size=13, family="Plus Jakarta Sans, sans-serif")
        )
        
        fig_scat.update_layout(
            template="plotly_dark",
            paper_bgcolor="rgba(30, 41, 59, 0.5)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(family="Inter, sans-serif", color="#E2E8F0"),
            title_font=dict(family="Plus Jakarta Sans, sans-serif", size=16, color="#F8FAFC"),
            xaxis=dict(title="Promedio General (0 - 100 pts)", gridcolor="#334155"),
            yaxis=dict(title="Cantidad de Materias Reprobadas", gridcolor="#334155"),
            margin=dict(t=50, b=20, l=20, r=20),
            legend=dict(orientation="h", yanchor="bottom", y=-0.25, xanchor="center", x=0.5)
        )
        
        st.plotly_chart(fig_scat, use_container_width=True)
