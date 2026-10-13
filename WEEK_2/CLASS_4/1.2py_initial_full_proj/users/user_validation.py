def validate_username(username):
    return bool(username.strip())


def validate_password(password):
    return len(password) >= 6


def validate_role(role):
    return role.lower() in ["admin", "employee"]