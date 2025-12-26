from datetime import datetime

def generate_salary_notice(salary: dict, entitlement: dict, proof_hash: str):
    return {
        "document_type": "SALARY_PAYMENT_NOTICE",
        "issued_on": datetime.utcnow().date().isoformat(),
        "employer": salary["employer"],
        "employee_id": salary["employee_id"],
        "amount_due": entitlement["total_due"],
        "currency": entitlement["currency"],
        "delay_days": entitlement["delay_days"],
        "reference_proof": proof_hash,
        "notice_text": (
            f"This notice is issued for non-payment of salary due on "
            f"{salary['due_date']}. As of today, the employer owes "
            f"{entitlement['total_due']} {entitlement['currency']} "
            f"including statutory interest. Proof reference: {proof_hash}."
        )
    }
