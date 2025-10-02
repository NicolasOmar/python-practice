# A different case is when you use a global variable, which is declared outside any function and can be used inside any function
my_blockchain = []

# In this case, the function is using an input (part of python default library) to get a value from the user, which is a string by default and its converted to an float number
def get_user_input():
    # This part uses a local variable, which will only be accesible inside the function
    # If there is another funciton with a variable with the same name, it will not affect this one because its a different scope
    # But if you want to use a global variable inside a function, you must use the 'global' keyword before using it
        # global user_input = 'Any value'
    user_input = float(input('Please enter your transaction value: '))
    return user_input

# A thing to have in mind, python has a way to get the last item of a list without knowing its length, using negative indexes
# In this case, -1 will always be the last item of the list, -2 the second to last, and so on
def take_last_blockchain_value():
    return my_blockchain[-1]

"""
    - A function is declared first with the def keyword, then its name and parentheses with any parameters it could receive
    - The code block must be indented by 4 spaces
    - Other thing to have in mind is the use of default values in arguments to include other value only when is necessary
"""
def add_block(transaction_value, last_transaction=[1]):
    """
        This type of comment is called docstring, and its used to explain the function's purpose
        You can use triple double quotation marks to write a multiline comment
    """
    # Another way to get the last value of the blockchain inside the function without providing it as an argument
    # In order to improve code's readability, you can call other functions inside a function to reuse its logic
        # last_blockchain_value = take_last_blockchain_value()
    # On this part, the function reuses a simple logic, add a new block of data to its original list, the print it
    my_blockchain.append([last_transaction, transaction_value])
    print(my_blockchain)

input_transaction_value = get_user_input()
# it returns [[-1], [[-1], input_transaction_value]]
add_block(input_transaction_value)
# We can keep adding blocks, each time using a different input which will be asigned to the same variable
input_transaction_value = get_user_input()
# it returns [[-1], [[-1], input_transaction_value], [[[-1], input_transaction_value], 2]]
add_block(2, take_last_blockchain_value())
input_transaction_value = get_user_input()
# it returns [[-1], [[-1], input_transaction_value], [[[-1], input_transaction_value], 2], [[[[-1], input_transaction_value], 2], 3]]
add_block(3, take_last_blockchain_value())
input_transaction_value = get_user_input()
# it returns [[-1], [[-1], input_transaction_value], [[[-1], input_transaction_value], 2], [[[[-1], input_transaction_value], 2], 3], [[[[[-1], input_transaction_value], 2], 3], 4]]
add_block(4, take_last_blockchain_value())
input_transaction_value = get_user_input()
# it returns [[-1], [[-1], input_transaction_value], [[[-1], input_transaction_value], 2], [[[[-1], input_transaction_value], 2], 3], [[[[[-1], input_transaction_value], 2], 3], 4], [[[[[[-1], input_transaction_value], 2], 3], 4], 5]]
# In this case, you can reorder the provided values and maintain the same logic by asigning to each value its corresponding keyword argument
add_block(last_transaction=take_last_blockchain_value(), transaction_value=input_transaction_value)
