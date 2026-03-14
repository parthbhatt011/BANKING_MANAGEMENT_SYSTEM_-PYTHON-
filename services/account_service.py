from database.queries import create_account, get_account
from utils.helpers import get_current_timestamp

def create_user_account(user_id, account_type="savings"):
    created_at = get_current_timestamp()
    create_account(user_id, account_type, created_at)
    return "Account created successfully"

def get_account_details(account_id):
    account = get_account(account_id)
    if not account:
        raise ValueError("Account not found")
    return account