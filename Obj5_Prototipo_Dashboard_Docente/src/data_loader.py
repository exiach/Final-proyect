"""
Servicio de Carga y Procesamiento de Datos de Estudiantes.
Maneja la lectura del dataset CSV base y la integración de nuevos archivos subidos.
"""

import os
import pandas as pd
import streamlit as st
from typing import Optional
from config import DATA_PATH, SUBJECT_COLS, MIN_APROBACION_NOTA

REQUIRED_META = ['gestion', 'anio_escolaridad', 'paralelo', 'rude']


def validate_dataframe(df: pd.DataFrame, allow_missing_notes: bool = False) -> pd.DataFrame:
    """Valida esquema, identificadores y dominio de las calificaciones."""
    if df.empty:
        raise ValueError("El archivo no contiene registros.")
    missing = [c for c in REQUIRED_META + SUBJECT_COLS if c not in df.columns]
    if missing:
        raise ValueError(f"Faltan columnas obligatorias: {', '.join(missing)}")
    checked = df.copy()
    for col in SUBJECT_COLS:
        checked[col] = pd.to_numeric(checked[col], errors='coerce')
    invalid_numeric = checked[SUBJECT_COLS].isna().any(axis=1)
    if invalid_numeric.any() and not allow_missing_notes:
        rows = (invalid_numeric[invalid_numeric].index + 2).tolist()[:10]
        raise ValueError(f"Hay notas vacías o no numéricas en filas: {rows}")
    invalid_range = ((checked[SUBJECT_COLS] < 0) | (checked[SUBJECT_COLS] > 100)).any(axis=1)
    if invalid_range.any():
        rows = (invalid_range[invalid_range].index + 2).tolist()[:10]
        raise ValueError(f"Hay notas fuera del rango 0-100 en filas: {rows}")
    if checked['rude'].isna().any() or checked['rude'].astype(str).str.strip().eq('').any():
        raise ValueError("Todos los registros deben incluir un RUDE seudonimizado válido.")
    if checked.duplicated(['rude', 'gestion']).any():
        raise ValueError("Existen registros duplicados para la combinación RUDE-gestión.")
    return checked


def process_dataframe(df: pd.DataFrame, allow_missing_notes: bool = False) -> pd.DataFrame:
    """
    Procesa, valida y estandariza las columnas necesarias en el dataset de estudiantes.
    
    Args:
        df (pd.DataFrame): DataFrame bruto.
        
    Returns:
        pd.DataFrame: DataFrame procesado con nombre_completo, promedio y reprobadas calculadas.
    """
    df = validate_dataframe(df, allow_missing_notes=allow_missing_notes)
    
    # Formatear nombre completo
    paterno = df['paterno'].fillna('') if 'paterno' in df.columns else pd.Series([''] * len(df))
    materno = df['materno'].fillna('') if 'materno' in df.columns else pd.Series([''] * len(df))
    nombres = df['nombres'].fillna('') if 'nombres' in df.columns else pd.Series([''] * len(df))
    
    if 'nombre_completo' not in df.columns:
        df['nombre_completo'] = (paterno + " " + materno + " " + nombres).str.strip().str.title()
        df['nombre_completo'] = df['nombre_completo'].replace('', 'Estudiante sin nombre')

    # Validar y calcular métricas académicas de materias presentes
    subjs_present = [col for col in SUBJECT_COLS if col in df.columns]
    if subjs_present:
        complete_notes = df[subjs_present].notna().all(axis=1)
        calculated_average = df[subjs_present].mean(axis=1).where(complete_notes)
        calculated_failed = (df[subjs_present] < MIN_APROBACION_NOTA).sum(axis=1).where(complete_notes)
        if 'promedio_general' not in df.columns:
            df['promedio_general'] = calculated_average
        else:
            df['promedio_general'] = pd.to_numeric(df['promedio_general'], errors='coerce').where(complete_notes)
            df['promedio_general'] = df['promedio_general'].fillna(calculated_average)
        if 'num_materias_reprobadas' not in df.columns:
            df['num_materias_reprobadas'] = calculated_failed
        else:
            df['num_materias_reprobadas'] = pd.to_numeric(
                df['num_materias_reprobadas'], errors='coerce'
            ).where(complete_notes)
            df['num_materias_reprobadas'] = df['num_materias_reprobadas'].fillna(calculated_failed)
        if 'rezago' not in df.columns:
            # Etiqueta descriptiva de la gestión cargada; no es una predicción T+1.
            df['rezago'] = (df['num_materias_reprobadas'] > 0).astype('Int64').where(complete_notes)
        df['datos_completos'] = complete_notes

    return df


@st.cache_data
def load_base_data() -> Optional[pd.DataFrame]:
    """
    Carga y procesa el dataset base en caché.
    
    Returns:
        Optional[pd.DataFrame]: DataFrame cargado o None si el archivo no existe.
    """
    if os.path.exists(DATA_PATH):
        df = pd.read_csv(DATA_PATH)
        # El histórico conserva faltantes reales; se identifican y no se predicen.
        return process_dataframe(df, allow_missing_notes=True)
    return None


def merge_uploaded_data(df_base: pd.DataFrame, df_new: pd.DataFrame) -> pd.DataFrame:
    """
    Combina el dataset base con una nueva nómina subida por el usuario.
    
    Args:
        df_base (pd.DataFrame): Dataset histórico base.
        df_new (pd.DataFrame): Nuevo dataset procesado.
        
    Returns:
        pd.DataFrame: Dataset unificado sin duplicados.
    """
    df_new_proc = process_dataframe(df_new)
    merged = pd.concat([df_new_proc, df_base], ignore_index=True)
    return merged.drop_duplicates(subset=['rude', 'gestion'], keep='first')
