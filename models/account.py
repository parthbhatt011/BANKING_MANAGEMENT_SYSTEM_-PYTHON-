class Account:

    def __init__(self, account_id, user_id, balance, account_type, created_at):
        self.account_id = account_id
        self.user_id = user_id
        self.balance = balance
        self.account_type = account_type
        self.created_at = created_at
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount
    def __repr__(self):
        return f"Account(id={self.account_id}, user={self.user_id}, balance={self.balance})"