# OTHER IMPORTS
from utils import hash_block, hash_string_256

# On this particular class, we will implement a different type of class itself
# This type of class will use static and class methods
# We will do this change to avoid instance creations on the program
  # It only need to class methods and never access its attributes
  # None of this cases need to access to class attributes
    # therefore there is no [__init__] method nor self reference (because does not access the class attributes, again)
# The way to implement this type of methods in the class is through a decorator (starts with an @) that indicates the type of method
class Verification:
  # classmethod can access inside class references (such as other methods)
  # It has a reference to class context (called [cls] as convention, but you can rename it)
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

  # staticmethod is an isolated method that only works with the provided data
  # It has NO reference to the class, so its arguments are referencing what the calling will require
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
    # A good way to avoid to include that much code as the OrderedDict creation is to assign that logic inside the component
    # Doing it so will make callable for each object in a one-lined for floop
    guess = (str([tx.to_ordered_dict() for tx in transactions]) + str(last_hash) + str(proof)).encode()
    guess_hash = hash_string_256(guess)
    
    return guess_hash[0:2] == '00'