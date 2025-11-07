def add__line():
    print('--------------------')
    
# 1) Create a Food class with a “name” and a “kind” attribute as well as a “describe() ” method (which prints “name” and “kind” in a sentence).

class Food:
  def __init__(self, name, kind):
    self.name = name
    self.kind = kind

  def describe(self):
    print(f'{self.name} - {self.kind}')
  
example_food = Food('fries', 'delicious')
example_food.describe()
add__line()

# 2) Try turning describe()  from an instance method into a class and a static method. Change it back to an instance method thereafter.

class FoodClass:
  name='apple'
  kind='fruit'

  @classmethod
  def describe(cls):
    print(f'{cls.name} - {cls.kind}')

class FoodStatic:
  @staticmethod
  def describe(name, kind):
    print(f'{name} - {kind}')
  
FoodClass.describe()
FoodStatic.describe('onion', 'vegetable')
add__line()

# 3) Create a  “Meat” and a “Fruit” class – both should inherit from “Food”. Add a “cook() ” method to “Meat” and “clean() ” to “Fruit”.

class Meat(Food):
  def __init__(self, name):
    super().__init__(name, 'fruit')

  def cook(self):
    print(f'{self.name} is being cooked')

class Fruit(Food):
  def __init__(self, name):
    super().__init__(name, 'meat')

  def clean(self):
    print(f'{self.name} is beign cleaned')

lobster_meat = Meat('lobster')
lobster_meat.describe()
lobster_meat.cook()

banana_meat = Fruit('banana')
banana_meat.describe()
banana_meat.clean()
add__line()

# 4) Overwrite a “dunder” method to be able to print your “Food” class.

class FoodDunder:
  def __init__(self, name, kind):
    self.name = name
    self.kind = kind

  def __repr__(self):
    print(self.__dict__)
  
dunder_food = FoodDunder('dunder', 'flour')
dunder_food.__repr__()