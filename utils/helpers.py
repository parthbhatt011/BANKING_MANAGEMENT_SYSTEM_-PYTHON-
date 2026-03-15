import random
from datetime import datetime

def generate_userid():
    return random.randint(10000000, 99999999)

def generate_account_number():
    return random.randint(10000000, 99999999)

def get_current_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def generate_transaction_description(transaction_type, amount):
    return f"{transaction_type.capitalize()} of {amount}"