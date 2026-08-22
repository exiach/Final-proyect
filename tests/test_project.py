import sys
import unittest
from pathlib import Path

import joblib
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
APP = ROOT / "Obj5_Prototipo_Dashboard_Docente"
sys.path.insert(0, str(APP))

from src.data_loader import process_dataframe  # noqa: E402
from src.predictor import enrich_with_predictions, predict_student_risk_details  # noqa: E402
from scripts.train_models import build_transitions  # noqa: E402


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


if __name__ == "__main__":
    unittest.main()
