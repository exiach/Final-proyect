"""
Servicio de Carga y Procesamiento de Datos de Estudiantes.
Maneja la lectura del dataset CSV base y la integración de nuevos archivos subidos.
"""

import os
import pandas as pd
import streamlit as st
from typing import Optional
from config import DATA_PATH, SUBJECT_COLS, MIN_APROBACION_NOTA


def process_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Procesa, valida y estandariza las columnas necesarias en el dataset de estudiantes.
    
    Args:
        df (pd.DataFrame): DataFrame bruto.
        
    Returns:
        pd.DataFrame: DataFrame procesado con nombre_completo, promedio y reprobadas calculadas.
    """
    df = df.copy()
    
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
        if 'promedio_general' not in df.columns or df['promedio_general'].isnull().all():
            df['promedio_general'] = df[subjs_present].mean(axis=1)
        if 'num_materias_reprobadas' not in df.columns or df['num_materias_reprobadas'].isnull().all():
            df['num_materias_reprobadas'] = (df[subjs_present] < MIN_APROBACION_NOTA).sum(axis=1)

    # Valores por defecto para metadatos requeridos
    if 'gestion' not in df.columns:
        df['gestion'] = 2025
    if 'anio_escolaridad' not in df.columns:
        df['anio_escolaridad'] = 'PRIMERO'
    if 'paralelo' not in df.columns:
        df['paralelo'] = 'A'
    if 'rude' not in df.columns:
        df['rude'] = [f"RUDE-{i+1}" for i in range(len(df))]
        
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
        return process_dataframe(df)
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
