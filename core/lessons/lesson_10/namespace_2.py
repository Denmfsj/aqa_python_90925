
class PathDefinition:

    ROOT_PATH = ...
    RESOURSE_PATH = ...



class Animal:

    number_of_pews = 4  # class attribute
    def __init__(self, name):
        self.name = name
        self.local_number_of_pews = 4


class Cat(Animal):

    type_of_animal = 'Cat'

    def make_noize(self):
        print('Meaw')


class Dog(Animal):

    type_of_animal = 'DOG'

    def make_noize(self):
        print('Rrrrr')


naida = Dog('naida')
riabko  = Dog('riabko')


print(Dog.number_of_pews)
Dog.number_of_pews = 5  # змінив атрибут класа
riabko.local_number_of_pews = 6

print(naida.name, naida.number_of_pews)
print(naida.name, naida.local_number_of_pews)
print('-------------')
print(riabko.name, riabko.number_of_pews)
print(riabko.name, riabko.local_number_of_pews)


