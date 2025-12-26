def user_summary(entitlement: dict):
    if entitlement["status"] != "ENTITLED":
        return {
            "status": "NOT_ENTITLED",
            "message": "No entitlement detected"
        }

    return {
        "status": "ENTITLED",
        "amount_due": f"{entitlement['amount_due']} {entitlement['currency']}",
        "reason": entitlement["type"].replace("_", " ").title(),
        "action": "Notice generated automatically"
    }
