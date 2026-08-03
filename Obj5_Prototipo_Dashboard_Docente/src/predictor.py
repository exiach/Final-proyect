"""
Servicio de Machine Learning y Reglas de Resguardo Pedagógico.
Encapsula los modelos entrenados (Random Forest / MLP) y la lógica híbrida de decisión.
"""

import os
import joblib
import pandas as pd
import streamlit as st
from typing import Tuple, Any
from config import MODELS_DIR, PALETA_RIESGO, MIN_APROBACION_NOTA


@st.cache_resource
def load_trained_models() -> Tuple[Any, Any, Any]:
    """
    Carga los modelos entrenados y el escalador desde la carpeta de modelos.
    
    Returns:
        Tuple[Any, Any, Any]: (rf_model, mlp_model, scaler)
    """
    rf_model = joblib.load(os.path.join(MODELS_DIR, "random_forest_model.pkl"))
    mlp_model = joblib.load(os.path.join(MODELS_DIR, "mlp_model.pkl"))
    scaler = joblib.load(os.path.join(MODELS_DIR, "scaler.pkl"))
    return rf_model, mlp_model, scaler


def predict_student_risk(
    promedio: float,
    reprobadas: int,
    modelo_nombre: str,
    rf_model: Any,
    mlp_model: Any,
    scaler: Any
) -> Tuple[float, str, str, str, str]:
    """
    Calcula la probabilidad de rezago para un estudiante e integra reglas de resguardo normativo.
    
    Args:
        promedio (float): Promedio general del estudiante.
        reprobadas (int): Cantidad de materias reprobadas.
        modelo_nombre (str): Nombre del modelo seleccionado ("Random Forest" o "Red Neuronal").
        rf_model (Any): Modelo Random Forest cargado.
        mlp_model (Any): Modelo MLP cargado.
        scaler (Any): Escalador StandardScaler cargado.
        
    Returns:
        Tuple[float, str, str, str, str]: (probabilidad, nivel_riesgo, color, badge, recomendacion)
    """
    input_data = pd.DataFrame({
        "promedio_general_prev": [promedio],
        "num_materias_reprobadas_prev": [reprobadas]
    })
    
    # Inferencia del modelo de Machine Learning
    if "Random Forest" in modelo_nombre:
        prob = float(rf_model.predict_proba(input_data)[0][1])
    else:
        input_scaled = scaler.transform(input_data)
        prob = float(mlp_model.predict_proba(input_scaled)[0][1])
        
    # --- CAPA DE RESGUARDO PEDAGÓGICO NORMATIVO (SISTEMA HÍBRIDO) ---
    # Garantiza coherencia pedagógica: promedio < 51 o 2+ reprobadas es Alto Riesgo
    if promedio < MIN_APROBACION_NOTA or reprobadas >= 2:
        prob = max(prob, 0.85)
    elif reprobadas == 1 or (MIN_APROBACION_NOTA <= promedio < 60.0):
        prob = max(prob, 0.50)

    # Categorización según umbrales institucionales
    if prob >= 0.70:
        cat = "Alto Riesgo"
    elif prob >= 0.40:
        cat = "Medio Riesgo"
    else:
        cat = "Bajo Riesgo"
        
    info = PALETA_RIESGO[cat]
    return prob, cat, info["color"], info["badge"], info["rec"]


def enrich_with_predictions(
    df: pd.DataFrame,
    modelo_nombre: str,
    rf_model: Any,
    mlp_model: Any,
    scaler: Any
) -> pd.DataFrame:
    """
    Agrega las columnas de predicción (prob_rezago, nivel_riesgo, badge_riesgo, recomendacion) al DataFrame.
    
    Args:
        df (pd.DataFrame): DataFrame de estudiantes.
        modelo_nombre (str): Nombre del modelo ML seleccionado.
        rf_model (Any): Modelo RF.
        mlp_model (Any): Modelo MLP.
        scaler (Any): Escalador StandardScaler.
        
    Returns:
        pd.DataFrame: DataFrame enriquecido con columnas de riesgo.
    """
    df = df.copy()
    if df.empty:
        df['prob_rezago'] = []
        df['nivel_riesgo'] = []
        df['badge_riesgo'] = []
        df['recomendacion'] = []
        return df

    probs = []
    riesgos = []
    badges = []
    recs = []
    
    for _, row in df.iterrows():
        prom = float(row['promedio_general']) if ('promedio_general' in row and pd.notnull(row['promedio_general'])) else 60.0
        reprob = int(row['num_materias_reprobadas']) if ('num_materias_reprobadas' in row and pd.notnull(row['num_materias_reprobadas'])) else 0
        p, r, _, b, rc = predict_student_risk(prom, reprob, modelo_nombre, rf_model, mlp_model, scaler)
        probs.append(p)
        riesgos.append(r)
        badges.append(b)
        recs.append(rc)

    df['prob_rezago'] = probs
    df['nivel_riesgo'] = riesgos
    df['badge_riesgo'] = badges
    df['recomendacion'] = recs
    return df

