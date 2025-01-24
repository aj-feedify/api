def validator_checks(validation_conditions: list, validation_message: str) -> dict:
    for condition, message in validation_conditions:
        if condition:
            return {"ok": False, "message": message}

    return {"ok": True, "message": validation_message}


def validator_checks_dict(validation_conditions: dict, validation_message: str) -> dict:
    for condition in validation_conditions:
        if not condition["ok"]:
            return condition

    return {"ok": True, "message": validation_message}
