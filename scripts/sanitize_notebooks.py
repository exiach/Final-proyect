"""Elimina salidas sensibles y alinea los cuadernos de modelado con el pipeline canónico."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK_DIR = ROOT / "notebooks"
PRIVACY_NOTICE = (
    "⚠️ **Privacidad:** las salidas se eliminaron porque los datos contienen información "
    "de estudiantes menores. Ejecute este cuaderno solo en un entorno institucional "
    "autorizado y no publique tablas con nombres, RUDE o fechas de nacimiento."
)


def markdown_cell(text: str) -> dict:
    return {"cell_type": "markdown", "metadata": {}, "source": [line + "\n" for line in text.splitlines()]}


def code_cell(code: str) -> dict:
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [line + "\n" for line in code.splitlines()],
    }


def clear_outputs(path: Path) -> None:
    notebook = json.loads(path.read_text(encoding="utf-8"))
    for cell in notebook.get("cells", []):
        if cell.get("cell_type") == "code":
            cell["outputs"] = []
            cell["execution_count"] = None
    first_text = "".join(notebook.get("cells", [{}])[0].get("source", [])) if notebook.get("cells") else ""
    if "Privacidad:" not in first_text:
        notebook.setdefault("cells", []).insert(0, markdown_cell(PRIVACY_NOTICE))
    path.write_text(json.dumps(notebook, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def canonical_notebook(title: str, focus: str, model_keys: list[str]) -> dict:
    setup = """from pathlib import Path
import json
import pandas as pd

ROOT = Path.cwd().parent if Path.cwd().name == 'notebooks' else Path.cwd()
METRICS_PATH = ROOT / 'resultados_modelos' / 'metricas_modelos.json'

# Ejecute `python scripts/train_models.py` desde la raíz para reconstruir modelos y métricas.
with METRICS_PATH.open(encoding='utf-8') as stream:
    resultados = json.load(stream)

resultados['entrenamiento_temporal'], resultados['prueba_temporal']"""
    keys_literal = repr(model_keys)
    table = f"""filas = []
for nombre in {keys_literal}:
    m = resultados['evaluacion'][nombre]
    filas.append({{
        'modelo': nombre,
        'matriz_confusion': m['confusion_matrix'],
        'precision_rezago': m['precision_rezago'],
        'recall_rezago': m['recall_rezago'],
        'f1_rezago': m['f1_rezago'],
        'balanced_accuracy': m['balanced_accuracy'],
        'average_precision': m['average_precision'],
    }})
pd.DataFrame(filas)"""
    return {
        "cells": [
            markdown_cell(f"# {title}\n\n{PRIVACY_NOTICE}"),
            markdown_cell(
                f"{focus}\n\nLa fuente canónica es `scripts/train_models.py`: construye transiciones "
                "T→T+1, entrena con 2022→2023 y prueba con 2023→2024. Solo existen seis "
                "transiciones positivas, por lo que los resultados son exploratorios."
            ),
            code_cell(setup),
            code_cell(table),
        ],
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3.12"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def main() -> None:
    for path in NOTEBOOK_DIR.glob("*.ipynb"):
        clear_outputs(path)

    replacements = {
        "Obj3a_Entrenamiento_Arboles_RF.ipynb": canonical_notebook(
            "Objetivo 3a — Árbol de Decisión y Random Forest",
            "Este cuaderno resume la evaluación temporal de los modelos basados en árboles.",
            ["decision_tree", "random_forest"],
        ),
        "Obj3b_Entrenamiento_Redes_Neuronales.ipynb": canonical_notebook(
            "Objetivo 3b — Red Neuronal MLP",
            "Este cuaderno resume la evaluación temporal de la MLP con StandardScaler.",
            ["mlp"],
        ),
        "Obj4_Evaluacion_Segregacion_Riesgo.ipynb": canonical_notebook(
            "Objetivo 4 — Evaluación y segregación de riesgo",
            "Este cuaderno compara los tres clasificadores. La regla pedagógica del prototipo es una salida operativa separada de estas métricas.",
            ["decision_tree", "random_forest", "mlp"],
        ),
    }
    for filename, notebook in replacements.items():
        (NOTEBOOK_DIR / filename).write_text(
            json.dumps(notebook, ensure_ascii=False, indent=1) + "\n", encoding="utf-8"
        )


if __name__ == "__main__":
    main()
