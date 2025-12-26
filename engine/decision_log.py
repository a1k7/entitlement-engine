import json
from datetime import datetime
from pathlib import Path
import uuid

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

def log_decision(payload: dict):
    record = {
        "decision_id": f"DEC-{uuid.uuid4()}",
        "timestamp": datetime.utcnow().isoformat(),
        **payload
    }

    with open(LOG_DIR / "decisions.jsonl", "a") as f:
        f.write(json.dumps(record) + "\n")

    return record["decision_id"]
