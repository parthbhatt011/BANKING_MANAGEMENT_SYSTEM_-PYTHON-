from database.queries import create_user, get_user_by_email
from utils.security import hash_password, verify_password
from utils.helpers import get_current_timestamp


def register_user(name, email, password, role="customer"):
    existing_user = get_user_by_email(email)
    if existing_user:
        raise ValueError("Email already registered")
    password_hash = hash_password(password)
    created_at = get_current_timestamp()
    create_user(name, email, password_hash, role, created_at)
    return "User registered successfully"

def login_user(email, password):
    user = get_user_by_email(email)
    if not user:
        raise ValueError("User not found")
    if not verify_password(password, user["password_hash"]):
        raise ValueError("Invalid password")
    return user