my_blockchain = []

def get_transaction_value():
    user_input = float(input('Please enter your transaction value: '))
    return user_input

def take_last_blockchain_value():
    return my_blockchain[-1]

def add_block(transaction_value, last_transaction=[1]):
    my_blockchain.append([last_transaction, transaction_value])
    print(my_blockchain)

def get_user_input():
    user_input = input('Please enter your transaction value: ')
    return user_input

def return_all_blocks():
    print('---Outputting all blocks---')
        # A for loop is used to iterate over a list, executing the same block of code for each item in the list
        # In this case, the loop will print each block of the blockchain in a different line
    for block in my_blockchain:
        print('Outputting block: ' + str(block))

input_transaction_value = get_transaction_value()
add_block(input_transaction_value)

# A while loop is used to execute a block of code as long as a certain condition is true
# In this case, the true is permanenet, so the loop will run indefinitely until it is manually stopped
while True:
    print('Please choose an option:')
    print('1: Add a new block to the blockchain')
    print('2: Output all blockchain blocks')
    
    user_choice = get_user_input()
    
    # The if else conditional statement gives you the option to execute different blocks of code based on a condition
    if user_choice == '1':
        input_transaction_value = get_transaction_value()
        add_block(input_transaction_value, take_last_blockchain_value())
    # In this case, I am using a different condition to execute another block of code called elif (which equals to else if in javascript)
    # You can list as many elif conditions as you want between the if and else statements (but there are better and cleaner ways to do this)
    elif user_choice == '2':
        return_all_blocks()
    # The final else statement will execute a block of code if none of the previous conditions were met
    else:
        print('Invalid input, please choose a valid option')