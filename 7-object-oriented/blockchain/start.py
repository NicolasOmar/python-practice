from utils import add__line
from uuid import uuid4
# CLASS IMPORTS
# Have in mind that in order to correctly import a class located in a folder
# You have to call first the folder (or folders in order) and lastly, the file
# In this case, I make the import of the Class at the end to avoid verbosity
from classes.blockchain import Blockchain
from classes.verification import Verification

class Node:
  def __init__(self):
     # ANY UUID is not JSON parseable, so we have to stringify it
     self.id = str(uuid4())
     self.blockchain = Blockchain(self.id)
     print(self.blockchain.chain)

  def generate_options_menu(self):
    add__line()
    print('Please choose an option:')
    print('1: Add a new transaction')
    print('2: Mine a new block')
    print('3: Output all blockchain blocks')
    print('h: Manipulate blockchain')
    print('q: Quit')
    add__line()

  def get_user_input(self):
    user_input = input('Please enter your selection: ')
    add__line()
    return user_input

  def get_transaction_value(self):
    """ Returns the input of the user (a new transaction amount and its recipient) as a tuple """
    tx_recipient_input = input('Please enter the recipient of the transaction: ')
    tx_amount_input = float(input('Please enter your transaction input: '))
    add__line()

    return tx_recipient_input, tx_amount_input
  
  def return_all_blocks(self):
    print('---Outputting all blocks---')
    
    for block in self.blockchain.chain:
        print(f'Outputting block: {block}')
    add__line()

  def listen_for_input(self):
    waiting_for_input = True

    while waiting_for_input:
        self.generate_options_menu()
        
        user_choice = self.get_user_input()
        
        if user_choice == '1':
            tx_input_data = self.get_transaction_value()
            recipient, amount = tx_input_data
            self.blockchain.add_transaction(self.id, recipient, amount)
        elif user_choice == '2':
            self.blockchain.mine_block()
        elif user_choice == '3':
            self.return_all_blocks()
        elif user_choice == '4':
          # Using class and static methods, those can be called without need to instanciate it
          if Verification.verify_transactions(self.blockchain.open_transactions):
            print('Trasnsaction VALID')
          else:
            print('Trasnsaction INVALID')
        elif user_choice == 'q':
            waiting_for_input = False
        else:
            print('Invalid input, please choose a valid option')
            # Using class and static methods, those can be called without need to instanciate it
        if not Verification.verify_chain(self.blockchain.chain):
            print('Invalid blockchain!')
            waiting_for_input = False
        print(f"Balance of {self.id}: {self.blockchain.get_balance(self.id)}")
    else:
        print('User left!')

    add__line()
    print('Done!')

node = Node()
node.listen_for_input()