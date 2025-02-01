from .feed import valid_uid
from .validator_checks import validator_checks, validator_checks_dict


def valid_response_text(text: str):
    validation_conditions = [
        (len(text) < 1, "Text must be at least 1 character long"),
    ]

    return validator_checks(validation_conditions, "Text is valid")


def valid_create_response(feed_uid: str, text: str):
    validation_conditions = [
        valid_uid(feed_uid),
        valid_response_text(text),
    ]

    return validator_checks_dict(validation_conditions, "Response is valid")
