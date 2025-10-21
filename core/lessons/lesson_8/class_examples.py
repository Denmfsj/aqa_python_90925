

class Car:

    brand = 'Nissan'
    number_of_wheels = 4

    @staticmethod
    def drive_to(destination):
        print(f'Im driving to {destination}')


my_name = str("denys")  # instance
my_f_name = str("alla")  # instance
my_car1 = Car()  # instance
my_car2 = Car()  # instance

my_name.upper()
my_car1.drive_to('Kyiv')
print(my_car1.brand)

print(id(my_car1))
print(id(my_car2))
