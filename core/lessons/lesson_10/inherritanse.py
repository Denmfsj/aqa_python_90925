

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print('Unknown sound')

class Mammal(Animal):

    def __init__(self, name, num_legs):
        Animal.__init__(self, name)
        self.num_legs = num_legs

    def sound(self):
        print('Rrrrrr')


class Bird(Animal):

    def __init__(self, name, wingspan):
        self.wingspan = wingspan
        Animal.__init__(self, name)

    def sound(self):
        print('url...')

class Bat(Mammal, Bird):
    def __init__(self, name, num_legs, wingspan):
        Mammal.__init__(self, name, num_legs)
        Bird.__init__(self, name, wingspan)


    def sound(self):
        return super(Mammal, self).sound()


print('Mammal', Mammal.__mro__)  # MRO method resolution order
print('Bird', Bird.__mro__)
print('Bat', Bat.__mro__)

Bat(name='Bruce', num_legs=2, wingspan=2).sound()

# (Bat'>, Mammal'>, Bird'>, Animal'>,)

# dog = Mammal('Brovko', 4)
# parrot = Bird('Alex', 2)
#
# man = Bat(name='Bruce', num_legs=2, wingspan=2)
#
# print(dog.num_legs)
# print(parrot.wingspan)


