"""Actualiza los índices estáticos tras la paginación final verificada."""

from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt


ROOT = Path(__file__).resolve().parents[1]
DOCX = ROOT / "documentacion/Proyecto_Revisado_Academicamente_Ampliado.docx"


TOC_PAGES = {
    "3.10.": 20,
    "3.10.1.": 20,
    "3.10.2.": 21,
    "3.10.3.": 22,
    "3.10.4.": 23,
    "3.10.5.": 24,
    "4.": 27,
    "4.1.": 27,
    "4.1.1.": 27,
    "4.1.2.": 28,
    "4.2.": 28,
    "4.2.1.": 28,
    "4.2.2.": 30,
    "4.3.": 31,
    "4.3.1.": 31,
    "4.3.2.": 32,
    "4.4.": 33,
    "4.4.1.": 33,
    "4.4.2.": 34,
    "4.5.": 36,
    "4.5.1.": 37,
    "4.6.": 37,
    "5.": 39,
    "6.": 40,
    "Bibliografía": 41,
    "Anexos": 43,
}


FIGURES = [
    ("Figura 3.1. Área de estudio de la U.E. José María Santiváñez", 10),
    ("Figura 3.2. Flujo metodológico CRISP-DM adaptado", 11),
    ("Figura 3.3. Carpetas por gestión escolar", 12),
    ("Figura 3.4. Boletines centralizados", 13),
    ("Figura 3.5. Boletín anual", 13),
    ("Figura 3.6. Boletines transformados a Excel", 14),
    ("Figura 3.7. Validación, construcción de variables y resultado agregado del objetivo 1", 21),
    ("Figura 3.8. Código reproducible y tasas descriptivas de reprobación por asignatura", 22),
    ("Figura 3.9. Entrenamiento reproducible y evaluación temporal de los tres clasificadores", 23),
    ("Figura 3.10. Trazabilidad de la segregación operativa y distribución de categorías", 24),
    ("Figura 3.11. Panel principal del prototipo con filtros e indicadores agregados", 25),
    ("Figura 3.12. Simulador libre y separación entre probabilidad y puntaje operativo", 26),
    ("Figura 4.1. Tasa de reprobación por asignatura", 29),
    ("Figura 4.2. Materias reprobadas según condición de rezago", 31),
    ("Figura 4.3. Evolución del rezago por gestión", 35),
    ("Figura 4.4. Rezago promedio por grado", 35),
    ("Figura 4.5. Trayectoria longitudinal de ejemplo", 36),
    ("Figura 4.6. Matrices de confusión de la prueba temporal", 32),
    ("Figura 4.7. Distribución operativa del riesgo", 34),
]


TABLES = [
    ("Tabla 3.1. Matriz de trazabilidad entre objetivos, procesos y evidencias", 20),
    ("Tabla 3.2. Reglas de validación y tratamiento de datos académicos", 21),
    ("Tabla 3.3. Construcción y partición de la muestra predictiva longitudinal", 22),
    ("Tabla 4.1. Caracterización del conjunto consolidado", 28),
    ("Tabla 4.2. Tasas de reprobación por asignatura", 29),
    ("Tabla 4.3. Promedios por condición de rezago", 30),
    ("Tabla 4.4. Hiperparámetros de los modelos", 32),
    ("Tabla 4.5. Umbrales operativos de riesgo", 33),
]


def restyle(paragraph) -> None:
    paragraph.alignment = WD_ALIGN_PARAGRAPH.LEFT
    for run in paragraph.runs:
        run.font.name = "Arial"
        run.font.size = Pt(11)


def main() -> None:
    doc = Document(DOCX)
    paragraphs = doc.paragraphs
    fig_heading = next(i for i, p in enumerate(paragraphs) if p.text.strip() == "Lista de figuras")
    tab_heading = next(i for i, p in enumerate(paragraphs) if p.text.strip() == "Lista de tablas")
    intro_heading = next(i for i, p in enumerate(paragraphs) if p.text.strip() == "Introducción")

    # Índice general: solo se modifica la sección previa a la lista de figuras.
    for p in paragraphs[:fig_heading]:
        text = p.text.strip()
        if not text:
            continue
        key = text.split("\t", 1)[0]
        if key in TOC_PAGES:
            parts = text.split("\t")
            title = "\t".join(parts[:-1]) if len(parts) > 1 else key
            p.text = f"{title}\t{TOC_PAGES[key]}"
            restyle(p)

    figure_paragraphs = [p for p in paragraphs[fig_heading + 1 : tab_heading] if p.text.strip()]
    if len(figure_paragraphs) != len(FIGURES):
        raise ValueError(f"Se esperaban {len(FIGURES)} entradas de figuras y existen {len(figure_paragraphs)}")
    for p, (title, page) in zip(figure_paragraphs, FIGURES):
        p.text = f"{title}\t{page}"
        restyle(p)

    table_paragraphs = [p for p in paragraphs[tab_heading + 1 : intro_heading] if p.text.strip()]
    if len(table_paragraphs) != len(TABLES):
        raise ValueError(f"Se esperaban {len(TABLES)} entradas de tablas y existen {len(table_paragraphs)}")
    for p, (title, page) in zip(table_paragraphs, TABLES):
        p.text = f"{title}\t{page}"
        restyle(p)

    doc.save(DOCX)
    print(DOCX)


if __name__ == "__main__":
    main()
