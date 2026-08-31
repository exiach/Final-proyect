import sys
import unittest
from pathlib import Path

import joblib
import json
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
APP = ROOT / "Obj5_Prototipo_Dashboard_Docente"
sys.path.insert(0, str(APP))

from src.data_loader import process_dataframe  # noqa: E402
from src.privacy import public_student_code  # noqa: E402
from src.predictor import enrich_with_predictions, predict_student_risk_details  # noqa: E402
from scripts.train_models import FEATURE_MODEL, build_transitions  # noqa: E402


class ProjectTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rf = joblib.load(ROOT / "modelos_entrenados/random_forest_model.pkl")
        cls.mlp = joblib.load(ROOT / "modelos_entrenados/mlp_model.pkl")
        cls.scaler = joblib.load(ROOT / "modelos_entrenados/scaler.pkl")

    def valid_row(self):
        row = {"gestion": 2025, "anio_escolaridad": "PRIMERO", "paralelo": "A", "rude": "PSEUDO-1"}
        for name in [
            'com_lenguajes', 'cs_sociales', 'edu_fisica', 'edu_musical',
            'art_plasticas', 'matematica', 'tec_tecnologica', 'cs_naturales',
            'valores_religion'
        ]:
            row[name] = 70
        return row

    def test_valid_upload_is_processed(self):
        result = process_dataframe(pd.DataFrame([self.valid_row()]))
        self.assertEqual(result.loc[0, "promedio_general"], 70)
        self.assertEqual(result.loc[0, "num_materias_reprobadas"], 0)

    def test_missing_columns_are_rejected(self):
        with self.assertRaises(ValueError):
            process_dataframe(pd.DataFrame([{"gestion": 2025}]))

    def test_out_of_range_notes_are_rejected(self):
        row = self.valid_row()
        row["matematica"] = 101
        with self.assertRaises(ValueError):
            process_dataframe(pd.DataFrame([row]))

    def test_rule_and_model_are_reported_separately(self):
        detail = predict_student_risk_details(50, 0, "Random Forest", self.rf, self.mlp, self.scaler)
        self.assertEqual(detail["nivel_riesgo"], "Alto Riesgo")
        self.assertGreaterEqual(detail["probabilidad_operativa"], 0.85)
        self.assertIn("Regla pedagógica", detail["motivo"])

    def test_incomplete_historical_row_is_not_predicted(self):
        row = self.valid_row()
        row["matematica"] = None
        historical = process_dataframe(pd.DataFrame([row]), allow_missing_notes=True)
        result = enrich_with_predictions(historical, "Random Forest", self.rf, self.mlp, self.scaler)
        self.assertEqual(result.loc[0, "nivel_riesgo"], "Sin datos")
        self.assertTrue(pd.isna(result.loc[0, "prob_modelo"]))

    def test_transition_with_incomplete_target_is_excluded(self):
        rows = []
        for year, average, failed, label in [(2022, 70, 0, 0), (2023, None, None, 0)]:
            rows.append({
                "rude": "PSEUDO-1",
                "gestion": year,
                "promedio_general": average,
                "num_materias_reprobadas": failed,
                "rezago": label,
            })
        self.assertTrue(build_transitions(pd.DataFrame(rows)).empty)

    def test_model_feature_schema_is_explicit_and_stable(self):
        self.assertEqual(FEATURE_MODEL, ["promedio_general_prev", "num_materias_reprobadas_prev"])
        self.assertEqual(list(self.rf.feature_names_in_), FEATURE_MODEL)

    def test_metrics_include_reproducibility_metadata_and_baseline(self):
        metrics = json.loads((ROOT / "resultados_modelos/metricas_modelos.json").read_text(encoding="utf-8"))
        self.assertEqual(metrics["orden_variables_modelo"], FEATURE_MODEL)
        self.assertEqual(len(metrics["dataset_sha256"]), 64)
        self.assertIn("python", metrics["entorno"])
        baseline = metrics["evaluacion"]["baseline_sin_rezago"]
        self.assertEqual(baseline["confusion_matrix"], [[245, 0], [3, 0]])
        self.assertEqual(baseline["balanced_accuracy"], 0.5)

    def test_public_code_is_stable_and_does_not_expose_identifier(self):
        code = public_student_code("809800682020086")
        self.assertEqual(code, public_student_code("809800682020086"))
        self.assertNotIn("809800682020086", code)
        self.assertTrue(code.startswith("EST-"))


if __name__ == "__main__":
    unittest.main()
