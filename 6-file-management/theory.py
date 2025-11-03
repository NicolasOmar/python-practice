# Open is a method to work on a file using python
# On its arguments, the second one is the mode to open the file
  # r, read
  # w, write
  # r+, read and write
  # x, create and if files exists it will return an error
  # a, append the text to the end of the file
  # b, binary mode
demo_file = open('theory.txt', mode='a')
demo_file.write('This is a demo file.\n')
demo_file.write('This is a demo file.\n')
demo_file.write('This is a demo file.\n')
demo_file.write('This is a demo file.\n')
# ALWAYS close the file after working on it (to avoid memory leaks)
demo_file.close()
# Now we will read the file we just created
demo_file = open('theory.txt', mode='r')
file_content = demo_file.read()
demo_file.close()
print(file_content)