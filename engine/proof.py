import json
import hashlib
from datetime import datetime

def generate_proof(flight, entitlement):
    payload = {
        "timestamp": datetime.utcnow().isoformat(),
        "flight": flight,
        "entitlement": entitlement
    }

    proof_hash = hashlib.sha256(
        json.dumps(payload, sort_keys=True).encode()
    ).hexdigest()

    payload["proof_hash"] = proof_hash
    return payload
