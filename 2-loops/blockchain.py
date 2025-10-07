my_blockchain = []
waiting_for_input = True

def get_transaction_value():
    user_input = float(input('Please enter your transaction value: '))
    add__line()
    return user_input

def take_last_blockchain_value():
    # The first line above checks list/array length and ask if is less than 1 (empty list/array)
    # In case that statement is true, it will return None, a special data type that represents the absence of a value (like null in javascript)
    if len(my_blockchain) < 1:
        return None
    
    return my_blockchain[-1]

def add_block(transaction_value, last_transaction):
    # To update the logic related to the None value, it will asign a default value of [1] to last_transaction in case its value is abscent (None)
    if last_transaction is None:
        last_transaction = [1]
        
    my_blockchain.append([last_transaction, transaction_value])
    print(my_blockchain)
    add__line()

def get_user_input():
    user_input = input('Please enter your transaction value: ')
    add__line()
    return user_input

def return_all_blocks():
    print('---Outputting all blocks---')
        # A for loop is used to iterate over a list, executing the same block of code for each item in the list
        # In this case, the loop will print each block of the blockchain in a different line
    for block in my_blockchain:
        print('Outputting block: ' + str(block))
    add__line()

def verify_chain_by_index():
    """ The same function as verify_chain but using the index of the blocks instead of the block itself """
    is_valid_chain = True
    # There is no index number in a for loop for python, but it can be used through the range() function
    for block_index in range(len(my_blockchain)):
        if block_index == 0:
            # In case you are in the first index, there is no need to check anything, so just continue to the next iteration (continue will skip the iteration and will continue with the next one)
            block_index += 1
            continue
        # The idea in this if is that che the first element of the current block (block[0]) should be equal to the entire previous block (my_blockchain[block_index - 1])
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
            # In case you are in the first index, there is no need to check anything, so just continue to the next iteration (continue will skip the iteration and will continue with the next one)
            block_index += 1
            continue
        # The idea in this if is that che the first element of the current block (block[0]) should be equal to the entire previous block (my_blockchain[block_index - 1])
        elif block[0] != my_blockchain[block_index - 1]:
            is_valid_chain = False
            break

        block_index += 1
    return is_valid_chain

def add__line():
    print('---------------------')

# A while loop is used to execute a block of code as long as a certain condition is true
# In this case, the true related to the waiting_for_input variable
while waiting_for_input:
    add__line()
    print('Please choose an option:')
    print('1: Add a new block to the blockchain')
    print('2: Output all blockchain blocks')
    print('h: Manipulate blockchain')
    print('q: Quit')
    add__line()

    user_choice = get_user_input()
    
    # The if else conditional statement gives you the option to execute different blocks of code based on a condition
    if user_choice == '1':
        input_transaction_value = get_transaction_value()
        add_block(input_transaction_value, take_last_blockchain_value())
    # In this case, I am using a different condition to execute another block of code called elif (which equals to else if in javascript)
    # You can list as many elif conditions as you want between the if and else statements (but there are better and cleaner ways to do this)
    elif user_choice == '2':
        return_all_blocks()
    elif user_choice == 'q':
        # Break is used to exit the loop (in this case, to quit the program)
            # break
        waiting_for_input = False
    elif user_choice == 'h':
        if len(my_blockchain) >= 1:
            my_blockchain[0] = [2.0]
    # The final else statement will execute a block of code if none of the previous conditions were met
    else:
        print('Invalid input, please choose a valid option')
    # As a foot note, does not exists such a thing as switch statements in python (sorry about that)
    # In this scenario, an not keyword equals '!= value', but is more readable this way
    # There are other keywords like 'is' and 'in' that can be used in conditional statements, but it will be seen in other exercises
    if not verify_chain_by_index():
        print('Invalid blockchain!')
        waiting_for_input = False
# The else at the end of the while loop will be executed when the while condition is no longer true
else:
    print('User left!')

add__line()
print('Done!')