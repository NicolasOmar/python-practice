def add__line():
    print('--------------------')

# 1) Write a short Python script which queries the user for input (infinite loop with exit possibility) and writes the input to a file.

  # waiting_for_input = True

  # while waiting_for_input:
  #     add__line()
  #     print('Please choose an option:')
  #     print('1: Add a new phrase')
  #     print('q: Quit')
  #     add__line()

  #     user_choice = input('Please enter your selection: ')
  #     add__line()

  #     if user_choice == '1':
  #         tx_input_data = input('Please enter the new phrase: ')
  #         with open('exercise.txt', mode='a') as f:
  #             f.write(tx_input_data + '\n')
  #     elif user_choice == 'q':
  #         waiting_for_input = False
  #     else:
  #         print('Invalid input, please choose a valid option')
  # else:
  #     print('User left!')

# 2) Add another option to your user interface: The user should be able to output the data stored in the file in the terminal.

  # waiting_for_input = True

  # while waiting_for_input:
  #     add__line()
  #     print('Please choose an option:')
  #     print('1: Add a new phrase')
  #     print('2: Show all phrases')
  #     print('q: Quit')
  #     add__line()

  #     user_choice = input('Please enter your selection: ')
  #     add__line()

  #     if user_choice == '1':
  #         tx_input_data = input('Please enter the new phrase: ')
  #         with open('exercise.txt', mode='a') as f:
  #             f.write(tx_input_data + '\n')
  #         add__line()
  #     elif user_choice == '2':
  #         with open('exercise.txt', mode='r') as f:
  #             line = f.readline()
  #             while line:
  #                 print(line)
  #                 line = f.readline()
  #         add__line()
  #         print('Done reading the file.')
  #     elif user_choice == 'q':
  #         waiting_for_input = False
  #     else:
  #         print('Invalid input, please choose a valid option')
  # else:
  #     print('User left!')

# 3) Store user input in a list (instead of directly adding it to the file) and write that list to the file – both with pickle and json.

waiting_for_input = True

while waiting_for_input:
    user_inputs = []

    add__line()
    print('Please choose an option:')
    print('1: Add a new phrase')
    print('2: Show all phrases')
    print('q: Quit')
    add__line()

    user_choice = input('Please enter your selection: ')
    add__line()

    if user_choice == '1':
        tx_input_data = input('Please enter the new phrase: ')
        user_inputs.append(tx_input_data)
    elif user_choice == '2':
        print('Stored phrases:')
        for phrase in user_inputs:
            print(phrase)
        add__line()
        print('Reading from the file:')
        with open('exercise.txt', mode='r') as f:
            line = f.readline()
            while line:
                print(line)
                line = f.readline()
        add__line()
        print('Done reading the file.')
    elif user_choice == 'q':
        with open('exercise.txt', mode='a') as f:
            f.write(tx_input_data + '\n')
        add__line()
        waiting_for_input = False
    else:
        print('Invalid input, please choose a valid option')
else:
    print('User left!')

# 4) Adjust the logic to load the file content to work with pickled/ json data.