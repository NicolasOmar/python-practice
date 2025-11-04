# A class is a blueprint for created instances (objects)
class Car:
  # This is a property for this class
  top_speed = 100

  # Here you are declaring a method for the class
  def drive(self):
    # To add a class reference to be used in the method, you have to invoke the class itself
    # with the self [keyword] as an argument, that will give you access
    print(f'I am driving! But they are faster than {self.top_speed}/mph')

test_car = Car()
test_car.drive() # It will return 'I am driving! But they are faster than 100/mph'

Car.top_speed = 200

faster_car = Car()
# It will return 'I am driving! But they are faster than 200/mph'
# Why? Because new Class property update will affect only to those instances created after the change
faster_car.drive()