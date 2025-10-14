# A built in module that provides functions from python standard library
import functools
import hashlib
import json

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
    return hashlib.sha256(json.dumps(block).encode())

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
    print('Block added!')
    add__line()
    return True

def get_transaction_value():
    """ Returns the input of the user (a new transaction amount and its recipient) as a tuple """
    tx_recipient_input = input('Please enter the recipient of the transaction: ')
    tx_amount_input = float(input('Please enter your transaction input: '))
    add__line()

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
        participants.add(sender)
        participants.add(recipient)
    else:
        print('Transaction failed! Not enough balance!')
    add__line()

def return_all_blocks():
    print('---Outputting all blocks---')
    
    for block in my_blockchain:
        print(f'Outputting block: {block}')
    add__line()
    
def get_balance(participant):
    sent_transactions = [[tx['amount'] for tx in block['transactions'] if tx['sender'] == participant] for block in my_blockchain]
    recieved_transactions = [[tx['amount'] for tx in block['transactions'] if tx['recipient'] == participant] for block in my_blockchain]
    open_sent_transactions = [tx['amount'] for tx in open_transactions if tx['sender'] == participant]

    sent_transactions.append(open_sent_transactions)
    sent_amounts = functools.reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_amt + 0, sent_transactions, 0)

    recieved_amounts = functools.reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_amt + 0, recieved_transactions, 0)

    return recieved_amounts - sent_amounts

def verify_chain():
    """ The function helps to verify the integrity of the blockchain by checking if each block's previous hash matches the hash of the previous block. """
    for (index, block) in enumerate(my_blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(my_blockchain[index - 1]):
            return False
    return True

def verify_transactions():
    """ The function verifies all open transactions to ensure they are valid. """
    return all([tx for tx in open_transactions if not verify_transaction(tx)])

while waiting_for_input:
    generate_options_menu()
    
    user_choice = get_user_input()
    
    if user_choice == '1':
        tx_input_data = get_transaction_value()
        recipient, amount = tx_input_data
        add_transaction(owner, recipient, amount)
    elif user_choice == '2':
        if mine_block():
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
    print(f"Balance of {owner}: {get_balance(owner)}")
else:
    print('User left!')

add__line()
print('Done!')
