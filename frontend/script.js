const API_BASE = "http://127.0.0.1:8000"; 
// replace with https://api.yourdomain.com after deployment

function showLoading(message) {
  const resultCard = document.getElementById("resultCard");
  resultCard.classList.remove("hidden");

  document.getElementById("resultTitle").innerText = "Evaluating entitlement…";
  document.getElementById("resultMessage").innerText = message;
  document.getElementById("checkedTime").innerText = "";
  document.getElementById("decisionId").innerText = "";
  document.getElementById("details").classList.add("hidden");
}

function showResult(data, entitledMessage, notEntitledMessage) {
  const now = new Date().toLocaleDateString("en-GB", {
    day: "2-digit",
    month: "short",
    year: "numeric"
  });

  document.getElementById("checkedTime").innerText =
    `Checked on: ${now}`;
  document.getElementById("decisionId").innerText =
    `Decision reference: ${data.decision_id}`;

  if (data.summary?.status === "ENTITLED") {
    document.getElementById("resultTitle").innerText = "You are entitled";
    document.getElementById("resultMessage").innerText = entitledMessage;
  } else {
    document.getElementById("resultTitle").innerText = "No entitlement detected";
    document.getElementById("resultMessage").innerText = notEntitledMessage;
  }

  document.getElementById("details").innerText =
    JSON.stringify(data.details, null, 2);
}

/* ================= SALARY ================= */

async function checkSalaryEntitlement() {
  showLoading(
    "Decision is being calculated based on today’s date and salary rules."
  );

  try {
    const response = await fetch(
      `${API_BASE}/salary/check?mode=${document.getElementById("mode").value}`,
      {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          employee_id: "USER",
          employer: document.getElementById("employer").value,
          amount: Number(document.getElementById("amount").value),
          currency: "INR",
          due_date: document.getElementById("date").value
        })
      }
    );

    const data = await response.json();

    showResult(
      data,
      `${data.summary.amount_due} — Salary payment delayed`,
      "Based on the information provided, no action is required today."
    );

  } catch {
    document.getElementById("resultTitle").innerText =
      "Unable to evaluate entitlement";
    document.getElementById("resultMessage").innerText =
      "Please try again or check your connection.";
  }
}

/* ================= FLIGHT ================= */

async function checkFlightEntitlement() {
  showLoading(
    "Decision is being calculated based on flight delay compensation rules."
  );

  try {
    const response = await fetch(
      `${API_BASE}/flight/check?mode=${document.getElementById("flightMode").value}`,
      {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          flight_number: document.getElementById("flightNumber").value,
          delay_hours: Number(document.getElementById("delayHours").value),
          region: document.getElementById("region").value,
          date: document.getElementById("flightDate").value
        })
      }
    );

    const data = await response.json();

    showResult(
      data,
      `${data.summary.amount_due} — Flight delay compensation`,
      "Based on the flight details, no compensation applies."
    );

  } catch {
    document.getElementById("resultTitle").innerText =
      "Unable to evaluate entitlement";
    document.getElementById("resultMessage").innerText =
      "Please try again or check your connection.";
  }
}

/* ================= DETAILS TOGGLE ================= */

function toggleDetails() {
  document.getElementById("details").classList.toggle("hidden");
}
