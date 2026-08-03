"""
Módulo de Configuración Global del Prototipo Docente (Objetivo 5).
Define rutas de archivos, materias, constantes de evaluación y colores de alerta.
"""

import os
from typing import List, Dict

# Rutas principales
BASE_DIR: str = os.path.dirname(os.path.abspath(__file__))
MODELS_DIR: str = os.path.join(BASE_DIR, "../modelos_entrenados")
DATA_PATH: str = os.path.join(BASE_DIR, "../data/03_Datasets_Procesados/primaria_dataset.csv")

# Materias del Currículo Educativo
SUBJECT_COLS: List[str] = [
    'com_lenguajes', 'cs_sociales', 'edu_fisica', 'edu_musical',
    'art_plasticas', 'matematica', 'tec_tecnologica', 'cs_naturales',
    'valores_religion'
]

SUBJECT_NAMES: Dict[str, str] = {
    'com_lenguajes': 'Comunicación y Lenguajes',
    'cs_sociales': 'Ciencias Sociales',
    'edu_fisica': 'Educación Física y Deportes',
    'edu_musical': 'Educación Musical',
    'art_plasticas': 'Artes Plásticas y Visuales',
    'matematica': 'Matemática',
    'tec_tecnologica': 'Técnica Tecnológica',
    'cs_naturales': 'Ciencias Naturales',
    'valores_religion': 'Valores, Espiritualidad y Religiones'
}

# Ordenamiento estándar de Grados
ORDEN_GRADOS: List[str] = ["PRIMERO", "SEGUNDO", "TERCERO", "CUARTO", "QUINTO", "SEXTO"]

# Umbrales y Colores de Alerta
MIN_APROBACION_NOTA: float = 51.0

PALETA_RIESGO: Dict[str, Dict[str, str]] = {
    "Alto Riesgo": {
        "color": "#F43F5E",
        "badge": "🔴 ALTO RIESGO",
        "rec": "Intervención pedagógica prioritaria y tutoría intensiva inmediata."
    },
    "Medio Riesgo": {
        "color": "#F59E0B",
        "badge": "🟡 MEDIO RIESGO",
        "rec": "Alerta Temprana: Seguimiento bimensual y apoyo en materias críticas."
    },
    "Bajo Riesgo": {
        "color": "#10B981",
        "badge": "🟢 BAJO RIESGO",
        "rec": "Desempeño estable. Mantener acompañamiento estándar."
    }
}
