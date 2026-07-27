/**
 * CardioPulse AI - Prediction Form & API Handler (v2.5.0)
 */

document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("predictionForm");
    const heightInput = document.getElementById("height_cm");
    const weightInput = document.getElementById("weight_kg");
    const clearBtn = document.getElementById("clearFormBtn");

    if (heightInput && weightInput) {
        heightInput.addEventListener("input", calculateBMI);
        weightInput.addEventListener("input", calculateBMI);
        calculateBMI();
    }

    if (form) {
        form.addEventListener("submit", handlePredictionSubmit);
    }

    if (clearBtn) {
        clearBtn.addEventListener("click", function () {
            form.reset();
            calculateBMI();
            const resultSection = document.getElementById("resultSection");
            if (resultSection) resultSection.classList.add("d-none");
        });
    }
});

function calculateBMI() {
    const h = parseFloat(document.getElementById("height_cm").value) || 170;
    const w = parseFloat(document.getElementById("weight_kg").value) || 70;
    const bmiVal = document.getElementById("bmiValue");
    const bmiBadge = document.getElementById("bmiBadge");

    if (!bmiVal || !bmiBadge) return;

    const bmi = (w / Math.pow(h / 100, 2)).toFixed(1);
    bmiVal.innerText = `${bmi} kg/m²`;

    if (bmi < 18.5) {
        bmiBadge.innerText = "Underweight";
        bmiBadge.className = "badge-minimal";
    } else if (bmi >= 18.5 && bmi < 25) {
        bmiBadge.innerText = "Normal";
        bmiBadge.className = "badge-success-minimal";
    } else if (bmi >= 25 && bmi < 30) {
        bmiBadge.innerText = "Overweight";
        bmiBadge.className = "badge-minimal";
    } else {
        bmiBadge.innerText = "Obese";
        bmiBadge.className = "badge-danger-minimal";
    }
}

async function handlePredictionSubmit(e) {
    e.preventDefault();

    const spinner = document.getElementById("loadingSpinner");
    const resultSection = document.getElementById("resultSection");
    const submitBtn = document.getElementById("submitBtn");

    const payload = {
        age: parseInt(document.getElementById("age").value),
        sex: document.getElementById("sex").value,
        chest_pain: document.getElementById("chest_pain").value,
        resting_bp: parseInt(document.getElementById("resting_bp").value),
        cholesterol: parseInt(document.getElementById("cholesterol").value),
        fasting_bs: parseInt(document.getElementById("fasting_bs").value),
        resting_ecg: document.getElementById("resting_ecg").value,
        max_hr: parseInt(document.getElementById("max_hr").value),
        exercise_angina: document.getElementById("exercise_angina").value,
        oldpeak: parseFloat(document.getElementById("oldpeak").value),
        st_slope: document.getElementById("st_slope").value
    };

    if (spinner) spinner.classList.remove("d-none");
    if (resultSection) resultSection.classList.add("d-none");
    if (submitBtn) submitBtn.disabled = true;

    try {
        const apiBase = window.API_BASE_URL || "";
        const response = await fetch(`${apiBase}/api/predict`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });

        if (!response.ok) {
            throw new Error(`Server returned HTTP ${response.status}`);
        }

        const data = await response.json();
        renderPredictionResult(data, payload);
    } catch (err) {
        console.error("Prediction API Error:", err);
        alert("Prediction request failed. Ensure backend server is running on http://127.0.0.1:8000.");
    } finally {
        if (spinner) spinner.classList.add("d-none");
        if (submitBtn) submitBtn.disabled = false;
    }
}

function renderPredictionResult(data, payload) {
    const resultSection = document.getElementById("resultSection");
    const cardContainer = document.getElementById("resultCardContainer");
    const recSection = document.getElementById("recommendationsContainer");

    if (!resultSection || !cardContainer) return;

    const isHighRisk = data.prediction === 1;

    cardContainer.innerHTML = `
        <div class="med-card text-start bg-white">
            <div class="d-flex justify-content-between align-items-center mb-3">
                <span class="${isHighRisk ? 'badge-danger-minimal' : 'badge-success-minimal'}">
                    ${isHighRisk ? '⚠️ High Risk Stratification' : '✅ Low Risk Profile'}
                </span>
                <span class="text-muted small">Confidence: <b>${data.confidence}%</b></span>
            </div>
            <h3 class="fw-bold mb-2">${isHighRisk ? 'Elevated Cardiac Disease Risk Detected' : 'Healthy Cardiac Risk Profile'}</h3>
            <p class="text-muted mb-3">
                ${isHighRisk 
                    ? 'Significant risk indicators were identified based on ST depression, blood pressure, or cholesterol markers.' 
                    : 'No major risk indicators were detected by the predictive model for the provided physiological parameters.'}
            </p>
            <hr class="my-3"/>
            <div class="d-flex justify-content-between align-items-center flex-wrap">
                <span>Health Score: <b>${data.health_score}/100</b></span>
                <span class="text-muted small">Evaluated: ${data.timestamp}</span>
            </div>
        </div>
    `;

    if (recSection && data.recommendations) {
        recSection.innerHTML = `
            <div class="med-card bg-white">
                <h4 class="fw-bold mb-3">📋 Clinical & Lifestyle Recommendations</h4>
                <div class="row g-4">
                    <div class="col-md-6">
                        <h5>🏃 Exercise & Activity</h5>
                        <ul>${data.recommendations.exercise.map(item => `<li>${item}</li>`).join('')}</ul>
                    </div>
                    <div class="col-md-6">
                        <h5>🥗 Dietary Pattern</h5>
                        <ul>${data.recommendations.diet.map(item => `<li>${item}</li>`).join('')}</ul>
                    </div>
                    <div class="col-md-6">
                        <h5>💧 Hydration & Sleep</h5>
                        <ul>${data.recommendations.hydration_sleep.map(item => `<li>${item}</li>`).join('')}</ul>
                    </div>
                    <div class="col-md-6">
                        <h5>👨‍⚕️ Medical Action</h5>
                        <ul>${data.recommendations.medical_action.map(item => `<li>${item}</li>`).join('')}</ul>
                    </div>
                </div>
            </div>
        `;
    }

    const downloadBtn = document.getElementById("downloadReportBtn");
    if (downloadBtn) {
        downloadBtn.onclick = () => downloadReportText(data, payload);
    }

    resultSection.classList.remove("d-none");
    resultSection.scrollIntoView({ behavior: "smooth" });
}

function downloadReportText(data, payload) {
    const report = `
=====================================================
CARDIOPULSE AI - CLINICAL ASSESSMENT REPORT
=====================================================
Date/Time: ${data.timestamp}
Patient Age: ${payload.age} | Gender: ${payload.sex}
Resting BP: ${payload.resting_bp} mm Hg | Cholesterol: ${payload.cholesterol} mg/dl
Max Heart Rate: ${payload.max_hr} bpm | ST Depression: ${payload.oldpeak}

PREDICTION RESULT: ${data.risk_label.toUpperCase()}
CONFIDENCE SCORE: ${data.confidence}%
DISEASE PROBABILITY: ${data.disease_probability}%
HEALTH SCORE: ${data.health_score}/100

Disclaimer: Generated by AI decision support algorithm. Not a substitute for certified medical diagnosis.
=====================================================
    `;

    const blob = new Blob([report], { type: "text/plain" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = `CardioPulse_Report_${Date.now()}.txt`;
    a.click();
    URL.revokeObjectURL(url);
}
