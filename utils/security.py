import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(input_password: str, stored_has: str)->bool:
    return hash_password(input_password) == stored_has