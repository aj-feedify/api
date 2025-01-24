from .validator_checks import validator_checks, validator_checks_dict
from .user import valid_id as valid_user_id


def valid_title(text: str) -> dict:
    validation_conditions = [
        (len(text) < 5, "Title must be at least 5 characters long"),
    ]

    return validator_checks(validation_conditions, "Title is valid")


def valid_text(text: str) -> dict:
    validation_conditions = [
        (len(text) < 10, "Text must be at least 10 characters long"),
    ]

    return validator_checks(validation_conditions, "Text is valid")


def valid_id(id: int) -> dict:
    validation_conditions = [
        (not isinstance(id, int), "ID must be a number"),
        (id < 1, "ID must be greater than 0"),
    ]

    return validator_checks(validation_conditions, "ID is valid")


def valid_get_input(user_id: int, feed_id: int) -> dict:
    validation_conditions = [valid_user_id(user_id), valid_id(feed_id)]
    return validator_checks_dict(validation_conditions, "Get input is valid")


def valid_update_input(title: str, text: str, user_id: int, feed_id: int) -> dict:
    validation_conditions = [
        valid_title(title),
        valid_text(text),
        valid_user_id(user_id),
        valid_id(feed_id),
    ]
    return validator_checks_dict(validation_conditions, "Update input is valid")


def valid_feed(title: str = "", text: str = "", id: int = 0) -> dict:
    validation_conditions = [
        valid_title(title) if title else {"ok": True},
        valid_text(text) if text else {"ok": True},
        valid_user_id(id) if id else {"ok": True},
    ]
    return validator_checks_dict(validation_conditions, "Feed is valid")
