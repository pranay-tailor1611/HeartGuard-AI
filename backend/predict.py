import joblib
import pandas as pd
import numpy as np
import logging
from backend.config import MODEL_PATH, SCALER_PATH, COLUMNS_PATH
from backend.schemas import PatientInput

logger = logging.getLogger(__name__)

class Predictor:
    def __init__(self):
        self.model = None
        self.scaler = None
        self.expected_columns = None
        self.is_loaded = False

    def load_assets(self):
        """Loads trained KNN model, scaler, and expected dummy columns."""
        try:
            self.model = joblib.load(MODEL_PATH)
            self.scaler = joblib.load(SCALER_PATH)
            self.expected_columns = joblib.load(COLUMNS_PATH)
            self.is_loaded = True
            logger.info("ML model, scaler, and column definitions loaded successfully.")
        except Exception as e:
            logger.error(f"Failed to load ML assets: {e}")
            raise e

    def predict(self, patient: PatientInput):
        """
        Executes prediction preserving exact original encoding, scaling, and classification logic.
        """
        if not self.is_loaded:
            self.load_assets()

        # Construct raw input mapping exactly as required by the model dummy columns
        raw_input = {
            'Age': patient.age,
            'RestingBP': patient.resting_bp,
            'Cholesterol': patient.cholesterol,
            'FastingBS': patient.fasting_bs,
            'MaxHR': patient.max_hr,
            'Oldpeak': patient.oldpeak,
            'Sex_' + patient.sex: 1,
            'ChestPainType_' + patient.chest_pain: 1,
            'RestingECG_' + patient.resting_ecg: 1,
            'ExerciseAngina_' + patient.exercise_angina: 1,
            'ST_Slope_' + patient.st_slope: 1
        }

        input_df = pd.DataFrame([raw_input])

        # Fill missing expected dummy columns with 0
        for col in self.expected_columns:
            if col not in input_df.columns:
                input_df[col] = 0

        # Reorder columns to match scaler and model expectation exactly
        input_df = input_df[self.expected_columns]

        # Transform using trained scaler
        scaled_input = self.scaler.transform(input_df)

        # Perform inference
        prediction = int(self.model.predict(scaled_input)[0])

        # Get probability / confidence
        if hasattr(self.model, "predict_proba"):
            probs = self.model.predict_proba(scaled_input)[0]
            confidence_score = round(float(probs[prediction]) * 100, 1)
            disease_probability = round(float(probs[1]) * 100, 1)
        else:
            confidence_score = 90.0
            disease_probability = 90.0 if prediction == 1 else 10.0

        return prediction, confidence_score, disease_probability

predictor = Predictor()
