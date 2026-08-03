"""
Punto de Entrada Principal: Sistema de Apoyo a la Decisión Docente.
Prototipo de Alertas Tempranas para la Prevención de Rezago Escolar.
"""

import streamlit as st
from src.data_loader import load_base_data
from src.predictor import load_trained_models, enrich_with_predictions
from src.ui.styles import apply_custom_styles, render_header_banner
from src.ui.sidebar import render_sidebar
from src.ui.filters_bar import render_top_filters_bar
from src.ui.tab_course_mon import render_tab_course_monitoring
from src.ui.tab_student_sim import render_tab_student_simulation
from src.ui.tab_free_sim import render_tab_free_simulation


# Configuración principal de la aplicación Streamlit
st.set_page_config(
    page_title="Sistema de Alertas Tempranas - Apoyo a la Decisión Docente",
    page_icon="🏫",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main() -> None:
    # 1. Aplicar diseño visual sofisticado (Warm Academic Modern CSS)
    apply_custom_styles()
    render_header_banner()
    
    # 2. Cargar recursos de Machine Learning
    try:
        rf_model, mlp_model, scaler = load_trained_models()
    except Exception as e:
        st.error(f"❌ Error al cargar los modelos predictivos: {e}. Verifique la carpeta `modelos_entrenados`.")
        return

    # 3. Cargar dataset base
    df_data = load_base_data()
    if df_data is None:
        st.error("❌ No se pudo cargar el dataset de estudiantes.")
        return

    # 4. Renderizar la barra lateral (Uploader 2025 y Leyendas)
    df_data = render_sidebar(df_data)

    # 5. Renderizar la BARRA HORIZONTAL DE FILTROS SUPERIOR (Arriba de las Pestañas)
    modelo_sel, df_filtered, sel_gestion, gestion_predicha, sel_grado, sel_paralelo = render_top_filters_bar(df_data)

    # 6. Calcular predicciones de riesgo para el dataset filtrado
    df_filtered = enrich_with_predictions(df_filtered, modelo_sel, rf_model, mlp_model, scaler)

    # 7. Renderizar las pestañas de navegación principales
    tab1, tab2, tab3 = st.tabs([
        "📊 Monitoreo de Curso & Alertas Tempranas",
        "👤 Ficha de Estudiante & Simulador de Notas",
        "🧪 Simulador Libre"
    ])

    with tab1:
        render_tab_course_monitoring(
            df_filtered, sel_gestion, gestion_predicha, sel_grado, sel_paralelo
        )

    with tab2:
        render_tab_student_simulation(
            df_filtered, modelo_sel, rf_model, mlp_model, scaler
        )

    with tab3:
        render_tab_free_simulation(
            df_data, modelo_sel, rf_model, mlp_model, scaler
        )

if __name__ == "__main__":
    main()
