from pydantic import BaseModel, Field
from typing import List, Dict, Optional

class PatientInput(BaseModel):
    age: int = Field(..., ge=1, le=120, description="Patient age in years")
    sex: str = Field(..., description="Gender ('M' or 'F')")
    chest_pain: str = Field(..., description="Chest pain type ('ATA', 'NAP', 'TA', 'ASY')")
    resting_bp: int = Field(..., ge=50, le=250, description="Resting blood pressure in mm Hg")
    cholesterol: int = Field(..., ge=0, le=700, description="Serum cholesterol in mg/dl")
    fasting_bs: int = Field(..., ge=0, le=1, description="Fasting blood sugar > 120 mg/dl (1 or 0)")
    resting_ecg: str = Field(..., description="Resting ECG ('Normal', 'ST', 'LVH')")
    max_hr: int = Field(..., ge=50, le=250, description="Maximum heart rate achieved")
    exercise_angina: str = Field(..., description="Exercise-induced angina ('Y' or 'N')")
    oldpeak: float = Field(..., ge=0.0, le=10.0, description="ST depression induced by exercise")
    st_slope: str = Field(..., description="Peak exercise ST slope ('Up', 'Flat', 'Down')")

    class Config:
        json_schema_extra = {
            "example": {
                "age": 55,
                "sex": "M",
                "chest_pain": "ASY",
                "resting_bp": 140,
                "cholesterol": 260,
                "fasting_bs": 1,
                "resting_ecg": "Normal",
                "max_hr": 130,
                "exercise_angina": "Y",
                "oldpeak": 2.0,
                "st_slope": "Flat"
            }
        }

class Recommendations(BaseModel):
    exercise: List[str]
    diet: List[str]
    hydration_sleep: List[str]
    medical_action: List[str]

class PredictionResponse(BaseModel):
    prediction: int
    risk_label: str
    confidence: float
    disease_probability: float
    health_score: int
    recommendations: Recommendations
    timestamp: str

class HealthCheckResponse(BaseModel):
    status: str
    model_loaded: bool
    version: str
