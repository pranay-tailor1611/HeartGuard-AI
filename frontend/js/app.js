/**
 * CardioPulse AI - Global Application Controller (v2.5.0)
 */

document.addEventListener("DOMContentLoaded", function () {
    // Active Nav Link Highlighting
    const currentPath = window.location.pathname.split("/").pop() || "index.html";
    document.querySelectorAll(".nav-link").forEach(link => {
        const href = link.getAttribute("href");
        if (href === currentPath || (currentPath === "" && href === "index.html")) {
            link.classList.add("active");
        } else {
            link.classList.remove("active");
        }
    });

    // Check Backend Status
    checkBackendHealth();
});

async function checkBackendHealth() {
    const statusBadge = document.getElementById("systemStatusBadge");
    if (!statusBadge) return;

    try {
        const response = await fetch("/api/health");
        if (response.ok) {
            const data = await response.json();
            statusBadge.innerHTML = `🟢 <b>System Status:</b> Operational (v${data.version})`;
            statusBadge.className = "badge-success-minimal";
        } else {
            statusBadge.innerHTML = "🔴 <b>Backend Status:</b> Offline";
            statusBadge.className = "badge-danger-minimal";
        }
    } catch (error) {
        console.warn("Backend health check failed:", error);
        statusBadge.innerHTML = "🟡 <b>API:</b> Standalone / Connecting...";
    }
}
