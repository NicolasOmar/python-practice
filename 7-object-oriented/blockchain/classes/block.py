from time import time
# CLASS IMPORTS
# Have in mind that in order to correctly import a class located in a folder
# You have to call first the folder (or folders in order) and lastly, the file
# In this case, I make the import of the Class at the end to avoid verbosity
from classes.printable import Printable

# Inject Printable class to include a repetable function to reuse that logic across other classes
class Block(Printable):
  def __init__(self, index, previous_hash, transactions, proof, timestamp=None):
    self.index = index
    self.previous_hash = previous_hash
    self.transactions = transactions
    self.proof = proof
    self.timestamp = time() if timestamp is None else timestamp