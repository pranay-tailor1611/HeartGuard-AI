from fastapi import APIRouter, HTTPException, status
from datetime import datetime
import logging

from schemas import PatientInput, PredictionResponse, HealthCheckResponse
from predict import predictor
from utils import generate_recommendations, compute_health_score, get_dataset_stats
from config import APP_VERSION

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api")

@router.get("/health", response_model=HealthCheckResponse)
def health_check():
    """Health check endpoint to verify backend and ML model status."""
    return HealthCheckResponse(
        status="healthy",
        model_loaded=predictor.is_loaded,
        version=APP_VERSION
    )

@router.post("/predict", response_model=PredictionResponse)
def predict_cardiac_risk(patient: PatientInput):
    """
    Main prediction endpoint accepting JSON patient clinical data and returning ML risk evaluation.
    """
    try:
        prediction, confidence, disease_prob = predictor.predict(patient)
        
        risk_label = "High Risk of Heart Disease" if prediction == 1 else "Low Risk / Healthy Profile"
        health_score = compute_health_score(prediction, disease_prob)
        recommendations = generate_recommendations(prediction, disease_prob)

        return PredictionResponse(
            prediction=prediction,
            risk_label=risk_label,
            confidence=confidence,
            disease_probability=disease_prob,
            health_score=health_score,
            recommendations=recommendations,
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
    except Exception as e:
        logger.error(f"Error executing prediction endpoint: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Inference execution failed: {str(e)}"
        )

@router.get("/dataset/stats")
def fetch_dataset_stats():
    """Endpoint returning dataset summary statistics for the analytics dashboard."""
    stats = get_dataset_stats()
    if "error" in stats:
        raise HTTPException(status_code=500, detail=stats["error"])
    return stats
