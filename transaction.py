

class Transaction:

    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount

    def get_transaction(self):
        return {"sender": self.sender, "recipient": self.recipient, "amount": self.amount}
