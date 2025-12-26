def notify(user, entitlement):
    print(
        f"You are entitled to {entitlement['amount']} {entitlement['currency']} "
        f"under {entitlement['law']}. No action needed."
    )
