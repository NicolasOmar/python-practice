def add__line():
    print('--------------------')
    
# 1) Import the random function and generate both a random number between 0 and 1 as well as a random number between 1 and 10.
import random

def generate_random_number():
    first_random_number = random.randrange(0, 10)
    second_random_number = random.randint(1, 10)
    return first_random_number, second_random_number

print(generate_random_number())
print(generate_random_number())
print(generate_random_number())
add__line()

# 2) Use the datetime library together with the random number to generate a random, unique value.
import datetime

def generate_unique_value_from_datetime():
  current_date_time = datetime.datetime.now()
  random_number = random.randint(1, 1000)
  unique_value = f"{current_date_time.year}{current_date_time.month}{current_date_time.day}{current_date_time.hour}{current_date_time.minute}{current_date_time.second}{random_number}"
  return unique_value

print(generate_unique_value_from_datetime())
print(generate_unique_value_from_datetime())
print(generate_unique_value_from_datetime())
add__line()