from database.queries import create_user, get_user_by_email, create_account
from utils.security import hash_password, verify_password
from utils.helpers import (
    generate_otp,
    send_otp,
    verify_otp,
    get_current_timestamp,
    generate_account_number,
    generate_userid
)
from database.db_connection import initialize_db


def register_user(name, email, password, role="customer"):
    initialize_db()
    existing_user = get_user_by_email(email)
    if existing_user:
        raise ValueError("Email already registered")
    otp, totp = generate_otp()
    send_otp(email, otp)
    for _ in range(3):
        if verify_otp(totp):
            break
    else:
        raise ValueError("OTP verification failed")
    password_hash = hash_password(password)
    created_at = get_current_timestamp()
    account = generate_account_number()
    user_id = generate_userid()
    create_user(name, email, password_hash, role, created_at)
    create_account(email, user_id, account, created_at)
    return "User registered successfully"



def login_user(email, password):
    user = get_user_by_email(email)
    if not user:
        raise ValueError("User not found")
    if not verify_password(password, user["password_hash"]):
        raise ValueError("Invalid password")
    return user