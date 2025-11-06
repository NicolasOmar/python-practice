# This class has been created to share properties and methods usable in other classes without duplication, that is called [inheritance]
class Vehicle:
  def __init__(self, starting_top_speed=100):
    self.top_speed = starting_top_speed
    self.__warnings=[]

  def get_warnings(self):
    return self.__warnings

  def drive(self):
    print(f'I am driving! But they are faster than {self.top_speed}/mph')

  def add_warning(self, warning_text):
    if len(self.__warnings) == 0:
      self.__warnings.append(warning_text)
      print(f'New warning: {warning_text}')

# Now, to inherance all [Vehicle] properties and methods, you add its references as a method argument right after [Car] class
class Car(Vehicle):
  def stop(self):
    print('Car stopped')

# As you can see, all Car instanciated properties and methods are usable after getting from [Vehicle] class
first_car = Car()
first_car.drive()

test_car = Car(200)
test_car.drive()

Car.top_speed = 200

faster_car = Car(1)
faster_car.drive()
print(faster_car.__dict__)

private_car = Car()
private_car.add_warning('Engine not functioning')
print(private_car.get_warnings())


class Bus(Vehicle):
  def __init__(self, starting_speed=100):
    # Adding a self calling like this will give Bus class access to private properties and init arguments from the classes it calls upon (like Vehicle)
    super().__init__(starting_speed)
    self.passangers = []

  def add_group(self, group_to_add):
    self.passangers.extend(group_to_add)

new_bus = Bus()
# This particular line will return an error if [Bus] class does not access [Vehicle] private methods through [super().__init__]
new_bus.add_warning('Engine not functioning')
new_bus.add_group(['Marta', 'Maximilian'])
print(new_bus.passangers)