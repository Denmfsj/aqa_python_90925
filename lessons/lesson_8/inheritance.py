



class Animal:

    number_of_pews = 4

    def __init__(self, name):
        self.name = name


class Cat(Animal):

    def make_noize(self):
        print('Meaw')


class Dog(Animal):

    def make_noize(self):
        print('Rrrrr')


naida = Dog('Naida')
yakov = Cat('Yak')

print(naida.name, naida.number_of_pews)
naida.make_noize()
print('--'*89)
print(yakov.name, yakov.number_of_pews)
yakov.make_noize()