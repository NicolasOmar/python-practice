from collections import OrderedDict
# CLASS IMPORTS
# Have in mind that in order to correctly import a class located in a folder
# You have to call first the folder (or folders in order) and lastly, the file
# In this case, I make the import of the Class at the end to avoid verbosity
from classes.printable import Printable

# Inject Printable class to include a repetable function to reuse that logic across other classes
class Transaction(Printable):
  def __init__(self, sender, recipient, amount):
    self.sender = sender
    self.recipient = recipient
    self.amount = amount

  def to_ordered_dict(self):
    return OrderedDict([
      ('sender'), self.sender,
      ('recipient'), self.recipient,
      ('amount'), self.amount])