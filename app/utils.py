import re


def validate_username(username):
    if not 4 <= len(username) <= 20:
        return True
    if not re.match(r"^[a-zA-Z0-9_-]+$", username):
        return True
    return None

def validate_password(password):
    if not 6 <= len(password) <= 40:
        return True
    return None
