from block import Block
from transaction import Transaction
from proof_of_work import proof_of_work as p_of_w
import json
import hashlib


class Blockchain:

    def __init__(self):
        self.chain = []
        self.current_transactions = []

        # Genesis block creation
        self.new_block(prev_hash=1, proof=100)

    def new_block(self, proof, prev_hash=None):
        index = len(self.chain) + 1
        block = Block(index, proof, prev_hash)

        # Reset the current list of transactions
        self.current_transactions = []

        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        """
               Creates a new transaction to go into the next mined Block
               :param sender: <str> Address of the Sender
               :param recipient: <str> Address of the Recipient
               :param amount: <int> Amount
               :return: <int> The index of the Block that will hold this transaction
        """
        transaction = Transaction(sender, recipient, amount)
        self.current_transactions.append(transaction)

        return self.last_block['index'] + 1

    @staticmethod
    def proof_of_work(last_proof):
        return p_of_w(last_proof)

    @property
    def last_block(self):
        return self.chain[-1]

    @staticmethod
    def hash(block):
        """
            Creates a SHA-256 hash of a Block
            :param block: <dict> Block
            :return: <str>
        """

        # To avoid inconsistent hashes, make sure that the Dictionary is Ordered
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

