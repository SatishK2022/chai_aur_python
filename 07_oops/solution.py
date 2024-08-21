class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        # self.total_car += 1 # Can also write like this
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + "!"

    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_desc():
        return "Cars are means of transport."
    
    @property
    def model(self):
        return self.__model
    

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"


# my_tesla = ElectricCar("Tesla", "Model S", "85kwh")

# print(isinstance(my_tesla, Car))
# print(isinstance(my_tesla, ElectricCar))

# print(my_tesla.fuel_type())
# print(my_tesla.battery_size)
# print(my_tesla.brand)
# print(my_tesla.full_name())

# safari = Car("Tata", "Safari")
# print(safari.fuel_type())

# safari.model = "Nexon"
# print(safari.model)
# print(safari.model())

# my_car = Car("Hyundi", "Verna")
# print(my_car.__brand) # __brand is a private attribute it can be accessed within the class itself
# print(my_car.get_brand()) # The brand is now only accessable with this getter method

# print(my_car.general_desc()) # objects can't access the static methods
# print(Car.general_desc())

# Get the Total Number of Objects Created with class Car
# print(Car.total_car)

# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

# my_new_car = Car("Tata", "Nano")
# print(my_new_car.brand)
# print(my_new_car.model)

class Battery:
    def battery_info(self):
        return "This is a battery"

class Engine:
    def engine_info(self):
        return "This is a engine"

class ElectricCar2(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCar2("Tesla", "Model S")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())