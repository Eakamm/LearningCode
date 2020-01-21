from Car import Car
class Dog():
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def sit(self):
    print(self.name.title()+" is sit!")

  def rool_over(self):
    print(self.age.title()+" is rool_over!")

my_dog = Dog("小小","3")
my_dog.sit()
my_dog.rool_over()

#2、使用技巧
my_new_car = Car('audi', 'a4', 2015)
my_new_car.update_odometer(24)
my_new_car.update_odometer(22)
my_new_car.read_odometer()
