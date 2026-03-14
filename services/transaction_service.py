from database.queries import update_balance, create_transaction, get_account
from utils.helpers import get_current_timestamp

def deposit_money(account_id, amount):
    if amount <= 0:
        raise ValueError("Invalid deposit amount")
    account = get_account(account_id)
    if not account:
        raise ValueError("Account not found")
    update_balance(account_id, amount)
    timestamp = get_current_timestamp()
    create_transaction(
        account_id,
        "deposit",
        amount,
        timestamp,
        "Deposit transaction"
    )
    return "Deposit successful"

def withdraw_money(account_id, amount):
    if amount <= 0:
        raise ValueError("Invalid withdrawal amount")
    account = get_account(account_id)
    if not account:
        raise ValueError("Account not found")
    if account["balance"] < amount:
        raise ValueError("Insufficient balance")
    update_balance(account_id, -amount)
    timestamp = get_current_timestamp()
    create_transaction(
        account_id,
        "withdraw",
        amount,
        timestamp,
        "Withdrawal transaction"
    )
    return "Withdrawal successful"