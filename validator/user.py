from .validator_checks import validator_checks, validator_checks_dict


def valid_id(id: int) -> dict:
    validation_conditions = [
        (not isinstance(id, int), "ID must be a number"),
        (id < 1, "ID must be greater than 0"),
    ]

    return validator_checks(validation_conditions, "ID is valid")


def valid_name(name: str) -> dict:
    validation_conditions = [
        (len(name) < 3, "Name must be at least 3 characters long"),
    ]

    return validator_checks(validation_conditions, "Name is valid")


def valid_username(username: str) -> dict:
    validation_conditions = [
        (len(username) < 3, "Username must be at least 3 characters long"),
        (len(username) > 20, "Username must not exceed 20 characters"),
        (username[0].isdigit(), "Username cannot start with a number"),
        (not username.isalnum(), "Username must only contain letters and numbers"),
    ]

    return validator_checks(validation_conditions, "Username is valid")


def valid_password(password: str) -> dict:
    validation_conditions = [
        (len(password) < 8, "Password must be at least 8 characters long")
    ]

    return validator_checks(validation_conditions, "Password is valid")


def valid_user(
    username: str = "", password: str = "", name: str = "", id: int = 0
) -> dict:
    validation_conditions = [
        valid_username(username) if username else {"ok": True},
        valid_password(password) if password else {"ok": True},
        valid_name(name) if name else {"ok": True},
        valid_id(id) if id else {"ok": True},
    ]
    return validator_checks_dict(validation_conditions, "User is valid")
