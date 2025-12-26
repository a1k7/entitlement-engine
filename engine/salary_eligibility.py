from datetime import datetime
import math

def is_salary_due(salary, rules):
    due_date = datetime.fromisoformat(salary["due_date"])
    today = datetime.utcnow()

    delay_days = (today - due_date).days

    if delay_days <= rules["payment_grace_days"]:
        return None

    months_delayed = math.ceil(delay_days / 30)
    interest = (salary["amount"] * rules["monthly_interest_percent"] * months_delayed) / 100

    return {
        "delay_days": delay_days,
        "months_delayed": months_delayed,
        "base_amount": salary["amount"],
        "interest_amount": round(interest, 2),
        "total_due": round(salary["amount"] + interest, 2),
        "currency": salary["currency"],
        "employer": salary["employer"]
    }
