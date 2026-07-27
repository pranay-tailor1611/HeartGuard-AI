import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODELS_DIR = os.path.join(BASE_DIR, "models")

MODEL_PATH = os.path.join(MODELS_DIR, "model.pkl")
SCALER_PATH = os.path.join(MODELS_DIR, "scaler.pkl")
COLUMNS_PATH = os.path.join(MODELS_DIR, "columns.pkl")

DATASET_PATH = os.path.join(os.path.dirname(BASE_DIR), "heart.csv")

APP_TITLE = "CardioPulse AI API"
APP_VERSION = "2.4.0"
DEBUG = True
