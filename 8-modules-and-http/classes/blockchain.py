import functools
import json
# CLASS IMPORTS
from classes.block import Block
from classes.transaction import Transaction
from classes.verification import Verification
# OTHER IMPORTS
from utils import hash_block, add__line

MINING_REWARD = 10

class Blockchain:
    def __init__(self, public_key):
        genesis_block = Block(0, '', [], 100)
        self.public_key = public_key
        self.chain = [genesis_block]
        self.open_transactions = []
        # You create a set of nodes to include unique values (which will not be added
        # if are repeated)
        self.peer_nodes = set()
        self.load_data()
    
    @property
    def chain(self):
        return self.__chain[:]
    
    @property
    def open_transactions(self):
        return self.__open_transactions[:]
    
    @chain.setter
    def chain(self, val):
        self.__chain = val
    
    @open_transactions.setter
    def open_transactions(self, val):
        self.__open_transactions = val
    
    def save_data(self):
        savable_chain = [block.__dict__ for block in [Block(block_el.index, block_el.previous_hash, [tx.__dict__ for tx in block_el.transactions], block_el.proof, block_el.timestamp) for block_el in self.__chain]]
        savable_transactions = [tx.__dict__ for tx in self.__open_transactions]

        with open('blockchain.txt', mode='w') as f:
            f.write(json.dumps(savable_chain))
            f.write('\n')
            f.write(json.dumps(savable_transactions))
            f.write('\n')
            # Whey you create the file (or save it), you change the peer nodes to a list
            # as another list of information to be saved
            f.write(json.dumps(list(self.peer_nodes)))
        
    def load_data(self):
        try:
            with open('blockchain.txt', mode='r') as f:
                file_content = f.readlines()
                
                loaded_blockchain = json.loads(file_content[0])
                loaded_open_transactions = json.loads(file_content[1])
                # When you load the file, its third line now will be all the loaded peer lines
                loaded_peer_nodes = json.loads(file_content[2])
                updated_blockchain = []
                updated_transactions = []
                
                for current_block in loaded_blockchain:
                    block_transactions = [Transaction(tx['sender'], tx['recipient'], tx['signature'], tx['amount']) for tx in current_block['transactions']]
                    updated_block = Block(
                        current_block['proof'],
                        current_block['previous_hash'],
                        block_transactions,
                        current_block['proof'])
                    updated_blockchain.append(updated_block)

                for tx in loaded_open_transactions:
                    updated_transaction = Transaction(tx['sender'], tx['recipient'], tx['signature'], tx['amount'])
                    updated_transactions.append(updated_transaction)
                    
                self.chain = updated_blockchain
                self.open_transactions = updated_transactions
                # After loading them, you adjust them again as a set of values instead a list
                self.peer_nodes = set(loaded_peer_nodes)
        except (IOError, IndexError):
            # Exception logic has been handled in class initializer
            pass
        finally:
            print('Cleanup')

    def get_balance(self):
        if self.public_key == None:
            return None
        
        participant = self.public_key
        tx_sender = [[tx.amount for tx in block.transactions
                      if tx.sender == participant] for block in self.__chain]
        open_tx_sender = [tx.amount
                          for tx in self.__open_transactions if tx.sender == participant]
        tx_sender.append(open_tx_sender)
        print(tx_sender)
        amount_sent = functools.reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt)
                             if len(tx_amt) > 0 else tx_sum + 0, tx_sender, 0)
        tx_recipient = [[tx.amount for tx in block.transactions
                         if tx.recipient == participant] for block in self.__chain]
        amount_received = functools.reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt)
                                 if len(tx_amt) > 0 else tx_sum + 0, tx_recipient, 0)
        return amount_received - amount_sent

    def take_last_blockchain_value(self):
        if len(self.__chain) < 1:
            return None
        
        return self.__chain[-1]
    
    def add_transaction(self, recipient, sender, signature, amount=1.0):
        """
            Add a new transaction to the list of open transactions (which will be added to the next mined block)

            Arguments:
                :sender: The sender of the coins.
                :recipient: The recipient of the coins.
                :amount: The amount of the transaction.
        """
        if self.public_key == None:
            return False
        
        new_transaction = Transaction(sender, recipient, signature, amount)

        if Verification.verify_transaction(new_transaction, self.get_balance):
            self.__open_transactions.append(new_transaction)
            self.save_data()
            return True
        else:
            return False
        
    def get_open_transactions(self):
        return self.__open_transactions[:]

    def mine_block(self):
        if self.public_key == None:
            return None
        
        last_block = self.__chain[-1]
        hashed_block = hash_block(last_block)
        proof_of_work_value = self.proof_of_work()
        
        reward_transaction = Transaction('MINING', self.public_key, '', MINING_REWARD)

        transactions = self.__open_transactions.copy()
        transactions.append(reward_transaction)
        new_block = Block(
            len(self.__chain),
            hashed_block,
            transactions,
            proof_of_work_value
        )
        self.__chain.append(new_block)
        self.__open_transactions = []
        self.save_data()
        
        print('Block added!')
        add__line()

        return new_block
    
    def proof_of_work(self):
        last_block = self.__chain[-1]
        hash_last_block = hash_block(last_block)
        proof = 0
        while not Verification.valid_proof(self.__open_transactions, hash_last_block, proof):
            proof += 1
        return proof
    
    def add_peer_node(self, node):
        self.peer_nodes.add(node)
        self.save_data()

    def remove_peer_node(self, node):
        self.peer_nodes.discard(node)
        self.save_data()

    def get_all_nodes(self):
        return list(self.peer_nodes)