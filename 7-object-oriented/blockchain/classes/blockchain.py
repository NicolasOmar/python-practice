import functools
import json
# CLASS IMPORTS
# Have in mind that in order to correctly import a class located in a folder
# You have to call first the folder (or folders in order) and lastly, the file
# In this case, I make the import of the Class at the end to avoid verbosity
from classes.block import Block
from classes.transaction import Transaction
from classes.verification import Verification
# OTHER IMPORTS
from utils import hash_block, add__line

MINING_REWARD = 10

class Blockchain:
    def __init__(self, node_hosting_id):
        genesis_block = Block(0, '', [], 100)
        self.verifier = Verification()
        self.chain = [genesis_block]
        self.open_transactions = []
        self.hosting_id = node_hosting_id
        # When you create an instance of this class, it will start the load data process
        self.load_data()
        
    def load_data(self):
        try:
            with open('blockchain.txt', mode='r') as f:
                file_content = f.readlines()
                
                blockchain = json.loads(file_content[0])
                updated_blockchain = []
                updated_transactions = []
                
                for current_block in blockchain:
                    block_transactions = [Transaction(tx['sender'], tx['recipient'], tx['amount']) for tx in current_block.transactions]
                    updated_block = Block(
                        current_block.proof,
                        current_block.previous_hash,
                        block_transactions,
                        current_block.proof)
                    updated_blockchain.append(updated_block)

                for tx in current_block.transactions:
                    updated_transaction = Transaction(tx['sender'], tx['recipient'], tx['amount'])
                    updated_transactions.append(updated_transaction)
                    
                self.chain = updated_blockchain
                self.open_transactions = updated_transactions
        except (IOError, IndexError):
            # Exception logic has been handled in class initializer
            pass
        finally:
            print('Cleanup')

    def save_data(self):
        # To create the chain in a json-accepted format, we have to parse the list as a dictionary list
        savable_chain = [block.__dict__ for block in [Block(block_el.index, block_el.previous_hash, [tx.__dict__ for tx in block_el.transactions], block_el.proof, block_el.timestamp) for block_el in self.chain]]
        savable_transactions = [tx.__dict__ for tx in self.open_transactions]

        with open('blockchain.txt', mode='w') as f:
            f.write(json.dumps(savable_chain))
            f.write('\n')
            f.write(json.dumps(savable_transactions))

    def get_balance(self, participant):
        sent_transactions = [[tx.amount for tx in block.transactions if tx.sender == participant] for block in self.chain]
        recieved_transactions = [[tx.amount for tx in block.transactions if tx.recipient == participant] for block in self.chain]
        open_sent_transactions = [tx.amount for tx in self.open_transactions if tx.sender == participant]

        sent_transactions.append(open_sent_transactions)
        sent_amounts = functools.reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt), sent_transactions, 0)
        recieved_amounts = functools.reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt), recieved_transactions, 0)

        return recieved_amounts - sent_amounts

    def take_last_blockchain_value(self):
        if len(self.chain) < 1:
            return None
        
        return self.chain[-1]
    
    def add_transaction(self, sender, recipient, amount=1):
        """
            Add a new transaction to the list of open transactions (which will be added to the next mined block)

            Arguments:
                :sender: The sender of the coins.
                :recipient: The recipient of the coins.
                :amount: The amount of the transaction.
        """
        new_transaction = Transaction(sender, recipient, amount)

        if self.verifier.verify_transaction(new_transaction, self.get_balance):
            self.open_transactions.append(new_transaction)
            self.save_data()
        else:
            print('Transaction failed! Not enough balance!')
        add__line()

    def mine_block(self):
        last_block = self.chain[-1]
        hashed_block = hash_block(last_block)
        proof_of_work_value = self.proof_of_work()
        
        reward_transaction = Transaction('MINING', self.hosting_id, MINING_REWARD)

        transactions = self.open_transactions.copy()
        transactions.append(reward_transaction)
        new_block = Block(
            len(self.chain),
            hashed_block,
            transactions,
            proof_of_work_value
        )
        self.chain.append(new_block)
        self.open_transactions = []
        self.save_data()
        print('Block added!')
        add__line()
        return True
    
    def proof_of_work(self):
        last_block = self.chain[-1]
        hash_last_block = hash_block(last_block)
        proof = 0
        while not self.verifier.valid_proof(self.open_transactions, hash_last_block, proof):
            proof += 1
        return proof