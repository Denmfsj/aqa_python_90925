
my_number = 10
my_name = 'Den'

def custom_separator_short():
    print('111')

print(my_number + 5)
print(my_name + '  Mer')

class Cat:

    def make_noize(self):
        print('Meaw')

class Dog:

    def make_noize(self):
        print('Rrrrr')


yakov = Cat()
naida = Dog()

for pet in [yakov, naida]:
    pet.make_noize()