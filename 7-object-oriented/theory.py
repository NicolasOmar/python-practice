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
    self.top_speed = starting_top_speed

  # Here you are declaring a method for the class
  def drive(self):
    # To add a class reference to be used in the method, you have to invoke the class itself
    # with the self [keyword] as an argument, that will give you access
    print(f'I am driving! But they are faster than {self.top_speed}/mph')

first_car = Car()
first_car.drive() # It will return 'I am driving! But they are faster than 100/mph', bacause is the default value

test_car = Car(200)
test_car.drive() # It will return 'I am driving! But they are faster than 200/mph'

Car.top_speed = 200

faster_car = Car(1)
# It will return 'I am driving! But they are faster than 1/mph'
faster_car.drive()