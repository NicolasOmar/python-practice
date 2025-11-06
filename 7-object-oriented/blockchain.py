import functools
import collections
import json
# CLASS IMPORTS
from classes.block import Block
# OTHER IMPORTS
from utils import hash_block, hash_string_256

MINING_REWARD = 10
# genesis_block now will be a block instance
genesis_block = Block(0, '', [], 100)
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

def valid_proof(transactions, last_hash, proof):
    guess = (str(transactions) + str(last_hash) + str(proof)).encode()
    guess_hash = hash_string_256(guess)
    
    return guess_hash[0:2] == '00'

def proof_of_work():
    last_block = my_blockchain[-1]
    hash_last_block = hash_block(last_block)
    proof = 0
    while not valid_proof(open_transactions, hash_last_block, proof):
        proof += 1
    return proof

def mine_block():
    last_block = my_blockchain[-1]
    hashed_block = hash_block(last_block)
    proof_of_work_value = proof_of_work()
    
    reward_transaction = collections.OrderedDict([('sender', 'MINING'), ('recipient', owner), ('amount', MINING_REWARD)])

    transactions = open_transactions.copy()
    transactions.append(reward_transaction)
    new_block = Block(
        len(my_blockchain),
        hashed_block,
        transactions,
        proof_of_work_value
    )
    my_blockchain.append(new_block)
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
    
    new_transaction = collections.OrderedDict([('sender', sender), ('recipient', recipient), ('amount', amount)])

    if verify_transaction(new_transaction):
        open_transactions.append(new_transaction)
        participants.add(sender)
        participants.add(recipient)
        save_data()
    else:
        print('Transaction failed! Not enough balance!')
    add__line()

def return_all_blocks():
    print('---Outputting all blocks---')
    
    for block in my_blockchain:
        print(f'Outputting block: {block}')
    add__line()
    
def get_balance(participant):
    sent_transactions = [[tx['amount'] for tx in block.transactions if tx['sender'] == participant] for block in my_blockchain]
    recieved_transactions = [[tx['amount'] for tx in block.transactions if tx['recipient'] == participant] for block in my_blockchain]
    open_sent_transactions = [tx['amount'] for tx in open_transactions if tx['sender'] == participant]

    sent_transactions.append(open_sent_transactions)
    sent_amounts = functools.reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt), sent_transactions, 0)
    recieved_amounts = functools.reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt), recieved_transactions, 0)
    return recieved_amounts - sent_amounts

def verify_chain():
    """ The function helps to verify the integrity of the blockchain by checking if each block's previous hash matches the hash of the previous block. """
    print(my_blockchain)
    for (index, block) in enumerate(my_blockchain):
        if index == 0:
            continue
        if block.previous_hash != hash_block(my_blockchain[index - 1]):
            return False
        if not valid_proof(block.transactions[:-1], block.previous_hash, block.proof):
            print('Proof of work is invalid')
            return False
    return True

def verify_transactions():
    """ The function verifies all open transactions to ensure they are valid. """
    return all([tx for tx in open_transactions if not verify_transaction(tx)])

def load_data():
    try:
        with open('blockchain.txt', mode='r') as f:
            global my_blockchain
            global open_transactions
            file_content = f.readlines()
            
            my_blockchain = json.loads(file_content[0])
            updated_blockchain = []
            updated_transactions = []
            
            for current_block in my_blockchain:
                # genesis_block now will be a block instance
                block_transactions = [collections.OrderedDict(
                    [('sender', tx['sender']), ('recipient', tx['recipient']), ('amount', tx['amount'])]) for tx in current_block.transactions]
                updated_block = Block(
                    current_block.proof,
                    current_block.previous_hash,
                    block_transactions,
                    current_block.proof)
                updated_blockchain.append(updated_block)

            for tx in current_block.transactions:
                updated_transaction = collections.OrderedDict(
                    [('sender', tx['sender']), ('recipient', tx['recipient']), ('amount', tx['amount'])])
                updated_transactions.append(updated_transaction)
                
            my_blockchain = updated_blockchain
            open_transactions = updated_transactions
    except (IOError, IndexError):
        genesis_block = Block(0, '', [], 100)
        my_blockchain = [genesis_block]
        open_transactions = []
    finally:
        print('Cleanup')

def save_data():
    print([block.__dict__ for block in my_blockchain])
    savable_chain = [block.__dict__ for block in my_blockchain]
    with open('blockchain.txt', mode='w') as f:
        f.write(json.dumps(savable_chain))
        f.write('\n')
        f.write(json.dumps(open_transactions))

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
            save_data()
    elif user_choice == '3':
        return_all_blocks()
    elif user_choice == '4':
        print(participants)
    elif user_choice == 'q':
        waiting_for_input = False
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
