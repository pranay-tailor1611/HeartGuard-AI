/**
 * CardioPulse AI - FAQ Search Filter Controller
 */

document.addEventListener("DOMContentLoaded", function () {
    const searchInput = document.getElementById("faqSearchInput");
    if (!searchInput) return;

    searchInput.addEventListener("input", function (e) {
        const query = e.target.value.toLowerCase().trim();
        const accordionItems = document.querySelectorAll("#faqAccordion .accordion-item");

        accordionItems.forEach(item => {
            const questionText = item.querySelector(".accordion-button").innerText.toLowerCase();
            const answerText = item.querySelector(".accordion-body").innerText.toLowerCase();

            if (questionText.includes(query) || answerText.includes(query)) {
                item.style.display = "";
            } else {
                item.style.display = "none";
            }
        });
    });
});
