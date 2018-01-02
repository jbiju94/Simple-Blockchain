from block import Block
from transaction import Transaction
import json
import hashlib


class BlockChain:

    def __init__(self):
        self.chain = []
        self.current_transactions = []

        # Create the genesis block
        self.new_block(previous_hash=1, proof=100)

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

        # We must make sure that the Dictionary is Ordered, or we'll have inconsistent hashes
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
