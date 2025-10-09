# Types of iterables
  # A [list] is mutable, ordered collection of items that allows duplicates and uses mostly one type of data
    # [1, 2, 3, 4, 5]
  # A [set] is also mutable, not ordered, no duplicates, and also uses mostly one type of data
    # {1, 2, 3, 4, 5}
  # A [tuple] is immutable, ordered collection of items that allows duplicates and can use multiple types of data
    # (1, 2, 3, "honey", true)
  # A [dictionary] is mutable, not ordered, no duplicates, and uses key-value pairs. Is similar to a JavaScript object
    # {"name": "Alice", "age": 30, "city": "New York"}

# Other thigs to have in mind when you are using iterables
    # If you copy a list from another one and change any of its values inside, it will change the value in both lists because they are pointing to the same memory address
        # That is because is copying the reference of the list, not the actual values
        # To avoid that, you can use the LIST_NAME[:] function to create a new list with the same values
            # copy_list = original_list[:]

MINING_REWARD = 10
genesis_block = {
    'previous_hash': '',
    'index': 0,
    'transactions': []
}
my_blockchain = [genesis_block]
open_transactions = []
waiting_for_input = True
owner = 'Nicolas'
# A set can be created without any previous values or with a iterable like a list
participants = set([owner])

def add__line():
    print('------------------------------')

def generate_options_menu():
    add__line()
    print('Please choose an option:')
    print('1: Add a new transaction')
    print('2: Mine a new block')
    print('3: Output all blockchain blocks')
    print('4: Output all participants')
    print('h: Manipulate blockchain')
    print('q: Quit')
    add__line()

def get_user_input():
    user_input = input('Please enter your selection: ')
    add__line()
    return user_input

def hash_block(block):
    """ Hash a block using its strucutre as base """
    # In order to create a new hash for the new block, we will use a list comprehension
    # List comprehension creates a new list based on an existing iterable, applying an expression to each item in the iterable, in this case, concatinating each value of the dictionary into a single string
        # hashed_block = str([last_block[key] for key in last_block])
    # You can use an if for this comprehension to filter items from the original iterable
        # hashed_block = str([last_block[key] for key in last_block if key != 'transactions'])
    return str(block[key] for key in block)

def mine_block():
    last_block = my_blockchain[-1]
    hashed_block = hash_block(last_block)

    reward_transaction = {
        'sender': 'MINING',
        'recipient': owner,
        'amount': MINING_REWARD
    }

    block = {
        'previous_hash': hashed_block,
        'index': len(my_blockchain),
        'transactions': [open_transactions, reward_transaction]
    }
    
    my_blockchain.append(block)
    # Here if you try to reset the open_transactions list, it will create a new local variable instead of modifying the global one
        # open_transactions = []
    print('Block added!')
    add__line()
    return True

def get_transaction_value():
    """ Returns the input of the user (a new transaction amount and its recipient) as a tuple """
    tx_recipient_input = input('Please enter the recipient of the transaction: ')
    tx_amount_input = float(input('Please enter your transaction input: '))
    add__line()

    # When you return a tuple, it does not need to be enclosed in parentheses (is optional i guess)
    return tx_recipient_input, tx_amount_input

def take_last_blockchain_value():
    if len(my_blockchain) < 1:
        return None
    
    return my_blockchain[-1]

def verify_transaction(transaction):
    sender_balance = get_balance(transaction['sender'])
    
    if sender_balance >= transaction['amount']:
        return True
    return False

def add_transaction(sender, recipient, amount=1):
    """
        Add a new transaction to the list of open transactions (which will be added to the next mined block)

        Arguments:
            :sender: The sender of the coins.
            :recipient: The recipient of the coins.
            :amount: The amount of the transaction.
    """

    new_transaction = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    }

    if verify_transaction(new_transaction):
        open_transactions.append(new_transaction)
        # When you add a new element to a set, if the element already exists, it will not be added again
        participants.add(sender)
        participants.add(recipient)
    else:
        print('Transaction failed! Not enough balance!')
    add__line()

def return_all_blocks():
    print('---Outputting all blocks---')
    
    for block in my_blockchain:
        print('Outputting block: ' + str(block))
    add__line()
    
def get_balance(participant):
    final_balance = 0
    sent_transactions = [[tx['amount'] for tx in block['transactions'] if tx['sender'] == participant] for block in my_blockchain]
    recieved_transactions = [[tx['amount'] for tx in block['transactions'] if tx['recipient'] == participant] for block in my_blockchain]
    open_sent_transactions = [tx['amount'] for tx in open_transactions if tx['sender'] == participant]

    sent_transactions.append(open_sent_transactions)
    
    for sent_amount in sent_transactions:
        if len(sent_amount) > 0:
            final_balance -= sent_amount

    for recieved_amount in recieved_transactions:
        if len(recieved_amount) > 0:
            final_balance += recieved_amount
    
    return final_balance

def verify_chain():
    """ The function helps to verify the integrity of the blockchain by checking if each block's previous hash matches the hash of the previous block. """
    # Enumerate is a function that will convert your list in a tuple with the index and the value of each item in the list
    # By creating a tuple, we you can unpack its values into different variables
    for (index, block) in enumerate(my_blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(my_blockchain[index - 1]):
            return False
    return True
    
while waiting_for_input:
    generate_options_menu()
    
    user_choice = get_user_input()
    
    if user_choice == '1':
        tx_input_data = get_transaction_value()
        # A way to unpack values from a tuple into different variables
        recipient, amount = tx_input_data
        add_transaction(owner, recipient, amount)
    elif user_choice == '2':
        if mine_block():
            # Here you can reset the open_transactions list after mining a block because is referring to the global variable
            open_transactions = []
    elif user_choice == '3':
        return_all_blocks()
    elif user_choice == '4':
        print(participants)
    elif user_choice == 'q':
        waiting_for_input = False
    elif user_choice == 'h':
        if len(my_blockchain) >= 1:
            my_blockchain[0] = [2.0]
    else:
        print('Invalid input, please choose a valid option')
    if not verify_chain():
        print('Invalid blockchain!')
        waiting_for_input = False
    print('Balance: ' + str(get_balance(owner)))
else:
    print('User left!')

add__line()
print('Done!')
