# ---STRING FORMATTING (BEFORE PYTHON 3.6)---
name = "Nicolas"
age = 33

# This version of a concatenated string is the base idea to start working, but it becoames hard to read
string_name="My name is " + name + " and I am " + str(age) + " years old."
print(string_name) # Returns My name is Nicolas and I am 33 years old.

# A better way to format strings is using the format method, which inserts the variables in the string and has no arguments limit
string_name = "My name is {} and I am {} years old.".format(name, age)
print(string_name) # Returns My name is Nicolas and I am 33 years old.

# An alternative way to inject the variables is by using positional arguments
# On this case, it will put first the age and then the name (because arguments are 0 indexed)
string_name = "My name is {1} and I am {0} years old.".format(name, age)
print(string_name) # Returns My name is 33 and I am Nicolas years old.

# Another alternative way to inject the variables is by using named arguments
# By assigning a name to each argument, we can use them in any order
string_name = "My name is {name} and I am {years} years old.".format(name=name, years=age)
print(string_name) # Returns My name is Nicolas and I am 33 years old.

founds = 150.978

founds_statement = "Founds: {}.".format(founds)
print(founds_statement) # Returns Founds: 150.97.

# We can also format numbers, in this case, we can ask to show a float number. By default, it shows 6 decimals
founds_statement = "Founds: {:f}.".format(founds)
print(founds_statement) # Returns Founds: 150.978000.

# If you want to reduce the number of decimals, you can specify it after the point
founds_statement = "Founds: {:.2f}.".format(founds)
print(founds_statement) # Returns Founds: 150.98.

# ---STRING INTERPOLATION (AFTER PYTHON 3.6)---

# After Python 3.6, we can use f-strings, which are more readable and easier to use
# In this case, you can directly inject the variables in the string using {}
string_name = f"My name is {name} and I am {age} years old."
print(string_name) # Returns My name is Nicolas and I am 33 years old.

# And can be extended to formatting numbers as well
string_name = f"My name is {name} and I am {age:.1f} years old."
print(string_name) # Returns My name is Nicolas and I am 33.0 years old.

# ---LIST MAPPING AND LAMBDA FUNCTIONS---
simple_list = [1, 2, 3, 4, 5]

# The map function applies a function to all items in an iterable (like a list) and returns a map object (which is an iterator)
# First arguments is the same as an callback function in javascript, the second argument is the iterable to apply the function to
def multiply_by_two(item):
    return item * 2

mapped_list = map(multiply_by_two, simple_list)
print(mapped_list) # Returns <map object at 0x...>

# You can convert the map object to a list or a tuple using the list() or tuple
print(list(mapped_list)) # Returns [2, 4, 6, 8, 10]
# TO HAVE IN MIND: It is recommended to use list comprehensions instead of map function for better readability and performance

# An alternative way to use the map function is by using a lambda function as the first argument
# A lambda function is an anonymous function that can take any number of arguments, but can only have one expression
mapped_list = map(lambda item: item * 2, simple_list)
print(list(mapped_list)) # Returns [2, 4, 6, 8, 10]