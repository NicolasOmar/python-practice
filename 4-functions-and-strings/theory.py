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

