from flask import url_for
import re


def validate_username(username):
    if not 4 <= len(username) <= 20:
        return f"Username must be between 4 and 20 characters. <a href='{ url_for('auth.sign_up') }'>Try again.</a>"
    if not re.match(r"^[a-zA-Z0-9_-]+$", username):
        return f"Only Latin letters, numbers, _ and - are allowed. <a href='{ url_for('auth.sign_up') }'>Try again.</a>"
    return None

def validate_password(password):
    if not 6 <= len(password) <= 40:
        return f"Password must be between 6 and 40 characters. <a href='{ url_for('auth.sign_up') }'>Try again.</a>"
    return None
