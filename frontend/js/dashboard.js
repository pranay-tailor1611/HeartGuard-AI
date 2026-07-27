/**
 * CardioPulse AI - Dashboard Analytics Controller (Chart.js)
 */

document.addEventListener("DOMContentLoaded", function () {
    fetchDashboardStats();
});

async function fetchDashboardStats() {
    try {
        const apiBase = window.API_BASE_URL || "";
        const response = await fetch(`${apiBase}/api/dataset/stats`);
        if (!response.ok) return;
        const data = await response.json();
        renderDashboardCharts(data);
    } catch (err) {
        console.warn("Failed to fetch dashboard stats:", err);
    }
}

function renderDashboardCharts(data) {
    // Metric Updates
    if (document.getElementById("totalPatientsVal")) {
        document.getElementById("totalPatientsVal").innerText = data.total_records;
    }
    if (document.getElementById("diseaseRateVal")) {
        document.getElementById("diseaseRateVal").innerText = `${data.disease_rate}%`;
    }
    if (document.getElementById("avgAgeVal")) {
        document.getElementById("avgAgeVal").innerText = `${data.avg_age} Yrs`;
    }
    if (document.getElementById("avgCholVal")) {
        document.getElementById("avgCholVal").innerText = `${data.avg_cholesterol} mg/dl`;
    }

    // Chart 1: Chest Pain Type Breakdown (Bar Chart)
    const ctxCp = document.getElementById("chartChestPain");
    if (ctxCp && data.chest_pain_counts) {
        new Chart(ctxCp, {
            type: "bar",
            data: {
                labels: Object.keys(data.chest_pain_counts),
                datasets: [{
                    label: "Patient Count",
                    data: Object.values(data.chest_pain_counts),
                    backgroundColor: "#111111",
                    borderRadius: 6
                }]
            },
            options: {
                responsive: true,
                plugins: { legend: { display: false } },
                scales: { y: { beginAtZero: true } }
            }
        });
    }

    // Chart 2: ST Slope Segment Distribution (Doughnut Chart)
    const ctxSlope = document.getElementById("chartSlope");
    if (ctxSlope && data.st_slope_counts) {
        new Chart(ctxSlope, {
            type: "doughnut",
            data: {
                labels: Object.keys(data.st_slope_counts),
                datasets: [{
                    data: Object.values(data.st_slope_counts),
                    backgroundColor: ["#111111", "#666666", "#E5E5E5"]
                }]
            },
            options: {
                responsive: true,
                plugins: { legend: { position: "bottom" } }
            }
        });
    }
}
