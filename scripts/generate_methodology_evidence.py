"""Genera evidencias visuales reproducibles para explicar los objetivos del proyecto.

Las imágenes se construyen únicamente con código y resultados ya presentes en el
repositorio. No muestran nombres, RUDE ni registros individuales.
"""

from __future__ import annotations

import json
import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/tmp/final_project_matplotlib")

import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
FIG_DIR = ROOT / "documentacion" / "figuras"
DATA_PATH = ROOT / "data" / "03_Datasets_Procesados" / "primaria_dataset.csv"
METRICS_PATH = ROOT / "resultados_modelos" / "metricas_modelos.json"
MODEL_PATH = ROOT / "modelos_entrenados" / "random_forest_model.pkl"

SUBJECTS = [
    "com_lenguajes",
    "cs_sociales",
    "edu_fisica",
    "edu_musical",
    "art_plasticas",
    "matematica",
    "tec_tecnologica",
    "cs_naturales",
    "valores_religion",
]

SUBJECT_LABELS = {
    "com_lenguajes": "Comunicación y Lenguajes",
    "cs_sociales": "Ciencias Sociales",
    "edu_fisica": "Educación Física",
    "edu_musical": "Educación Musical",
    "art_plasticas": "Artes Plásticas",
    "matematica": "Matemática",
    "tec_tecnologica": "Técnica Tecnológica",
    "cs_naturales": "Ciencias Naturales",
    "valores_religion": "Valores y Religión",
}


def code_panel(ax, title: str, code: str, footer: str) -> None:
    ax.set_facecolor("#111827")
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_color("#334155")
        spine.set_linewidth(1.2)
    ax.text(
        0.03,
        0.96,
        title,
        transform=ax.transAxes,
        va="top",
        color="#7DD3FC",
        fontsize=10.5,
        fontweight="bold",
    )
    ax.text(
        0.03,
        0.86,
        code,
        transform=ax.transAxes,
        va="top",
        color="#E5E7EB",
        fontsize=8.8,
        family="DejaVu Sans Mono",
        linespacing=1.45,
    )
    ax.text(
        0.03,
        0.04,
        footer,
        transform=ax.transAxes,
        va="bottom",
        color="#94A3B8",
        fontsize=8.3,
    )


def save(fig, filename: str) -> None:
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIG_DIR / filename, dpi=260, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def objective_1(dataset: pd.DataFrame) -> None:
    code = """checked = validate_dataframe(df, allow_missing_notes=True)

complete_notes = checked[SUBJECT_COLS].notna().all(axis=1)
checked[\"promedio_general\"] = (
    checked[SUBJECT_COLS].mean(axis=1).where(complete_notes)
)
checked[\"num_materias_reprobadas\"] = (
    (checked[SUBJECT_COLS] < 51).sum(axis=1).where(complete_notes)
)
checked[\"datos_completos\"] = complete_notes"""
    years = sorted(int(x) for x in dataset["gestion"].dropna().unique())
    complete = int(dataset[SUBJECTS].notna().all(axis=1).sum())
    incomplete = int(len(dataset) - complete)

    fig, axes = plt.subplots(1, 2, figsize=(12.2, 5.3), gridspec_kw={"width_ratios": [1.5, 1]})
    code_panel(
        axes[0],
        "Objetivo 1 · Validación y consolidación",
        code,
        "Cuaderno Obj1_Recoleccion_Limpieza.ipynb · implementación: src/data_loader.py",
    )
    axes[1].axis("off")
    rows = [
        ["Boletines procesados", "36"],
        ["Gestiones", f"{years[0]}–{years[-1]}"],
        ["Observaciones estudiante-año", f"{len(dataset):,}".replace(",", ".")],
        ["Estudiantes únicos", f"{dataset['rude'].nunique():,}".replace(",", ".")],
        ["Registros completos", f"{complete:,}".replace(",", ".")],
        ["Registros incompletos", f"{incomplete:,}".replace(",", ".")],
    ]
    table = axes[1].table(
        cellText=rows,
        colLabels=["Control", "Resultado verificable"],
        cellLoc="left",
        colLoc="left",
        loc="center",
        colWidths=[0.64, 0.36],
    )
    table.auto_set_font_size(False)
    table.set_fontsize(9.3)
    table.scale(1, 1.75)
    for (row, _), cell in table.get_celld().items():
        cell.set_edgecolor("#CBD5E1")
        if row == 0:
            cell.set_facecolor("#1D4ED8")
            cell.get_text().set_color("white")
            cell.get_text().set_weight("bold")
        else:
            cell.set_facecolor("#F8FAFC" if row % 2 else "#EFF6FF")
    axes[1].set_title("Salida agregada, sin datos personales", fontsize=11, fontweight="bold", pad=14)
    fig.tight_layout()
    save(fig, "fig_3_7_obj1_validacion_consolidacion.png")


def objective_2(dataset: pd.DataFrame) -> None:
    code = """tasas = (
    (dataset[materias] < 51)
    .mean()
    .sort_values(ascending=False) * 100
)

promedios = dataset.groupby(\"rezago\")[materias].mean()
reprobadas = dataset.groupby(\"rezago\")[
    \"num_materias_reprobadas\"
].mean()"""
    rates = ((dataset[SUBJECTS] < 51).mean() * 100).sort_values()
    labels = [SUBJECT_LABELS[x] for x in rates.index]

    fig, axes = plt.subplots(1, 2, figsize=(12.2, 5.3), gridspec_kw={"width_ratios": [1.25, 1.15]})
    code_panel(
        axes[0],
        "Objetivo 2 · Análisis descriptivo por asignatura",
        code,
        "Cuaderno Obj2a_Analisis_Patrones.ipynb · cálculo reproducido con el dataset consolidado",
    )
    colors = ["#EF4444" if x > 1.5 else "#F59E0B" if x > 0.8 else "#3B82F6" for x in rates]
    axes[1].barh(labels, rates.values, color=colors)
    axes[1].set_xlabel("Tasa descriptiva de reprobación (%)")
    axes[1].grid(axis="x", linestyle="--", alpha=0.35)
    axes[1].set_axisbelow(True)
    for i, value in enumerate(rates.values):
        axes[1].text(value + 0.03, i, f"{value:.2f}%", va="center", fontsize=8.5)
    axes[1].set_title("Salida del proceso exploratorio", fontsize=11, fontweight="bold")
    fig.tight_layout()
    save(fig, "fig_3_8_obj2_analisis_patrones.png")


def objective_3(metrics: dict) -> None:
    code = """transitions = build_transitions(dataset)
train = transitions[transitions[\"gestion\"].eq(2022)]
test  = transitions[transitions[\"gestion\"].eq(2023)]

models = make_models()
for name, model in models.items():
    model.fit(X_train, y_train)
    prob = model.predict_proba(X_test)[:, 1]
    evaluation[name] = metrics(y_test, prob)"""
    records = []
    labels = {"decision_tree": "Árbol", "random_forest": "Random Forest", "mlp": "MLP"}
    for key, label in labels.items():
        value = metrics["evaluacion"][key]
        records.append(
            [
                label,
                f"{value['precision_rezago']:.4f}",
                f"{value['recall_rezago']:.4f}",
                f"{value['f1_rezago']:.4f}",
                f"{value['balanced_accuracy']:.4f}",
            ]
        )

    fig, axes = plt.subplots(1, 2, figsize=(12.2, 5.3), gridspec_kw={"width_ratios": [1.38, 1]})
    code_panel(
        axes[0],
        "Objetivo 3 · Entrenamiento y evaluación temporal",
        code,
        "Cuadernos Obj3a/Obj3b · implementación canónica: scripts/train_models.py",
    )
    axes[1].axis("off")
    table = axes[1].table(
        cellText=records,
        colLabels=["Modelo", "Precisión", "Recall", "F1", "Balanced acc."],
        cellLoc="center",
        colLoc="center",
        loc="center",
    )
    table.auto_set_font_size(False)
    table.set_fontsize(8.3)
    table.scale(1, 1.75)
    for (row, _), cell in table.get_celld().items():
        cell.set_edgecolor("#CBD5E1")
        if row == 0:
            cell.set_facecolor("#1D4ED8")
            cell.get_text().set_color("white")
            cell.get_text().set_weight("bold")
        else:
            cell.set_facecolor("#F8FAFC" if row % 2 else "#EFF6FF")
    axes[1].set_title(
        f"Prueba temporal {metrics['prueba_temporal']['transicion']} · N={metrics['prueba_temporal']['n']}",
        fontsize=11,
        fontweight="bold",
        pad=14,
    )
    axes[1].text(
        0.5,
        0.18,
        "Solo 3 positivos en prueba: métricas exploratorias.",
        transform=axes[1].transAxes,
        ha="center",
        color="#B91C1C",
        fontsize=9.2,
        fontweight="bold",
    )
    fig.tight_layout()
    save(fig, "fig_3_9_obj3_entrenamiento_temporal.png")


def risk_levels(dataset: pd.DataFrame) -> pd.Series:
    model = joblib.load(MODEL_PATH)
    X = dataset[["promedio_general", "num_materias_reprobadas"]].copy()
    X.columns = ["promedio_general_prev", "num_materias_reprobadas_prev"]
    valid = X.notna().all(axis=1)
    prob = pd.Series(np.nan, index=dataset.index)
    prob.loc[valid] = model.predict_proba(X.loc[valid])[:, 1]
    high = valid & ((X["promedio_general_prev"] < 51) | (X["num_materias_reprobadas_prev"] >= 2))
    medium = valid & (
        (X["num_materias_reprobadas_prev"] == 1)
        | X["promedio_general_prev"].between(51, 60, inclusive="left")
    )
    prob.loc[high] = np.maximum(prob.loc[high], 0.85)
    prob.loc[medium] = np.maximum(prob.loc[medium], 0.50)
    levels = pd.cut(
        prob,
        [-np.inf, 0.40, 0.70, np.inf],
        right=False,
        labels=["Bajo riesgo", "Medio riesgo", "Alto riesgo"],
    ).astype(object)
    return levels.where(valid, "Sin datos")


def objective_4(dataset: pd.DataFrame) -> None:
    code = """detail = predict_student_risk_details(
    promedio, reprobadas, modelo, rf, mlp, scaler
)

salida = {
    \"probabilidad_modelo\": detail[\"probabilidad_modelo\"],
    \"puntaje_operativo\": detail[\"probabilidad_operativa\"],
    \"nivel_riesgo\": detail[\"nivel_riesgo\"],
    \"motivo\": detail[\"motivo\"],
}"""
    categories = ["Bajo riesgo", "Medio riesgo", "Alto riesgo", "Sin datos"]
    counts = risk_levels(dataset).value_counts().reindex(categories, fill_value=0)
    colors = ["#10B981", "#F59E0B", "#EF4444", "#94A3B8"]

    fig, axes = plt.subplots(1, 2, figsize=(12.2, 5.3), gridspec_kw={"width_ratios": [1.38, 1]})
    code_panel(
        axes[0],
        "Objetivo 4 · Segregación operativa y trazabilidad",
        code,
        "Cuaderno Obj4_Evaluacion_Segregacion_Riesgo.ipynb · implementación: src/predictor.py",
    )
    bars = axes[1].bar(categories, counts.values, color=colors, width=0.58)
    axes[1].set_ylabel("Observaciones estudiante-año")
    axes[1].tick_params(axis="x", rotation=20)
    axes[1].grid(axis="y", linestyle="--", alpha=0.35)
    axes[1].set_axisbelow(True)
    for bar, value in zip(bars, counts.values):
        axes[1].text(bar.get_x() + bar.get_width() / 2, value + 12, str(int(value)), ha="center", fontsize=9)
    axes[1].set_title("Salida operativa reproducida", fontsize=11, fontweight="bold")
    fig.tight_layout()
    save(fig, "fig_3_10_obj4_segregacion_riesgo.png")


def main() -> None:
    dataset = pd.read_csv(DATA_PATH)
    metrics = json.loads(METRICS_PATH.read_text(encoding="utf-8"))
    objective_1(dataset)
    objective_2(dataset)
    objective_3(metrics)
    objective_4(dataset)
    print("Evidencias metodológicas generadas sin datos personales.")


if __name__ == "__main__":
    main()
