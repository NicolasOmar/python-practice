from time import time
from printable import Printable

# Inject Printable class to include a repetable function to reuse that logic across other classes
class Block(Printable):
  def __init__(self, index, previous_hash, transactions, proof, timestamp=None):
    self.index = index
    self.previous_hash = previous_hash
    self.transactions = transactions
    self.proof = proof
    self.timestamp = time() if timestamp is None else timestamp