"""
Componente UI: Tab 2 - Ficha del Estudiante y Simulador de Calificaciones.
Permite seleccionar a un alumno, ver sus materias e ingresar/modificar notas para simular el riesgo.
"""

import numpy as np
import pandas as pd
import streamlit as st
from typing import Any
from config import SUBJECT_COLS, SUBJECT_NAMES, MIN_APROBACION_NOTA
from src.predictor import predict_student_risk
from src.ui.styles import render_kpi_card


def render_tab_student_simulation(
    df_filtered: pd.DataFrame,
    modelo_seleccionado: str,
    rf_model: Any,
    mlp_model: Any,
    scaler: Any
) -> None:
    """
    Renderiza la ficha individual de un estudiante y el simulador de notas por materia.
    
    Args:
        df_filtered (pd.DataFrame): Dataset filtrado actual.
        modelo_seleccionado (str): Nombre del modelo ML.
        rf_model (Any): Modelo RF.
        mlp_model (Any): Modelo MLP.
        scaler (Any): Escalador StandardScaler.
    """
    st.markdown(
        """
        <div style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 1.35rem; font-weight: 800; color: #F8FAFC; margin-bottom: 4px;">
            👤 Seguimiento Individual y Simulador de Rendimiento
        </div>
        <div style="font-size: 0.9rem; color: #94A3B8; margin-bottom: 20px;">
            Seleccione un alumno del curso para evaluar su perfil e <b>ingresar/modificar calificaciones</b> para proyectar el impacto en su nivel de riesgo.
        </div>
        """,
        unsafe_allow_html=True
    )
    
    if df_filtered.empty:
        st.warning("⚠️ No hay estudiantes disponibles en el filtro actual.")
        return

    # 1. Selector de Alumno
    estudiantes_list = df_filtered[['nombre_completo', 'rude']].drop_duplicates()
    opciones_estudiantes = {
        f"{row['nombre_completo']} (RUDE: {row['rude']})": row['rude']
        for _, row in estudiantes_list.iterrows()
    }
    
    sel_nombre = st.selectbox("🎯 Seleccionar Estudiante:", list(opciones_estudiantes.keys()))
    sel_rude = opciones_estudiantes[sel_nombre]
    
    # Datos del estudiante seleccionado
    est_row = df_filtered[df_filtered['rude'] == sel_rude].iloc[0]
    
    st.markdown("<hr style='border-color: rgba(255,255,255,0.08); margin: 20px 0;'>", unsafe_allow_html=True)
    
    col_info1, col_info2 = st.columns([1.1, 1.9])
    
    with col_info1:
        historial_completo = bool(est_row.get('datos_completos', True))
        historial_completo = historial_completo and pd.notnull(est_row['promedio_general']) and pd.notnull(est_row['num_materias_reprobadas'])
        prom_actual = float(est_row['promedio_general']) if historial_completo else float('nan')
        reprob_actual = int(est_row['num_materias_reprobadas']) if historial_completo else None
        if historial_completo:
            p_act, r_act, c_act, b_act, rec_act = predict_student_risk(
                prom_actual, reprob_actual, modelo_seleccionado, rf_model, mlp_model, scaler
            )
            promedio_texto = f"{prom_actual:.2f} pts"
            reprobadas_texto = f"{reprob_actual} materia(s)"
            probabilidad_texto = f"{p_act*100:.1f}%"
        else:
            p_act, r_act, c_act = float('nan'), "Sin datos", "#94A3B8"
            b_act = "⚪ SIN DATOS"
            rec_act = "Completar las nueve calificaciones antes de emitir una alerta."
            promedio_texto = reprobadas_texto = probabilidad_texto = "No disponible"
        
        g_next_lbl = str(int(est_row['gestion']) + 1) if str(est_row['gestion']).isdigit() else "Próximo Año"
        
        st.markdown(
            f"""
            <div style="background: rgba(30, 41, 59, 0.7); backdrop-filter: blur(12px); border: 1px solid rgba(255,255,255,0.08); border-radius: 16px; padding: 24px; box-shadow: 0 10px 25px rgba(0,0,0,0.3);">
                <div style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 1.1rem; font-weight: 700; color: #F8FAFC; margin-bottom: 12px;">
                    🪪 Perfil Histórico (Gestión Base {est_row['gestion']})
                </div>
                <div style="font-size: 0.9rem; color: #CBD5E1; line-height: 1.8;">
                    <div><b>Nombre:</b> <span style="color: #F8FAFC;">{est_row['nombre_completo']}</span></div>
                    <div><b>RUDE:</b> <span style="color: #38BDF8;">{est_row['rude']}</span></div>
                    <div><b>Grado / Paralelo:</b> {est_row['anio_escolaridad']} - '{est_row['paralelo']}'</div>
                    <div><b>Promedio Base:</b> {promedio_texto}</div>
                    <div><b>Reprobadas Base:</b> {reprobadas_texto}</div>
                </div>
                <hr style="border-color: rgba(255,255,255,0.08); margin: 16px 0;">
                <div style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 0.95rem; font-weight: 700; color: #818CF8; margin-bottom: 8px;">
                    🔮 Proyección de Riesgo ({g_next_lbl})
                </div>
                <div style="text-align: center; margin: 12px 0;">
                    <span style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 1.4rem; font-weight: 800; color: {c_act};">{b_act}</span>
                    <div style="font-size: 0.85rem; color: #94A3B8; margin-top: 4px;">Puntaje operativo: <b>{probabilidad_texto}</b></div>
                </div>
                <div style="background: rgba(15, 23, 42, 0.6); border: 1px solid rgba(255,255,255,0.06); padding: 12px; border-radius: 10px; font-size: 0.82rem; color: #CBD5E1;">
                    💡 <b>Acción Recomendada:</b> {rec_act}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col_info2:
        if not historial_completo:
            st.warning("El registro histórico está incompleto. Los valores 60 que aparecen en materias faltantes son solo un punto de partida editable para la simulación; no constituyen una imputación ni una predicción histórica.")
        st.markdown(
            """
            <div style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 1.1rem; font-weight: 700; color: #F8FAFC; margin-bottom: 8px;">
                📝 Simulador: Ingreso / Actualización de Notas
            </div>
            <div style="font-size: 0.85rem; color: #94A3B8; margin-bottom: 16px;">
                Ajuste las calificaciones en las materias para simular el efecto de una recuperación o intervención docente:
            </div>
            """,
            unsafe_allow_html=True
        )
        
        # Formulario de calificaciones por materia
        notas_simuladas = {}
        cols_materias = st.columns(2)
        
        for idx, subj in enumerate(SUBJECT_COLS):
            val_actual = float(est_row[subj]) if (subj in est_row and pd.notnull(est_row[subj])) else 60.0
            col_idx = idx % 2
            with cols_materias[col_idx]:
                nueva_nota = st.number_input(
                    f"{SUBJECT_NAMES[subj]}",
                    min_value=0.0,
                    max_value=100.0,
                    value=round(val_actual, 1),
                    step=1.0,
                    key=f"sim_{subj}_{sel_rude}"
                )
                notas_simuladas[subj] = nueva_nota

        # Recalcular métricas de simulación
        arr_notas = np.array(list(notas_simuladas.values()))
        nuevo_promedio = float(arr_notas.mean())
        nuevas_reprobadas = int((arr_notas < MIN_APROBACION_NOTA).sum())
        
        p_sim, r_sim, c_sim, b_sim, rec_sim = predict_student_risk(
            nuevo_promedio, nuevas_reprobadas, modelo_seleccionado, rf_model, mlp_model, scaler
        )

        st.markdown("<hr style='border-color: rgba(255,255,255,0.08); margin: 20px 0;'>", unsafe_allow_html=True)
        st.markdown(
            f"""
            <div style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 1.05rem; font-weight: 700; color: #F8FAFC; margin-bottom: 12px;">
                🔄 Proyección Posterior a la Intervención ({g_next_lbl})
            </div>
            """,
            unsafe_allow_html=True
        )
        
        sim_col1, sim_col2, sim_col3 = st.columns(3)
        delta_prom = nuevo_promedio - prom_actual if historial_completo else None
        delta_reprob = nuevas_reprobadas - reprob_actual if historial_completo else None
        delta_prob = (p_sim - p_act) * 100 if historial_completo else None
        
        with sim_col1:
            detalle = f"Diferencia: {delta_prom:+.2f}" if historial_completo else "Sin base comparable"
            st.markdown(render_kpi_card("Nuevo Promedio", f"{nuevo_promedio:.2f} pts", "cyan", detalle), unsafe_allow_html=True)
        with sim_col2:
            detalle = f"Diferencia: {delta_reprob:+d}" if historial_completo else "Sin base comparable"
            st.markdown(render_kpi_card("Reprobadas", f"{nuevas_reprobadas}", "amber" if nuevas_reprobadas > 0 else "emerald", detalle), unsafe_allow_html=True)
        with sim_col3:
            acc_c = "cyan" if not historial_completo else ("emerald" if p_sim < p_act else ("rose" if p_sim > p_act else "cyan"))
            detalle = f"Cambio: {delta_prob:+.1f}%" if historial_completo else "Simulación sin base histórica"
            st.markdown(render_kpi_card("Nuevo Puntaje Operativo", f"{p_sim*100:.1f}%", acc_c, detalle), unsafe_allow_html=True)
        
        st.markdown("<div style='margin-top: 16px;'></div>", unsafe_allow_html=True)
        if not historial_completo:
            st.info(f"Resultado simulado: **{r_sim}** ({b_sim}). {rec_sim}")
        elif p_sim < p_act:
            st.success(f"🎉 **¡Mejora Proyectada!** El nivel de riesgo se reduce a **{r_sim}** ({b_sim}). {rec_sim}")
        elif p_sim > p_act:
            st.error(f"⚠️ **Alerta:** Las calificaciones simuladas aumentan la probabilidad de rezago a **{r_sim}** ({b_sim}).")
        else:
            st.info("No se observan cambios en la categoría de riesgo.")
