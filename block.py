import time


class Block:
    def __init__(self, index, proof, prev_hash=None):
        self.index = index
        self.timestamp = int(time.time())
        self.transaction = []
        self.proof = proof
        self.prev_hash = prev_hash

    def add_transaction(self, transaction):
        self.transaction.append(transaction)

    """Getters"""

    @property
    def transactions(self):
        return self.transaction

    @property
    def index(self):
        return self.index

    @property
    def proof(self):
        return self.proof

    @property
    def prev_hash(self):
        return self.prev_hash

