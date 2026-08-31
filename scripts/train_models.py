"""Entrenamiento reproducible para predecir rezago en la gestión T+1.

Evalúa temporalmente con transiciones 2022->2023 / 2023->2024 y exporta
modelos de despliegue reentrenados con todas las transiciones disponibles.
No utiliza identificadores ni datos personales como predictores.
"""

from __future__ import annotations

import json
import hashlib
import platform
from pathlib import Path
from datetime import datetime, timezone

import joblib
import numpy as np
import pandas as pd
import sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    average_precision_score,
    balanced_accuracy_score,
    confusion_matrix,
    precision_recall_fscore_support,
)
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data/03_Datasets_Procesados/primaria_dataset.csv"
MODEL_DIR = ROOT / "modelos_entrenados"
RESULT_DIR = ROOT / "resultados_modelos"
FEATURE_SOURCE = ["promedio_general", "num_materias_reprobadas"]
FEATURE_MODEL = ["promedio_general_prev", "num_materias_reprobadas_prev"]
RANDOM_STATE = 42


def build_transitions(dataset: pd.DataFrame) -> pd.DataFrame:
    required = {"rude", "gestion", "rezago", *FEATURE_SOURCE}
    missing = sorted(required - set(dataset.columns))
    if missing:
        raise ValueError(f"Faltan columnas requeridas: {missing}")

    data = dataset.sort_values(["rude", "gestion"]).copy()
    data["gestion_objetivo"] = data.groupby("rude")["gestion"].shift(-1)
    data["rezago_next"] = data.groupby("rude")["rezago"].shift(-1)
    target_features = data.groupby("rude")[FEATURE_SOURCE].shift(-1)
    data["objetivo_completo"] = target_features.notna().all(axis=1)
    transitions = data[
        data["gestion_objetivo"].eq(data["gestion"] + 1)
        & data["rezago_next"].notna()
        & data[FEATURE_SOURCE].notna().all(axis=1)
        & data["objetivo_completo"]
    ].copy()
    transitions = transitions.rename(
        columns={
            "promedio_general": "promedio_general_prev",
            "num_materias_reprobadas": "num_materias_reprobadas_prev",
        }
    )
    transitions["rezago_next"] = transitions["rezago_next"].astype(int)
    return transitions


def make_models() -> dict[str, object]:
    return {
        "decision_tree": DecisionTreeClassifier(
            max_depth=3,
            min_samples_leaf=10,
            class_weight="balanced",
            random_state=RANDOM_STATE,
        ),
        "random_forest": RandomForestClassifier(
            n_estimators=300,
            max_depth=4,
            min_samples_leaf=5,
            class_weight="balanced",
            random_state=RANDOM_STATE,
        ),
        "mlp": MLPClassifier(
            hidden_layer_sizes=(4,),
            alpha=0.1,
            learning_rate_init=0.0001,
            max_iter=1000,
            random_state=RANDOM_STATE,
        ),
    }


def metrics(y_true: pd.Series, prob: np.ndarray, threshold: float = 0.5) -> dict:
    pred = (prob >= threshold).astype(int)
    precision, recall, f1, support = precision_recall_fscore_support(
        y_true, pred, labels=[0, 1], zero_division=0
    )
    return {
        "threshold": threshold,
        "confusion_matrix": confusion_matrix(y_true, pred, labels=[0, 1]).tolist(),
        "balanced_accuracy": float(balanced_accuracy_score(y_true, pred)),
        "average_precision": float(average_precision_score(y_true, prob)),
        "precision_rezago": float(precision[1]),
        "recall_rezago": float(recall[1]),
        "f1_rezago": float(f1[1]),
        "support_no_rezago": int(support[0]),
        "support_rezago": int(support[1]),
    }


def majority_baseline(y_true: pd.Series) -> dict:
    """Línea base que siempre predice la clase mayoritaria (sin rezago)."""
    probabilities = np.zeros(len(y_true), dtype=float)
    return metrics(y_true, probabilities)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    dataset = pd.read_csv(DATA_PATH)
    transitions = build_transitions(dataset)
    train = transitions[transitions["gestion"].eq(2022)].copy()
    test = transitions[transitions["gestion"].eq(2023)].copy()
    if train.empty or test.empty:
        raise ValueError("No existen transiciones temporales suficientes para 2022 y 2023.")

    X_train, y_train = train[FEATURE_MODEL], train["rezago_next"]
    X_test, y_test = test[FEATURE_MODEL], test["rezago_next"]
    evaluation = {}
    models = make_models()
    scaler_eval = StandardScaler().fit(X_train)

    for name, model in models.items():
        if name == "mlp":
            model.fit(scaler_eval.transform(X_train), y_train)
            prob = model.predict_proba(scaler_eval.transform(X_test))[:, 1]
        else:
            model.fit(X_train, y_train)
            prob = model.predict_proba(X_test)[:, 1]
        evaluation[name] = metrics(y_test, prob)
    evaluation["baseline_sin_rezago"] = majority_baseline(y_test)

    # Modelos de despliegue: se reentrenan con todas las transiciones observadas.
    X_all, y_all = transitions[FEATURE_MODEL], transitions["rezago_next"]
    deploy = make_models()
    scaler = StandardScaler().fit(X_all)
    deploy["random_forest"].fit(X_all, y_all)
    deploy["mlp"].fit(scaler.transform(X_all), y_all)

    MODEL_DIR.mkdir(parents=True, exist_ok=True)
    RESULT_DIR.mkdir(parents=True, exist_ok=True)
    joblib.dump(deploy["random_forest"], MODEL_DIR / "random_forest_model.pkl")
    joblib.dump(deploy["mlp"], MODEL_DIR / "mlp_model.pkl")
    joblib.dump(scaler, MODEL_DIR / "scaler.pkl")

    metadata = {
        "version_artefacto": "1.1.0",
        "fecha_entrenamiento_utc": datetime.now(timezone.utc).isoformat(),
        "dataset_sha256": sha256_file(DATA_PATH),
        "entorno": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "pandas": pd.__version__,
            "scikit_learn": sklearn.__version__,
            "joblib": joblib.__version__,
        },
        "metodologia": "Predictores de gestión T y rezago de gestión T+1",
        "periodo_dataset": sorted(int(x) for x in dataset["gestion"].unique()),
        "n_observaciones_dataset": int(len(dataset)),
        "n_estudiantes_unicos": int(dataset["rude"].nunique()),
        "n_transiciones": int(len(transitions)),
        "positivos_transiciones": int(transitions["rezago_next"].sum()),
        "entrenamiento_temporal": {
            "transicion": "2022->2023",
            "n": int(len(train)),
            "positivos": int(y_train.sum()),
        },
        "prueba_temporal": {
            "transicion": "2023->2024",
            "n": int(len(test)),
            "positivos": int(y_test.sum()),
        },
        "variables_predictoras": FEATURE_MODEL,
        "orden_variables_modelo": FEATURE_MODEL,
        "evaluacion": evaluation,
        "nota_limitacion": (
            "Solo existen seis transiciones positivas; las métricas son exploratorias "
            "y no demuestran generalización a otras cohortes ni eficacia pedagógica."
        ),
        "modelos_despliegue": {
            "random_forest": deploy["random_forest"].get_params(),
            "mlp": deploy["mlp"].get_params(),
        },
    }
    (RESULT_DIR / "metricas_modelos.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2, default=str), encoding="utf-8"
    )
    print(json.dumps(metadata, ensure_ascii=False, indent=2, default=str))


if __name__ == "__main__":
    main()
