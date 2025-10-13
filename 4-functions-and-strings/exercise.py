def add__line():
    print('--------------------')
    
# 1) Write a normal function that accepts another function as an argument. Output the result of that other function in your “normal” function.
def normal_function(callback):
  return callback()

def callback_function():
  return "Hello from callback function!"

print(normal_function(callback_function))
add__line()

# 2) Call your “normal” function by passing a lambda function – which performs any operation of your choice – as an argument.
print(normal_function(lambda: "Hello from lambda function!"))
add__line()

# 3) Tweak your normal function by allowing an infinite amount of arguments on which your lambda function will be executed.
number_list = [1, 2, 3, 4, 5]
def normal_function_with_infinite_args(callback, *args):
  return callback(*args)

def callback_infinite_args(*args):
  return args

print(normal_function_with_infinite_args(callback_infinite_args, *number_list))
add__line()

# 4) Format the output of your “normal” function such that numbers look nice and are centered in a 20 character column.
def normal_function_centered(callback, number):
  return callback(number)

def callback_function_centered(number):
  return f"{number:^20}"

print(normal_function_centered(callback_function_centered, 5))
print(normal_function_centered(callback_function_centered, 6))
print(normal_function_centered(callback_function_centered, 7))
print(normal_function_centered(callback_function_centered, 8))
print(normal_function_centered(callback_function_centered, 9))
print(normal_function_centered(callback_function_centered, 10))
add__line()