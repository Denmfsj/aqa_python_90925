class Car:

    brand = 'Nissan'
    number_of_wheels = 4


    def __init__(self, name, date_of_buy, tank=50):  # self = instance of class
        self.name = name
        self.date_of_buy = date_of_buy
        self.date_of_sell = None
        self.tank = tank
        self.l_to_rm = 1


    def drive_to(self, destination, q_in_km):

        if q_in_km * self.l_to_rm < self.tank:      # чи вистачить паилва на подорож
            print(f'Im driving to {destination}')
            self.tank = self.tank - q_in_km * self.l_to_rm  # віднімаю кількість палива з баку
        else:
            print('Not enough of fuel')


# my_first_car = Car(name='first', date_of_buy='01.01.2021')  # створення instance/екземпляр/об'єкт
my_second_car = Car('Alex',  '02.02.2022')



my_first_car = Car(name='first', date_of_buy='01.01.2021')
print(f'Fuel before {my_first_car.tank}')
my_first_car.drive_to('Lviv', 40)

print(f'Fuel after {my_first_car.tank}')
my_first_car.tank = 100
print(f'Fuel manual change {my_first_car.tank}')



# Car.drive_to(self=my_first_car, destination='Lviv', q_in_km=40)

#
# print('my_first_car', my_first_car.name, my_first_car.tank)
# print('my_second_car', my_second_car.name, my_second_car.tank)



