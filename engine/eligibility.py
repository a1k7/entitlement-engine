def is_eligible(flight, rules):
    delay = flight["delay_hours"]
    region = flight["region"]

    if region == "EU" and delay >= rules["EU261"]["delay_hours"]:
        return {
            "law": "EU261",
            "amount": rules["EU261"]["refund_eur"],
            "currency": "EUR"
        }

    if region == "IN" and delay >= rules["IN_DGCA"]["delay_hours"]:
        return {
            "law": "IN_DGCA",
            "amount": rules["IN_DGCA"]["refund_inr"],
            "currency": "INR"
        }

    return None
