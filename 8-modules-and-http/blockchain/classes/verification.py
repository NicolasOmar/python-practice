# OTHER IMPORTS
from utils import hash_block, hash_string_256

class Verification:
  @classmethod
  def verify_chain(cls, blockchain):
    """ The function helps to verify the integrity of the blockchain by checking if each block's previous hash matches the hash of the previous block. """
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block.previous_hash != hash_block(blockchain[index - 1]):
            return False
        if not cls.valid_proof(block.transactions[:-1], block.previous_hash, block.proof):
            print('Proof of work is invalid')
            return False
    return True
  
  @staticmethod
  def verify_transaction(transaction, get_balance):
    sender_balance = get_balance(transaction.sender)
    
    if sender_balance >= transaction.amount:
        return True
    return False
  
  @classmethod
  def verify_transactions(self, open_transactions):
    """ The function verifies all open transactions to ensure they are valid. """
    return all([tx for tx in open_transactions if not self.verify_transaction(tx)])
  
  @staticmethod
  def valid_proof(transactions, last_hash, proof):
    guess = (str([tx.to_ordered_dict() for tx in transactions]) + str(last_hash) + str(proof)).encode()
    guess_hash = hash_string_256(guess)
    
    return guess_hash[0:2] == '00'