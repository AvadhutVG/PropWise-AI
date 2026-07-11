function animatePrice(targetValue, unit) {

    const result = document.getElementById("result");
    const priceUnit = document.getElementById("price-unit");

    let current = 0;

    const duration = 700;
    const frameRate = 20;

    const increment = targetValue / (duration / frameRate);

    const timer = setInterval(() => {

        current += increment;

        if (current >= targetValue) {

            current = targetValue;
            clearInterval(timer);

        }

        result.innerHTML = `₹ ${current.toFixed(2)}`;
        priceUnit.innerHTML = unit;

    }, frameRate);

}

const locationSelect = document.getElementById("location");
const form = document.getElementById("prediction-form");
const result = document.getElementById("result");


async function loadLocations() {

    const response = await fetch("/locations");
    const locations = await response.json();

    locationSelect.innerHTML = "";

    locations.forEach(location => {

        const option = document.createElement("option");

        option.value = location;
        option.textContent = location;

        locationSelect.appendChild(option);

    });
}

loadLocations();

const predictButton = document.querySelector(".predict-btn");

form.addEventListener("submit", async function (event) {

    event.preventDefault();

    // Loading State
    predictButton.disabled = true;
    predictButton.innerHTML =
        '<i class="fa-solid fa-spinner fa-spin"></i> Estimating...';

    result.innerHTML = "₹ ---";
    document.getElementById("price-unit").innerHTML =
        "Analyzing property details...";


    // Clear previous errors

    const sqftInput = document.getElementById("sqft").value.trim();
    const bhkInput = document.getElementById("bhk").value.trim();
    const bathInput = document.getElementById("bath").value.trim();
    const balconyInput = document.getElementById("balcony").value.trim();

    const sqft = Number(sqftInput);
    const bhk = Number(bhkInput);
    const bath = Number(bathInput);
    const balcony = Number(balconyInput);

    // Clear previous errors

    document.getElementById("sqft-error").textContent = "";
    document.getElementById("bhk-error").textContent = "";
    document.getElementById("bath-error").textContent = "";
    document.getElementById("balcony-error").textContent = "";

    let valid = true;

    // Empty field checks

    if (sqftInput === "") {

        document.getElementById("sqft-error").textContent =
            "Please enter Total Sqft.";

        valid = false;
    }

    if (bhkInput === "") {

        document.getElementById("bhk-error").textContent =
            "Please enter Bedrooms.";

        valid = false;
    }

    if (bathInput === "") {

        document.getElementById("bath-error").textContent =
            "Please enter Bathrooms.";

        valid = false;
    }

    if (balconyInput === "") {

        document.getElementById("balcony-error").textContent =
            "Please enter Balcony.";

        valid = false;
    }

    // Value checks

    if (sqftInput !== "" && sqft <= 0) {

        document.getElementById("sqft-error").textContent =
            "Total Sqft must be greater than 0.";

        valid = false;
    }

    if (bhkInput !== "" && bhk <= 0) {

        document.getElementById("bhk-error").textContent =
            "Bedrooms must be at least 1.";

        valid = false;
    }

    if (bathInput !== "" && bath <= 0) {

        document.getElementById("bath-error").textContent =
            "Bathrooms must be at least 1.";

        valid = false;
    }

    if (balconyInput !== "" && balcony < 0) {

        document.getElementById("balcony-error").textContent =
            "Balcony cannot be negative.";

        valid = false;
    }

    if (!valid) {

        predictButton.disabled = false;

        predictButton.innerHTML =
            "Estimate Property Value";

        result.innerHTML = "₹ ---";

        document.getElementById("price-unit").innerHTML =
            "Awaiting property details";

        return;
    }

    try {

        const response = await fetch("/predict", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({

                location: locationSelect.value,

                total_sqft: document.getElementById("sqft").value,

                bhk: document.getElementById("bhk").value,

                bath: document.getElementById("bath").value,

                balcony: document.getElementById("balcony").value

            })

        });

        if (!response.ok) {

            throw new Error("Prediction request failed.");

        }

        const prediction = await response.json();

        const value = prediction.predicted_price;

        let display = value.toFixed(2);
        let unit = "Lakhs";

        if (value >= 100) {

            display = (value / 100).toFixed(2);
            unit = "Crore";

        }

        const finalValue = parseFloat(display);

        animatePrice(finalValue, unit);

    }
    catch (error) {

        result.innerHTML = "Unavailable";

        document.getElementById("price-unit").innerHTML =
            "Unable to generate an estimate. Please check your input or try again.";

    }
    finally {

        predictButton.disabled = false;
        predictButton.innerHTML = "Estimate Property Value";

    }

});

/* ================= PIPELINE ANIMATION ================= */

const pipelineSection = document.querySelector(".insights-section");

if (pipelineSection) {

    const observer = new IntersectionObserver((entries) => {

        entries.forEach(entry => {

            if (entry.isIntersecting) {

                const steps = document.querySelectorAll(".step");
                const arrows = document.querySelectorAll(".arrow");

                steps.forEach((step, index) => {

                    setTimeout(() => {

                        step.classList.add("active");

                        if (arrows[index]) {
                            arrows[index].classList.add("active");
                        }

                    }, index * 450);

                });

                observer.disconnect();

            }

        });

    }, {

        threshold: 0.35

    });

    observer.observe(pipelineSection);

}

/* ================= MODEL COMPARISON CHART ================= */

const ctx = document.getElementById("comparisonChart");

if (ctx) {

    new Chart(ctx, {

        type: "bar",

        data: {

            labels: [

                "Linear",

                "Lasso",

                "Ridge",

                "Decision Tree"

            ],

            datasets: [{

                label: "R² Score",

                data: [

                    0.8061,

                    0.7765,

                    0.8114,

                    0.7402

                ],

                backgroundColor: [

                    "#94a3b8",

                    "#94a3b8",

                    "#2563eb",

                    "#94a3b8"

                ],

                borderRadius: 10,

                borderSkipped: false

            }]

        },

        options: {

            responsive: true,

            animation: {

                duration: 1800

            },

            plugins: {

                legend: {

                    display: false

                },

                tooltip: {

                    callbacks: {

                        label: function (context) {

                            return "R² = " + context.raw;

                        }

                    }

                }

            },

            scales: {

                y: {

                    beginAtZero: false,

                    min: 0.70,

                    max: 0.85,

                    ticks: {

                        stepSize: 0.02

                    }

                }

            }

        }

    });

}