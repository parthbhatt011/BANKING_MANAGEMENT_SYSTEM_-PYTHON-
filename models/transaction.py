class Transaction:
        def __init__(self,transaction_id,account_id,type,amount,timestamp,description):
            self.transaction_id = transaction_id
            self.account_id = account_id
            self.type = type
            self.amount = amount
            self.timestamp = timestamp
            self.description = description

        def __repr__(self):
            return(
                f"Transaction(id={self.transaction_id}, "
                f"account={self.account_id}, "
                f"type={self.type}, "
                f"amount={self.amount})"
            )

def transaction_history():
    pass