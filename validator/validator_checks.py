def validator_checks(validation_conditions: list, validation_message: str) -> dict:
    for condition, message in validation_conditions:
        if condition:
            return {"ok": False, "message": message}

    return {"ok": True, "message": validation_message}
