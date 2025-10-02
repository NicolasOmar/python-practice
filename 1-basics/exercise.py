# 1) Create two variables – one with your name and one with your age
name = input('Enter your name: ')
age = input('Enter your age: ')

# 2) Create a function which prints your data as one string
print('Your name is ' + name + ' and you are ' + age + ' years old.')

# 3) Create a function which prints ANY data (two arguments) as one string
def print_random_data(data1, data2):
    print('The first data is ' + data1 +' and the second data is ' + data2 + '.')
print_random_data('Hello', 'World')

# 4) Create a function which calculates and returns the number of decades you already lived (e.g. 23 = 2 decades)
def give_decades_from_number(number):
    number_in_decades = int(number) // 10
    return str(number_in_decades) + ' decades'
print(give_decades_from_number(10))
print(give_decades_from_number(22))
print(give_decades_from_number(34))
print(give_decades_from_number(139))