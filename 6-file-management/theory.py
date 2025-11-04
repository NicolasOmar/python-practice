# Open is a method to work on a file using python
# On its arguments, the second one is the mode to open the file
  # r, read
  # w, write
  # r+, read and write
  # x, create and if files exists it will return an error
  # a, append the text to the end of the file
  # b, binary mode
demo_file = open('theory.txt', mode='a')
# The \n string is a new line character to jump to the next line
demo_file.write('This is a demo file.\n')
demo_file.write('This is a demo file.\n')
demo_file.write('This is a demo file.\n')
demo_file.write('This is a demo file.\n')
# ALWAYS close the file after working on it (to avoid memory leaks)
demo_file.close()


# This code adds a couple of interesting things
# First, you use the open block statement to open the file and close it when its code block ends
with open('theory.txt', mode='r') as f:
  # Second, you read the file line by line using the readline() method
  line = f.readline()
  # Then, you use a while loop to read each line until there are no more lines to read
  while line:
    print(line)
    line = f.readline()
# And when the block ends, the file is closed automatically (no need to call close())
print('Done reading the file.')