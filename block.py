import time


class Block:
    def __init__(self, index, proof, prev_hash=None):
        self.index = index
        self.timestamp = int(time.time())
        self.transactions = []
        self.proof = proof
        self.prev_hash = prev_hash

    @property
    def transactions(self):
        return self.transactions

    @transactions.setter
    def transactions(self, transactions):
        for transaction in transactions:
            self.transactions.append(transaction.get_transaction())

    @property
    def index(self):
        return self.index

    @property
    def proof(self):
        return self.proof

    @property
    def prev_hash(self):
        return self.prev_hash

