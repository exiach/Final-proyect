import streamlit as st
import pandas as pd
import joblib
import os
import plotly.express as px

# Configuración principal
st.set_page_config(page_title="Alerta Docente", page_icon="📚", layout="wide")

# Rutas a los recursos
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODELS_DIR = os.path.join(BASE_DIR, "../modelos_entrenados")
DATA_PATH = os.path.join(BASE_DIR, "../data/03_Datasets_Procesados/primaria_03_Datasets_Procesados.csv")

@st.cache_resource
def load_modelos_entrenados():
    """Carga los modelos entrenados y el escalador desde la carpeta modelos_entrenados/"""
    rf_model = joblib.load(os.path.join(MODELS_DIR, "random_forest_model.pkl"))
    mlp_model = joblib.load(os.path.join(MODELS_DIR, "mlp_model.pkl"))
    scaler = joblib.load(os.path.join(MODELS_DIR, "scaler.pkl"))
    return rf_model, mlp_model, scaler

@st.cache_data
def load_data():
    """Carga los datos históricos para contexto visual"""
    if os.path.exists(DATA_PATH):
        df = pd.read_csv(DATA_PATH)
        return df
    return None

def main():
    st.title("📚 Sistema de Prevención de Rezago Académico")
    st.markdown("Prototipo de apoyo a la decisión docente para la identificación temprana de estudiantes en riesgo, parte de los objetivos del diplomado.")

    # Intentar cargar los modelos
    try:
        rf_model, mlp_model, scaler = load_modelos_entrenados()
    except Exception as e:
        st.error(f"No se pudieron cargar los modelos: {e}. Asegurate de ejecutar la libreta 06_modelo_redes_neuronales.ipynb primero.")
        return

    # Cargar datos históricos
    df = load_data()
    
    # --- BARRA LATERAL (ENTRADAS) ---
    st.sidebar.header("Parámetros del Estudiante")
    st.sidebar.markdown("Ingrese el desempeño del estudiante en el año anterior:")
    
    promedio = st.sidebar.slider("Promedio General (Año Previo)", 0.0, 100.0, 60.0, 1.0)
    reprobadas = st.sidebar.slider("Materias Reprobadas (Año Previo)", 0, 9, 0, 1)
    
    modelo_seleccionado = st.sidebar.selectbox(
        "Seleccione el Modelo Predictivo", 
        ["Random Forest (Recomendado)", "Red Neuronal (MLP)"]
    )

    # --- LÓGICA DE PREDICCIÓN ---
    input_data = pd.DataFrame({
        "promedio_general_prev": [promedio],
        "num_materias_reprobadas_prev": [reprobadas]
    })
    
    if "Random Forest" in modelo_seleccionado:
        prob = rf_model.predict_proba(input_data)[0][1]
    else:
        input_scaled = scaler.transform(input_data)
        prob = mlp_model.predict_proba(input_scaled)[0][1]
        
    # --- CATEGORIZACIÓN ---
    if prob >= 0.7:
        riesgo = "Alto"
        color = "#ff4b4b"
    elif prob >= 0.4:
        riesgo = "Medio"
        color = "#ffa421"
    else:
        riesgo = "Bajo"
        color = "#00c04b"

    # --- PANTALLA PRINCIPAL ---
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Evaluación de Riesgo Actual")
        st.markdown(f"<h1 style='text-align: center; color: {color};'>{riesgo}</h1>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align: center;'>Probabilidad de Rezago: {prob*100:.1f}%</h3>", unsafe_allow_html=True)
        st.progress(float(prob))
        
        # Alertas Tempranas
        if riesgo == "Alto":
            st.error("⚠️ El estudiante presenta un **alto riesgo** de rezago escolar el próximo año. Se recomienda derivación pedagógica e intervención inmediata.")
        elif riesgo == "Medio":
            st.warning("⚠️ El estudiante presenta **signos de alerta temprana**. Se sugiere seguimiento bimensual y tutorías de apoyo.")
        else:
            st.success("✅ El estudiante presenta un **desempeño estable**. Continuar con la metodología actual.")
            
    with col2:
        if df is not None:
            st.subheader("Contexto Histórico General")
            st.markdown("Distribución del riesgo según el promedio y materias reprobadas en la base de históricos.")
            
            # Limpiar datos para el plot
            df_plot = df.dropna(subset=["promedio_general", "num_materias_reprobadas", "rezago"]).copy()
            df_plot["Estado"] = df_plot["rezago"].map({1: "Rezago (Histórico)", 0: "Estable (Histórico)"})
            
            fig = px.scatter(
                df_plot, 
                x="promedio_general", 
                y="num_materias_reprobadas", 
                color="Estado",
                color_discrete_map={"Rezago (Histórico)": "#ff4b4b", "Estable (Histórico)": "#00c04b"},
                opacity=0.3,
                title="Posicionamiento del Estudiante vs. Histórico"
            )
            
            # Agregar el punto de simulacion actual
            fig.add_scatter(
                x=[promedio], y=[reprobadas],
                mode='markers+text',
                marker=dict(size=18, color='black', symbol='star'),
                name='Estudiante Simulado',
                text=["Estudiante"], textposition="top center"
            )
            
            # Mejorar layout del grafico
            fig.update_layout(
                xaxis_title="Promedio General",
                yaxis_title="Cantidad de Materias Reprobadas"
            )
            
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No se encontró el archivo de datos históricos para visualización cruzada.")

if __name__ == "__main__":
    main()
