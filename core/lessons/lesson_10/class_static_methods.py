
date = '2025-10-10'

class DatetimeUtils:

    @staticmethod
    def get_difference_in_days(original_date, days_for_diff):
        return original_date + days(days_for_diff)


class Dog:

    type_of_animal = 'DOG'


    def __init__(self,name):
        self.name = name

    @staticmethod
    def make_noize():
        print('Rrrrr')

    @classmethod
    def print_type_of_animal(cls):
        print(f'This class is described {cls.type_of_animal}')


    def make_noize_v2(self):
        print(f'{self.name} says Rrrrr')


Dog.type_of_animal = 'Cat undercovered'

Dog.make_noize()
Dog.print_type_of_animal()
naida = Dog('naida')
naida.make_noize_v2()
naida.print_type_of_animal()

# DatetimeUtils.get_difference_in_days()



