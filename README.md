# ❤️ CardioPulse AI — Cardiovascular Disease Risk Prediction System

## 📌 Overview

CardioPulse AI is an enterprise-grade full-stack healthcare web application designed for **Cardiovascular Disease Risk Prediction**.

The application uses a pre-trained **K-Nearest Neighbors (KNN) Machine Learning classifier** with a **FastAPI backend** and a modern responsive frontend to analyze patient health parameters and predict cardiovascular disease risk.

This project demonstrates the integration of Artificial Intelligence, Machine Learning, and Full-Stack Web Development to build a real-world healthcare prediction system.

---

# 🚀 Features

## 🤖 Machine Learning Prediction
- Cardiovascular disease risk prediction using KNN classifier.
- Pre-trained ML model integration.
- Probability-based prediction results.
- Standardized input processing using saved scaler.

## 🩺 Patient Risk Assessment

Users can provide medical information including:

- Age
- Gender
- Chest Pain Type
- Resting Blood Pressure
- Cholesterol Level
- Fasting Blood Sugar
- Resting ECG
- Maximum Heart Rate
- Exercise Angina
- Oldpeak
- ST Slope

and receive instant risk prediction.

## 📊 Analytics Dashboard

- Interactive healthcare analytics dashboard.
- Dataset statistics visualization.
- Chart.js based data representation.

## ⚡ FastAPI Backend

- High-performance REST API.
- Automatic API documentation.
- Clean backend architecture.
- Health monitoring endpoint.

## 🎨 Modern Frontend

- Responsive healthcare interface.
- Bootstrap 5 styling.
- Vanilla JavaScript functionality.
- Interactive animations.

---

# 🏗️ System Architecture

```
User
 |
 ↓
Frontend Interface
(HTML + CSS + JavaScript)
 |
 ↓
FastAPI Backend
 |
 ↓
ML Prediction Pipeline
 |
 ↓
KNN Classification Model
 |
 ↓
Risk Prediction Result
```

---

# 📂 Project Structure

```
HeartDiseasePrediction/

├── backend/
│   ├── main.py
│   ├── routes.py
│   ├── predict.py
│   ├── schemas.py
│   ├── config.py
│   ├── utils.py
│   ├── requirements.txt
│   │
│   └── models/
│       ├── model.pkl
│       ├── scaler.pkl
│       └── columns.pkl
│
├── frontend/
│   ├── index.html
│   ├── prediction.html
│   ├── dashboard.html
│   ├── about.html
│   ├── faq.html
│   ├── contact.html
│   ├── developer.html
│   │
│   ├── css/
│   │   └── style.css
│   │
│   └── js/
│       ├── app.js
│       ├── prediction.js
│       ├── dashboard.js
│       └── animations.js
│
└── README.md
```

---

# 🔒 Machine Learning Model

The ML engine uses a trained:

### Model
- K-Nearest Neighbors (KNN)

### Saved ML Components

```
model.pkl
```
Contains the trained KNN classifier.

```
scaler.pkl
```
Contains StandardScaler for feature normalization.

```
columns.pkl
```
Contains expected feature mapping definitions.

The original ML pipeline is preserved including:

- Feature encoding
- Column mapping
- Data scaling
- Model prediction
- Probability calculation

---

# 🔌 API Endpoints

## Health Check

### GET

```
/api/health
```

Checks backend status and confirms ML model availability.

---

## Prediction API

### POST

```
/api/predict
```

Example Request:

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

---

## Dataset Statistics

### GET

```
/api/dataset/stats
```

Provides statistical information used for dashboard visualization.

---

# ⚙️ Installation & Setup

## Clone Repository

```bash
git clone https://github.com/pranay-tailor1611/HeartGuard-AI
```

Go to project folder:

```bash
cd HeartDiseasePrediction
```

---

## Install Dependencies

```bash
pip install -r backend/requirements.txt
```

---

## Run Application

```bash
python -m uvicorn backend.main:app --reload --host 127.0.0.1 --port 8000
```

---

## Access Application

Web Application:

```
http://127.0.0.1:8000/
```

Swagger API Documentation:

```
http://127.0.0.1:8000/docs
```

ReDoc Documentation:

```
http://127.0.0.1:8000/redoc
```

---

# 🛠️ Tech Stack

## Frontend

- HTML5
- CSS3
- JavaScript
- Bootstrap 5
- Chart.js
- AOS Animation

## Backend

- Python
- FastAPI
- Pydantic
- Uvicorn

## Machine Learning

- Scikit-learn
- Pandas
- NumPy

## Deployment

- Render
- GitHub

---

# 🌐 Live Demo

Live Application:

https://heartguard-ai-3.onrender.com/

---

# 📸 Screenshots

## 🏠 Home Page

![Home Page](screenshots/home.png)

## ❤️ Prediction Page

##   About Page

![about Page](screenshots/about.png)

![Prediction Page](screenshots/prediction.png)

## 📊 Dashboard

![Dashboard](screenshots/dashboard.png)

## ✅ Prediction Result

![Prediction Result](screenshots/predictOutput.png)

---

# 🔮 Future Improvements

- Add user authentication.
- Store prediction history.
- Add doctor dashboard.
- Integrate real-time health monitoring.
- Improve prediction accuracy using advanced ML/DL models.

---

# 👨‍💻 Developer

**Pranay Tailor**

B.Tech Computer Science Engineering

GitHub:
https://github.com/pranay-tailor1611

---

⭐ If you like this project, consider giving it a star on GitHub.