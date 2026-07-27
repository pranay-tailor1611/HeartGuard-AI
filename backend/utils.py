import pandas as pd
import os
import logging
from backend.config import DATASET_PATH
from backend.schemas import Recommendations

logger = logging.getLogger(__name__)

def generate_recommendations(prediction: int, disease_prob: float) -> Recommendations:
    """Generates structured clinical recommendations based on prediction outcome."""
    if prediction == 1:
        return Recommendations(
            exercise=[
                "Consult a cardiologist before engaging in high-intensity workouts.",
                "Begin with 20-30 minutes of mild walking daily under cardiac monitoring.",
                "Avoid heavy isometric strain or heavy lifting."
            ],
            diet=[
                "Adopt the DASH or Mediterranean dietary pattern.",
                "Restrict daily sodium intake to under 2,000 mg.",
                "Eliminate trans fats and fried foods to maintain cholesterol levels."
            ],
            hydration_sleep=[
                "Maintain 2.5 - 3.0 Liters of water daily to optimize blood viscosity.",
                "Ensure 7-9 hours of restful sleep daily to lower resting cortisol."
            ],
            medical_action=[
                "Schedule a comprehensive cardiologist consultation within 7 days.",
                "Obtain a full lipid panel and 12-lead resting ECG.",
                "Emergency Cardiac Hotline: Call 108 or 1800-123-CARDIAC for acute chest pressure."
            ]
        )
    else:
        return Recommendations(
            exercise=[
                "Aim for 150 minutes of moderate aerobic exercise per week.",
                "Incorporate strength and flexibility training 2 days per week."
            ],
            diet=[
                "Focus on whole grains, fresh vegetables, lean proteins, and healthy fats.",
                "Maintain low sodium and minimal refined sugar intake."
            ],
            hydration_sleep=[
                "Drink 2.5 - 3.0 Liters of water daily.",
                "Target 7-9 hours of sleep per night."
            ],
            medical_action=[
                "Maintain annual routine wellness checkups.",
                "Monitor resting blood pressure and lipid profile periodically."
            ]
        )

def compute_health_score(prediction: int, disease_prob: float) -> int:
    """Computes a baseline health score out of 100."""
    if prediction == 1:
        return max(15, int(100 - disease_prob))
    else:
        return min(98, int(100 - (disease_prob * 0.5)))

def get_dataset_stats():
    """Reads heart.csv and returns statistical summaries for the analytics dashboard."""
    if not os.path.exists(DATASET_PATH):
        return {"error": "Dataset heart.csv not found"}
    
    try:
        df = pd.read_csv(DATASET_PATH)
        total_records = len(df)
        disease_count = int(df['HeartDisease'].sum())
        healthy_count = total_records - disease_count
        disease_rate = round((disease_count / total_records) * 100, 1)

        age_distribution = df['Age'].tolist()
        cp_counts = df['ChestPainType'].value_counts().to_dict()
        slope_counts = df['ST_Slope'].value_counts().to_dict()

        return {
            "total_records": total_records,
            "disease_count": disease_count,
            "healthy_count": healthy_count,
            "disease_rate": disease_rate,
            "avg_age": round(float(df['Age'].mean()), 1),
            "avg_bp": round(float(df['RestingBP'].mean()), 1),
            "avg_cholesterol": round(float(df['Cholesterol'].mean()), 1),
            "chest_pain_counts": cp_counts,
            "st_slope_counts": slope_counts
        }
    except Exception as e:
        logger.error(f"Error computing dataset stats: {e}")
        return {"error": str(e)}
