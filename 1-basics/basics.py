# To declare a variable, just follow this sintax
# VARIABLE_NAME = VALUE

# You can reasign a variable value with another value
age = 29
print(age) # returns 29
age = 33
print(age) # returns the new value, 33

# Also, you can reasign a variable's value with another type of data
age = 'my age is'
print(age) # now it returns the text 'my age is'

# About numbers, if you want to work with numbers, the values must be numbers (in Javascirpt, that value can be coerced by operation's operators)
age = '29'
print(age)
  # age + 1 # returns an error because you are trying to add a number in a string value
print(age + '1') # returns '291' because you are concatenating

# A solution for this problem, you should convert the value into a number
age = '29'
age = int(age) + 1 # returns number 30
print(age)
int(1.8) # in case you want to convert a float number to integer, it will round down to its lowest value
float('29') # returns 29.0 (because is a number with its floater, that could even be cero if is converted)

# Operators
  # If you use '/' to divide 2 numbers, it will return a float by default
  # If you want to be returned an integer, use '//' operator
  # '**' equals a number pow

# Strings
# You can use single or double quotation marks, but it must begin and end with the same type
'hello' # is ok
"hello" # is ok
  # "hello' # is NOT ok
# In case you want to write a multiline string, you must use triple double quotation marks
"""This test
must be
enough to answer
the question""" # That returns "This test/nmust be/nenough to answer/nthe question"

# Lists, Python's array, can be variables (of several types of data, event other arrays inside the main one)
my_blockchain = [1, 2.9, 7]
my_blockchain[1] + 1 # it returns 3.9 because you are making an operation and returns its result
print(my_blockchain) # but the previous operations does not modify list's item value, it gives the original values instead ([1, 2.9, 7])
my_blockchain.append(3) # to add a new value into the list, you must exectue list's functions [append], which it will return [1, 2.9, 7, 3]
my_blockchain.pop() # to remove list's last item, you execute [pop] function from the list you want to execute it
print(my_blockchain) # now it returns [1, 2.9, 7] again