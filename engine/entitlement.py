from engine.eligibility import is_eligible
from engine.proof import generate_proof

def process_entitlement(flight, rules):
    eligibility = is_eligible(flight, rules)

    if not eligibility:
        return {"status": "NOT_ELIGIBLE"}

    proof = generate_proof(flight, eligibility)

    return {
        "status": "ENTITLED",
        "law": eligibility["law"],
        "amount": eligibility["amount"],
        "currency": eligibility["currency"],
        "proof": proof
    }
