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


def predict_student_risk_details(
    promedio: float,
    reprobadas: int,
    modelo_nombre: str,
    rf_model: Any,
    mlp_model: Any,
    scaler: Any,
) -> dict:
    """Devuelve por separado la inferencia estadística y la decisión híbrida."""
    input_data = pd.DataFrame({
        "promedio_general_prev": [promedio],
        "num_materias_reprobadas_prev": [reprobadas],
    })
    if "Random Forest" in modelo_nombre:
        prob_modelo = float(rf_model.predict_proba(input_data)[0][1])
    else:
        prob_modelo = float(mlp_model.predict_proba(scaler.transform(input_data))[0][1])
    prob_final, cat, color, badge, rec = predict_student_risk(
        promedio, reprobadas, modelo_nombre, rf_model, mlp_model, scaler
    )
    if promedio < MIN_APROBACION_NOTA or reprobadas >= 2:
        motivo = "Regla pedagógica: promedio < 51 o dos o más materias reprobadas"
    elif reprobadas == 1 or MIN_APROBACION_NOTA <= promedio < 60:
        motivo = "Regla preventiva: una materia reprobada o promedio entre 51 y 59.99"
    else:
        motivo = "Clasificación basada en la probabilidad del modelo"
    return {
        "probabilidad_modelo": prob_modelo,
        "probabilidad_operativa": prob_final,
        "nivel_riesgo": cat,
        "color": color,
        "badge": badge,
        "recomendacion": rec,
        "motivo": motivo,
    }


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
        df['prob_modelo'] = []
        df['nivel_riesgo'] = []
        df['badge_riesgo'] = []
        df['recomendacion'] = []
        df['motivo_alerta'] = []
        return df

    probs = []
    probs_modelo = []
    riesgos = []
    badges = []
    recs = []
    motivos = []
    
    for _, row in df.iterrows():
        complete = bool(row.get('datos_completos', True))
        complete = complete and pd.notnull(row.get('promedio_general')) and pd.notnull(row.get('num_materias_reprobadas'))
        if not complete:
            info = PALETA_RIESGO["Sin datos"]
            probs.append(float('nan'))
            probs_modelo.append(float('nan'))
            riesgos.append("Sin datos")
            badges.append(info['badge'])
            recs.append(info['rec'])
            motivos.append("Predicción no calculada: faltan una o más calificaciones")
            continue
        prom = float(row['promedio_general'])
        reprob = int(row['num_materias_reprobadas'])
        detail = predict_student_risk_details(prom, reprob, modelo_nombre, rf_model, mlp_model, scaler)
        probs.append(detail['probabilidad_operativa'])
        probs_modelo.append(detail['probabilidad_modelo'])
        riesgos.append(detail['nivel_riesgo'])
        badges.append(detail['badge'])
        recs.append(detail['recomendacion'])
        motivos.append(detail['motivo'])

    df['prob_rezago'] = probs
    df['prob_modelo'] = probs_modelo
    df['nivel_riesgo'] = riesgos
    df['badge_riesgo'] = badges
    df['recomendacion'] = recs
    df['motivo_alerta'] = motivos
    return df
