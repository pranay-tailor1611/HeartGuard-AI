# CardioPulse AI — Production Full-Stack Web Application

CardioPulse AI is a enterprise-grade full-stack healthcare web application for **Cardiovascular Disease Risk Prediction**. Powered by a pre-trained K-Nearest Neighbors (KNN) Machine Learning classifier, FastAPI microservice backend, and a modern Bootstrap 5 / Vanilla JS minimalist frontend.

---

## 🏗️ Architecture & Directory Structure

```
HeartDiseasePrediction/
├── backend/
│   ├── main.py              # FastAPI Application Entry & Static File Server
│   ├── routes.py            # API Route Handlers (/api/predict, /api/health, /api/dataset/stats)
│   ├── predict.py           # Preserved ML Inference Pipeline Engine
│   ├── schemas.py           # Pydantic Input/Output Schemas
│   ├── config.py            # Model File Locations & Configuration Settings
│   ├── utils.py             # Recommendation Generator & Dataset Analytics
│   ├── requirements.txt     # Backend Python Dependencies
│   └── models/
│       ├── model.pkl        # Preserved KNN Classifier Model
│       ├── scaler.pkl       # Preserved StandardScaler Object
│       └── columns.pkl      # Preserved Dummy Column Mapping Definitions
│
├── frontend/
│   ├── index.html           # Landing Page & Feature Showcase
│   ├── prediction.html      # 2-Column Assessment Form, BMI Calc & Results
│   ├── dashboard.html       # Chart.js Visual Analytics Dashboard
│   ├── about.html           # Pathology & Diagnostics Guide
│   ├── faq.html             # Accordion FAQ Component
│   ├── contact.html         # Emergency Contacts & Consultation Hotlines
│   ├── developer.html       # Senior Full-Stack AI Engineer Profile
│   ├── css/
│   │   └── style.css        # Minimalist Luxury SaaS Stylesheet
│   └── js/
│       ├── app.js           # Shared App Controller & Health Checks
│       ├── prediction.js    # Prediction Fetch API Request Handler
│       ├── dashboard.js     # Chart.js Visual Analytics Engine
│       └── animations.js   # AOS Animation Initializer
│
└── README.md
```

---

## 🔒 Preserved ML Engine

- Models loaded directly from `backend/models/`:
  - `model.pkl` (KNN Classifier)
  - `scaler.pkl` (StandardScaler)
  - `columns.pkl` (Expected Feature List)
- **Zero Retraining or Pipeline Modification**: Identical dummy column mapping (`Sex_`, `ChestPainType_`, `RestingECG_`, `ExerciseAngina_`, `ST_Slope_`), standard scaling, `predict()`, and `predict_proba()` functions preserved.

---

## 🚀 Quickstart & Server Launch

### 1. Install Backend Dependencies
```bash
pip install -r backend/requirements.txt
```

### 2. Launch FastAPI Full-Stack Web Server
```bash
python -m uvicorn backend.main:app --reload --host 127.0.0.1 --port 8000
```

### 3. Access Application in Browser
Open your browser and navigate to:
- **Web App UI**: `http://127.0.0.1:8000/`
- **Interactive Swagger API Docs**: `http://127.0.0.1:8000/docs`
- **ReDoc API Documentation**: `http://127.0.0.1:8000/redoc`

---

## 🔌 API Endpoints

### `GET /api/health`
Returns backend service health status and loaded model confirmation.

### `POST /api/predict`
Accepts patient physiological data JSON and executes ML inference.
```json
{
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
```

### `GET /api/dataset/stats`
Returns aggregated statistical metrics calculated from `heart.csv` for Chart.js visual analytics.
