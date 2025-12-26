from engine.salary_eligibility import is_salary_due
from engine.proof import generate_proof
from engine.notice import generate_salary_notice


def process_salary_entitlement(salary: dict, rules: dict):
    """
    Determines salary non-payment entitlement,
    calculates interest, generates proof and notice.
    """

    eligibility = is_salary_due(salary, rules)

    if not eligibility:
        return {"status": "NOT_ENTITLED"}

    proof = generate_proof(salary, eligibility)

    notice = generate_salary_notice(
        salary=salary,
        entitlement=eligibility,
        proof_hash=proof["proof_hash"]
    )

    return {
        "status": "ENTITLED",
        "type": "SALARY_NON_PAYMENT",
        "amount_due": eligibility["total_due"],
        "currency": eligibility["currency"],
        "interest": eligibility["interest_amount"],
        "notice": notice,
        "proof": proof
    }
