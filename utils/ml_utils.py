import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
from datetime import datetime

@st.cache_resource
def load_ml_assets():
    """Load machine learning model, scaler, and expected feature columns."""
    model_filename = "KNN_heart.pkl" if os.path.exists("KNN_heart.pkl") else "knn_heart.pkl"
    model = joblib.load(model_filename)
    scaler = joblib.load("scaler.pkl")
    expected_columns = joblib.load("columns.pkl")
    return model, scaler, expected_columns

@st.cache_data
def load_dataset():
    """Load clinical dataset heart.csv for dashboard statistics."""
    if os.path.exists("heart.csv"):
        return pd.read_csv("heart.csv")
    return None

def predict_heart_disease(age, sex, chest_pain, resting_bp, cholesterol, fasting_bs, 
                          resting_ecg, max_hr, exercise_angina, oldpeak, st_slope):
    """
    Executes model prediction preserving original encoding, scaling, and classification logic.
    """
    model, scaler, expected_columns = load_ml_assets()

    # Construct raw input mapping exactly as required by the model dummy columns
    raw_input = {
        'Age': age,
        'RestingBP': resting_bp,
        'Cholesterol': cholesterol,
        'FastingBS': fasting_bs,
        'MaxHR': max_hr,
        'Oldpeak': oldpeak,
        'Sex_' + sex: 1,
        'ChestPainType_' + chest_pain: 1,
        'RestingECG_' + resting_ecg: 1,
        'ExerciseAngina_' + exercise_angina: 1,
        'ST_Slope_' + st_slope: 1
    }

    input_df = pd.DataFrame([raw_input])

    # Fill missing dummy columns with 0
    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    # Ensure exact column order matching model expectation
    input_df = input_df[expected_columns]

    # Transform using trained scaler
    scaled_input = scaler.transform(input_df)

    # Perform inference
    prediction = int(model.predict(scaled_input)[0])

    # Get probability/confidence metrics
    if hasattr(model, "predict_proba"):
        probs = model.predict_proba(scaled_input)[0]
        confidence_score = round(float(probs[prediction]) * 100, 1)
        disease_probability = round(float(probs[1]) * 100, 1)
    else:
        confidence_score = 90.0
        disease_probability = 90.0 if prediction == 1 else 10.0

    return prediction, confidence_score, disease_probability
