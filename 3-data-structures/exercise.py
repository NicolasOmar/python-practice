# 1) Create a list of “person” dictionaries with a name, age and list of hobbies for each person. Fill in any data you want.
persons_list = [
  { 'name': 'Nicolas', 'age': 22, 'hobbies': ['reading', 'gaming'] },
  { 'name': 'Florencia', 'age': 19, 'hobbies': ['painting', 'cycling'] },
  { 'name': 'Martin', 'age': 25, 'hobbies': ['hiking', 'swimming'] }
]
print(persons_list)

# 2) Use a list comprehension to convert this list of persons into a list of names (of the persons).
person_comprehension = ', '.join([person['name'] for person in persons_list])
print('The persons names are:', person_comprehension)

# 3) Use a list comprehension to check whether all persons are older than 20.
all_older_than_20 = all([person['age'] > 20 for person in persons_list])
print('All persons older than 20:', all_older_than_20)

# 4) Copy the person list such that you can safely edit the name of the first person (without changing the original list).
persons_copy = [person.copy() for person in persons_list]
persons_copy[0]['name'] = 'Matias'
print('Original list:', persons_list)
print('Modified copy:', persons_copy)
