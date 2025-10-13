def add__line():
    print('--------------------')

# 1) Create a list of names and use a for loop to output the length of each name (len() ).
names_list = ['Nicolas', 'Florencia', 'Omar', 'Lucia', 'Elsie', 'Ruben', 'Emma', 'Juan']

def print_names_length(names):
    add__line()
    for name in names:
        print('The name ' + name + ' has ' + str(len(name)) + ' characters.')
    add__line()

print_names_length(names_list)

# 2) Add an if check inside the loop to only output names longer than 5 characters.
def print_long_names_length(names):
    add__line()
    for name in names:
        if len(name) > 5:
            print('The name ' + name + ' has ' + str(len(name)) + ' characters.')
    add__line()

print_long_names_length(names_list)

# 3) Add another if check to see whether a name includes a “n” or “N” character.
def print_names_with_n(names):
    add__line()
    for name in names:
        if 'n' in name or 'N' in name:
            print('The name ' + name + ' contains the letter "n".')
    add__line()

print_names_with_n(names_list)

# 4) Use a while loop to empty the list of names (via pop() )
def empty_names_list(names):
  add__line()
  while len(names) > 0:
      print('Removing name: ' + names.pop())
  add__line()
  print('All names removed!')
  
empty_names_list(names_list)

