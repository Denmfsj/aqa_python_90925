
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __del__(self):
        print(f"The {self.make} {self.model} object has been destroyed.")

    def print_model(self):
        print(self.make)


my_car = Car('Toyota', 'y60')

print(my_car)
del my_car   # my_car.__del__()
print(id(my_car))