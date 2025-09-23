
my_friends = ['Den', 'Alex', 'Yur']

# print(my_friends[0]) # Den
# print(my_friends[0][0]) # D
# print(my_friends[1:])

my_name_as_a_list = list('Den')

# print(my_name_as_a_list)

my_info = ['Den', 33, 36.6, None, True, [1,2,3], (True, False), None]

# print(my_info)
# print(my_info.count(None))
# print(my_info.index(33))

#print(id(my_info), my_info)
my_info.append(12312313212)  # додає в кінець елемент
my_info.append([1,2])  # додає в кінець елемент
#print(id(my_info), my_info)

last_el = my_info[-1]
last_el.append(3)  # я оновлю список додавши 3

#print(my_info)

my_numbers = [1,2,3]
not_my_names = my_numbers

#print('my_numbers', my_numbers)
#print('not_my_names', not_my_names)
not_my_names.append(42)
#print('my_numbers', my_numbers)
# print('not_my_names', not_my_names)

my_new_numbers = my_numbers[:]  # копія, тобто слайс з початку і до кінця
my_numbers.append(73)

#print(my_numbers)
#print(not_my_names)
print(my_new_numbers)

import copy

my_really_new_numbers = copy.deepcopy(my_new_numbers) # найправильніша копія, тобто слайс з початку і до кінця
my_new_numbers.append(777)
print(my_really_new_numbers)
print(my_new_numbers)