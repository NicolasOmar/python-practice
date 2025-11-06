# A class is a blueprint for created instances (objects)
class Car:
  # This is a property for this class
  # This way to create the property and asign a value to it can be improved by including it in a constructor
    # top_speed = 100

  # A dunder method (because starts with double under)
  # This method is a constructor to create the object with default values or the ones can exist
  # The init method uses object self reference as first argument, and then, adds the arguments you want to use to asign into object's class values
    # Each argument can have a default value in case you don't want to assign it every time
  def __init__(self, starting_top_speed=100):
    # If you do not provide that keyword in your built-in class method, it will not work from start. Built-in methods are such that start with double underscore
      # def __init__(): # This will return an error
      # def __print_it__(): # This will return an error
    self.top_speed = starting_top_speed
    # If a property starts with double underscore, is considered a private attribute
    # The idea of this type of data is that you cannot call it directly, but with a method (that is considered encapsulation in OOP)
    self.__warnings=[]

  def get_warnings(self):
    return self.__warnings

  # Here you are declaring a method for the class
  def drive(self):
    # To add a class reference to be used in the method, you have to invoke the class itself
    # with the [self] keyword as an argument, that will give you access
    print(f'I am driving! But they are faster than {self.top_speed}/mph')

  # This is another way to access a private property because you are accessing it in a method and not directly in program's logic
  def add_warning(self, warning_text):
    if len(self.__warnings) == 0:
      self.__warnings.append(warning_text)
      print(f'New warning: {warning_text}')

first_car = Car()
first_car.drive() # It will return 'I am driving! But they are faster than 100/mph', bacause is the default value

test_car = Car(200)
test_car.drive() # It will return 'I am driving! But they are faster than 200/mph'

Car.top_speed = 200

faster_car = Car(1)
faster_car.drive() # It will return 'I am driving! But they are faster than 1/mph'
# If you want to print the object in a more readable way, you can access it with the [__dict__] method 
print(faster_car.__dict__) # It returns {'top_speed': 1, 'warnings': []}, as a JSON (it is a dictionary)

private_car = Car()
private_car.add_warning('Engine not functioning') # This will return 'New warning: Engine not functioning'
# This will return car's warning list but with a warning from python ()
# It does not stop the program because Python lets you work on that way, but is prefferable to access it trough a method
print(private_car.__warnings)
print(private_car.get_warnings()) # It returns car's warning list without any warning