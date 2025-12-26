from fastapi import FastAPI
import json
from pathlib import Path
from engine.modes import ExecutionMode
from engine.decision_log import log_decision
from engine.user_view import user_summary
from engine.guards import execution_allowed

from engine.entitlement import process_entitlement
from engine.verify import verify_proof
from engine.salary_entitlement import process_salary_entitlement

# ----------------------------
# BASE DIRECTORY (FIX)
# ----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# ----------------------------
# APP INIT
# ----------------------------
app = FastAPI(
    title="Entitlement Engine",
    version="1.0"
)

# ----------------------------
# LOAD RULES
# ----------------------------
with open(BASE_DIR / "data" / "flight_rules.json") as f:
    flight_rules = json.load(f)

with open(BASE_DIR / "data" / "salary_rules.json") as f:
    salary_rules = json.load(f)

# ----------------------------
# ROUTES
# ----------------------------
@app.post("/check")
def check_flight_entitlement(flight: dict):
    return process_entitlement(flight, flight_rules)


@app.post("/salary/check")
def check_salary_entitlement(salary: dict):
    return process_salary_entitlement(salary, salary_rules)


@app.post("/verify")
def verify_entitlement(proof: dict):
    return {
        "valid": verify_proof(proof)
    }


@app.get("/ping")
def ping():
    return {"status": "alive"}
