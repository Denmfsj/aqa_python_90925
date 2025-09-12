print("My name is Sofa")

# незмінні типи
my_name = 'Denys'  # str, string, строка
my_age = 34  # int, integer, число
my_temp = 36.6  # float, число з плаваучою точккою
am_i_exist = True  # boolena, bool логічне True or False
None  # None, нічого
my_tuple = ('some info', 42)  # tuple, кортеж

# змінні типи
my_friends = ['Alex', 'Olena']  # list, список
my_info = {'name': 'Denys', 'age': 35}  # dict, словник
my_numbers = {1, 2, 3, 4}  # set, множина


print("My age is 35",  my_age == 35)  # False
print("My age is 34", my_age == 34)  # True
my_age == 34.0  # ?
my_age == '34'  # ?

# snake_case  - пишемо імена змінних і функцій, імена файлів і папок
# CAPS_LOCK_WITH_UNDERSCORE - константи
# MyClass - CamelCase - там пишуть імена клаксів


for number in [1, 2, 3]:
    print('Number is', number)
print('------------')
my__number = 42

# ctrl(command) + alt + l
