# Types of iterables
  # A [list] is mutable, ordered collection of items that allows duplicates and uses mostly one type of data
    # [1, 2, 3, 4, 5]
  # A [set] is also mutable, not ordered, no duplicates, and also uses mostly one type of data
    # {1, 2, 3, 4, 5}
  # A [tuple] is immutable, ordered collection of items that allows duplicates and can use multiple types of data
    # (1, 2, 3, "honey", true)
  # A [dictionary] is mutable, not ordered, no duplicates, and uses key-value pairs. Is similar to a JavaScript object
    # {"name": "Alice", "age": 30, "city": "New York"}

genesis_block = {
    'previous_hash': '',
    'index': 0,
    'transactions': []
}
my_blockchain = [genesis_block]
open_transactions = []
waiting_for_input = True
owner = 'Nicolas'

def mine_block():
    last_block = my_blockchain[-1]
    # In order to create a new hash for the new block, we will use a list comprehension
    # List comprehension creates a new list based on an existing iterable, applying an expression to each item in the iterable, in this case, concatinating each value of the dictionary into a single string
        # hashed_block = str([last_block[key] for key in last_block])
    # You can use an if for this comprehension to filter items from the original iterable
    hashed_block = str([last_block[key] for key in last_block if key != 'transactions'])

    block = {
        'previous_hash': hashed_block,
        'index': len(my_blockchain),
        'transactions': open_transactions
    }
    my_blockchain.append(block)
    add__line()
    print('Block added!')
    pass

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
    open_transactions.append(new_transaction)
    print(open_transactions)
    add__line()

def get_user_input():
    user_input = input('Please enter your transaction value: ')
    add__line()
    return user_input

def return_all_blocks():
    print('---Outputting all blocks---')
    
    for block in my_blockchain:
        print('Outputting block: ' + str(block))
    add__line()

def verify_chain_by_index():
    """ The same function as verify_chain but using the index of the blocks instead of the block itself """
    is_valid_chain = True

    for block_index in range(len(my_blockchain)):
        if block_index == 0:
            block_index += 1
            continue
        elif my_blockchain[block_index][0] != my_blockchain[block_index - 1]:
            is_valid_chain = False
            break

        block_index += 1
    return is_valid_chain

def verify_chain():
    """ The function helps to verify the integrity of the blockchain by checking if each block's previous hash matches the hash of the previous block. """
    block_index = 0
    is_valid_chain = True

    for block in my_blockchain:
        if block_index == 0:
            block_index += 1
            continue
        elif block[0] != my_blockchain[block_index - 1]:
            is_valid_chain = False
            break

        block_index += 1
    return is_valid_chain

def generate_options_menu():
    add__line()
    print('Please choose an option:')
    print('1: Add a new transaction')
    print('2: Mine a new block')
    print('3: Output all blockchain blocks')
    print('h: Manipulate blockchain')
    print('q: Quit')
    add__line()

def add__line():
    print('---------------------')
    
while waiting_for_input:
    generate_options_menu()
    
    user_choice = get_user_input()
    
    if user_choice == '1':
        tx_input_data = get_transaction_value()
        # A way to unpack values from a tuple into different variables
        recipient, amount = tx_input_data
        add_transaction(owner, recipient, amount)
    elif user_choice == '2':
        mine_block()
    elif user_choice == '3':
        return_all_blocks()
    elif user_choice == 'q':
        waiting_for_input = False
    elif user_choice == 'h':
        if len(my_blockchain) >= 1:
            my_blockchain[0] = [2.0]
    else:
        print('Invalid input, please choose a valid option')
    if not verify_chain_by_index():
        print('Invalid blockchain!')
        waiting_for_input = False
else:
    print('User left!')

add__line()
print('Done!')
