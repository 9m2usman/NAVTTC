def is_positive(value):
    return value > 0


def is_non_negative(value):
    return value >= 0


def is_valid_email(email):
    return "@" in email and "." in email.split("@")[-1]


def is_valid_phone(phone):
    cleaned = phone.replace(" ", "").replace("-", "").replace("+", "")

    return cleaned.isdigit() and len(cleaned) >= 10


def is_valid_percentage(value):
    return 0 <= value <= 100


def is_not_empty(value):
    return bool(value and value.strip())


def is_valid_status(status):
    return status.lower() in ("active", "inactive")